#1000번
# a,b = map(int, input().split())
# print(a+b)

#1001번
# a, b = map(int, input().split())
# print(a-b)

#1008번
# a,b = map(int, input().split())
# print(a/b)

#1271번
# n, m = map(int, input().split())
# print(n // m)
# print(n % m)

#1330번
# A, B = map(int, input().split())
# if(A > B): 
#     print(">")
# elif(A == B):
#     print("==")
# else:
#     print("<")

#1809번
# "(___)
# (o o)____/
#  @@      \\
#   \\ ____,/
#   //   //
#  ^^   ^^"

# #2338번
# A = int(input())
# B = int(input())
# print(A+B)
# print(A-B)
# print(A*B)

# #2372번
# print("""\
# Animal      Count
# -----------------
# Chickens      100
# Clydesdales     5
# Cows           40
# Goats          22
# Steers          2\
# """)

# #2393번
# print("""\
#   ___  ___  ___
#   | |__| |__| |
#   |           |
#    \\_________/
#     \\_______/
#      |     |
#      |     |
#      |     |
#      |     |
#      |_____|
#   __/       \\__
#  /             \\
# /_______________\\\
# """)

# #2420번
# N, M = map(int, input().split())
# print(abs(N-M))

# # 2438번
# iterate = int(input())
# for i in range(iterate):
#     print("*" * (i+1))

# #2475번
# a,b,c,d,e = map(int, input().split())
# result = ((a ** 2) + (b ** 2) + (c ** 2) + (d ** 2) + (e ** 2)) % 10
# print(result)

# #2557번
# print("Hello World!")

# #2558번
# A = int(input())
# B = int(input())
# print(A+B)  

#2738번
# import sys
# I = sys.stdin.readline

# N, M = map(int, I().split())
# arr = [[0 for _ in range(M)] for _ in range(N)]
# for _ in range(2):
#     for i in range(N):
#         input_list = list(map(int, I().split()))
#         for j in range(M):
#             arr[i][j] += input_list[j]
    
# for col in range(N):
#     print(*arr[col])

# 2739번
# import sys
# I = sys.stdin.readline
# N = int(I())
# for i in range(9):
#     print("{} * {} = {}".format(N,i+1, N*(i+1)))

# #2741번
# import sys
# I = sys.stdin.readline
# N = int(I())

# for i in range(N):
#     print(i+1)

# 2743번
# import sys
# I = sys.stdin.readline

# str = I().strip("\n")
# print(len(str))

# #2744번
# import sys
# I = sys.stdin.readline
# str = I().strip("\n")

# str = str.swapcase()
# print(str)
## 2안
# for char in str:
#     if(char.isupper()) :
#         char = char.lower()
#     else :
#         char = char.upper()
# print(str)

# # 2753번
# import sys
# I = sys.stdin.readline

# N = int(I())
# res = 0
# if(N % 400 == 0):
#     res = 1
# elif((N % 4 ==0) and (N % 100 != 0)):
#     res = 1
# else:
#     res = 0
# print(res)

# #2753번
# import sys
# I = sys.stdin.readline

# input = I().strip("\n")
# res = -1
# if(input == "A+"):
#     res = 4.3
# elif(input == "A0"):
#     res = 4.0
# elif(input == "A-"):
#     res = 3.7
# elif(input == "B+"):
#     res = 3.3
# elif(input == "B0"):
#     res = 3.0
# elif(input == "B-"):
#     res = 2.7
# elif(input == "C+"):
#     res = 2.3
# elif(input == "C0"):
#     res = 2.0
# elif(input == "C-"):
#     res = 1.7
# elif(input == "D+"):
#     res = 1.3
# elif(input == "D0"):
#     res = 1.0
# elif(input == "D-"):
#     res = 0.7
# elif(input == "F"):
#     res = 0.0
# print(res)

# #3003번
# import sys
# I = sys.stdin.readline

# arr = [1,1,2,2,2,8]
# result_arr = [0] * 6
# input_arr = list(map(int,I().split()))
# for i in range(len(arr)):
#     result_arr[i] = arr[i] - input_arr[i]
    
# print(*result_arr)

# #4101번
# import sys
# I = sys.stdin.readline

# while(1):
#     N,M = map(int, I().split())
#     if(N == 0 and M == 0):
#         break
#     if(N > M):
#         print("Yes")
#     else:
#         print("No")
    
# #4999번
# import sys
# I = sys.stdin.readline

# arr1 = I()
# arr2 = I()
# if(len(arr1) >= len(arr2)):
#     print("go")
# else:
#     print("no")

# # 5337번
# print("""\
# .  .   .
# |  | _ | _. _ ._ _  _
# |/\\|(/.|(_.(_)[ | )(/.\
# """)

# #5338번
# print("""\
#        _.-;;-._
# '-..-'|   ||   |
# '-..-'|_.-;;-._|
# '-..-'|   ||   |
# '-..-'|_.-''-._|\
# """)

# #5339번
# print("""\
#      /~\\
#     ( oo|
#     _\\=/_
#    /  _  \\
#   //|/.\\|\\\\
#  ||  \\ /  ||
# ============
# |          |
# |          |
# |          |\
#       """)

# #5341번
# import sys
# I = sys.stdin.readline

# while(1):
#     N = int(I())
#     if(N == 0):
#         break
#     result = 0
#     for i in range(N):
#         result += (i+1)
#     print(result)

# #5522번
# import sys
# I = sys.stdin.readline
# result  = 0
# for _ in range(5):
#     N = int(I())
#     result += N
# print(result)

# # 5597번
# import sys
# I = sys.stdin.readline

# arr = [i for i in range(1,31)]
# for _ in range(28):
#     input = int(I())
#     arr.remove(input)
# print(arr[0])
# print(arr[1])

# #6840번
# import sys
# I = sys.stdin.readline

# arr = []
# for _ in range(3):
#     N = int(I())
#     arr.append(N)
# arr.sort()
# print(arr[1])

# #7891번
# import sys
# I = sys.stdin.readline

# N = int(I())
# for _ in range(N):
#     p,q = map(int, I().split())
#     print(p + q)

# #8370번
# # 비즈니스 : n1 * k1
# # 이코노미 : n2 * k2
# import sys
# I = sys.stdin.readline

# arr = list(map(int, I().split()))
# result = 0
# result += arr[0] * arr[1]
# result += arr[2] * arr[3]
# print(result)

# # 8393번
# import sys
# I = sys.stdin.readline

# N = int(I())
# result = N * (N+1) // 2
# print(result)