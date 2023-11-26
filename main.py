# import cv2
# import mediapipe as mp
# import time
# import pyautogui
# import math
#
#
#
# class handDetector():
#     def __init__(self, mode=False, maxHands=1, detectionCon=0.5, trackCon=0.5):
#         self.mode = mode
#         self.maxHands = maxHands
#         self.detectionCon = detectionCon
#         self.trackCon = trackCon
#
#         self.mpHands = mp.solutions.hands
#         self.hands = self.mpHands.Hands(self.mode, self.maxHands,1, self.detectionCon, self.trackCon)
#         self.mpDraw = mp.solutions.drawing_utils
#
#     def findHands(self, img, draw=True):
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         self.results = self.hands.process(imgRGB)
#         # print(results.multi_hand_landmarks)
#
#         if self.results.multi_hand_landmarks:
#             for handLms in self.results.multi_hand_landmarks:
#                 if draw:
#                     self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
#         return img
#
#     def findPosition(self, img, handNo=0, draw=True):
#
#         lmlist = []
#         if self.results.multi_hand_landmarks:
#             myHand = self.results.multi_hand_landmarks[handNo]
#
#             for id, lm in enumerate(myHand.landmark):
#
#
#                 h, w, c = img.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 lmlist.append([id, cx, cy])
#                 if draw:
#                     cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
#         return lmlist
#
#
# def main():
#     pTime = 0
#     cTime = 0
#     cap = cv2.VideoCapture(0)
#     detector = handDetector()
#     success, img = cap.read()
#     sizeScaler1 = pyautogui.size()[0] / img.shape[1]
#     sizeScaler2 = pyautogui.size()[1] / img.shape[0]
#     while True:
#         success, img = cap.read()
#         img = detector.findHands(img)
#         #print(img.shape)
#         lmlist = detector.findPosition(img)
#         if len(lmlist) != 0:
#             #print(lmlist[4])
#
#
#             # print(pyautogui.size())
#             # print(img.shape)
#             # print(sizeScaler1)
#             # print(sizeScaler2)
#             #
#             # # print(pyautogui.size()[1] - (lmlist[4][1] * sizeScaler1))
#             # # print(lmlist[4][2] * sizeScaler2)
#             #
#             # print("Positions on small screen")
#             # #0,0 is the top right o the screen
#             # print(lmlist[8][1]) #x greatest is 640
#             # print(lmlist[8][2]) #y greatest is 480
#
#             pyautogui.moveTo(pyautogui.size()[0] - (lmlist[8][1] * sizeScaler2),lmlist[8][2] * sizeScaler1)
#             #
#             # (960 -(pyautogui.size()[0] - (lmlist[8][1] * sizeScaler2)))*0.01
#             # (540 - lmlist[8][2] * (sizeScaler1))*0.01
#             #
#             #pyautogui.moveRel((960 -(pyautogui.size()[0] - (lmlist[8][1] * sizeScaler2)))*0.001,(540 - lmlist[8][2] * (sizeScaler1))*0.001)
#             if (abs((lmlist[4][1]-lmlist[8][1]) + abs(lmlist[4][2]-lmlist[8][2])+abs(lmlist[4][0]-lmlist[8][0]))<25):
#                 pyautogui.click(pyautogui.size()[0] - (lmlist[8][1] * sizeScaler2), lmlist[8][2] * sizeScaler1)
#
#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime
#
#
#         #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
#
#         #cv2.imshow("Image", img)
#         #cv2.waitKey(1)
#
#
# if __name__ == "__main__":
#     main()
#
#
#


#
#
#
#
#
#
#
#
#


import cv2
import mediapipe as mp
import time
import pyautogui
import math
pyautogui.PAUSE = 0



class handDetector():
    def __init__(self, mode=False, maxHands=1, detectionCon=0.75, trackCon=0.75):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,1, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
        return lmlist


def main():
    pTime = 0
    cTime = 0
    totalTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    framemove = 0
    totalframetime = 0

    isdrag = False

    while True:

        t0 = time.time()




        success, img = cap.read()
        img = detector.findHands(img)

        lmlist = detector.findPosition(img)


        t1 = time.time()
        total = t1 - t0

        print("Time1")
        print(total)

        #print(img.shape)




        if len(lmlist) != 0:

            sizeScaler1 = pyautogui.size()[0]/img.shape[1]
            sizeScaler2 = pyautogui.size()[1]/img.shape[0]
            cTime = time.time()

            pTime = cTime
            timeDifference = cTime - pTime

            totalframetime +=timeDifference
            framemove += 1
            #if (math.pow(abs(lmlist[4][1]-lmlist[8][1]),2) + math.pow(abs(lmlist[4][2]-lmlist[8][2]),2)>20):


            pyautogui.moveTo(pyautogui.size()[0] - (lmlist[8][1] * sizeScaler2), lmlist[8][2] * sizeScaler1)
            # if (framemove%3 == 0):
            #     t2 = time.time()
            #
            #     totalframetime = 0
            #     t3 = time.time()
            #     total2 = t3 - t2
            #
            #     print("Time2")
            #     print(total2)


            #pyautogui.moveTo(pyautogui.size()[0] - (lmlist[8][1] * sizeScaler2),lmlist[8][2] * sizeScaler1)

        #next iteration only move the curosr if we have moved past a certain point/distanc
            totalTime += t1 - t0
            if (math.sqrt(math.pow(abs(lmlist[4][1]-lmlist[8][1]),2) + math.pow(abs(lmlist[4][2]-lmlist[8][2]),2)+math.pow(abs(lmlist[4][0]-lmlist[8][0]),2))<25 and totalTime>1):
                totalTime = 0
                pyautogui.click(pyautogui.size()[0] - (lmlist[8][1] * sizeScaler2), lmlist[8][2] * sizeScaler1)







        #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        #cv2.imshow("Image", img)
        #cv2.waitKey(1)


if __name__ == "__main__":
    main()
