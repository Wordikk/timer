from tkinter import *
import time
from playsound import playsound

file = open("czas.txt", 'w')
root = Tk()
root.geometry('400x300')
root.resizable(0, 0)
root.config(bg='blanched almond')
root.title('Minutnik')
Label(root, text='Minutnik', font='arial 20 bold', bg='papaya whip').pack()

Label(root, font='arial 15 bold', text='aktualny czas:', bg='papaya whip').place(x=40, y=70)

file.write("Godzina włączenia minutnika: " + time.strftime('%H:%M:%S'))
file.close()


def clock():
    clock_time = time.strftime('%H:%M:%S')
    current_time.config(text=clock_time)
    current_time.after(1000, clock)


current_time = Label(root, font='arial 15 bold', text='', fg='gray25', bg='papaya whip')
current_time.place(y=70, x=190)
clock()

sec = StringVar()
Entry(root, textvariable=sec, width=2, font='arial 12').place(x=275, y=155)
Label(root, font='arial 12', text='s', fg='gray25', bg='papaya whip').place(x=300, y=155)
sec.set('00')
min = StringVar()
Entry(root, textvariable=min, width=2, font='arial 12').place(x=215, y=155)
Label(root, font='arial 12', text='min', fg='gray25', bg='papaya whip').place(x=240, y=155)
min.set('00')
hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font='arial 12').place(x=165, y=155)
Label(root, font='arial 12', text='h', fg='gray25', bg='papaya whip').place(x=190, y=155)
hrs.set('00')


def countdown():
    times = int(hrs.get()) * 3600 + int(min.get()) * 60 + int(sec.get())
    while times > -1:
        minute, second = (times // 60, times % 60)

        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)

        sec.set(second)
        min.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)
        if times == 0:
            playsound('Alarm.mp3')
            sec.set('00')
            min.set('00')
            hrs.set('00')
        times -= 1


Label(root, font='arial 15 bold', text='ustaw czas', bg='papaya whip').place(x=40, y=150)
Button(root, text='START', bd='5', command=countdown, bg='antique white', font='arial 10 bold').place(x=150, y=210)

root.mainloop()
