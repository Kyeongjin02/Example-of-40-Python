import itertools

# 압축 푸는 코드 만들고 실행

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for len in range(1, 4):
    to_attempt = itertools.product(passwd_string, repeat = len) # a, b, c... ->ab, bc...->abc...
    for attempt in to_attempt:
        passwd = ''.join(attempt) #join(리스트)는 리스트의 값을 문자열로 변환합니다. 
        print(passwd)