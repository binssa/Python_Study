# 방법 1
print("나는 %d살입니다." %20)
print("나는 %s를 좋아해용." % "Python")
print("Apple은 %c로 시작해요." %"A")

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}을 좋아합니다.".format(age=20,color="빨간색"))

# 방법 4
age = 20
color = "Red"
print(f"나는 {age}살이며, {color}를 좋아해요")

# 탈출 문자 1 \n : 줄 바꿈
print("백문이 불여일견\n 백견이 불여일타")

# 탈출 문자 2 
print("저는 \"나도 코딩\"입니다.")
print("저는 \'나도 코딩\'입니다.")

# \\ : 하나의 \로 표현 가능
print("C:\\Users\\Code\\data")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : Tab
print("Red\tApple")


# Quiz
site = "http://nate.com"
passwd1 = site[7:10]
passwd2_start_index = site.index('.')
passwd2 = str(len(site[7:passwd2_start_index]))
passwd3 = str(site.count('e'))

print(passwd1)
print(passwd2)
print(passwd3)
mypassword= passwd1 + passwd2 + passwd3 + '!'
print(mypassword)