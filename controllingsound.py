import cv2
import mediapipe as mp

from pynput.keyboard import Key,Controller

import pyautogui

mykeyboard=Controller()

state=None

video=cv2.VideoCapture(0)
width=int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width,height)

# to draw hands
myhands=mp.solutions.hands

# to display landmarks
mydrawing=mp.solutions.drawing_utils


hand_obj=myhands.Hands(min_detection_confidence=0.75,
                        min_tracking_confidence=0.75  	)
print("what is hand obj ",hand_obj)

def countFingers(lst):
   count=0
   global state

   thresh=(lst.landmark[0].y*100-lst.landmark[9].y*100)/2
   #print("what is thresh ",thresh)#


   if(lst.landmark[5].y*100-lst.landmark[8].y*100)>thresh:
      count+=1

   if(lst.landmark[9].y*100-lst.landmark[12].y*100)>thresh:
      count+=1  

   if(lst.landmark[13].y*100-lst.landmark[16].y*100)>thresh:
      count+=1

   if(lst.landmark[17].y*100-lst.landmark[20].y*100)>thresh:
      count+=1

   # if(lst.landmark[5].x*100-lst.landmark[4].x*100)>thresh:
   #    count+=1  

   totalfingers=count

   if totalfingers==4:
      state="play"
   if totalfingers==0 and state=="play" or state=="backward" or state=="forward":
      state="pause"
      mykeyboard.press(Key.space) 

   print("what is state",state)   
   finger_tip_x=(lst.landmark[8].x)*width
   if totalfingers ==1:
      if finger_tip_x<width-400:
         state="backward"
         mykeyboard.press(Key.left)
      if finger_tip_x>width-100:
         state="forward"
         mykeyboard.press(Key.right)   
      
   finger_tip_y=(lst.landmark[8].y)*height 
   if totalfingers==2:
      if finger_tip_y<height-250:
         print("Increase volume")
         pyautogui.press("volumeup") 
      if finger_tip_y>height-250:
         print("Decrease volume")
         pyautogui.press("volumedown")   

   return totalfingers 



while True:
    dummy,image=video.read()
    flipimage=cv2.flip(image,1)

    result=hand_obj.process(cv2.cvtColor(flipimage,cv2.COLOR_BGR2RGB))

    if result.multi_hand_landmarks:
        hand_keyPoints=result.multi_hand_landmarks[0]
        print(hand_keyPoints)
        count=countFingers(hand_keyPoints)
        print("what is fingercount",count)
        cv2.putText(flipimage,"Fingures "+str(count),(200,100),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)
        cv2.putText(flipimage,"state "+str(state),(100,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)



        print(count)
        mydrawing.draw_landmarks(flipimage,hand_keyPoints,myhands.HAND_CONNECTIONS)
    cv2.imshow("handgestures",flipimage)    

    key=cv2.waitKey(1)
    if key==27:
     break

video.release()
cv2.destroyAllWindows()
