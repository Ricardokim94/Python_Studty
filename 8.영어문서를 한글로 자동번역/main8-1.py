import googletrans

translator = googletrans.Translator()

str1 = "행복하세요"
result1 = translator.translate(str1, dest='en' , src='auto') #"행복하세요"를 영어로 번역하여 출력 / dest에 번역될 문자를 입력 
print(f"행복하세요 => {result1.text}")                       #/ src는 en으로 영어로 설정(auto로 해도 영어로 설정)

str2 = "I an happy"
result2 = translator.translate(str2, dest='ko' , src='en')
print(f"I am happy => {result2.text}")