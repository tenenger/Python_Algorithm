data = [int(input()) for _ in range(10)]
cnt = 0

for i in range(10):
    cnt += data[i]
    m_cnt = cnt
    if cnt > 100:        
        cnt -= data[i]
        break

if 100 - cnt == m_cnt - 100:
    print(m_cnt)
elif 100-cnt > m_cnt-100:
    print(m_cnt)
else:
    print(cnt)