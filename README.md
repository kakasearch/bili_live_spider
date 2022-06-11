# bili_live_spider

 爬取B站直播的数据。

包含两个部分，油猴脚本 和 服务器，油猴脚本负责采集信息后上传，服务器负责保存数据。



## 安装

```bash
pip install fastapi uvicorn
```

安装油猴脚本管理器插件

安装[油猴脚本](https://greasyfork.org/zh-CN/scripts/446315)

## 运行

1. 双击```run_server.bat``` 或者 执行 ``` uvicorn server:app --reload --host 0.0.0.0 --port 1775```

2. 打开要爬取的B站直播间

3. 网页空白处单击右键，点击```Tampermonkey``` 、```Bili直播数据爬虫```、```【🕸开始爬取直播信息】```

   





