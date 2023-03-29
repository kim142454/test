#컴퓨터공학과, 20234043, 김현우
print("컴퓨터공학과, 20234043, 김현우")

#초기값 설정
sum = 0
number = 1#1~100까지의 덧셈이므로 초기값은 1

while number < 100:
    sum = sum + number#아래에서 넘겨진 number값과 늘어난 sum값을 더한다
    number = number + 2#공차는 2씩 더해지므로 +2이다. 1,3,5,7,9...
    
print(sum)
