#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT
    QImage image;

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

public slots:
    void loadImage();
    void saveImage();
    void encodeMsg();
    void decodeMsg();

private:
    Ui::MainWindow *ui;
    const std::array<char, 3> marker {
           static_cast<char>(0b11100010),
           static_cast<char>(0b10011101),
           static_cast<char>(0b10100100)
       };
    int masage_bytes = 4;
    int image_size;
    int bytes_size;
    int need_size = masage_bytes + marker.size();
};
#endif // MAINWINDOW_H
