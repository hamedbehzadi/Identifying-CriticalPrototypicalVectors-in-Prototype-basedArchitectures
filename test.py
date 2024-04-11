import numpy as np

a = 20
c = 2
b = np.zeros((a,c))
for i in range(20):
    b[i,i // 10] = 1
    print(i,i//10)
print('**********')
for i in range(20):
    print(i,b[i,:])