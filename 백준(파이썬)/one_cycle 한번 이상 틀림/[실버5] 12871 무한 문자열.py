import math
s = input()
t = input()
lcm_number = math.lcm(len(s), len(t))
s_string = s * (lcm_number//len(s))
t_string = t * (lcm_number//len(t))
if s_string == t_string:
    print(1)
else:
    print(0)
