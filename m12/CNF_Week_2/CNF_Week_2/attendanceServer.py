import socket
import threading
import xlrd
import random
def main():
    s=socket.socket()
    ip=str(socket.gethostbyname(socket.gethostname()))
    port=5900
    s.bind((ip,port))
    s.listen()
    location = ("E:\msit\CNF\m12\CNF_Week_2\CNF_Week_2")
    data_ = xlrd.open_workbook(location)
    data_sheet = data_.sheet_by_index(0)
    data_sheet.cell_value = (0,0)
    rollNum = []
    dictQandA = {}
    for i in range(data_sheet.nrows):
        rollNum.append(data_sheet.cell_value(i, 0))
        dictQandA[data_sheet.cell_value(i, 1)] = data_sheet.cell_value(i, 2)

    while True:
        c,addr = s.accept()
        data = c.recv(1024).decode()
        rolln = data.split()
        if rolln[1] not in rollNum:
            string = "ROLLNUMBER NOT FOUND"
        else:
            sQues = list(dictQandA)
            userQues = random.choice(sQues)
            string = "SECRET-QUESTION "+userQues
        c.send(string.encode())
        answer = c.recv(1024).decode()
        if answer in dictQandA:
            report = "ATTENDANCESUCCESS"
        else:
            report = "ATTENDANCEFAILURE"
        c.send(report.encode())
        if report == "ATTENDANCEFAILURE":
            string = "SECRET-QUESTION "+userQues
            c.send(string.encode())


main()