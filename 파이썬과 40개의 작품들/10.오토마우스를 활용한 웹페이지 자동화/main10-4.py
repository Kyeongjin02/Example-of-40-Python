import pyautogui
import time
import pyperclip

weather = ["서울 날씨", "진도 날씨", "용인 날씨"]

#Point(x=1113, y=62)
addr_x = 1113
addr_y = 62
start_x = 993
start_y = 223
end_x = 1650
end_y = 880

for local_weather in weather:
    pyautogui.moveTo(addr_x, addr_y)
    time.sleep(0.2)
    pyautogui.click()
    pyautogui.write("www.naver.com", interval=0.1)
    pyautogui.write(['enter'])
    time.sleep(1)

    pyperclip.copy(local_weather)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.write(['enter'])
    time.sleep(1)
    save_path = '10.오토마우스를 활용한 웹페이지 자동화\\' + local_weather + '.png'
    pyautogui.screenshot(save_path, region=(start_x, start_y, end_x-start_x, end_y-start_y))
