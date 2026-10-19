import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setGeometry(700,300,500,500) # Set the position and size of the window(x, y, width, height)
    self.checkBox=QCheckBox("Do you like food?",self)
    self.initUI()
    
  def initUI(self):
    self.checkBox.setGeometry(10,0,500,100)
    self.checkBox.setStyleSheet("font-size:30px;"
                                "font-family:Arial;")
    self.checkBox.setChecked(False)
    self.checkBox.stateChanged.connect(self.checkbox_changed)
    
  def checkbox_changed(self,state):
     #print("You like food!!")
     #print(state)
     if state==Qt.Checked:
       print("You like food!!")
     else:
       print("You do not like food!!")   
     
  
if __name__=='__main__':
  app=QApplication(sys.argv)
  window=MainWindow()
  window.show()
  sys.exit(app.exec_())
    
    
    