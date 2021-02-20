# 별 찍기!

a = int(input())

for i in range(a):
    for j in range(a-i-1):
        print('0', end='')
    print('1')

# 00001
# 0001
# 001
# 01
# 1

for i in range(a):
    for j in range((2*i)+1):
        print('*', end='')
    print()

# *
# ***
# *****
# *******
# *********

for i in range(a):
    for j in range(a-i-1):
        print(' ', end='')
    for j in range((2*i)+1):
        print('*', end='')
    print()

#     *
#    ***
#   *****
#  *******
# *********

# 모범 답안 (컴팩트)

for i in range(1, a+1):
    print(' '*(a-i) + '*'*(2*i-1), i)

#     * 1
#    *** 2
#   ***** 3
#  ******* 4
# ********* 5