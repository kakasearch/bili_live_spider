from starlette.responses import RedirectResponse
from fastapi import Body, FastAPI
from fastapi.staticfiles import StaticFiles
import time

app = FastAPI()
@app.post('/submit')
def index(data=Body(...)):

	#{'title': '【新v出道回】初次见面', 
	#'up': '轩沐呀_', 'watched': '2673人看过', 
	#'chats': ['扭一扭真可爱', '明早摸鱼是吧']}

	print(f'{data["title"]}:{data["watched"]},{len(data["chats"])}条弹幕')
	timeStamp = time.time()
	today = time.strftime("%Y_%m_%d", time.localtime(timeStamp))
	now =  time.strftime("%Y_%m_%d %H:%M:%S", time.localtime(timeStamp))
	with open(f'./data/观看人数_{data["title"]}_{today}.csv',"a+",encoding="utf-8")as f:
		f.write(f'{now},{data["watched"]}\n')
	with open(f'./data/弹幕数据_{data["title"]}_{today}.csv',"a+",encoding="utf-8")as f:
		f.write(f'{",".join(data["chats"])}\n')
	return {
		"code":0,
		"msg":"success"
	}

	
    
 