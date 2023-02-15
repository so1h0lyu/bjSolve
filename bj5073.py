"""
백준 5073번

삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의
- Equilateral: 세 변의 길이가 모두 같은 경우
- Isosceles: 두 변의 길이만 같은 경우
- Scalene: 세 변의 길이가 모두 다른 경우
주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 출력
ex. 6, 3, 2가 이 경우에 해당
가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 조건 만족 X
세 변의 길이가 주어질 때 정의에 따른 결과 출력

입력: 각 줄에는 1000을 넘지 않는 양의 정수 3개 입력 마지막 줄 0 0 0
출력: Equilateral, Isosceles, Scalene, Invalid 중 하나 출력
"""

while True: 
    a, b, c = map(int, input().split())
    otherSum = 0

    if a == 0 & b == 0 & c == 0:
        break
    elif a == b == c:
        print("Equilateral")
        continue

    tri = [a, b, c]
    max = 0

    for i in range(0, 3):
        if tri[i] >= max:
            max = tri[i]
    if max == tri[0]:
        otherSum = tri[1] + tri[2]
    elif max == tri[1]:
        otherSum = tri[0] + tri[2]
    else:
        otherSum = tri[0] + tri[1]
    
    if max >= otherSum:
        print("Invalid")
        continue

    if a != b | b != c | c != a:
        print("Scalene")
    else:
        print("Isosceles")
