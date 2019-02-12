import hashlib
import os
import shutil


def read_chunks(fh):
  fh.seek(0)
  chunk = fh.read(8096)
  while chunk:
    yield chunk
    chunk = fh.read(8096)
  else:
    fh.seek(0)

def md5sum(filename):
  m = hashlib.md5()
  if isinstance(filename, str) and os.path.exists(filename):
    with open(filename, "rb") as fh:
      for chunk in read_chunks(fh):
        m.update(chunk)
  # print(m.hexdigest())
  return m.hexdigest()

ROOT = os.getcwd()
PATH1 = os.path.join(ROOT,r'md5_cmp\1')
PATH2 = os.path.join(ROOT,r'md5_cmp\2')

if __name__ == '__main__':

  fmd5list = set()

  # build left dir md5 dict
  if not os.path.exists(PATH1):
    PATH1 = ROOT

  for root, dirs, files in os.walk(PATH1):
    for file in files:
      filename = os.path.join(root,file)
      fmd5 = md5sum(filename)
      if fmd5 not in fmd5list:
        fmd5list.add(fmd5)
      else:
        print("%s is a duplicate file"%filename)
        os.remove(filename)

  print("Total %d unique files"%len(fmd5list))

  # compare with right
  if os.path.exists(PATH2):
    for root, dirs, files in os.walk(PATH2):
      for file in files:
        filename = os.path.join(root,file)
        fmd5 = md5sum(filename)
        if fmd5 not in fmd5list:
          fmd5list.add(fmd5)
          # copy this file from path2 to path1
          filename_cp = os.path.join(PATH1,file)
          if os.path.exists(filename_cp):
            filename_cp += '_1'
          shutil.copy(filename, filename_cp)
          os.remove(filename)
        else:
          print("%s is a duplicate file"%filename)
          os.remove(filename)


  print("Total %d unique files"%len(fmd5list))