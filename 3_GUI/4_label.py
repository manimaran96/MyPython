import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
    app = QApplication(sys.argv)

    #initialize the widget and label
    win = QWidget()
    l1=QLabel()
    l2=QLabel()
    l3=QLabel()
    l4=QLabel()
    
    #set values and image on the label
    l1.setText("Hello World")
    l2.setText("<a href='#'>welcome to Python GUI Programming</a>")
    l3.setPixmap(QPixmap("python.png"))
    l4.setText("<a href='www.manimaran.wordpress.com'>Click to go My Blog</a>")
    
    #label alignments
    l1.setAlignment(Qt.AlignCenter)
    l2.setAlignment(Qt.AlignLeft)
    l3.setAlignment(Qt.AlignCenter)
    l4.setAlignment(Qt.AlignRight)
    
    #Layout BOX
    vbox=QVBoxLayout()
    
    vbox.addWidget(l1)
    vbox.addStretch()
    vbox.addWidget(l2)
    vbox.addStretch()
    vbox.addWidget(l3)
    vbox.addStretch()
    vbox.addWidget(l4)

    l1.setOpenExternalLinks(True)
    l2.linkHovered.connect(hovered)
    l4.linkActivated.connect(clicked)

    l1.setTextInteractionFlags(Qt.TextSelectableByMouse)
    win.setLayout(vbox)
    win.setWindowTitle("QLabel Demo")
    win.show()

    sys.exit(app.exec_())

def hovered():
    print "hovering"

def clicked():
    print "clicked"

if __name__ == '__main__':
    window()
