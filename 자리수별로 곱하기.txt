# b의 자리수별로 곱해서 print()하기
a = int(input())
b = int(input())
print("{}\n{}\n{}\n{}".format(a*(b%10), a* ((b%100)//10), a*(b//100), a*b))