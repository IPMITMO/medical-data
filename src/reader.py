import xlrd
import datetime
import mapper

def read(filename):
    workbook = xlrd.open_workbook(filename, on_demand = True)
    name =  workbook.sheet_names()[0]
    sheet = workbook.sheet_by_name(name)

    arr = []
    for i in range(1, sheet.nrows):
        obj = {
            "id": int(sheet.cell(i, 0).value),
            "abbr": sheet.cell(i, 1).value,
            "name": sheet.cell(i, 2).value,
        }
        arr.append(obj)

    return mapper.do(arr)

def xldate_to_datetime(xldate):
  tempDate = datetime.datetime(1900, 1, 1)
  deltaDays = datetime.timedelta(days=int(xldate))
  secs = (int((xldate%1)*86400)-60)
  detlaSeconds = datetime.timedelta(seconds=secs)
  TheTime = (tempDate + deltaDays + detlaSeconds )
  return TheTime.strftime("%Y-%m-%d %H:%M:%S")

def readmain(filename):
    workbook = xlrd.open_workbook(filename, on_demand = True)
    name =  workbook.sheet_names()[0]
    sheet = workbook.sheet_by_name(name)

    arr = []
    for i in range(1, sheet.nrows):
        obj = {
            "id": int(sheet.cell(i, 0).value),
            "birthday": xldate_to_datetime(sheet.cell(i, 1).value),
            "sex": sheet.cell(i, 2).value,
            "street": sheet.cell(i, 3).value,
            "streetype": sheet.cell(i, 4).value,
            "area": sheet.cell(i, 5).value,
            "dateout": sheet.cell(i, 5).value,
            "diagnosis": sheet.cell(i, 6).value,
            "diag_pref": sheet.cell(i, 7).value,
            "id_prvs": sheet.cell(i, 8).value,
            "id_exitus": sheet.cell(i, 9).value,
            "qresult": sheet.cell(i, 10).value,
        }
        arr.append(obj)

    return arr
