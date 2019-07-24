import sys

lineIn = sys.stdin.readline()
n = int(lineIn)

r_l = []

for i in range(n):
    lineIn = sys.stdin.readline().split(" ")
    l_tmp = (int(lineIn[0]))
    r_tmp = (int(lineIn[1]))
    r_l.append([r_tmp, l_tmp])
    
r_l.sort()

m_coord = []
m_coord.append(r_l[0][0])
m = 1

for i in range(n):
    if r_l[i][1] > m_coord[(len(m_coord) - 1)]:
        m = m + 1
        m_coord.append(r_l[i][0])


#sys.stdout.write(str([m, m_coord]))
        
print(len(m_coord))
print(' '.join(map(str, m_coord)))
#sys.stdout.write(str(len(points)) + '\n')
#for i in range(len(points)):
#    sys.stdout.write(str(points[i]) + ' ')