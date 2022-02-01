w, h = map(int, input().split())
p, q = map(int, input().split())
time = int(input())

a = (p + time) // w  # time만큼 x축 왕복 횟수
b = (q + time) // h  # time만큼 y축 왕복 횟수

if a % 2 == 0:  # x축 왕복횟수가 짝수라면 그위치로
    x = (p + time) % w
# x축 왕복횟수가 홀수라면 처음 움직였던 오른쪽 방향과 방향이 같으므로, w의 전체길이에서 (p + time) % w를 빼주면 위치값을 도출할 수 있다.
else:
    x = w - (p + time) % w

if b % 2 == 0:
    y = (q + time) % h
else:
    y = h - (q + time) % h
print(x, y)
