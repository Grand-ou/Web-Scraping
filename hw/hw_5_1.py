line = input()
line = line.split(' ')
x = int(line[0])-1
y = int(line[1])-1
z = x + y
r = 1
for i in range(1, z+1):
	r *= i
for i in range(1, x+1):
	r /= i
for i in range(1, y+1):
	r /= i
print(int(r))