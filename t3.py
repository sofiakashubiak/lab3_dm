# A = 2,5,3,7,4
# B = 1,6,8,7,3,4
# U = 1,2,3,4,5,6,7,8
A = list(input('Множина А: ').split(","))
B = list(input('Множина B: ').split(","))
U = list(input('Множина U: ').split(","))
def bitStringA(A, U):
    result = []
    for i in U:
        if i in A:
            i = 1
        else:
            i = 0
        result.append(i)

    return result


def bitStringB(B, U):
    result = []
    for i in U:
        if i in B:
            i = 1
        else:
            i = 0
        result.append(i)

    return result
print("Бітовий рядок А:", bitStringA(A, U))
print("Бітовий рядок В:", bitStringB(B, U))