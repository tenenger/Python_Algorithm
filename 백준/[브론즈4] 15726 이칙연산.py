'''
NPC 운영진들은 고심 끝에 뉴비를 1학년 혹은 2학년인 학생으로 정의 내렸고 뉴비를 정의하는 김에 올드비와 TLE도 정의 내리기로 하였습니다. 올드비는 N학년 이하이면서 뉴비가 아닌 학생으로 정의하기로 하였고 TLE은 뉴비도 아니고 올드비도 아닌 학생으로 정의하였습니다.

3 1
'''
a, b, c = map(int, input().split())
num_1 = int(a*b/c)
num_2 = int(a/b*c)
if num_1 >= num_2 :
    print(num_1)
else :
    print(num_2)

