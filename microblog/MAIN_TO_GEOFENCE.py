# -*- coding: utf-8 -*-
from tkinter import *
import calendar
import time
import datetime
import http.client
import urllib
import json
import ast
import csv
import sys
import codecs
import sched, time
import threading
import xlwt
import xlrd
#https://vk.com/dev/newsfeed.search?params[q]=%D0%93%D0%B0%D1%82%D1%87%D0%B8%D0%BD%D0%B0&params[extended]=0&params[count]=200&params[v]=5.95
#https://vk.com/dev/photos.search?params[lat]=60.275458&params[long]=30.557796&params[start_time]=1517494966&params[end_time]=1519827766&params[count]=100&params[radius]=100&params[v]=5.73
def get_vk(q, count):
    get_request =  '/method/newsfeed.search?q=' + str(q)
    get_request+= '&extended=0&count' + str(count)
    get_request+= '&v=5.95'
    get_request+= '&access_token=cca64ed929c1212f14e398d1e477e3ff75735cb83cf9630929ec724056978fbdb565a17df12f531ea0c0c'
    local_connect = http.client.HTTPSConnection('api.vk.com', 443)
    local_connect.request('GET', get_request)
    return local_connect.getresponse().read()
ccc=get_vk('Гатчина'.encode('utf-8'),200)
pp=json.loads(ccc)
print (len(pp['response']))
if 'response' in pp:
    texts=[]
    j=0
    while j<len(pp['response']['items']):
        texts.append(pp['response']['items'][j]['text'].encode('utf-8'))
        #print ((pp['response']['items'][0]['from_id']))
        #print ((pp['response']['items'][0]['date']))
        #print ((pp['response']['items'][0]['text'].encode('utf-8')))
        #print ((pp['response']['items'][0]['comments']['count']))
        #print ((pp['response']['items'][0]['likes']['count']))
        j=j+1
