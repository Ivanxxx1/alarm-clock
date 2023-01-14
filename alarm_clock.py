import time
import pyglet



print("Привет! Что бы установить вреям будильника напиши его в таком формате: HH:MM:SS")
alarm_time = str(input())


while True:
    if len(alarm_time) != 8:
        print("Даже будильник установить не можешь? Попробуй ещё раз")
        alarm_time = str(input())
    elif alarm_time[3] != ":" and alarm_time[5] != ":":
        print("Даже будильник установить не можешь? Попробуй ещё раз")
        alarm_time = str(input())
    elif int(alarm_time[0:2]) > 23:
        print("Даже будильник установить не можешь? Попробуй ещё раз")
        alarm_time = str(input())
    elif int(alarm_time[3:5]) > 59:
        print("Даже будильник установить не можешь? Попробуй ещё раз")
        alarm_time = str(input())

    elif int(alarm_time[6:8]) > 59:
        print("Даже будильник установить не можешь? Попробуй ещё раз")
        alarm_time = str(input())
    else:
        print(f"Будильник установлен на: {alarm_time}")
        break
        
        
        
while True:
    now = str(time.ctime())
    now = now[11:19]
    if int(now[0:2]) == int(alarm_time[0:2]):
        if int(now[3:5]) == int(alarm_time[3:5]):
            if int(now[6:8]) == int(alarm_time[6:8]):
                print("Вставай!")
                music = pyglet.resource.media(r"SONG.mp3")
                music.play()
                pyglet.app.run()