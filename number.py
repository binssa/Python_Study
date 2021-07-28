from math import *
from random import *

print(abs(-5)) # 절대값 
print(pow(4, 2)) # 4^2
print(max(5, 12))  # 12
print(min(5, 12))  # 5
print(round(3.14)) # 3
print(round(4.99)) # 5


print(floor(4.99)) # 4 (내림)
print(ceil(3.14))  # 4 (올림)
print(sqrt(16)) # 4 (제곱근)


print(random()) # 0.0 ~ 1.0 미만의 임의의값 생성
print(random()* 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))
print(int(random() * 10) + 1)

# 로또 번호 생성
print("#1 : " + str(int(random() * 45) + 1))
print("#2 : " + str(int(random() * 45) + 1))
print("#3 : " + str(int(random() * 45) + 1))
print("#4 : " + str(int(random() * 45) + 1))
print("#5 : " + str(int(random() * 45) + 1))
print("#6 : " + str(int(random() * 45) + 1))

# 로또 번호 생성 ver 2
print(randrange(1, 46)) # 1 ~ 46 미만
print(randint(1, 45)) # 양쪽의 숫자 포함 (즉, 1~45)

# Quiz 
number = str(randint(4,28)) 
print("오프라인 스터디 모임 날짜는 매월 "+ number + "일로 선정되었습니다.")