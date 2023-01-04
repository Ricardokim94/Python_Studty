from gtts import gTTS
from playsound import playsound

text = "안녕하세요. 파이썬 입니다."

tts = gTTS(text=text, lang='ko')
tts.save(r"2.텍스트를 음성으로 변환하기\hi.mp3")