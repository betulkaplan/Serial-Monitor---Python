print("my test")

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