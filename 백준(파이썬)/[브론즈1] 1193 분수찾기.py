n = int(input())
line = 1
end = 1
while n > end:
    line += 1
    end += line

gap = end - n

if line % 2 == 1:
    top = gap +1
    bot = line - gap
else:
    top = line - gap
    bot = gap + 1

print(f"{top}/{bot}")