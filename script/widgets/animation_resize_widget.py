from PySide6.QtCore import QEventLoop, QPropertyAnimation, QEasingCurve, QSize
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class AnimationResizeWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.m_pAnimation = QPropertyAnimation(self, b'size')
        self.m_pAnimation.setEasingCurve(QEasingCurve.Linear)
        # self.m_pAnimation.finished.connect()
        self.m_Button = QPushButton()
        self.m_Button.setText("Run")
        self.m_Button.clicked.connect(self.textbuttonclick)
        
        self.m_layout = QHBoxLayout()
        self.setLayout(self.m_layout)
        self.m_layout.addWidget(self.m_Button)

        self.setAnimDuration(2000)
    
    def getAnimSize(self):
        return self.size()
    
    def setAnimSize(self, size:QSize):
        self.setFixedSize(size)

    def setAnimDuration(self, msecs):
        self.m_pAnimation.setDuration(msecs)
    
    def setAnimStartSize(self, size:QSize):
        self.m_pAnimation.setStartValue(size)
    
    def setAnimEndSize(self, size:QSize):
        self.m_pAnimation.setEndValue(size)
    
    def textbuttonclick(self):
        self.setAnimStartSize(self.size())
        if self.size() != QSize(200,400):
            self.setAnimEndSize(QSize (200,400));
        else:
            self.setAnimEndSize(QSize(300,200));
        
        self.runAnim();
    
    def runAnim(self):
        if self.m_pAnimation.startValue() == self.m_pAnimation.endValue():
            print(111)
            return
        self.m_pAnimation.start()
        print(555)


        
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = AnimationResizeWidget()
    window.setFixedSize(300, 200)
    window.show()
    sys.exit(app.exec())


