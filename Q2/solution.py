n = int(input())
N = []

for i in range(n):
    user_input = input().split()
    N.append(user_input)

def isValid(record):
    if record[1] == "true":
        return True
    return False

allValid = True
errorCodes = []

for record in N:
    if not isValid(record):
        errorCodes.append(record[2])
        allValid = isValid(record)

if allValid:
    print("Yes")
else:
    print("No")
    print(' '.join(errorCodes))
