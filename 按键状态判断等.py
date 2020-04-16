'''
尝试用python对大漠插件进行初步的封装
基本的按键和鼠标功能已经能够满足

按键状态判断
'''

from damo import vk
from my_time import Time
#初始化
tt = Time() # 该模块支持64位python

if(1):
    # 判断鼠标右键是否处于按下状态 *右键虚拟按键码 vk_code = 2
    for i in range(100):
        tt.sleep(0.1)
        print(tt.get_key_state(2))  # from win32api import GetKeyState

if(0):
    # 判断 a 是否按下
    for i in range(100):
        tt.sleep(0.1)
        print( tt.get_key_state(vk.a) )

if(0):
    # 组合键判断: Alt + a
    for i in range(100):
        tt.sleep(0.1)

        state = 0
        if(tt.get_key_state(vk.alt)):
            if(tt.get_key_state(vk.a)):
                state = 1
        print(state)
    1


if(0):
    # 按下's'或者按下'p'跳出循环
    for i in range(100):
        tt.sleep(0.1)
        if (tt.stop_0('s', pre_alt=1)):  # 暂停程序,确认后退出,否则继续. 若后者不取 False 则需要 Alt+s 才能触发
            print('break')
            break
        if (tt.stop('p')):  # 直接跳出
            print('break')
            break
        print(i)
    #

if(0):
    # 按下's'跳出双重循环
    for i in range(10):

        try:
            if (break_flag):
                break_flag = 0
                break
        except:
            break_flag = 0

        for j in range(10):
            tt.sleep(0.1)

            print(tt.get_key_state('s'))
            if (tt.stop('s')):  # 确认后再跳出
                break_flag = 1
                print('break')
                break
            else:
                break_flag = 0

            print(i, j)
    1

# sssssssssssssssssssssssssssssssssssssss