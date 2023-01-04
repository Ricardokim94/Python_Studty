import itertools
import zipfile


def un_zip(pw_string, min_len, max_len, zFile):
    for len in range(1, 6):
        to_attempt = itertools.product(pw_string, repeat= len)
        for attempt in to_attempt:
            pw = ''.join(attempt) 
            print(pw)
            try:
                zFile.extractall(pw.encode())
                print(f"비밀번호는 {pw}입니다.")
                return 1
                break
            except:
                pass
            
pw_string ="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile(r'4.압축파일 암호 푸는 프로그램\암호1234.zip')

min_len = 1
max_len = 5

unzip_result = un_zip(pw_string, min_len, max_len, zFile)

if unzip_result ==1:
    print("암호찾기에 성공했습니다.")
else :
    print("암호찾기에 실패했습니다.")