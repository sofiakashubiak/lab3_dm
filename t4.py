# A = 2,5,3,7,4
# B = 1,6,8,7,3,4
# U = 1,2,3,4,5,6,7,8
A = list(input('Множина А: ').split(","))
B = list(input('Множина B: ').split(","))
U = list(input('Множина U: ').split(","))


def transfer(X, mU):
    result = ""
    for i in mU:
        if i in X:
            result += "1"
        else:
            result += "0"
    return result


# Об'єднання
def union(mA, mB, mU):
    result = []
    for i in mU:
        if i in mB and mA:
            i = 1
        else:
            i = 0
        result.append(i)

    return result


# Перетин
def intersection(mA, mB, mU):
    result = []
    for i in mU:
        if i in mA and mB:
            i = 1
        else:
            i = 0
        result.append(i)

    return result


# Різниця
def difference1(mA, mB, mU):
    result = []
    for i in mU:
        if i in list(set(mA) - set(mB)):
            i = 1
        else:
            i = 0
        result.append(i)

    return result


def difference2(mA, mB, mU):
    result = []
    for i in mU:
        if i in list(set(mB) - set(mA)):
            i = 1
        else:
            i = 0
        result.append(i)

    return result


# Симетрична різниця
def symmetrical_difference(mA, mB, mU):
    result = []
    for i in mU:
        if i in list(set(mA) ^ set(mB)):
            i = 1
        else:
            i = 0
        result.append(i)

    return result


print("Множина A у вигляді бітових рядків:", transfer(A, U))
print("Множина B у вигляді бітових рядків:", transfer(B, U))
print("-----------------------------------------------")
print("Розрахунок у вигляді бітових рядків:")
print("Об’єднання:", union(A, B, U))
print("Перетин:", intersection(A, B, U))
print("Різниця А та В:", difference1(A, B, U))
print("Різниця B та A:", difference2(A, B, U))
print("Симетрична різниця А та В:", symmetrical_difference(A, B, U))
print("-----------------------------------------------")
print("Розрахунок у вигляді звичайних рядків:")

# Об'єднання
myList1 = union(A, B, U)
newList1 = []
for i in range(len(myList1)):
    if myList1[i] == 1:
        newList1.append(i + 1)
print("Об’єднання:", newList1)

# Перетин
myList2 = intersection(A, B, U)
newList2 = []
for i in range(len(myList2)):
    if myList2[i] == 1:
        newList2.append(i + 1)
print("Перетин:", newList2)

# Різниця
myList3 = difference1(A, B, U)
newList3 = []
for i in range(len(myList3)):
    if myList3[i] == 1:
        newList3.append(i + 1)
print("Різниця А та В:", newList3)

myList4 = difference2(A, B, U)
newList4 = []
for i in range(len(myList4)):
    if myList4[i] == 1:
        newList4.append(i + 1)
print("Різниця B та A:", newList4)

# Симетрична різниця
myList5 = symmetrical_difference(A, B, U)
newList5 = []
for i in range(len(myList5)):
    if myList5[i] == 1:
        newList5.append(i + 1)
print("Симетрична різниця А та В:", newList5)
