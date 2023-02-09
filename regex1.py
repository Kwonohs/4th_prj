import re

def text_match(text, patterns):
    if re.search(patterns, text):
        return("일치하는 항목을 찾았습니다!")
    else:
        return("일치하지 않음!")

print(text_match("ac", "ab?")) #정규표현식 ?는 {0,1}의 의미 있어도 되고 없어도되고
print(text_match("abc","ab?"))
print(text_match("abbc","ab?"))
print(text_match("ac","ab*")) #*는 곱하기 반복 0~n까지 곱한수만큼 있어야한다.
print(text_match("abc","ab*"))
print(text_match("abbc","ab*"))
print(text_match("ac","ab+")) #+는 0을 더해도 b가 있어야하고 b가 몇개 있어도 된다.
print(text_match("abc","ab+"))
print(text_match("abbc","ab+"))

print("ab{2}")


