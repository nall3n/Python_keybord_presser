from SMWinservice import SMWinservice




import time
import datetime
import pyautogui


#run_time = datetime.datetime(2024,2,26,14,31,0)
#delta_time = datetime.timedelta(days=1)


#run = True



def press_button():
    pyautogui.press('1')
    pyautogui.press('enter')


class Auto_key_klicker(SMWinservice):
    _svc_name_ = 'Auto_clicker1'
    _svc_description_ = 'Klicks button 1 and Enter once a day'
    _svc_display_name_ = 'Auto clicker'

    def start(self):
        self.isrunning = True
        self.run_time = datetime.datetime(2024,2,26,14,40,0)
        self.delta_time = datetime.timedelta(minutes=1)



    def stop(self):
        self.isrunning = False

    def main(self):
        
        while self.isrunning: 
            if datetime.datetime.now() >= self.run_time:
                press_button()
                self.run_time += self.delta_time
                print(self.run_time)




if __name__ == '__main__':
    Auto_key_klicker.parse_command_line()