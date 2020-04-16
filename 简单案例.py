'''
尝试用python对大漠插件进行初步的封装
基本的按键和鼠标功能已经能够满足
更多功能函数请查阅《大漠接口说明》

后台键鼠模拟以及部分高级功能需要付费，注册后才能使用，我的注册码应该能用很久~
'''
from time import time,sleep
from damo import DM,Mouse,Key,VK
#初始化
dm = DM()
#dm.reg()    #注册
dm.Beep(2000,550)


## 绑定窗口，实现后台键鼠操作。可同时创建多个dm对象
#dm.BindWindow(hwnd,display,mouse,keypad,mode)
#dm.UnBindWindow()


#基本的鼠标操作
ms = Mouse()    #生成一个新的大漠鼠标对象
ms = Mouse(dm)  #继承旧的大漠鼠标对象，用于后台鼠标，建议使用这种

ms.position()   #当前鼠标位置

x, y = (0, 0)
ms.move_to(x, y)    #移动鼠标
ms.LeftClick()  #单击
ms.LeftDoubleClick()    #双击

# 组合功能
sleep(1)
ms.click_left(x, y, 2)  # 左键单击(x,y)位置，按下抬起的间隔为2s
sleep(1)
ms.click_right(x, y, 1) #右键单击(x,y)位置，按下抬起的间隔为1s

# 键盘操作
kk = Key(dm)

kk.test_dp('a', 1)  # 测试用，1秒后按下a键
kk.dp('a')  # 按下a键
kk.test_dp(VK.enter, 1)  # 测试enter键

#全选操作
sleep(1)
kk.down(VK.ctrl)
kk.down('a')
kk.up(VK.ctrl)
kk.up('a')
