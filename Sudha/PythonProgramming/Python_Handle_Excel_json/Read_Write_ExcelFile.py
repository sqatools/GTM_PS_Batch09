import openpyxl


# pip install openpyxl


def read_excel_data(filepath, sheet_name, cell_name):
    wb = openpyxl.load_workbook(filepath)
    sheet = wb[sheet_name]
    cell = sheet[cell_name]
    print(cell.value)


#read_excel_data("test_data.xlsx", "Sheet1", "A1")
#read_excel_data("test_data.xlsx", "Sheet2", "A1")

#for i in range(1, 6):
    #read_excel_data("test_data.xlsx", "Sheet1", f"A{i}")


def write_data_Excel(filepath,sheet_name,cell_name,cell_value):
    wb = openpyxl.load_workbook(filepath)
    sheet = wb[sheet_name]
    cell_n = sheet[cell_name]
    cell_n.value = cell_value
    wb.save(filepath)

write_data_Excel("test_data.xlsx","Sheet1","A1","Tnagar")
