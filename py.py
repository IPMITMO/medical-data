import xlrd
#workbook = xlrd.open_workbook('./area.xls')
workbook = xlrd.open_workbook('./area.xls', on_demand = True)
name =  workbook.sheet_names()[0]
sheet = workbook.sheet_by_name(name)
print sheet
#print sheet.cell(0, 0).value
