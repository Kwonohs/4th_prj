import re

url = "http://www.telegraph.co.uk/formula-1/2018/10/28/mexican-grand-prix-2017-time-does-start-tv-channel-odds-lewis1/"
date_regex = '/(\d{4})/(\d{1,2})/(\d{1,2})/' #\d는 0~9의 숫자를 의미

print("URL에서 찾은 날짜 :", re.findall(date_regex, url))

def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]') #영어 소문자와 대문자, .까지를 표현
    #k = "[^a-zA-Z0-9.]"
    string = charRe.search(string)
    return not bool(string)


print(is_allowed_specific_char("ABC123."))
print(is_allowed_specific_char("*@(#!"))
