import itertools
import zipfile

# 압축파일 암호푸는 프로그램 

passwd_string = "0123456789" # 암호 숫자로 가정

zFile = zipfile.ZipFile(r"6.압축파일 암호 푸는 프로그램\암호1234.zip")

# 암호를 찾아서 break를 걸어도 두개의 for문중 하나만 break가 걸리기때문에 출력이 종료되지 않음
for len in range(4, 6):
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:
            zFile.extractall(pwd = passwd.encode())
            print("비밀번호는 {} 입니다.".format(passwd))
            break
        except:
            pass