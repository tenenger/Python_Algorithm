import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_data = set([input().strip() for _ in range(n)])
m_data = set([input().strip() for _ in range(m)])
result = sorted(n_data & m_data)

print(len(result))
for i in result:
    print(i)
