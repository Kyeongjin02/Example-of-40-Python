import googletrans

# 번역 프로그램 코드 만들기 

translator = googletrans.Translator()

str1 = "행복하세요"
result1 = translator.translate(str1, dest='en', src='ko')
print(str1, ':', result1.text)

str2 = "I am happy"
result2 = translator.translate(str2, dest='ko', src='en')
print(str2, ":", result2.text)