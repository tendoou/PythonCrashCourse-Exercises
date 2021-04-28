from PyQt5 import QtWidgets, uic
from Password_Manager import PasswordManager
import sys


def consult(win, pm, website):
    credential = pm.consult_login_info(website)
    if credential:
        win.label.setText(credential.password)
    else:
        win.label.setText("No esta reistrado el website")

def delete(win, pm, website):
    result = pm.delete_login_info(website)

    if result:
        initialize_list(win, pm)

def initialize_list(win, pm):
    win.comboBox.clear()
    for c in pm.credentials:
        win.comboBox.addItem(c.website)

app = QtWidgets.QApplication([])
pm = PasswordManager()
win = uic.loadUi("C:/Users/zerod/Desktop/ui.ui") #specify the location of your .ui file
initialize_list(win, pm)
win.deleteButton.clicked.connect(lambda: delete(win, pm, win.comboBox.currentText()))
win.comboBox.currentTextChanged.connect(lambda: consult(win, pm, win.comboBox.currentText()))
win.show()

sys.exit(app.exec())