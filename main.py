import time

from PyQt5 import QtWidgets
from dedilack_ui import Ui_DEDILAK2
import serial
from work_module import (serial_ports,
                         _generic_command,
                         handler)


class DEDILACK_UI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.w_root = Ui_DEDILAK2()
        self.w_root.setupUi(self)
        self.w_root.comboBox.addItems(serial_ports())
        self.w_root.pushButton.clicked.connect(self.send)

    def send(self):
        global ser, SlaveID
        try:
            COM = self.w_root.comboBox.currentText()
            SlaveID = self.w_root.textEdit.toPlainText()
            ser = serial.Serial(COM,
                                9600,
                                timeout=0.002,
                                bytesize=8,
                                stopbits=1
                                )
        except Exception as e:
            pass
        output_1 = self.w_root.checkBox.isChecked()
        output_2 = self.w_root.checkBox_3.isChecked()
        output_3 = self.w_root.checkBox_4.isChecked()
        output_4 = self.w_root.checkBox_2.isChecked()
        cmd = handler(output_1,
                      output_2,
                      output_3,
                      output_4
                      )
        try:
            cmd = _generic_command(int(SlaveID), cmd)
            ser.write(cmd)
            time.sleep(5)
            cmd_2 = _generic_command(int(SlaveID), 0)
            ser.write(cmd_2)
        except:
            pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication([])
    application = DEDILACK_UI()
    application.show()
    sys.exit(app.exec())
