import time
from utils.clear_terminal import clear_terminal

def pause(secs):
  time.sleep(secs)
  clear_terminal()