import sys
import time
import os
os.system('clear')

x = []
sizes = [sys.getsizeof(x)]

for i in range(0, 20):
    x.append(1)
    sizes.append(sys.getsizeof(x))
    time.sleep(1)
    print(sizes)


# print(sizes)
