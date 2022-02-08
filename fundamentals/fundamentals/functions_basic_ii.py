# 1
# def countdown(num):
#     count = []
#     for i in range(num, 0, -1):
#         count.append(i)
#     return count
# print(countdown(5))

# # 2
# def printreturn(arr):
#     print(arr[0])
#     return arr[1]
# print(printreturn([1, 2]))

# # 3
# def sumreturn(arr):
#     return arr[0] + len(arr)
# print(sumreturn([1,2,3,4]))

# 4
# def greaterthansecond(arr):
#     sum = 0
#     newlist = []
#     for i in range(len(arr)+1):
#         if i > arr[1]:
#             sum += 1
#             newlist.append(i)
#     print(sum)
#     if len(newlist) < 2:
#         return False
#     return newlist
# print(greaterthansecond([1,2,3]))
# print(greaterthansecond([1,2,3,4,5,6]))

# # 5
# def lengthvalue(a, b):
#     newlist = []
#     for i in range(a):
#         newlist.append(b)
#     return newlist
# print(lengthvalue(4,5))
