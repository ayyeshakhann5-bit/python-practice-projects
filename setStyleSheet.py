import sys

from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QWidget,QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
      super().__init__()
      
      self.button1=QPushButton("#1")
      self.button2=QPushButton("#2")
      self.button3=QPushButton("#3")
      self.initUI()
      
    def initUI(self):
      central_widget=QWidget()
      self.setCentralWidget(central_widget)
      
      hBox=QHBoxLayout()
      
      hBox.addWidget(self.button1)
      hBox.addWidget(self.button2)
      hBox.addWidget(self.button3)
      
      central_widget.setLayout(hBox)
      
      self.button1.setObjectName("button1")
      self.button2.setObjectName("button2")
      self.button3.setObjectName("button3")
      
      self.setStyleSheet("""
           QPushButton{
             font-size:40px;
             border-radius:15px;
             font-family:Arial;
             padding:15px 75px;
             border:3px solid;
             margin:25px
             
           }  
           
           QPushButton#button1{
             background-color:hsl(4, 85%, 61%);
           }  
           
           QPushButton#button2{
              background-color:hsl(181, 66%, 80%);
           }           
           QPushButton#button3{
             background-color:rgb(131, 231, 158);
           }    
           QPushButton#button1:hover{
             background-color:hsl(4, 85%, 31%);
           }  
           
           QPushButton#button2:hover{
              background-color:hsl(181, 66%, 50%);
           }           
           QPushButton#button3:hover{
             background-color:rgb(131, 231, 108);
           }                             
                         
                         
                         """)
      
    
if __name__=='__main__':
  app=QApplication(sys.argv)
  window=MainWindow()
  window.show()
  sys.exit(app.exec_())    