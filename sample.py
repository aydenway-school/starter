import math

print("hello, this is Ayden practicing for CS210")

i = 0

while i < 1000:
    print(math.sqrt(i))
    i += 1
    if i % 2 == 0:
        print(f"This number {i} is even")