print (texts)
"""
def get_vk_foto(location_latitude, location_longitude, distance, min_timestamp, max_timestamp):
    get_request =  '/method/photos.search?lat=' + str(location_latitude)
    get_request+= '&long=' + str(location_longitude)

    get_request+= '&start_time=' + str(min_timestamp)
    get_request+= '&end_time=' + str(max_timestamp)
    get_request+= '&count=1000'
    get_request+= '&radius=' + str(distance)
    get_request+= '&v=5.73'
    get_request+= '&access_token=cca64ed929c1212f14e398d1e477e3ff75735cb83cf9630929ec724056978fbdb565a17df12f531ea0c0c'
    local_connect = http.client.HTTPSConnection('api.vk.com', 443)
    local_connect.request('GET', get_request)
    return local_connect.getresponse().read()
def execute():
    print (e10.get())
    print (e6.get())
    print (e7.get())
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2
    font0.bold = True

    style0 = xlwt.XFStyle()
    style0.font = font0
    s = sched.scheduler(time.time, time.sleep)
    latitude1= e6.get()#"43.671829"
    longitude1=e7.get()#"40.297253"
    distance1=e10.get()
    min_timestamp1=int(time.mktime(datetime.datetime.strptime(e8.get(), "%d-%m-%Y %H:%M:%S").timetuple()))
    max_timestamp1=int(time.mktime(datetime.datetime.strptime(e9.get(), "%d-%m-%Y %H:%M:%S").timetuple()))
    ccc=get_vk_foto(latitude1, longitude1, distance1, min_timestamp1, max_timestamp1)
    #print (type(ccc))
    pp=json.loads(ccc)

    #pp = ast.literal_eval(ccc)
    j=0
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    ws.write(0, 0,'x',style0)
    ws.write(0, 1,'y',style0)
    ws.write(0, 2,'time',style0)
    ws.write(0, 3,'id',style0)
    ws.write(0, 4,'fotolink',style0)
    #f = open('helloworld3333.html','w')
    xx=list()
    yy=list()
    #file_inst = open('vk GEO:'+str(location_latitude)+str(location_longitude)+'.html','w')
    #file_inst.write('<html>')
    if 'response' in pp:
        
        #print len(pp['response'][1])
        #print pp['response'][1]['src_small']
        print (u"Найдено геометок: ", len(pp['response']['items']))
        
        while j<len(pp['response']['items']):
            y=str(pp['response']['items'][j]['long'])
            x=str(pp['response']['items'][j]['lat'])
            yy.append(y)
            xx.append(x)

                 
            #urllib.urlretrieve(str(pp['response'][j]['src_big']), (str(j)+".jpg"))

            ws.write(j+1, 0, x)
            ws.write(j+1, 1, y)
            ws.write(j+1, 2, str(datetime.datetime.fromtimestamp(int(pp['response']['items'][j]['date'])).strftime('%d-%m-%Y %H:%M:%S')))
            ws.write(j+1, 3, str(int(pp['response']['items'][j]['owner_id'])))
            ws.write(j+1, 4, str(pp['response']['items'][j]['photo_604']))                      
            print (j+1, pp['response']['items'][j]['photo_130'])
            #file_inst.write('<br>')
            j=j+1
    wb.save('VK.xls')
    i=1
    file_inst = open('vk.html','w')
    file_inst.write('<html>')
    rb = xlrd.open_workbook('VK.xls',formatting_info=True)
    sheet = rb.sheet_by_index(0)
    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
        file_inst.write('<br>')
        file_inst.write('<img src='+row[4]+'><br>')
        file_inst.write('http://vk.com/id'+row[3]+'<br>')
        file_inst.write('<br>')
        i=i+1
    file_inst.write('</html>')


def show_entry_login():
    if e1.get()=='admin' and e2.get()=='aBram!1':
        e4.insert(END, u'Верный пароль')
    else:
        e4.insert(END, u'Не верный пароль')
    
def show_entry_fields():
    if e1.get()=='admin' and e2.get()=='aBram!1':
        a=1569888000   
        if int(time.time())<a:
            
                execute()

    else:
        e4.insert(END, u'Не верный пароль')
master = Tk()
master.title(u'Грета')
Label(master, text=u"Логин").grid(row=0, column=0)
Label(master, text=u"Пароль").grid(row=0, column=2)
Label(master, text=u"Проверка").grid(row=1, column=1)
#Label(master, text=u"Выберете социальную сеть").grid(row=6, column=0)
#Label(master, text=u"Ключ доступа").grid(row=6, column=2)
Label(master, text=u"X").grid(row=8, column=0)
Label(master, text=u"Y").grid(row=9, column=0)
Label(master, text=u"Начало:").grid(row=8, column=2)
Label(master, text=u"Конец:").grid(row=9, column=2)
Label(master, text=u"Задача координат").grid(row=7, column=1)
Label(master, text=u"Задача времени").grid(row=7, column=3)
Label(master, text=u"Погрешность (метры)").grid(row=10, column=0)
e1 = Entry(master)
e2 = Entry(master)
e3=Entry(master)
e4=Text(master, height=1, width=10)
e5=Text(master, height=1, width=10)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e10 = Entry(master)
e1.grid(row=0, column=1, sticky=N, padx=5, pady=10)
e2.grid(row=0, column=3, sticky=N, padx=5, pady=10)
#e3.grid(row=6,column=3)
e4.grid(row=1,column=2, columnspan=1, sticky=W+E+S, pady=5)
#e5.grid(row=7,column=2, columnspan=2, sticky=W+E+S, pady=5)
e6.grid(row=8,column=1, columnspan=1, sticky=W+E+S, pady=5)
e7.grid(row=9,column=1, columnspan=1, sticky=W+E+S, pady=5)
e8.grid(row=8,column=3, columnspan=1, sticky=W+E+S, pady=5)
e9.grid(row=9,column=3, columnspan=1, sticky=W+E+S, pady=5)
e10.grid(row=10,column=1, columnspan=1, sticky=W+E+S, pady=5)
#var = StringVar(master)
#var.set("---\\---")
#option = OptionMenu(master, var, u"Вконтакте", u"Одноклассники","Facebook", "Instagram", "Twitter")
#option.grid(row=6, column=1, sticky=N+W+E+S, pady=5)
Button(master, text=u'Зайти', command=show_entry_login).grid(row=1, column=0, sticky=N+W+E+S, pady=4)#
Button(master, text=u'Старт', command=show_entry_fields).grid(row=12, column=5, sticky=N+W+E+S, pady=4)
mainloop( )
"""
