import copy
t = int(input())

for _ in range(t):
    a, b = list(input().split())
    arr_a, arr_b = [], []
    a,b = list(a),list(b)
    c = copy.deepcopy(b)
    
    try:
        for i in a:
            c.remove(i)
        if c:
            print(f'{"".join(a)} & {"".join(b)} are NOT anagrams.')
        else:
            print(f'{"".join(a)} & {"".join(b)} are anagrams.')
    except Exception:
        print(f'{"".join(a)} & {"".join(b)} are NOT anagrams.')

