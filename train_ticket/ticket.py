# coding: utf-8
"""Train tickets query via command-line.

Usage:
  tickets [-gdtkz] <from> <to> <date>

Options:
  -h,--help        显示帮助菜单
  -g               高铁
  -d               动车
  -t               特快
  -k               快速
  -z               直达

Example:
  tickets 南京 北京 2016-07-01
  tickets 南京 北京 now(today/tom/tomorrow)
  tickets 南京 北京 0 (stand for day from now)
  tickets -dg 南京 北京 2016-07-01
"""
from docopt import docopt
import requests
import re
import time
from prettytable import PrettyTable
from colorama import Fore

# configures
STATION_URL = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
REQUEST_URL = 'https://kyfw.12306.cn/otn/leftTicket/queryZ'
PROXIES = {
}
STA_DIC = {}
STA_REV = {}

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

class Train(object):

  headers = '车次 始终 区间 时间 历时 过夜 商务 一等 二等 高软 软卧 动卧 硬卧 硬座 无座'.split()

  def __init__(self, raw_data, options = ''):
    self.raw_data = raw_data
    self.options = options

  def colored(self, color, string):
    # return ''.join([getattr(Fore, color.upper()), string, Fore.RESET])
    return string

  def seatColored(self, seat):
    if seat == '无':
      return self.colored('red', seat)
    elif seat == '有':
      return self.colored('green', seat)
    else:
      return seat or '--'

  def parseTrainInfo(self, d):
    ret = {
          # 车次信息
          'train_code': d[3],

          # 车站信息
          'station_start':  self.colored('green', STA_REV.get(d[4])), #始发
          'station_end':    self.colored('red', STA_REV.get(d[5])), #终到
          'station_from':   self.colored('green', STA_REV.get(d[6])), #出发
          'station_to':     self.colored('red', STA_REV.get(d[7])), #到达

          # 时间信息
          'time_go':        self.colored('green', d[8]), #发时
          'time_arrive':    self.colored('red', d[9]), #到时
          'time_during':    d[10], #历时
          'time_overnight': self.colored('red', '是') if d[18]!='1' else '', #过夜

          # 座位信息
          'seat_business':  self.seatColored(d[32]), #商务
          'seat_first':     self.seatColored(d[31]), #一等
          'seat_second':    self.seatColored(d[30]), #二等
          'bed_highsoft':   self.seatColored(d[21]), #高软
          'bed_soft':       self.seatColored(d[23]), #软卧
          'bed_emu':        self.seatColored(d[33]), #动卧
          'bed_hard':       self.seatColored(d[28]), #硬卧
          'seat_hard':      self.seatColored(d[29]), #硬座
          'seat_no':        self.seatColored(d[26]), #无座
          }
    return ret

  def needPrint(self, d):
    station_train_code = d[3]
    initial = station_train_code[0].lower()
    return (not self.options or initial in self.options)

  @property
  def trains(self):
    for row in self.raw_data:
      d = row.split('|')
      if self.needPrint(d):
        yield self.parseTrainInfo(d)

  def prettyPrint(self):
    pt = PrettyTable()
    pt._set_field_names(self.headers)
    for train in self.trains:
      row1 = [
        train['train_code'],
        train['station_start'],
        train['station_from'],
        train['time_go'],
        train['time_during'],
        train['time_overnight'],
        train['seat_business'],
        train['seat_first'],
        train['seat_second'],
        train['bed_highsoft'],
        train['bed_soft'],
        train['bed_emu'],
        train['bed_hard'],
        train['seat_hard'],
        train['seat_no'],
      ]
      row2 = [
        '',
        train['station_end'],
        train['station_to'],
        train['time_arrive'],
      ]
      row2 += ['']*(len(row1)-len(row2))
      pt.add_row(row1)
      pt.add_row(row2)
    print(pt)

class Cli():

  def __init__(self):
    self.station_url = STATION_URL
    self.request_url = REQUEST_URL
    self.initStation()
    args = self.parseArgs()
    self.options = ''.join([key for key, value in args.items() if value is True])

  def initStation(self):
    # get station information
    r = requests.get(self.station_url, proxies = PROXIES)
    stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', r.text)
    for chn, code in stations:
      STA_DIC[chn] = code
      STA_REV[code] = chn

  def parseArgs(self):
    args = docopt(__doc__)
    # test
    # args = {'-d': True,
    #         '-g': True,
    #         '-k': False,
    #         '-t': True,
    #         '-z': True,
    #         '<date>': '2019 3 1',
    #         '<from>': '上海',
    #         '<to>': '长春'
    #         }
    # parse arguments
    try:
      self.from_station = STA_DIC.get(args['<from>'])
      self.to_station = STA_DIC.get(args['<to>'])
    except:
      raise ValueError('invalid station name')
    t_str = args['<date>']
    self.date = self.convTime(t_str)
    return args

  def convTime(self, t_str):
    t = time.time()
    day = 24*60*60
    # condition: now/tomorrow
    if t_str == 'now' or t_str == 'today':
      date = time.strftime('%Y-%m-%d', time.localtime(t))
    elif t_str == 'tom' or t_str == 'tomorrow':
      date = time.strftime('%Y-%m-%d', time.localtime(t+1*day))
    # condition: number
    elif is_number(t_str):
      date = time.strftime('%Y-%m-%d', time.localtime(t+int(t_str)*day))
    # condition: strftime
    else:
      obj = re.search(r'(\d{4})[/\- ](\d{1,2})[/\- ](\d{1,2})$', t_str)
      if obj:
        date = '%04d-%02d-%02d'%tuple(int(num) for num in obj.group(1,2,3))
      else:
        raise ValueError('The date string is not supported')

    # time < current time condition
    if time.strptime(date, '%Y-%m-%d') < time.strptime(time.strftime('%Y-%m-%d'), '%Y-%m-%d'):
      raise ValueError('The date is before current date')
    else:
      return date

  def getTrainInfo(self):
    # get train info
    self.request_url += '?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(self.date, self.from_station, self.to_station)
    r = requests.get(self.request_url, proxies = PROXIES)
    try:
      raw_data = r.json()['data']['result']
    except:
      raise ConnectionError('This is not a valid date on server')
    return raw_data

  def run(self):
    """command-line interface"""

    raw_data = self.getTrainInfo()
    print('查询日期：%s'%self.date)
    Train(raw_data, self.options).prettyPrint()

if __name__ == '__main__':
  Cli().run()