import tkinter
from bs4 import BeautifulSoup as bs
from pprint import pprint #pprint=리스트,딕셔너리 등이 길 경우 정리되서 나옴
import requests
import ctypes
import time
import threading
from tkinter import *
from tkinter import ttk

win = Tk()

win.title("Weather affected to Background (WAB)")
win.geometry("380x55")

def changeBG(imagePath):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0,imagePath,0)
    return;

def check():
    html = requests.get('https://search.naver.com/search.naver?query=날씨')  # 페이지의 소스코드 불러옴

    soup = bs(html.text, 'html.parser')  # 보기 좋게 parser로 변환

    weather = soup.find('p', {'class': 'cast_txt'}).text  # 여러개일경우 첫번째것만 가져옴
    weather = weather.split(',')[0]  # '맑음,흐림' 등의 부분만 선택
    print(weather)

    tt = threading.Timer(1, check)

    tt.start()

    def stop():
        tt.cancel()

    button2 = tkinter.Button(win, width=10, height=3, text="STOP", command=stop)
    button2.grid(row=0, column=3)

    global directory

    if weather == '맑음':
        imagePath = directory + "\맑음.jpg"
        changeBG(imagePath)

    elif weather == '구름조금':
        imagePath = directory + "\구름조금.jpg"
        changeBG(imagePath)

    elif weather == '구름많음':
        imagePath = directory + "\구름많음.jpg"
        changeBG(imagePath)

    elif weather == '흐림':
        imagePath = directory + "\흐림.jpg"
        changeBG(imagePath)

    elif weather == '비':
        imagePath = directory + "\비.jpg"
        changeBG(imagePath)

    else:
        imagePath = directory + "\눈.jpg"
        changeBG(imagePath)

button1 = tkinter.Button(win,width=10,height=3,text="START",command=check)
button1.grid(row=0,column=1)

e1 = Entry(win)
e1.grid(row=0,column=5)

drirectory = ""

def dir():
    global directory
    directory = str(e1.get())

button3 = tkinter.Button(win,width=10,height=3,text="설정",command=dir)
button3.grid(row=0,column=6)


win.mainloop()