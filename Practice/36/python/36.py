from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QByteArray
from PySide6.QtGui import QImage

def set_bit(image: QImage, index, value) -> None:
    pixel_index = index // 3
    x = pixel_index % image.width()
    y = pixel_index // image.width()

    switch = index % 3
    if switch == 0:
        image.setPixel(x, y, (image.pixel(x, y) & ~0x010000) | (value << 16))
    elif switch == 1:
        image.setPixel(x, y, (image.pixel(x, y) & ~0x000100) | (value << 8))
    elif switch == 2:
        image.setPixel(x, y, (image.pixel(x, y) & ~0x000001) | value)


def get_bit(image: QImage, index) -> bool:
    pixel_index = index // 3
    x = pixel_index % image.width()
    y = pixel_index // image.width()

    switch = index % 3
    if switch == 0:
        return (image.pixel(x, y) >> 16) & 1
    elif switch == 1:
        return (image.pixel(x, y) >> 8) & 1
    elif switch == 2:
        return image.pixel(x, y) & 1
    else:
        raise Exception()


def read_bytes(image: QImage, begin, length) -> QByteArray:
    byte_array = QByteArray()
    buffer = 0
    end = (begin + length) * 8

    for i in range(begin * 8, end):
        buffer = (buffer << 1) | get_bit(image, i)

        if i % 8 == 7:
            byte_array.push_back(bytes((buffer,)))
            buffer = 0

    return byte_array

    
def write_bytes(image: QImage, byte_array: QByteArray, begin) -> None:
    end = (begin + byte_array.size()) * 8
    for i in range(begin * 8, end):
        set_bit(image, i, (int.from_bytes(byte_array[i // 8], "big") >> (7 - i % 8)) & 1)


if __name__ == "__main__":
    import sys
    from steganography import MainWindow
    app = QApplication(sys.argv)
  
    window = MainWindow()
    window.show()
  
    sys.exit(app.exec_())