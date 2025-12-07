million = []
for i in range(1,1000001):
    million.append(i)

#print(min(million))
#print(max(million))
#print(sum(million))

#for i in range(1, 21, 2):

#multiples = []
#for i in range(3,31,3):
#    multiples.append(i)

#cube = []
#for i in range(1,11):
#    cube.append(i ** 3)

cube = [i ** 3 for i in range(1,11)]
print(cube)