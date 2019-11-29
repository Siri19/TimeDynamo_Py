import openpyxl
path="/home/siri/Documents/TimeDynamo_Automation/TD_Web_ExcelData.xlsx"
workbook=openpyxl.load_workbook(path)
sheet=workbook.get_sheet_by_name("Test")
for row in range(1,6):
    for col in range(1,4):
        sheet.cell(row=row,column=col).value="Welcome"

workbook.save(path)