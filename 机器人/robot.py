from datetime import datetime

import requests

#使用python -m pip install xxx 安装包

# http://t.weather.sojson.com/api/weather/city/101210101
robot_name ="Ai"
user_name ="主人"

wea_url = 'http://t.weather.sojson.com/api/weather/city/101210101'


def wea():
    res = requests.get(wea_url)
    da =res.text()
    print(da)

def hello():
    nt =datetime.now()
    print("""-------------------------""")
    print(nt)
    print("""-------------------------""")
    print("你好我是",robot_name,"""我能为你做点什么?""",user_name)

def AiProcess(cmd):
    if(cmd=="天气"):
        wea()
    else :
        print("我不明白")