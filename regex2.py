import re
def text_match(text, patterns):
    if re.search(patterns, text):
        return("일치하는 항목을 찾았습니다!")
    else :
        return("일치하지 않음!")


print("테스트 패턴은 다음으로 시작하고 끝남")
print(text_match("abbc", "^a.*c$")) #a와 c사이의 문자가 있고 c는 반복

print("단어로 시작함")
print(text_match("Tuffy eats pie, Loki eats peas!", "^\w+")) #\w는 영숫자를 표기하는 표현식
