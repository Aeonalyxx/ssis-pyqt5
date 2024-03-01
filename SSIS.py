import csv
from PyQt5 import QtCore, QtGui, QtWidgets

class AddStudentDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Student")
        self.setFixedSize(500, 210)

        self.student_id_label = QtWidgets.QLabel("Student ID:")
        self.name_label = QtWidgets.QLabel("Student Name:")
        self.gender_label = QtWidgets.QLabel("Student Gender:")
        self.course_label = QtWidgets.QLabel("Student Course:")
        self.year_label = QtWidgets.QLabel("Student Year:")

        self.Student_id_edit= QtWidgets.QLineEdit(self)
        self.name_edit = QtWidgets.QLineEdit(self)
        
        self.gender_combobox = QtWidgets.QComboBox(self)
        self.gender_combobox.addItems(["Male", "Female"])

        self.course_combobox = QtWidgets.QComboBox(self)
        self.course_combobox.addItems(["BS Computer Science", "BS Information Technology", "BS Information System", "BS Computer Application"])

        self.year_combobox = QtWidgets.QComboBox(self)
        self.year_combobox.addItems(["1", "2", "3", "4"])

        self.ok_button = QtWidgets.QPushButton("Ok", self)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button = QtWidgets.QPushButton("Cancel", self)
        self.cancel_button.clicked.connect(self.reject)

        # Create layouts
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow(self.student_id_label, self.Student_id_edit)
        form_layout.addRow(self.name_label, self.name_edit)
        form_layout.addRow(self.gender_label, self.gender_combobox)
        form_layout.addRow(self.course_label, self.course_combobox)
        form_layout.addRow(self.year_label, self.year_combobox)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.ok_button)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        main_layout.addLayout(button_layout)
        
    def accept(self):
        if not all((field.text() if isinstance(field, QtWidgets.QLineEdit) else field.currentText()) for field in [self.Student_id_edit, self.name_edit, self.gender_combobox, self.course_combobox, self.year_combobox]):
            QtWidgets.QMessageBox.critical(self, "Error", "Please fill in all fields.")
        else:
            super().accept()

class EditStudentDialog(QtWidgets.QDialog):
    def __init__(self, student_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Student")
        self.setFixedSize(500, 210)

        self.student_id_label = QtWidgets.QLabel("Student ID:")
        self.name_label = QtWidgets.QLabel("Student Name:")
        self.gender_label = QtWidgets.QLabel("Student Gender:")
        self.course_label = QtWidgets.QLabel("Student Course:")
        self.year_label = QtWidgets.QLabel("Student Year:")

        self.Student_id_edit = QtWidgets.QLineEdit(self)
        self.name_edit = QtWidgets.QLineEdit(self)
        
        self.gender_combobox = QtWidgets.QComboBox(self)
        self.gender_combobox.addItems(["Male", "Female"])

        self.course_combobox = QtWidgets.QComboBox(self)
        self.course_combobox.addItems(["BS Computer Science", "BS Information Technology", "BS Information System", "BS Computer Application"])

        self.year_combobox = QtWidgets.QComboBox(self)
        self.year_combobox.addItems(["1", "2", "3", "4"])

        self.ok_button = QtWidgets.QPushButton("Ok", self)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button = QtWidgets.QPushButton("Cancel", self)
        self.cancel_button.clicked.connect(self.reject)

        # Create layouts
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow(self.student_id_label, self.Student_id_edit)
        form_layout.addRow(self.name_label, self.name_edit)
        form_layout.addRow(self.gender_label, self.gender_combobox)
        form_layout.addRow(self.course_label, self.course_combobox)
        form_layout.addRow(self.year_label, self.year_combobox)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.ok_button)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        main_layout.addLayout(button_layout)

        # Set the provided student data to the dialog
        self.setStudentData(student_data)
        
    def setStudentData(self, student_data):
        self.Student_id_edit.setText(student_data[0])
        self.name_edit.setText(student_data[1])
        self.gender_combobox.setCurrentText(student_data[2])
        self.course_combobox.setCurrentText(student_data[3])
        self.year_combobox.setCurrentText(student_data[4])

    def accept(self):
        if not all((field.text() if isinstance(field, QtWidgets.QLineEdit) else field.currentText()) for field in [self.Student_id_edit, self.name_edit, self.gender_combobox, self.course_combobox, self.year_combobox]):
            QtWidgets.QMessageBox.critical(self, "Error", "Please fill in all fields.")
        else:
            # Update the student data list with the edited data
            edited_student_data = [
                self.Student_id_edit.text(),
                self.name_edit.text(),
                self.gender_combobox.currentText(),
                self.course_combobox.currentText(),
                self.year_combobox.currentText()
            ]  
            self.setStudentData(edited_student_data)
            
            super().accept()
        
