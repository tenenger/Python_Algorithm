from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    documents = deque(map(int, input().split()))
    idx = deque(range(n))
    cnt = 0

    while documents:
        if documents[0] == max(documents):
            if idx[0] == m:
                print(cnt + 1)
                break
            documents.popleft()
            idx.popleft()
            cnt += 1
        else:
            documents.append(documents.popleft())
            idx.append(idx.popleft())
