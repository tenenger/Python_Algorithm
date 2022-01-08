data = input()
# 사전자료형은 순서가 바뀌기 때문에 값이 달라 질 수 있다.
croatia = ["c=", "c-", "dz=", "d-","lj", "nj", "s=", "z="]

for i in croatia:
    data = data.replace(i, '*')
print(len(data))