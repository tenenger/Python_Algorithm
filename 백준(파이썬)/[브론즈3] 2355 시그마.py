a, b = map(int, input().split())
m_n = max(a, b)
n_n = min(a, b)
c = m_n - n_n
print(int(n_n*(c+1) + (c*(c+1))/2))