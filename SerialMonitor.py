#import serial.tools.list_ports
from tkinter import *
master = Tk()

canvas = Canvas(master, height=750, width=750)
canvas.pack()


frame_ust = Frame(master, bg="#546523")
frame_ust.place(relx=0.05, rely=0.05, relwidth=0.75, relheight=0.5)

master.mainloop()

# print("my test")

# ports = serial.tools.list_ports.comports()
# serialInst = serial.Serial()

# portList = []

# for onePort in ports:
#     portList.append(str(onePort))
#     print("here your ports->", str(onePort))

# val = input("select port: COM:")

# for x in range(0, len(portList)):
#     if portList[x].startswith("COM"+str(val)):
#         portVar = "COM" + str(val)
#         print(portList[x])

# serialInst.baudrate = 115200
# serialInst.port = portVar
# serialInst.open()

# while True:
#     if serialInst.in_waiting:
#         packet = serialInst.readline()
#         print(packet.decode('utf'))
