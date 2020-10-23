import sys
from PyQt5.QtWidgets import *
from speed_test import Ui_Dialog 
import speedtest


st= speedtest.Speedtest()


class speedtest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)



        self.ui.pushButton.clicked.connect(self.buttonClick)

    def buttonClick(self):
      
        self.ui.down_load.setText(str(st.download()//10**6)+" Mbps")
        self.ui.up_load.setText(str(st.upload()//10**6)+" Mbps")
        self.ui.ping.setText(str(int(st.results.ping))+" MS")


uygulama=QApplication(sys.argv)
pencere= speedtest()
pencere.show()
sys.exit(uygulama.exec_())
