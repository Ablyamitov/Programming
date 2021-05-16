from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

def getBit(image: QImage, index) -> bool:
    x = (index // 3) % image.width()
    y = (index // 3) // image.width()

    rez = index % 3
    if rez == 0:
        return (image.pixel(x, y) >> 16) & 1
    elif rez == 1:
        return (image.pixel(x, y) >> 8) & 1
    elif rez == 2:
        return image.pixel(x, y) & 1
    else:
        raise Exception()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(972, 632)
        MainWindow.setStyleSheet(u"QPushButton:hover{color: blue; font: bold 10pt;}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0442\u0435\u043a\u0441\u0442", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0442\u0435\u043a\u0441\u0442", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<span style=\"font-size:10pt; color:#ff0000;\"><b>\u041f\u0440\u0438\u0432\u0435\u0442:</b></span>", None))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.image = QImage()
        self.image_size = 0
        self.byte_list_size = 0
        self.marker = bytes((0b11100010, 0b10011101, 0b10100100))
        self.masage_bytes = 4
        self.is_loaded = False
        self.need_size = self.masage_bytes + len(self.marker)
        self.ui.pushButton.clicked.connect(self.loadImage)
        self.ui.pushButton_2.clicked.connect(self.saveImage)
        self.ui.pushButton_3.clicked.connect(self.encodeMsg)
        self.ui.pushButton_4.clicked.connect(self.decodeMsg)

    @Slot()
    def loadImage(self):
        fileName, _ = QFileDialog.getOpenFileName(self, self.tr("Open Image"), "", self.tr("Доступные форматы (*.png)"))
        self.image.convertTo(QImage.Format_ARGB32)
        if self.image.load(fileName):
            self.ui.label.setText('Изображение успешно загружено')
            return
        else:
            self.ui.label.setText('Изображение не загружено')
        self.is_loaded = True
    @Slot()
    def saveImage(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Сохранить изображение", "", "Допустимые форматы (*.png)")
        if self.image.save(fileName, "PNG"):
            self.ui.label.setText("Изображение успешно сохранено")
        else:
            self.ui.label.setText('Не удалось сохранить изображение')
        self.is_loaded = True
    @Slot()
    def encodeMsg(self):
        text = self.ui.plainTextEdit.toPlainText()
        byte_list = text.encode()
        self.byte_list_size = len(byte_list)
        self.image_size = (self.image.width() * self.image.height() * 3) // 8 - len(self.marker)-self.masage_bytes
        if (self.image_size<self.byte_list_size):
            self.ui.label.setText("Ошибка. Не достаточно места!")
            return

        byte_vector = QByteArray()
        byte_vector.push_back(self.ui.plainTextEdit.toPlainText().encode())
        for i in range(4):
            byte_vector.push_front(bytes(((self.byte_list_size >> i * 8) & 0xff,)))
        #
        for i in range(len(self.marker) - 1, -1, -1):
            byte_vector.push_front(bytes((self.marker[i],)))

        str_text = self.ui.plainTextEdit.toPlainText()
        #byte_list_str_text = str_text.encode()
        #byte_vector.push_back(byte_list_str_text)
        index = 0
        #stop = 0
        stop = (index +  byte_vector.size())*8
        for i in range(index * 8,stop):
            x = (i // 3) % self.image.width()
            y = (i // 3) // self.image.width()
            shift = (int.from_bytes(byte_vector[i // 8], "big" )>> (7 - i % 8)) & 1
            rez = i % 3
            if (rez == 0):
                self.image.setPixel(x, y, (self.image.pixel(x, y) & ~0x010000) | (shift << 16))
            elif (rez == 1):
                self.image.setPixel(x, y, (self.image.pixel(x, y) & ~0x000100) | (shift << 8))
            elif rez == 2:
                self.image.setPixel(x, y, (self.image.pixel(x, y) & ~0x000001) | shift)
        self.ui.label.setText("Сообщение добавлено в картинку!")

    
    @Slot()
    def decodeMsg(self):
        vector_byte=QByteArray()
        temp = 0
        index = 0
        stop = (index + len(self.marker)+4) * 8

        for i in range (index * 8,stop,1):
            temp = (temp << 1) | getBit(self.image, i)
            if (i % 8 == 7):
                vector_byte.push_back(bytes((temp,)))
                temp = 0

        for i in range (0,len(self.marker)):
            if bytes((self.marker[i],)) != vector_byte[i]:
                self.ui.label.setText("Сообщение не обнаружено")
                return

        all_size = 0

        for i in range(len(self.marker),len(self.marker)+4):
            all_size = (all_size << 8) + int.from_bytes(vector_byte[i],"big")
        vector_byte.clear()
        
        

        vector_byte2 = QByteArray()
        temp2 = 0
        index2 = len(self.marker)+4

        stop2 = (index2 + all_size) * 8


        for i in range(index2 * 8,stop2):
            temp2 = (temp2 << 1) | getBit(self.image, i)

            if (i % 8 == 7):
                vector_byte2.push_back(bytes((temp2,)))
                temp2 = 0



        self.ui.plainTextEdit.setPlainText(bytes(vector_byte2).decode("utf-8"))
        self.ui.label.setText(f"Присутствует сообщение длиной {all_size} байт.")

        

            
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
  
    window = MainWindow()
    window.show()
  
    sys.exit(app.exec_())