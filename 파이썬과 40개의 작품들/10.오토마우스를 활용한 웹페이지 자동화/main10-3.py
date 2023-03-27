import pyautogui
import time
import pyperclip

# 수원 날씨 화면 자동 캡처 후 저장하는 코드 만들기

#Point(x=993, y=223)
#Point(x=1650, y=880)

pyautogui.moveTo(1251, 210, 0.2) # 좌표로 0.2초 동안 이동합니다.
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("수원 날씨") # 클립보드에 '수원 날씨' 를 저장합니다.
pyautogui.hotkey("ctrl", "v") # 클립보드에 저장된 내용을 붙여넣기 합니다.
time.sleep(0.5)

pyautogui.write(["enter"]) # 엔터키를 입력합니다.
time.sleep(1)

start_x = 993
start_y = 223
end_x = 1650
end_y = 880

pyautogui.screenshot(r'10.오토마우스를 활용한 웹페이지 자동화\수원날씨.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))






