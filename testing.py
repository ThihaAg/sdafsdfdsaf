table = []
row = []
for i in range(1,12):
    for o in range(1,12):
        row.append(i*o)
    table.append(row)
    row = []
print(table)