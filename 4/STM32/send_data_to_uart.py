import serial


startWrd = "START\n"
endWrd = "END\n"
ack = b'A\r\n'

file = open("data.txt", "r")

data = file.read().splitlines()

ser = serial.Serial('COM7', 115200, timeout=1)


def send_line_to_uart(line):

    line = line + "\n"
    ser.write(line.encode())
    print("send: ", line)

    while(True):
        response = ser.read(3)
        print("Response:", response)

        if response == ack:
            print("ACK received")
            return
    

def main():

    ser.write(startWrd.encode())

    while(True):
        response = ser.read(3)
        print("Response:", response)

        if response == ack:
            print("ACK received")
            break

    for x in data:
        send_line_to_uart(x)

    ser.write(endWrd.encode())

        



if __name__ == "__main__":
    main()


