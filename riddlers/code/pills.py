tot = 1000
queue = []
for n in range(1, tot+1):
    for a in range(1+(3*n)//2):
        b = 3*n-2*a
        queue.append([a, b])
ys = ['a']*(3*tot+1)
values = []
for i in range(2*tot+1):
    values.append(ys.copy())

for p in queue:
    x = p[0]
    y = p[1]
    if p == [0, 3]:
        values[x][y] = 1
    elif p == [1, 1]:
        values[x][y] = 0
    elif x == 0:
        values[x][y] = values[x][y-3]
    elif y == 0:
        values[x][y] = values[x-2][y+1]
    elif y == 1:
        values[x][y] = (2*values[x-1][y-1] + (x-1)*values[x-2][y+1])/(x+1)
    elif y == 2:
        values[x][y] = ((4*x+2)*values[x-1][y-1] + (x)*(x-1)*values[x-2][y+1])/((x+2)*(x+1))
    elif x == 1:
        values[x][y] = ((y-2)*values[x][y-3] + 3*values[x-1][y-1])/(y+1) 
    else:
        values[x][y] = (y*(y-1)*(y-2)*values[x][y-3] + x*y*(2*x+3*y-5)*values[x-1][y-1] + x*(x-1)*(x+y-2)*values[x-2][y+1])/((x+y)*(x+y-1)*(x+y-2))
        
for k in range(tot//2):
    print(3*k+3, values[3*k+3][0])
