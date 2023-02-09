import re

raw = "I am big! It's the pictures that got small"
print(re.split(r' +', raw))
print()
print(re.split(r'\W+', raw)) #W가 대문자여야 단어들로 출력
print(re.findall(r'\w+|\S\w*',raw))
