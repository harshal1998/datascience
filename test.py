# a = [0, 1, 0, 3, 12]
# b = [0, 1, 0, 3, 17]
#
# def x(a):
#     if sum(a) > 20:
#         for i in a:
#             if i == 0:
#                 a.remove(i)
#     else:
#         for i in a:
#             if i == 0:
#                 a.append(i)
#                 a.remove(i)
#     print(a)
#
# x(a)
# x(b)

# a="(()"
# b=")()())"
# c= ")()()))()())"
#
# def y(n):
#     if "()()" in n:
#         count+=1
#     elif "()" in n:
#
# y(c)


# n = int(input("enter n:"))
#
# def fib(n):
#     a = [0, 1]
#     if n < 2:
#         return a[n]
#     while len(a) <= n:
#         b = a[-1] + a[-2]
#         a.append(b)
#     return a[n]
#
#
# for i in range(n):
#     print(i * fib(i))


# n = int(input("enter n:"))
# for i in range(n):
#     if i == 0:
#         b = 1
#         print(b)
#     else:
#         b += 4 * i
#         print(b)

# a = "(()"
# b = ")()())"
# c1 = ")()()))()())"
# d = "))))()()((((()()))()()"
# import re
#
# c = 0
# l = list(d)
# for i in range(len(l)):
#     if l[i] == "(":
#         if l[i + 1] == ")":
#             c = c + 1
# if c == 1:
#     print(c)
# else:
#     print(c // 2)
