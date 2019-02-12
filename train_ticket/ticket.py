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
  tickets -dg 南京 北京 2016-07-01
"""
from docopt import docopt
import requests
import re
import time
from prettytable import PrettyTable

STATION_URL = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
REQUEST_URL = 'https://kyfw.12306.cn/otn/leftTicket/queryZ'
PROXIES = {}
STA_DIC = {}
STA_REV = {}


def parseargs():
  """command-line interface"""
  arguments = docopt(__doc__)
  return arguments

def parseTrainInfo(row):
  # 从row中根据headers过滤信息, 然后调用pt.add_row()添加到表中
  d = row.split('|')
  # 车次信息
  newrow = [d[3]]
  # 车站信息
  for idx in range(4,8):
    newrow.append(STA_REV.get(d[idx]))
  # 时间信息
  newrow += d[8:11]
  newrow.append('是' if d[18]!='1' else '') #过夜
  # 座位信息
  newrow.append(d[32]) #商务
  newrow.append(d[31]) #一等
  newrow.append(d[30]) #二等
  newrow.append(d[21]) #高软
  newrow.append(d[23]) #软卧
  newrow.append(d[33]) #动卧
  newrow.append(d[28]) #硬卧
  newrow.append(d[29]) #硬座
  newrow.append(d[26]) #无座
  return newrow

def cli():
  args = parseargs()
  # get station information
  r = requests.get(STATION_URL, proxies = PROXIES)

  stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', r.text)
  for chn, code in stations:
    STA_DIC[chn] = code
    STA_REV[code] = chn

  # parse argument
  from_station = STA_DIC.get(args['<from>'])
  to_station = STA_DIC.get(args['<to>'])
  date = args['<date>']

  if date == 'now' or date == 'today':
    date = time.strftime('%Y-%m-%d')
  elif time.strptime(date, '%Y-%m-%d') < time.strptime(time.strftime('%Y-%m-%d'), '%Y-%m-%d'):
    print('The date is before current date')
    exit(1)

  # get train info
  url = REQUEST_URL+'?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, from_station, to_station)
  r = requests.get(url, proxies = PROXIES)
  # print(r.json())
  rows = r.json()['data']['result']
  headers = '车次 始发 终到 出发 到达 发时 到时 历时 过夜 商务 一等 二等 高软 软卧 动卧 硬卧 硬座 无座'.split()
  pt = PrettyTable()
  pt._set_field_names(headers)
  for row in rows:
    newrow = parseTrainInfo(row)
    pt.add_row(newrow)
  print(pt)

if __name__ == '__main__':
  cli()