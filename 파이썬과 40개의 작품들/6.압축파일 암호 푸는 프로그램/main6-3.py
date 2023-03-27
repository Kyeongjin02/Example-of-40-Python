import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len+1):
        to_attempt = itertools.product(passwd_string, repeat = len)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            print(passwd)
            try:
                zFile.extractall(pwd = passwd.encode())
                print("비밀번호는 {} 입니다.".format(passwd))
                return 1
            except:
                pass

passwd_string = "0123456789" # 암호 숫자로 가정

zFile = zipfile.ZipFile(r"6.압축파일 암호 푸는 프로그램\암호1234.zip")

# 비밀번호 4~5자리 가정
min_len = 4
max_len = 5

unzip_result = un_zip(passwd_string, min_len, max_len, zFile)