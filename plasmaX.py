#!/usr/bin/python3
# coding: utf-8
#  **__**__***********_********_*********_____******_*****************_***
#  *|**\/**|*********|*|******(_)*******|**__*\****|*|***************|*|**
#  *|*\**/*|*__*_**__|*|*___***_*_*__***|*|__)*|__*|*|*__*_*_*__***__|*|**
#  *|*|\/|*|/*_`*|/*_`*|/*_*\*|*|*'_*\**|**___/*_*\|*|/*_`*|*'_*\*/*_`*|**
#  *|*|**|*|*(_|*|*(_|*|**__/*|*|*|*|*|*|*|**|*(_)*|*|*(_|*|*|*|*|*(_|*|**
#  *|_|**|_|\__,_|\__,_|\___|*|_|_|*|_|*|_|***\___/|_|\__,_|_|*|_|\__,_|**
#  *********************_****************_***___***___*___***___*****_****
#  *****/\*************|*|************/\|*|/\__*\*/*_*\__*\*/*_*\*/\|*|/\*
#  ****/**\***_*__***__|*|_***_*******\*`*'*/**)*|*|*|*|*)*|*|*|*|\*`*'*/*
#  ***/*/\*\*|*'_*\*/*_`*|*|*|*|*****|_*****_|/*/|*|*|*|/*/|*|*|*|_*****_|
#  **/*____*\|*|*|*|*(_|*|*|_|*|******/*,*.*\/*/_|*|_|*/*/_|*|_|*|/*,*.*\*
#  */_/****\_\_|*|_|\__,_|\__,*|******\/|_|\/____|\___/____|\___/*\/|_|\/*
#  ************************__/*|******************************************
#  ***********************|___/*******************************************
import math
from curses import wrapper
from time import sleep
import curses 
from numpy import arange



