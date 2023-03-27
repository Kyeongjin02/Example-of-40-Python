import pyautogui
import time
import pyperclip

# 네이버에서 자동으로 수원 날씨 검색하는 코드 만들기
#Point(x=1251, y=210)
pyautogui.moveTo(1251, 210, 0.2) # 좌표로 0.2초 동안 이동합니다.
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("수원 날씨") # 클립보드에 '수원 날씨' 를 저장합니다.
pyautogui.hotkey("ctrl", "v") # 클립보드에 저장된 내용을 붙여넣기 합니다.
time.sleep(0.5)

pyautogui.write(["enter"]) # 엔터키를 입력합니다.
time.sleep(1)
