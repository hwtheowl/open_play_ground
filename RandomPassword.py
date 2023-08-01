# 조건1 대문자, 소문자, 특수문자, 숫자 각각 1자 이상
# 조건2 총 10자
# 조건3 같은 문자 3회 연속 x

import random
import string

def generate_password():
    limited_special_chars = "!@#$%^"
    while True:
        password = ''.join(random.choices(string.ascii_letters + string.digits + limited_special_chars, k=10))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in limited_special_chars for c in password) and
            not any(c * 3 in password for c in set(password))):
            return password

password = generate_password()
print(password)