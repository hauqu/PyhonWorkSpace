# 函数
# 定义函数
from datetime import datetime

import time
def hello():
    dt =datetime.now()
    
    print("我是Ai\n",dt,"\n")
    print("""
    QQQQ      QQQQ
    Q  Q      Q  Q
    @@@@      @@@@
    	 ！ ！
    
    ——————————————
    
    
    
    """)
    i=0
    while(True):
        print("哈哈哈\n")
        i =i+1
        if(i>=10):
        	break




hello()

import headOrclass as fun

# 可以起一个别名 方便调用

#headOrclass.headHello("二狗子","弱智Ai")
# id(变量名) 返回该变量的地址

print("报上名来")
name =input()
time.sleep(1) #延迟一秒
fun.headHello(name,"stupid ai")
