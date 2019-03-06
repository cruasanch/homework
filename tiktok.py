"""Здесь задача состоит в том, что бы сделать часы, которые на каждой 10 секунде издают звук"""
import time
import winsound
i = 0
winsound.Beep(2500,1000)
print(time.strftime("%H:%M:%S", time.localtime()))
time.sleep(1)
while True:
    print(time.strftime("%H:%M:%S", time.localtime()))
    i += 1
    if i == 10:
        winsound.Beep(2500,1000)
        i = 0
    else:
        time.sleep(1)