S = input()
pre_fix = []
for i in range(len(S)):
    pre_fix.append(S[i:])
pre_fix.sort()
print('\n'.join(pre_fix))
