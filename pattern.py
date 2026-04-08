1
22
333
4444
55555

# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print(i, end="")
#     print()

'''
*
**
***
****
'''

# n = int(input())

# for i in range(1,n):
#     for j in range(i):
#         print("*", end="")
#     print()

'''
*****
****
***
**
*
'''
# n = int(input())
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end="")

#     print()

'''
    *
   * *
  * * *
 * * * * 
* * * * *
'''

# n = int(input())

# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
    # print()

'''
*
**
***
****
*****
'''
# n = int(input())
# for i in range(1,n+1):
#     for j in range(n-1):
#         print(" ",end="")
#     for k in range(i):
#         print("*", end="")
#     print()
'''
      *
    * *
  * * *
* * * * 
'''
# n = int(input())
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()

'''
A
AB
ABC
ABCD
'''
n = int(input())
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(i):
        print(chr(65+j),end=" ")
    print()