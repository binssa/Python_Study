def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

# 전달값과 반환값
def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance + money


def withdraw(balance, money): # 출금
    if balance >= money :
        print("출금이 완료되었습니다. 잔액은 {0}입니다.".format(balance-money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다.")
        return balance
balance = 0
balance = deposit(balance, 1000)
print(balance)
withdraw(balance, 2000)
print(balance)


# 기본값 
def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t 사용 언어 : {2}\t".format(name, age, main_lang))

profile("유재석")
profile("김태호", 19)
# 키워드를 이용한 함수 호출
profile(main_lang="Java", name="박명수", age=29)

def profile_new(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile_new("하하", 19)
profile_new("정형돈", 24, "java", "python", "c++")

