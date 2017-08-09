# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 22:03:41 2017

@author: 310247467
"""

import string
from ctypes import windll
import os
from Tkinter import Tk,Frame,Canvas,Button,LEFT,RIGHT,BOTH
import sqlite3
import sqlitedatabase as sq

globaldictionary={}
def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives

def get_rootfolders(drivename):
    foldernames=os.listdir(drivename)
#    print foldernames
    return [drivename+folder for folder in foldernames]
def get_folders(drivename):
    try:
        foldernames=os.listdir(drivename)
    except Exception as e:
#       print 'error'+str(e)
        return []
    #print foldernames
    return [drivename+'\\'+folder for folder in foldernames]
def get_files(listofnames):
    #print listofnames
    for name in listofnames:
        if os.path.isdir(name):
            get_files(get_folders(name))
        else:
            globaldictionary[name.split('\\')[-1]]=name


if __name__ == '__main__':
    conn=sq.ConnectAndCreate()
    drives=get_drives()
    #print drives
    drives.remove('D')
    drives=[drive+':\\' for drive in drives]
#    print drives
    rootfolders=[get_rootfolders(drive) for drive in drives]
#    print rootfolders
    for rootfolder in rootfolders:
        output=[get_files(get_folders(drive)) for drive in rootfolder]
    #print globaldictionary
    dictlist=[]
    for key, value in globaldictionary.iteritems():
        temp = [key,value]
        dictlist.append(temp)
    sq.LoadToDatabase(conn,dictlist)
    dicton=sq.LoadFromDatabase(conn)
    print dicton
#    top = Tk()
##    top.overrideredirect(True)
#    top.title='guru'
#    # make a frame for the title bar
#    title_bar = Frame(top, bg='white', relief='raised', bd=2)
#    
#    # put a close button on the title bar
#    close_button = Button(title_bar, text='X', command=top.destroy)
#    
#    # a canvas for the main area of the window
#    window = Canvas(top, bg='black')
#    
#    # pack the widgets
#    title_bar.pack(expand=1)
#    close_button.pack(side=RIGHT)
#    window.pack(expand=1, fill=BOTH)
#    #top.wm_attributes('-type', 'splash')
#    top.geometry("500x40")
#    top.mainloop()