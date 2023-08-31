# 조건1 대문자, 소문자, 특수문자(!@#$로 제한), 숫자 각각 1자 이상
# 조건2 비밀번호 자릿수 기본값 10(조절 가능)
# 조건3 같은 문자 3회 연속 x
# 조건4 txt 파일 만들어서 비밀번호 저장

import random, string
from datetime import date

def generate_password(symbol=None, save=True, path="./password.txt", k=10):
    # 기본 특수문자
    if symbol is None:
        symbol = "!@#$"

    while True:
        # create password
        password = ''.join(random.choices(string.ascii_letters + string.digits + symbol, k=k))

        # check password
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in symbol for c in password) and
            not any(c * 3 in password for c in set(password))):
            break
        
    # 저장여부 확인 및 저장
    if save:
        with open(path, "a") as f:
            data = str(date.today()) + ": " + password
            f.write(data + "\n")
        
    return password

password = generate_password(k=16)
print(password)