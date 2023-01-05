import pyautogui
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__))) #pyautogui에서는 한글을 인식하지 못하여 경로를 이동함.

picPosition = pyautogui.locateOnScreen('pic1.png') #pic1.png 파일과 동일한 그림을 찾아 좌표를 출력합니다.
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic2.png') #pic2.png 파일과 동일한 그림을 찾아 좌표를 출력합니다.
    print(picPosition)
if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic3.png') #pic3.png 파일과 동일한 그림을 찾아 좌표를 출력합니다.
    print(picPosition)