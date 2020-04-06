import time

# O(n)


def add_to_back(n):
    x = []
    for i in range(0, n):
        x.append(i + 1)
    return x

# O(n^2)


def add_to_front(n):
    x = []
    # O(n)
    for i in range(0, n):
        # O(n) - hidden for-loop!!!
        x.insert(0, n - i)

    return x


start_time = time.time()
add_to_back(500000)  # O(n)
end_time = time.time()
print(f"runtime: {end_time - start_time} seconds")

# runtime: 0.08344292640686035 seconds

start_time = time.time()
add_to_front(500000)  # O(n^2)
end_time = time.time()
print(f"runtime: {end_time - start_time} seconds")

# runtime: 50.613221168518066 seconds

'''
NOTE: add_to_back() is over 600x faster than add_to_front()!!!
'''
