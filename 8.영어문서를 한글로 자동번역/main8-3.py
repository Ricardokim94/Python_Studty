from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r"8.영어문서를 한글로 자동번역\영어파일.txt"

with open(read_file_path, 'r') as f: #파일을 줄별로 읽어 readlines에 리스트 형식으로 바인딩 합니다.
    readLine = f.readlines()         
    
for lines in readLine:                 #리스트형태로 저장된 readLines에서 한 줄씩 한글로 변환하여 출력합니다.
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)