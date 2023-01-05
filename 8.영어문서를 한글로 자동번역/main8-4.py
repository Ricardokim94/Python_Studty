#번역 내용을 새 파일로 저장하는 코드

from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r"8.영어문서를 한글로 자동번역\영어파일.txt"
write_file_path = r"8.영어문서를 한글로 자동번역\한글파일.txt"

with open(read_file_path, 'r') as f:
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    with open(write_file_path, 'a', encoding='UTF-8') as f:  #a 는 마지막에 추가로 쓰는 모드이다. 한글을 사용하기 위해 encoding=UTF-8 옵션을 넣었다
        f.write(result1.text + '\n')
    
    