# A = 2,5,3,7,4
# B = 1,6,8,7,3,4
# U = 1,2,3,4,5,6,7,8
A = list(input('Множина А: ').split(","))
B = list(input('Множина B: ').split(","))
U = list(input('Множина U: ').split(","))


# Об'єднання
def union(m1, m2):
    result = []
    for i in m1:
        if i not in result:
            result.append(i)

    for i in m2:
        if i not in result:
            result.append(i)

    return result


# Перетин
def intersection(m1, m2):
    result = []
    for i in m1:
        for k in m2:
            if i == k:
                result.append(i)

    return result


# Різниця
def difference(m1, m2):
    result = []
    for i in m1:
        if i not in m2:
            result.append(i)
    return result


# ДоповненняA
def addition1(m1, m2):
    result = []
    for i in m2:
        if i not in m1:
            result.append(i)
    return result


# ДоповненняA
def addition2(m1, m2):
    result = []
    for i in m2:
        if i not in m1:
            result.append(i)
    return result


# Симетрична різниця
def symmetrical_difference(m1, m2):
    result = []
    for i in m1:
        if not i in m2:
            result.append(i)
    for i in m2:
        if not i in m1:
            result.append(i)
    return result


# Декартовий добуток
def cartesian_product(m1, m2):
    result = []
    for i in m1:
        for k in m2:
            multiplication = [i, k]
            result.append([multiplication])

    return result


print("- Об’єднання А та В:", union(A, B))
print("- Перетин А та В:", intersection(A, B))
print("- Різниця А та В:", difference(A, B))
print("- Доповнення А:", addition1(A, U))
print("- Доповнення B:", addition2(B, U))
print("- Симетрична різниця А та В:", symmetrical_difference(A, B))
print("- Декартовий добуток A та B:", cartesian_product(A, B))
