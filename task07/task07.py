from xlwt import Workbook


def get_max_salary(f, max_sal_local):
    for line in f.readlines()[1:]:
        data = line.split(",")
        data[1] = int(data[1])
        if max_sal_local < data[1]:
            max_sal_local = data[1]
    return max_sal_local


def get_sum(f, month):
    partial_sum = 0
    for line in f.readlines()[1:]:
        if month in line or month.lower() in line:
            data = line.split(",")
            data[1] = int(data[1])
            partial_sum += data[1]
    return partial_sum


def get_avg(f, months):
    partial_sum = 0
    no_of_entries = 0
    for line in f.readlines()[1:]:
        for month in months:
            if month in line or month.lower() in line:
                data = line.split(",")
                data[1] = int(data[1])
                partial_sum += data[1]
                no_of_entries += 1
    return partial_sum, no_of_entries


wb = Workbook()

sheet1 = wb.add_sheet("Sheet 1")

f1 = open("f1.txt", "r")
f2 = open("f2.txt", "r")
f3 = open("f3.txt", "r")

max_sal_local = 0

max_sal_f1 = get_max_salary(f1, max_sal_local)
max_sal_f2 = get_max_salary(f2, max_sal_local)
max_sal_f3 = get_max_salary(f3, max_sal_local)

max_sal = max_sal_f3
print(max_sal)

f1.seek(0)
f2.seek(0)
f3.seek(0)

month = 'Octombrie'
sum_f1 = get_sum(f1, month)
sum_f2 = get_sum(f2, month)
sum_f3 = get_sum(f3, month)
total_sum = sum([sum_f1, sum_f2, sum_f3])
print(total_sum)

f1.seek(0)
f2.seek(0)
f3.seek(0)

months = ['August', 'Septembrie', 'Octombrie']
sum_f1, no_of_entriesf1 = get_avg(f1, months)
sum_f2, no_of_entriesf2 = get_avg(f2, months)
sum_f3, no_of_entriesf3 = get_avg(f3, months)
total_sum = sum([sum_f1, sum_f2, sum_f3])
total_no_of_entries = no_of_entriesf1 + no_of_entriesf2 + no_of_entriesf3
print(total_sum / total_no_of_entries)

sheet1.write(0, 1, "Salariu maxim")
sheet1.write(1, 1, str(max_sal))
sheet1.write(0, 2, "Suma salariilor - Octombrie")
sheet1.write(1, 2, str(total_sum))
sheet1.write(0, 3, "Media salariilor")
sheet1.write(1, 3, str(total_sum / total_no_of_entries))

wb.save("example.xls")

f1.close()
f2.close()
f3.close()