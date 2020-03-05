'''
尝试用python对大漠插件进行初步的封装
基本的按键和鼠标功能已经能够满足

后台键鼠模拟以及部分高级功能需要付费，注册后才能使用，我的注册码可能用不太久~
'''

from damo import DM,Mouse,Key,VK
#初始化
dm = DM()
#dm.reg()    #注册

#基本的鼠标操作
ms = Mouse()    #生成一个新的大漠鼠标对象
ms = Mouse(dm)  #继承旧的大漠鼠标对象，用于后台鼠标
ms = Mouse()

ms.position()   #当前鼠标位置

x, y = (0, 0)
ms.move_to(x, y)
sleep(1)
ms.click_left(x, y, 2)  #单击左键，按下抬起的间隔为2s
sleep(1)
ms.click_right(x, y, 1) #单击右键，按下抬起的间隔为1s

# 键盘操作
kk = Key(dm)
kk.test_dp('a', 1)  # 测试用，1秒后按下a键
kk.dp('a')  # 按下a键
kk.dp(VK.enter) # 按下enter键