import serial
import serial.serialutil as sutil

port = input("Введите номер COM-порта: ")

try:
    with serial.Serial(port, baudrate=9600, bytesize=8, stopbits=1, parity=serial.PARITY_NONE, timeout=60) as ser:
        filename = input("Введите имя файла (без расширения) для выходных данных: ")

        with open(filename + ".txt", 'a') as output_file:
            while True:
                try:
                    line = ser.read_until(expected=sutil.CR)
                    output_file.write(line)
                except serial.SerialTimeoutException:
                    break
                except KeyboardInterrupt:
                    break

except serial.SerialException:
    print(f"Порт {port} недоступен")



