#弹幕数据去重

import time
import os
import csv

def walkFile(file):
  timu = []
  for root, dirs, files in os.walk(file):
    for f in files:
      if "弹幕数据" in f:
        addr = os.path.join(root, f).replace(file+'\\','').replace('\\','/')
        timu.append(file+'/'+addr)
  return timu

path = "./data"
files = walkFile(path)
# print(files)

datas = set({})
for file in files:
	with open(file,"r",encoding="utf-8")as f:
		items = csv.reader(f)
		for i in items:
			datas.update(i)
	file = "./弹幕清洗/"+file.split("/")[-1]
	with open(file,"w",encoding="utf-8")as f:
		f.write("\n".join(list(datas)))

print("处理完毕")
os.startfile(os.path.abspath('./弹幕清洗'))