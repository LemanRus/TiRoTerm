import serial
import serial.serialutil as sutil
import os

path = os.path.join("c:", os.sep, "TIRAtest", str(datetime.now().year))
if not os.path.exists(path):
    os.makedirs(path)

port = 'COM5'
try:
    with serial.Serial(port, baudrate=9600, bytesize=8, stopbits=1, parity=serial.PARITY_NONE, timeout=60) as ser:
        filename = input("Введите имя файла (без расширения) для выходных данных: ") + ".txt"

        while True:
            try:
                line = ser.read_until(b'\r')
                decoded = line.decode("utf-8", errors='replace')
                decoded = decoded.replace("@D", " ")
                decoded = decoded.replace("", " ")
                decoded = decoded.replace(b'\x1bK\x07\x00\x06\x1ab\xef\xbf\xbdb\x1a\x06\x08\x1bf\x00\x01'.decode("utf-8"), "Δ")
                decoded = decoded.replace(b'\x1bK\x07\x00\x00H\xef\xbf\xbd\xef\xbf\xbdH\x00\x00\x08\x1bf\x00\x01'.decode("utf-8"), "²")
                decoded = decoded.strip(b'\x00\t\r\n '.decode("utf-8"))
                print(decoded)
                with open(os.path.join(path, filename), 'a', encoding="utf-8") as output_file:
                    output_file.write(decoded + '\n')
            except serial.SerialException:
                break

except serial.SerialException:
    print(f"Порт {port} недоступен")



