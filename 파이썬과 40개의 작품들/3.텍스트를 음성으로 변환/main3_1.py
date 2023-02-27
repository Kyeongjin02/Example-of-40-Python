from gtts import gTTS

text = "안녕하세요 저는 김경진 입니다."

tts = gTTS(text=text, lang='ko')
tts.save(r"파이썬과 40개의 작품들\3.텍스트를 음성으로 변환\hi2.mp3")