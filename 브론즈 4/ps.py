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

#5575번
# import sys
# I = sys.stdin.readline


# for _ in range(3):
#     minus = 0
#     input = list(map(int, I().split()))
#     output = [0,0,0]
#     for i in range(3):
#         sub = input[5 - i] - input[2 - i] - minus
#         # print(sub)
#         if(sub < 0):
#             if(i != 2):
#                 output[2-i] = 60 + sub
#             else :
#                 output[2-i] = 24 + sub
#             minus = 1     
#         else:
#             output[2 - i] = sub
#             minus = 0
#     print(*output)

# #5596번
# import sys
# I = sys.stdin.readline

# 민국 = list(map(int, I().split()))
# 만세 = list(map(int, I().split()))

# 차이 = 0
# for idx in range(4):
#     차이 += 민국[idx] - 만세[idx]
# if(차이 > 0):
#     print(sum(민국))
# else:
#     print(sum(만세))


# #5717번
# import sys
# I = sys.stdin.readline
# while(True):
#     M,F = map(int, I().split())
#     if(M == 0 and F ==0) :
#         break
#     print(M+F)

# #5928번
# import sys
# I = sys.stdin.readline
# D, H, M = map(int, I().split())
# t1 = D*24*60 + H*60 + M
# t2 = 11*24*60 + 11*60 + 11
# t = t1 - t2
# if t < 0:
#     print(-1)
# else:
#     print(t)
    
# #6749번
# import sys
# I = sys.stdin.readline
# N = int(I())
# M = int(I())
# print(M + M - N)

# #6763번
# import sys
# I = sys.stdin.readline
# N = int(I())
# M = int(I())
# if(M > N):
#     sub = M - N
#     fine = None
#     if(sub >= 1 and sub <= 20):
#         fine = 100
#     elif(sub >= 21 and sub <= 30):
#         fine = 270
#     elif(sub >= 31):
#         fine = 500
#     print("You are speeding and your fine is ${}.".format(fine))
# else:
#     print("Congratulations, you are within the speed limit!")

# #6764번
# import sys
# I = sys.stdin.readline

# input = [0 for _ in range(4)]
# for idx in range(4):  
#     N =   int(I())
#     input[idx] = N
    
# if(input[0] == input[1] and input[1] == input[2] and input[2] == input[3]):
#     print("Fish At Constant Depth")    
# elif(input[0] < input[1] and input[1] < input[2] and input[2] < input[3]):
#     print("Fish Rising")
# elif(input[0] > input[1] and input[1] > input[2] and input[2] > input[3]):
#     print("Fish Diving")
# else:
#     print("No Fish")