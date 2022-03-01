import sys
input = sys.stdin.readline

computers = int(input())
networks = int(input())
dic = {}
result = []

for computer in range(computers):
    dic[computer+1] = set()

for network in range(networks):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)


def virus(start, dic):
    for i in dic[start]:
        if i not in result:
            result.append(i)
            virus(i, dic)


virus(1, dic)
print(len(result) - 1)
