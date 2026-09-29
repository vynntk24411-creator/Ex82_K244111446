from PyQt6.QtWidgets import QMessageBox

from Chapter5.ex82.libs.my_module import calc_electricity_bill
from Chapter5.ex82.ui.MyMainWindow import Ui_MainWindow


class MyMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.radioButton_type1.setChecked(True)  # chọn sẵn Type 1
        self.kWhUsedLineEdit.setReadOnly(True)
        self.totalBillLineEdit.setReadOnly(True)
        self.setupSignalAndSlot()

    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_calculate.clicked.connect(self.process_calculate)
        self.pushButton_clear.clicked.connect(self.process_clear)
        self.pushButton_exit.clicked.connect(self.call_close_app)

    def process_calculate(self):
        name = self.customerNameLineEdit.text().strip()
        if not name:
            self._show_warning("Vui lòng nhập tên khách hàng!")
            return

        try:
            kwh_old = float(self.kWhOldLineEdit.text())
            kwh_new = float(self.kWhNewLineEdit.text())
        except ValueError:
            self._show_warning("kWh cũ và kWh mới phải là số. Vui lòng nhập lại!")
            self.kWhOldLineEdit.clear()
            self.kWhNewLineEdit.clear()
            self.kWhOldLineEdit.setFocus()
            return

        if kwh_new < kwh_old:
            self._show_warning("kWh mới phải lớn hơn hoặc bằng kWh cũ!")
            return

        customer_type = 1 if self.radioButton_type1.isChecked() else 2
        kwh_used, total = calc_electricity_bill(customer_type, kwh_old, kwh_new)

        self.kWhUsedLineEdit.setText(str(kwh_used))
        self.totalBillLineEdit.setText(f"{total:,.0f} VND")

    def process_clear(self):
        self.customerNameLineEdit.clear()
        self.kWhOldLineEdit.clear()
        self.kWhNewLineEdit.clear()
        self.kWhUsedLineEdit.clear()
        self.totalBillLineEdit.clear()
        self.radioButton_type1.setChecked(True)
        self.customerNameLineEdit.setFocus()

    def _show_warning(self, message):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Lỗi dữ liệu")
        msgBox.setText(message)
        msgBox.setIcon(QMessageBox.Icon.Warning)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()

    def call_close_app(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Xác nhận thoát")
        msgBox.setText("Bạn muốn thoát hay không?")
        msgBox.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgBox.setStandardButtons(buttons)
        ret = msgBox.exec()
        if ret == QMessageBox.StandardButton.Yes:
            exit(0)