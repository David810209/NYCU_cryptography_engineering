import random
import os
random.seed(12345)
print(random.random()) 
print(random.random())  

random.seed(12345)

print(random.random()) 
print(random.random())
print()
for _ in range(5):
    seed_bytes = int.from_bytes(os.urandom(32), byteorder='big')
    random.seed(seed_bytes)
    print(random.random())