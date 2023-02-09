import re

street = '21 Teheran Road'
print(re.sub("Road", "Rd", street)) #re.sub함수는 Road를 Rd로 축약할 수 있게 해준다. 입력은 문자열 객체 street이다.

text = "Diwali is a festival of light, Holi is a festival of color!"
print(re.findall(r"\b\w{5}\b", text)) #\b~~\b는 경계집합을 사용해 단어와 {}표기법 사이의 경계를 식별해 다섯글자인 단어만 단락 표시한다.