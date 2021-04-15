# import the time module
import time
from win10toast import ToastNotifier
  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    # print('Fire in the hole!!')
    toaster = ToastNotifier()
    toaster.show_toast("Alien World", "aight champ, go mine")
  
  
# input time in seconds
t = 470
  
# function call
countdown(int(t))