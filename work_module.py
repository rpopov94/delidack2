import glob
import sys
import time
from crc_mdb import addcrc
import serial


def serial_ports():
    '''
    :return: list comname which connected
    '''
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def _generic_command(SlaveID: int, cmd: int):
    cmd = addcrc([SlaveID, 16, 0, 50, 0, 1, 2, 0, cmd])
    return bytearray(cmd)


def handler(output_1, output_2, output_3, output_4) -> int:
    cmd = 0
    if output_1:
        cmd = 1  # 1 output
    if output_2:
        cmd = 2  # 2 output
    if output_3:
        cmd = 4  # 3 output
    if output_4:
        cmd = 8  # 4 output
    if output_1 and output_2:
        cmd = 3
    if output_1 and output_3:  # not work
        cmd = 5
    if output_2 and output_3:
        cmd = 6
    if output_2 and output_4:  # not - 4
        cmd = 10
    if output_3 and output_4:  #
        cmd = 12
    if output_1 and output_2 and output_4:
        cmd = 11
    if output_1 and output_2 and output_3:
        cmd = 7
    if output_2 and output_3 and output_4:
        cmd = 14
    if output_1 and output_2 and output_3 and output_4:
        cmd = 15
    return cmd

# print(handler(1, 0, 0, 0))
# print(handler(0, 1, 0, 0))
# print(handler(0, 0, 1, 0))
# print(handler(0, 0, 0, 1))
# print(handler(1, 1, 0, 0))
# print(handler(1, 0, 1, 0))
# print(handler(1, 0, 0, 1))
# print(handler(0, 1, 1, 0))
# print(handler(0, 1, 0, 1))
# print(handler(1, 1, 1, 0))
# print(handler(1, 1, 0, 1))
# print(handler(0, 1, 1, 1))
# print(handler(1, 1, 1, 1))
