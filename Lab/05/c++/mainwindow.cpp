#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QImage>
#include <QFileDialog>
#include <QBitArray>
#include <QFile>



bool getBit(QImage image, int i) {
    int x = (i / 3) % image.width();
    int y = (i / 3) / image.width();
    int rez = i % 3;
    if (rez == 0)
        return (image.pixel(x, y) >> 16) & 1;
    else if (rez == 1)
        return (image.pixel(x, y) >> 8) & 1;
    else
        return image.pixel(x, y) & 1;

}

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->pushButton, &QPushButton::clicked, this, &MainWindow::loadImage);
    connect(ui->pushButton_2, &QPushButton::clicked, this, &MainWindow::saveImage);
    connect(ui->pushButton_3, &QPushButton::clicked, this, &MainWindow::encodeMsg);
    connect(ui->pushButton_4, &QPushButton::clicked, this, &MainWindow::decodeMsg);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::loadImage()
{
    QString fileName = QFileDialog::getOpenFileName(this, tr("Open Image"), "", tr("Допустимые форматы (*.png)"));
    image.load(fileName,"PNG");
    image.convertTo(QImage::Format_ARGB32);
    if (image.load(fileName, "PNG")) {
           ui->label->setText("Изображение успешно загружено");
           return;
       }
    else{
       ui->label->setText("Изображение не загружено");
    }
}

void MainWindow::saveImage()
{
    QString fileName = QFileDialog::getSaveFileName(this, tr("Сохранить картинку"), "", tr("Допустимые форматы (*.png)"));
    if (image.save(fileName, "PNG")) {
            ui->label->setText("Изображение успешно сохранено");
        }
    else {
            ui->label->setText("Изображение не сохранено");
        }
}

void MainWindow::encodeMsg()
{
    QString text = ui->plainTextEdit->toPlainText();
    QByteArray charset = text.toUtf8();
    int bytes_size = charset.size();
    image_size = (image.width() * image.height() * 3) / 8 - marker.size()-masage_bytes;
    if (image_size<bytes_size ) {
        ui->label->setText("Ошибка. Не достаточно места!");
        return;
    }
    QByteArray byte_vector;
        byte_vector.push_back(marker);
        for (int i = masage_bytes - 1; i >= 0; i--) {
            byte_vector.push_back((bytes_size >> i*8) & 0xff);
        }
        QString str = ui->plainTextEdit->toPlainText();
        QByteArray str_charset = str.toUtf8();
        byte_vector.push_back(str_charset);
        int index = 0;
        int stop = (index + byte_vector.size()) * 8;
        for (int i = index * 8; i < stop; ++i) {

            int x = (i / 3) % image.width();
            int y = (i / 3) / image.width();
            bool shift = (byte_vector[i / 8] >> (7 - i % 8)) & 1;
            int rez = i % 3;
            if (rez == 0)
                image.setPixel(x, y, (image.pixel(x, y) & ~0x010000) | (shift << 16));
            else if (rez == 1)
                image.setPixel(x, y, (image.pixel(x, y) & ~0x000100) | (shift << 8));
            else
                image.setPixel(x, y, (image.pixel(x, y) & ~0x000001) | shift);
        }

       ui->label->setText("Сообщение добавлено в картинку!");

}

void MainWindow::decodeMsg()
{

        QByteArray vector_byte;
        char temp = 0;
        int index = 0;

        int stop = (index + need_size) * 8;



        for (int i = index * 8; i < stop; ++i) {
            temp = (temp << 1) | getBit(image, i);

            if (i % 8 == 7) {
                vector_byte.push_back(temp);
                temp = 0;
            }
        }

        for (int i = 0; i < marker.size(); ++i) {
            if (marker[i] != vector_byte[i]) {
                ui->label->setText("Сообщение не обнаружено");
                return;
            }
        }

        int all_size = 0;
        for (int i = marker.size(); i < marker.size() + masage_bytes; ++i) {
            all_size = (all_size << 8) + static_cast<unsigned char>(vector_byte[i]);
        }

        if (all_size > image_size) {
            ui->label->setText("Ошибка. Размер сообщения в заголовке превышает размер изображения");
            return;
        }


        QByteArray vector_byte2;
        char temp2 = 0;
        int index2 = need_size;

        int stop2 = (index2 + all_size) * 8;



        for (int i = index2 * 8; i < stop2; ++i) {
            temp2 = (temp2 << 1) | getBit(image, i);

            if (i % 8 == 7) {
                vector_byte2.push_back(temp2);
                temp2 = 0;
            }
        }


        QString text = QString::fromUtf8(vector_byte2);

        ui->plainTextEdit->setPlainText(text);
        ui->label->setText(QString("Присутствует сообщение длиной %1 байт").arg(image_size-bytes_size));

}