class Ui_MainWindow(object):
    def __init__(self):
        self.saved_file_name = None
        self.student_data = []
        self.original_student_data = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SSIS")
        MainWindow.resize(995, 622)
        
        # Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Buttons
        self.Add_Student = self.createButton("Add Student", 10, 160, 101, 41)
        self.Edit_Student = self.createButton("Edit Student", 10, 230, 101, 41)
        self.Delete_Student = self.createButton("Delete Student", 10, 300, 101, 41)

        # Table Widget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(130, 80, 841, 491))
        self.setupTableWidget()

        # Text Browsers
        self.textBrowser = self.createTextBrowser(280, 20, 541, 51)
        self.textBrowser_2 = self.createTextBrowser(20, 80, 81, 51)

        # Set Central Widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu Bar
        self.setupMenuBar(MainWindow)

        # Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Actions
        self.setupActions(MainWindow)
        MainWindow.closeEvent = self.closeEvent

        # Connect Slots by Name
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.disableEditDeleteButtons()
        
    def updateOriginalData(self):
        # Update the original data with the current state of the table
        self.original_student_data = [[self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())] for row in range(self.tableWidget.rowCount())]
    
        
    def createButton(self, text, x, y, width, height):
        button = QtWidgets.QPushButton(self.centralwidget)
        button.setGeometry(QtCore.QRect(x, y, width, height))
        button.setObjectName(text)
        return button
    

    def createTextBrowser(self, x, y, width, height):
        text_browser = QtWidgets.QTextBrowser(self.centralwidget)
        text_browser.setGeometry(QtCore.QRect(x, y, width, height))
        text_browser.setObjectName("textBrowser")
        return text_browser

    def setupTableWidget(self):
        self.tableWidget.setMinimumSize(QtCore.QSize(841, 0))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.original_column_sizes = {}

        header_labels = ["Student ID:", "Name:", "Gender:", "Course:", "Year:"]
        for i, label in enumerate(header_labels):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(i, item)
            item.setText(label)
            
            if label == "Name:":
                self.tableWidget.setColumnWidth(i, 250)
            elif label == "Course:":
                self.tableWidget.setColumnWidth(i, 192)
            elif label == "Year:":
                self.tableWidget.setColumnWidth(i, 120)
            else:
                self.tableWidget.setColumnWidth(i, 126)
            
            self.original_column_sizes[i] = self.tableWidget.columnWidth(i)

        # Set the table to be non-editable
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Set the selection behavior to select entire rows
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)

    def setupMenuBar(self, MainWindow):
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 26))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())

    def setupActions(self, MainWindow):
        self.actionOpen = self.createAction("Open", "Ctrl+O")
        self.actionSave = self.createAction("Save", "Ctrl+S")
        self.actionClose = self.createAction("Close", "Alt+F4")

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)

        # Open Action
        self.actionOpen.triggered.connect(self.openCSV)

        # Save Action
        self.actionSave.triggered.connect(self.saveToCSV)
        self.actionSave.triggered.connect(self.hasUnsavedChanges)

        # Close Action
        self.actionClose.triggered.connect(MainWindow.close)

        # Add Student Action
        self.Add_Student.clicked.connect(self.addStudentInfo)

        # Edit Student Action
        self.Edit_Student.clicked.connect(self.editStudentInfo)

        # Delete Student Action
        self.Delete_Student.clicked.connect(self.deleteStudentInfo)
        
    def closeEvent(self, event):
        if self.hasUnsavedChanges():
            result = self.promptSaveChanges()
            if result == QtWidgets.QMessageBox.Save:
                self.saveToCSV()
            elif result == QtWidgets.QMessageBox.Cancel:
                event.ignore()
                return

        event.accept()

    def promptSaveChanges(self):
        reply = QtWidgets.QMessageBox.question(None, 'Save Changes', 'Do you want to save changes before closing?',
                                               QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel)
        return reply

    def hasUnsavedChanges(self):
        if not self.saved_file_name:
            # If there's no saved file, consider any changes as unsaved
            return bool(self.student_data)
        else:
            # Compare the current state with the original state
            current_data = [[self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())] for row in range(self.tableWidget.rowCount())]

            # Check if there are unsaved changes
            return current_data != self.original_student_data
        
    def openCSV(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Open CSV File", "", "CSV Files (*.csv)")

        if file_name:
            self.readCSV(file_name)

    def readCSV(self, file_name):
        with open(file_name, 'r') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader, None)

            if header:
                self.tableWidget.setColumnCount(len(header))
                self.tableWidget.setHorizontalHeaderLabels(header)

                self.student_data = [row for row in reader]

                self.updateTableWidget()
                
                self.saved_file_name = file_name

    
    def createAction(self, text, shortcut=None):
        action = QtWidgets.QAction(MainWindow)
        action.setObjectName("action" + text)
        action.setText(text)

        if shortcut:
            action.setShortcut(shortcut)

        return action

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Student Information System (SSIS)"))
        self.Add_Student.setText(_translate("MainWindow", "Add Student"))
        self.Edit_Student.setText(_translate("MainWindow", "Edit Student"))
        self.Delete_Student.setText(_translate("MainWindow", "Delete Student"))

        header_labels = ["Student ID:", "Name:", "Gender:", "Course:", "Year:"]
        for i, label in enumerate(header_labels):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", label))

        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Simple Student Information System</span></p></body></html>"))

        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom=0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">SSIS</span></p></body></html>"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def saveToCSV(self):
        if not self.saved_file_name:
            file_name, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", "StudentList", "CSV Files (*.csv)")
        else:
            file_name = self.saved_file_name

        if file_name:
            with open(file_name, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)

                header = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
                writer.writerow(header)

                for row in range(self.tableWidget.rowCount()):
                    row_data = [self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())]
                    writer.writerow(row_data)

            self.saved_file_name = file_name

            # Update the original data after saving
            self.original_student_data = [[self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())] for row in range(self.tableWidget.rowCount())]


    def addStudentInfo(self):
        dialog = AddStudentDialog()
        result = dialog.exec_()
        self.updateOriginalData()
        
        if result == QtWidgets.QDialog.Accepted:
            student_id = dialog.Student_id_edit.text()
            # Check if the entered student ID is already in the list
            if any(data[0] == student_id for data in self.student_data):
                QtWidgets.QMessageBox.warning(None, "Warning", "Student ID already exists. Please enter a unique ID.")
                return
            
            name = dialog.name_edit.text()
            gender = dialog.gender_combobox.currentText()
            course = dialog.course_combobox.currentText()
            year = dialog.year_combobox.currentText()
            
            student_data = [student_id, name, gender, course, year]
            self.student_data.append(student_data)
            self.original_column_sizes = {i: self.tableWidget.columnWidth(i) for i in range(self.tableWidget.columnCount())}
            
            self.updateTableWidget()
            self.updateStudentData()
            
    def updateStudentData(self):
      if self.saved_file_name:
        # If there's a saved file, update self.student_data with the current state of the table
        self.student_data = [[self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())] for row in range(self.tableWidget.rowCount())]

            
    def editStudentInfo(self):
      # Prompt user for the student ID
        student_id, ok = QtWidgets.QInputDialog.getText(None, "Edit", "Enter Student ID:")
        self.updateOriginalData()

        if ok:
            # Find the student data corresponding to the entered student ID
            student_data_to_edit = next((data for data in self.student_data if data[0] == student_id), None)

            if student_data_to_edit:
                # Create the dialog and set the data for editing
                dialog = EditStudentDialog(student_data_to_edit)
                result = dialog.exec_()

                if result == QtWidgets.QDialog.Accepted:
                    # Check if the edited student ID already exists in the list (excluding the current student being edited)
                    edited_student_id = dialog.Student_id_edit.text()
                    if edited_student_id != student_id and any(data[0] == edited_student_id for data in self.student_data):
                        QtWidgets.QMessageBox.warning(None, "Warning", "Edited Student ID already exists. Please enter a unique ID.")
                        return
                    
                    # Update the student data list
                    student_data_to_edit[1] = dialog.name_edit.text()
                    student_data_to_edit[2] = dialog.gender_combobox.currentText()
                    student_data_to_edit[3] = dialog.course_combobox.currentText()
                    student_data_to_edit[4] = dialog.year_combobox.currentText()

                    # Update the table widget
                    self.updateTableWidget()
                    self.updateStudentData()
                
            else:
                QtWidgets.QMessageBox.warning(None, "Warning", "Student ID not found or is empty.")

    def deleteStudentInfo(self):
      # Prompt user for the student ID
        self.updateOriginalData()
        student_id, ok = QtWidgets.QInputDialog.getText(None, "Delete", "Enter Student ID:")

        if ok:
            # Find the student data corresponding to the entered student ID
            student_data_to_delete = next((data for data in self.student_data if data[0] == student_id), None)

            if student_data_to_delete:
                # Confirm deletion with a dialog
                confirmation = QtWidgets.QMessageBox.question(None, "Confirmation", f"Do you want to delete student {student_id}?",
                                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                
                if confirmation == QtWidgets.QMessageBox.Yes:
                    # Delete the student data from the list
                    self.student_data.remove(student_data_to_delete)

                    # Update the table widget
                    self.updateTableWidget()
                    
                    # Notify about successful deletion
                    QtWidgets.QMessageBox.information(None, "Information", f"Student {student_id} has been deleted.")
                else:
                  QtWidgets.QMessageBox.information(None, "Information", "Canceled.")
            else:
                QtWidgets.QMessageBox.warning(None, "Warning", "Student ID not found or is empty.")

    def updateTableWidget(self):
        self.tableWidget.setRowCount(len(self.student_data))

        for row, data in enumerate(self.student_data):
            for col, value in enumerate(data):
                item = QtWidgets.QTableWidgetItem(value)
                self.tableWidget.setItem(row, col, item)
        
        if len(self.student_data) > 0:
            self.enableEditDeleteButtons()
        else:
            self.disableEditDeleteButtons()

    # Restore original column sizes
        for col in range(self.tableWidget.columnCount()):
            self.tableWidget.setColumnWidth(col, self.original_column_sizes[col])

    def enableEditDeleteButtons(self):
        self.Edit_Student.setEnabled(True)
        self.Delete_Student.setEnabled(True)

    def disableEditDeleteButtons(self):
        self.Edit_Student.setEnabled(False)
        self.Delete_Student.setEnabled(False)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
