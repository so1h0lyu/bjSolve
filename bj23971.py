"""
백준 23971번

한 명씩 앉을 수 있는 테이블이 행마다 W개씩 H행에 걸쳐 있을 때 (h X w)
모든 참가자는 세로로 N칸 또는 가로로 M칸 이상 비우고 앉아야 한다.
즉, 다른 모든 참가자와 세로줄 번호의 차가 N보다 크거나 
가로줄 번호의 차가 M보다 큰 곳에만 앉을 수 있다.
최대 몇 명을 수용할 수 있는지

입력: H, W, N, M이 공백으로 구분되어 주어짐
출력: 강의실이 수용할 수 있는 최대 인원 수 출력
"""

h, w, n, m = map(int, input().split())   # 한 번에 여러 개 입력받기
hp = 1                              # 한 행의 수용 인원
wp = 1                              # 한 열의 수용 인원
now = 0 

for i in range(1, h):
    if now == n:
        now = 0
        hp += 1
        continue
    now += 1

now = 0
for i in range(1, w):
    if now == m:
        now = 0
        wp += 1
        continue
    now += 1

print(hp * wp)