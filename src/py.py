import xlrd

## Basic xls reader

workbook = xlrd.open_workbook('../raw/street.xls', on_demand = True)
name =  workbook.sheet_names()[0]
sheet = workbook.sheet_by_name(name)

print sheet.nrows
print sheet.cell(1, 2).value

for i in range(1, sheet.nrows):
    print sheet.cell(i, 2).value, sheet.cell(i, 1).value, sheet.cell(i, 2).value
