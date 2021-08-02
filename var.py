# 지역변수
# 전역변수

gun = 10 

def checkpoint(soldiers):
    # gun = 20 # checkpoint 함수 내에서 선언된 지역변수
    global gun # 전역 변수 gun 사용
    gun -= soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))


# ==> return을 사용해서 global 함수 사용 X

def checkpoint_return(gun, soldiers):
    gun -= soldiers
    print("남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_return(gun, 2)
print("남은 총 : {0}".format(gun))