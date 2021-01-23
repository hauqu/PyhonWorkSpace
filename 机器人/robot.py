from datetime import datetime

import requests

import json

#使用python -m pip install xxx 安装包

# http://t.weather.sojson.com/api/weather/city/101210101
robot_name ="Ai"
user_name ="主人"

wea_url = 'http://t.weather.sojson.com/api/weather/city/101210101'




def wea():
    res =  requests.get(wea_url)
    tq_data = res.text
    tq_json =json.loads(tq_data)
    tq_wendu = tq_json["data"]["wendu"]
    print("现在的温度是 ",tq_wendu)

def fudu():
    print("输入你需要复读的内容,我会复读三遍")
    words =input()
    for i in range(3):
        print(words)


def hello():
    nt =datetime.now()
    print("""-------------------------""")
    print(nt)
    print("""-------------------------""")
    print("你好我是",robot_name,"""我能为你做点什么?""",user_name)






def AiProcess(cmd):
    if(cmd=="天气"):
        wea()
    elif(cmd=="复读"):
        fudu()