def main(ekr):
    pi=3.14159
    figura=0
    xx=0
    yy=0
    zz=15
    x=0
    y=0
    ekr.clear()
    curses.curs_set(0)


    zakres_y,zakres_x = ekr.getmaxyx()
    six=[]
    element=zakres_x-1
    sx=0
    for sx in arange(0,3.14159*2,3.14159*2/element):
        six.append(math.sin(sx)*11+11)
    def kolorowy():
            

        store_x=0
        store_y=int(element/3)
        store_x2=int(element/4)
        store_y2=int(element/7)
        xb=store_x
        xs=1
        xd=1
        yb=store_y
        ys=1
        yd=1
        xl=-1
        yl=-2
        col=1
        lista_kolorow=[[0,0,0],[500,0,0],[500,250,0],[500,500,0],[500,750,0],[0,1000,0],[0,750,250],[0,500,500],[0,250,750],[150,0,1000],[500,0,500],[750,0,250],[500,0,0],[500,250,0],[500,500,0],[500,750,0],[0,1000,0],[0,750,250],[0,500,500],[0,250,750],[150,0,1000],[500,0,500],[750,0,250]]
        
        zakres_figury=len(lista_kolorow)

        for intense in lista_kolorow:
            curses.init_color(col,intense[0],intense[1],intense[2])
            col=col+1
        
        for col in range(1,len(lista_kolorow)):
            curses.init_pair(col,col+10,col)
            
        while True:
            xs=-1
            xd=1
            xs2=-2
            xd2=1
            
            ys=2
            yd=2
            ys2=4
            yd2=-1
            
            store_x=store_x+xs
            store_x2=store_x2+xs2
            
            store_y=store_y+ys
            store_y2=store_y2+ys2
            
            if(store_x>=element):
                store_x=store_x-element
            if(store_x<0):
                store_x=store_x+element            
            if(store_x2>=element):
                store_x2=store_x2-element
            if(store_x2<0):
                store_x2=store_x2+element

            if(store_y>=element):
                store_y=store_y-element
            if(store_y<0):
                store_y=store_y+element    
            if(store_y2<0):
                store_y2=store_y2+element
            if(store_y2>element):
                store_y2=store_y2-element
                
            xb=store_x
            yb=store_y
            xb2=store_x2
            yb2=store_y2
            
            for y in range(0,zakres_y-1):
                yb=yb+yd
                if(yb>=element):
                    yb=yb-element
                if(yb<0):
                    yb=yb+element
                yb2=yb2+yd2
                if(yb2>=element):
                    yb2=yb2-element
                if(yb2<0):
                    yb2=yb2+element
                    
                for x in range(0,zakres_x-1):
                    xb=xb+xd
                    if(xb>=element):
                        xb=xb-element
                    if(xb<0):
                        xb=xb+element
                    xb2=xb2+element
                    if(xb2>=element):
                        xb2=xb2-element
                    if(xb2<0):
                        xb2=xb2+element
                   
                    z=int((six[xb]+six[xb2]+six[yb]+six[yb2])/3.9)
                    ekr.addch(y,x,chr(9629),curses.color_pair(z+2))
            ekr.refresh()
            sleep(.016)

    def czarny():
        gr=["0","#", "H","=","+","⢿","⢾","⢽","⢻","⢺","⢹","⢸","⢷","⢶","⢵","⢴"]
        pi=3.14159
        figura=0
        xx=0
        yy=0
        zz=15
        x=0
        y=0
        ekr.clear()
        curses.curs_set(0)


        zakres_y,zakres_x = ekr.getmaxyx()
        element=zakres_x+1
        six=[]
        sx=0
        #nowy sposob:
        store_x=0
        store_y=int(element/3)
        store_x2=int(element/4)
        store_y2=int(element/7)
        xb=store_x
        xs=1
        xd=1
        yb=store_y
        ys=1
        yd=1
        xl=-1
        yl=-2
        col=1
        lista_kolorow=[]
        
        zakres_figury=int(len(gr)/2)
        for sx in arange(0,pi*2,pi*2/element):
            six.append(math.sin(sx)*zakres_figury+zakres_figury)

        while True:
            xs=-1
            xd=1
            xs2=-2
            xd2=1
            
            ys=2
            yd=2
            ys2=4
            yd2=-1
            
            store_x=store_x+xs
            store_x2=store_x2+xs2
            
            store_y=store_y+ys
            store_y2=store_y2+ys2
            
            if(store_x>=element):
                store_x=store_x-element
            if(store_x<0):
                store_x=store_x+element            
            if(store_x2>=element):
                store_x2=store_x2-element
            if(store_x2<0):
                store_x2=store_x2+element

            if(store_y>=element):
                store_y=store_y-element
            if(store_y<0):
                store_y=store_y+element    
            if(store_y2<0):
                store_y2=store_y2+element
            if(store_y2>element):
                store_y2=store_y2-element
                
            xb=store_x
            yb=store_y
            xb2=store_x2
            yb2=store_y2
            
            for y in range(0,zakres_y-1):
                yb=yb+yd
                if(yb>=element):
                    yb=yb-element
                if(yb<0):
                    yb=yb+element
                yb2=yb2+yd2
                if(yb2>=element):
                    yb2=yb2-element
                if(yb2<0):
                    yb2=yb2+element
                    
                for x in range(0,zakres_x-1):
                    xb=xb+xd
                    if(xb>=element):
                        xb=xb-element
                    if(xb<0):
                        xb=xb+element
                    xb2=xb2+element
                    if(xb2>=element):
                        xb2=xb2-element
                    if(xb2<0):
                        xb2=xb2+element
                   
                    z=int((six[xb]+six[xb2]+six[yb]+six[yb2])/4)
                    ekr.addch(y,x,gr[z])
            sleep(.016)
            ekr.refresh()
                      
    if(curses.can_change_color()==1):
        kolorowy()
    else:
        czarny()
    ekr.getkey()
wrapper(main)
 
