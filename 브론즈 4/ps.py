# #1264번
# import sys
# i = sys.stdin.readline
# while(True):
#     input = i().strip("\n")
#     if(input == "#"):
#         break
#     ans = 0
#     for elm in input.lower():
#         if(elm == 'a' or elm == 'e' or elm == 'i' or elm == 'o' or elm == 'u'):
#             ans += 1
#     print(ans)
    
# #2083번
# import sys
# i = sys.stdin.readline

# while(True):
#     input = list(i().split())
#     if(input[0] == "#" and int(input[1]) == 0 and int(input[2]) == 0):
#         break
    
#     res = ""
#     if(int(input[1]) > 17 or int(input[2]) >= 80):
#         res = "{} {}".format(input[0],"Senior")
#     else: 
#         res = "{} {}".format(input[0],"Junior")
#     print(res)


# # 2439번
# import sys
# I = sys.stdin.readline

# N = int(I())
# for line in range(N):
#     num_blank = N - line-1
#     res = ""    
#     for _ in range(num_blank):
#         res += " "
#     for _ in range(line+1):
#         res += "*"
    
#     print(res)
    
# #2440번
# import sys
# I = sys.stdin.readline

# N = int(I())
# for line in range(N, 0, -1):
#     output = ""
#     for num in range(line):
#         output += "*"
#     print(output)

# # 2480번
# import sys
# I = sys.stdin.readline

# input = list(map(int, I().split()))
# a = input[0]
# b= input[1]
# c = input[2]
# result = None
# # 모두 같은 경우
# if(a ==b and b == c):
#     result = 10000 + a * 1000
# # 하나만 다른 경우
# elif(a == b and b != c):
#     result = 1000 + a * 100
# elif(b == c and b != a):
#     result = 1000 + b * 100
# elif(c == a and c != b):
#     result = 1000 + c * 100
# else :    
#     result = max(input) * 100
    
# print(result)

# # 2530번 구현
# import sys
# I = sys.stdin.readline

# input = list(map(int, I().split()))
# time = int(I())

# add_list = []
# add_list.append(time // 3600)
# time %= 3600
# add_list.append(time // 60)
# time %= 60
# add_list.append(time)

# # 2. 덧셈
# input[1] += (add_list[2] + input[2]) // 60
# input[2] = (add_list[2] + input[2]) % 60

# input[0] += (add_list[1] + input[1]) // 60
# input[1] = (add_list[1] + input[1]) % 60

# input[0] = (input[0] + add_list[0]) % 24

# print(*input)
    
# #2742번
# import sys
# I = sys.stdin.readline

# N = int(I())
# for i in range(N,0,-1):
#     print(i)

# # 2752번
# import sys
# I = sys.stdin.readline
# input = list(map(int, I().split()))
# input.sort()
# print(*input)

# #2845번
# import sys
# I = sys.stdin.readline

# L, P = map(int, I().split())
# people = L * P
# inputs = list(map(int, I().split()))
# output = []
# for input in inputs:
#     output.append(input - people)
# print(*output)

# # 4470번
# import sys
# I = sys.stdin.readline
# N = int(I())
# for line in range(N):
#     input = I().strip("\n")
#     output = "{}. ".format(line+1)
#     output += input
#     print(output)
    
# # 4562번
# import sys
# I = sys.stdin.readline
# N = int(I())
# for line in range(N):
#     a,b, = map(int, I().split())
#     if(a >= b): 
#         print("MMM BRAINS")
#     else:
#         print("NO BRAINS")

# #4589번
# import sys
# I = sys.stdin.readline

# N = int(I())
# print("Gnomes:")
# for line in range(N):
#     input = list(map(int, I().split()))
#     상승 = sorted(input)
#     하강 = sorted(input, reverse=True)    
#     if(input == 상승 or input == 하강):
#         print("Ordered")
#     else:
#         print("Unordered")
    
# #5524번
# import sys
# I = sys.stdin.readline
# N  = int(I())
# for line in range(N):
#     input = I().strip("\n")
#     print(input.lower())

# #5532번
# import sys
# I = sys.stdin.readline

# 방학 = int(I())
# 국어페이지 = int(I())
# 수학페이지 = int(I())
# 국어하루 = int(I())
# 수학하루 = int(I())
# 국어 = 0
# if(국어페이지 % 국어하루):
#     국어  = 1
# 국어 += 국어페이지 // 국어하루
# 수학 = 0
# if(수학페이지 % 수학하루):
#     수학  = 1
# 수학 += 수학페이지 // 수학하루
# 시간 = max(국어,수학)
# print(방학 - 시간)
    
# # 5543번
# import sys
# I = sys.stdin.readline

# 상덕버거 = int(I())
# 중덕버거 = int(I())
# 하덕버거 = int(I())

# 콜라 = int(I())
# 사이다 = int(I())

# result = min(상덕버거, 중덕버거, 하덕버거) + min(콜라,사이다) - 50
# print(result)

# #5554번
# import sys
# I = sys.stdin.readline
# list = []
# for _ in range(4):b
#     입력 = int(I())
#     list.append(입력)
# 분 = sum(list) // 60
# 초 = sum(list) % 60
# print(분)
# print(초)

지호 = "바보"
print(지호)