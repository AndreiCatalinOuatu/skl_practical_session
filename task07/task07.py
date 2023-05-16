from xlwt import Workbook


def get_max_salary(f, max_sal_local):
    for line in f.readlines()[1:]:
        data = line.split(",")
        data[1] = int(data[1])
        if max_sal_local < data[1]:
            max_sal_local = data[1]
    return max_sal_local


wb = Workbook()

sheet1 = wb.add_sheet("Sheet 1")

f1 = open("f1.txt", "r")
f2 = open("f2.txt", "r")
f3 = open("f3.txt", "r")

'''
print(f1.readline())
print(f2.readline())
print(f3.readline())
'''

max_sal_local = 0

max_sal_f1 = get_max_salary(f1, max_sal_local)
max_sal_f2 = get_max_salary(f2, max_sal_local)
max_sal_f3 = get_max_salary(f3, max_sal_local)

max_sal = max_sal_f3
print(max_sal)

sheet1.write(0, 1, "Salariu maxim")
sheet1.write(1, 1, str(max_sal))

wb.save("example.xls")

'''
for lst in [f1.readlines(), f2.readlines(), f3.readlines()]:
    for line in lst:
        data = line.split(",")
        data[1] = int(data[1])
        if max_sal < data[1]:
            max_sal = data[1]
'''

'''
for line in f2.readlines():
    data = line.split(",")
    data[1] = int(data[1])
    if max_sal < data[1]:
        max_sal = data[1]

for line in f3.readlines():
    data = line.split(",")
    data[1] = int(data[1])
    if max_sal < data[1]:
        max_sal = data[1]
'''
