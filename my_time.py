# 该模块支持64位python
from time import time
from time import sleep

class Time():
    def __init__(self):

        self.t0 = time()
        self.t1 = time()
        self.time = time
        self.sleep = sleep
        self.now()
        self.break_flag = 0       #break_flag

    def now(self,round_ = 3):

        self.t1 = time()
        now = self.t1 - self.t0
        #now = 3.1415926
        now_r = round(now, round_)
        return now_r

    def exceed(self, T):
        if (self.now() >= T):
            return 1
        else:
            return 0


    def during(self,T):
        if (self.now() <= T):
            return 1
        else:
            return 0

    # 检查是否按下了暂停按键p
    def stop(self,ch='p'):
        ch = ch.upper()

        from win32api import GetKeyState
        nVirtKey = GetKeyState(ord(ch))

        if (nVirtKey == -127 or nVirtKey == -128):      #按下
            self.break_flag = 1
            return 1
        else:
            self.break_flag = 0
            return 0

    def stop_0(self,ch='p', continue_key='p', pre_alt = True):
        # ch = 'a'
        break0 = 0
        ch = ch.upper()

        from win32api import GetKeyState
        from win32gui import MessageBox
        VK_Alt = 18         # alt键的虚拟键盘码

        nVirtKey = GetKeyState(ord(ch))     # 默认按键的状态
        if (nVirtKey == -127 or nVirtKey == -128):
            if (pre_alt):      # 若要求按下alt
                state_vk_alt = GetKeyState(VK_Alt)
                if (state_vk_alt == -127 or state_vk_alt == -128):
                    print('------- Stop! --------')
                    break0 = not (MessageBox(0, 'Do you break?', 'Stop!', 1) - 1)  # 询问是否退出
            else:       #不要求按下alt键
                break0 = not (MessageBox(0, 'Do you break?', 'Stop!', 1) - 1)  # 询问是否退出
            if (break0):
                print('------ Break!!! --------')
                return break0
            else:
                return break0
        else:
            return 0


    def get_key_state(self,ch='p'):
        from win32api import GetKeyState
        try:
            ch = ch.upper()
            nVirtKey = GetKeyState(ord(ch))
        except:
            nVirtKey = GetKeyState(ch)




        if (nVirtKey == -127 or nVirtKey == -128):
            return 1
        else:
            return 0

    def sleep_check_stop(self, t, type = 1, ch = 'p'):
        self.sleep(t)

        if(type):
            self.stop(ch)
        else:
            self.stop_0(ch)

        pass


    1

if __name__ == '__main__':
    tt = Time()

    while(tt.during(20)):
        tt.stop()
        print(tt.now())
        if(tt.break_flag):
            tt.break_flag = 0
            print('---')
            break