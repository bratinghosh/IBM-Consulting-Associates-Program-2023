from functools import cmp_to_key

n = int(input())
N = input().split()

m = int(input())
M = input().split()



def size_cmp(a, b):
    SIZE = {
        "S": 2,
        "M": 1,
        "L": 0
    }
    if SIZE[a[-1]] >SIZE[b[-1]]:
        return -1
    elif SIZE[a[-1]] == SIZE[b[-1]] and b[-1] == "S":
        if len(a) > len(b):
            return -1
        else:
            return 1
    elif SIZE[a[-1]] == SIZE[b[-1]] and b[-1] == "L":
        if len(a) > len(b):
            return 1
        else:
            return -1
    else:
        return 1


size_cmp_key = cmp_to_key(size_cmp)

N.sort(key=size_cmp_key)
N.reverse()

M.sort(key=size_cmp_key)
M.reverse()

def check_greater(a, b):
    SIZE = {
        "S": 2,
        "M": 1,
        "L": 0
    }
    if SIZE[a[-1]] >SIZE[b[-1]]:
        return False
    elif SIZE[a[-1]] == SIZE[b[-1]] and b[-1] == "S":
        if len(a) > len(b):
            return False
        elif len(a) == len(b):
            return True
        else:
            return True
    elif SIZE[a[-1]] == SIZE[b[-1]] and b[-1] == "L":
        if len(a) > len(b):
            return True
        elif len(a) == len(b):
            return True
        else:
            return False
    else:
        return True


if m > n:
    print("No")
else:
    flag = True
    for i in range(m):
        print("SHop:", N[i], "Order", M[i])
        if not check_greater(N[i], M[i]):
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")