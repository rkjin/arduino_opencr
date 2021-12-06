import serial  
import serial.tools.list_ports as sp
import os, sys, time

list = sp.comports() # get opened com port list
for i, c in enumerate(list):
    print(f"{i} : Connected COM ports: {c} " )
select_comport = input('select No of com port :')
os.system('sudo chmod 666 '+list[int(select_comport)].device) # make comport enable
ser = serial.Serial(list[int(select_comport)].device, 9600, timeout = 1)
ser.flush() # wait until com port finish job
print('serial open')

while True:
    op = input("숫자 입력")
    ser.write(op.encode('utf-8'))

    if op == '999':
        ser.close()
        break


