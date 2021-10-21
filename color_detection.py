

import cv2
import pandas as pd

img_path='c:\\users\\padamati.yesu babu\\downloads\\colorpic.jpg'
csv_path='c:\\users\\padamati.yesu babu\\downloads\\colors.csv'

# reading csv file
index=['color','color_name','hex','R','G','B']
df=pd.read_csv(csv_path, names=index,header=None)

# reading image
img=cv2.imread(img_path)
img=cv2.resize(img,(800,600))

# declaring global variable
clicked=False
r=g=b=xpos=ypos=0
#function to calculate minimum distance from all colors and get the matching color
def get_color_name(R,G,B):
    minium=1000
    for i in range(len(df)):
        d  = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B']))
        if d<= minimum:
                minium = d
                cname = df.loc[i, 'color_name']
                                                                                     
        return cnam
def draw_function(event,x,y,flags,params):
          if event == cv2.EVENT_LBUTTONDBLCK:
              global b,g,r ,xpos, ypos, clicked
              clicked= True
              xpos = x
              ypos = y
              b,g,r = img[y,x]
              b= int(b)
              g= int(g)
              r= int(r)

#creating window
cv2.namedWindow('image')
cv2.setMousecallback('image', draw_function)

while True:
    cv2.imshow('image', img)
    if clicked:
        cv2.rectangle(img,(20,20),(600,60),(b,g,r), -1)

        text=get_color_name(r,g,b)+'R='+str(g)+'B='+str(b)

        cv2.putText(img,text,(50,50),2,0.8, (255,255,255),2,cv2.LINE_AA)
        if r+g+b>=600:
                    cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
    if cv2.waitkey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
                
