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


# 2439번
import sys
I = sys.stdin.readline

N = int(I())
for line in range(N):
    num_blank = N - line-1
    res = ""    
    for _ in range(num_blank):
        res += " "
    for _ in range(line+1):
        res += "*"
    
    print(res)
    