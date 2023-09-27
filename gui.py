from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic,QtWidgets
import sys, subprocess
from encrypter import encrypt, decrypt, initialize_bin,deleteFile
from error import Ui_Dialog



class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("main.ui", self)

		# Define our widgets
		self.browse = self.findChild(QPushButton, "browse")
		
		self.encrypt = self.findChild(QPushButton, "encryptButton")
		self.decrypt = self.findChild(QPushButton, "decryptButton")
		self.deleteFile = self.findChild(QPushButton, "deleteFile")
		self.openFile=self.findChild(QPushButton,"openFile")
		self.openFile.clicked.connect(self.openf)
		self.browse.clicked.connect(self.clicker)
		self.encrypt.clicked.connect(self.encryption)
		self.decrypt.clicked.connect(self.decryption)
		self.deleteFile.clicked.connect(self.delete)
		self.filename='null'
		
		# Show The App
		self.show()
	def openf(self):
		if(self.filename!='null'):
			try:
				subprocess.run(['notepad',self.filename])
			except:
				print(self.filename)
				Ui_Dialog.openWindow(self,"file does not exist")
		else:
			Ui_Dialog.openWindow(self,"file does not exist")
	def delete(self):
		try:
			deleteFile()
			self.filename='null'
			self.fileName.setText('Choose File')
		except:
			Ui_Dialog.openWindow(self,"encrypted.bin does not exist")
	def encryption(self):
		try:
			encrypt()
		except:
			Ui_Dialog.openWindow(self,"Add a file first")
	def decryption(self):
		try:
			decrypt()
		except:
			Ui_Dialog.openWindow(self,"encrypt a file first")

	def clicker(self):
		# Open File Dialog
		fname = QFileDialog.getOpenFileName(self, "Open File", "C:", "BIN File (*.bin);; Text File (*.txt)" )
		if fname:
			self.fileName.setText(fname[0])
			try:
				self.filename=initialize_bin(fname[0])
			except:
				Ui_Dialog.openWindow(self,"please choose a .bin or .txt file")

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
