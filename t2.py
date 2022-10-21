# A = 2,5,3,7,4
# B = 1,6,8,7,3,4
A = list(input('Множина А: ').split(","))
B = list(input('Множина B: ').split(","))


# Підмножини
def isSubset1(m1, m2):
    for i in m1:
        if i not in m2:
            return False
    return True


def isSubset2(m1, m2):
    for i in m2:
        if i not in m1:
            return False
    return True


# Рівність
def isEqual(m1, m2):
    for i in m1:
        if i not in m2:
            return False
    for i in m2:
        if i not in m1:
            return False
    return True


print("Чи є множина A підмножиною B?", isSubset1(A, B))
print("Чи є множина B підмножиною A?", isSubset2(A, B))
print("Чи є А і В рівними множинами?", isEqual(A, B))
