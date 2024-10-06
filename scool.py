###################### Пример_1 ######################
def func_generator(n):
    i = 0
    while i != n:
        yield i
        i += 1


obj = func_generator(5)
print(obj)

for i in obj:
    print(i)
print("##########################################################################")
###################### Пример_2 #########################

def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
def fibonacci_v2(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# fib = fibonacci(n = 10)
# print(fib)
#
# for val in fib:
#     print(val)


# fib_2 = fibonacci_v2(n = 10)
# print(fib_2)
#
# for val in fib_2:
#     print(val)
print("##########################################################################")
###################### Пример_3 ###################################################
print("##########################################################################")
def fibonacci_v3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for i in fibonacci_v3():
    print(i)
    if i > 100 ** 6:
        break
print("##########################################################################")
###################### Пример_4 ###################################################
print("##########################################################################")

# import time
#
# start = time.time()
# def read_large(file_path):
#     with open(file_path, 'r', encoding= "utf-8") as f:
#         for line in f:
#             yield line
#
# for line in read_large("Lanarge_f.txt"):
#     print(line)
# fin = time.time()
#
# print((fin-start)*1000)