t = int(input())
for _ in range(t):
    n = int(input())
    m_n = 0
    m_s = ''
    for _ in range(n):
        name, score = input().split()
        score = int(score)
        if score > m_n :
            m_n = score
            m_s = name
    print(m_s)
