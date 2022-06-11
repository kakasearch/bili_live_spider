import time
import os
def walkFile(file):
  timu = []
  for root, dirs, files in os.walk(file):
    for f in files:
      if "观看人数" in f:
        addr = os.path.join(root, f).replace(file+'\\','').replace('\\','/')
        timu.append(file+'/'+addr)
  return timu

path = "./data"
files = walkFile(path)
# print(files)

datas = []
for file in files:
	with open(file,"r",encoding="utf-8")as f:
		items = f.readlines()
	for i in items[::-1]:
		if i:
			day = i.split(' ')[0]
			num = i.replace("\n",'').split(",")[-1]
			num = num.replace('人看过',"")
			num = num.replace('万',"*10000")
			num = eval(num)
			# num=============
			datas.append([day,num])
			break
with open("result.csv","w",encoding="utf-8")as f:
	for i in datas:
		print(i)
		f.write(f"{i[0]},{i[1]}\n")
os.startfile("result.csv")
print("处理完毕")