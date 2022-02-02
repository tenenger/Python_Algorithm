t = int(input())

for _ in range(t):
    m_cnt = 0
    name = ""
    p = int(input())
    data = [input().split() for _ in range(p)]
    for i in range(p):
        if m_cnt < int(data[i][0]):
            m_cnt = int(data[i][0])
            name = data[i][1]
    print(name)