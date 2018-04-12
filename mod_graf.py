from mod_logick import *
import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication, QAction
import sys
import os
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import PyQt5.QtWidgets



kolichestvo = 0
koloda = Koloda()
piramidnaa_koloda = Piramida_koloda(kolichestvo)
koloda_ostatok = Piramida_koloda(kolichestvo).kolod()

class piramida_bild():
    """
    собранная пирамида в виде двухмерного массива с которой можно играть
    """
    def piram_bild(self):
        b = Piramida_koloda(kolichestvo)
        b = b.piram()  # список из карт для заполнения пирамиды
        p = np.zeros((8, 14))
        v = 0
        h = 6  # начинаем с шестой позиции нулевой строки заполнять нашу пирамиду
        srez = 0  # номер элемента для заполнения
        m = 7
        while h < 15:
            piram_zapolnen(v, h, srez, p, b)
            srez += m
            m -= 1
            v += 1
            h += 1
        return p


#print(Sobrannaa_piramida)
def piram_zapolnen(v, h, srez, p, b):
    """
    функция заполняет массив данными для пираммиды
    :param v: высота
    :param h: порядковый номер в ряду
    :param srez: то что ставим на место координат
    :param p: пустой массив
    :param b: данные которые мы должны положить
    :return: заполненую пирамиду
    """
    while h >= 0 and v < 7:
        p[v][h] = (b[srez])[:-2]
        h -= 1
        v += 1
        srez += 1
    return p

Sobrannaa_piramida = piramida_bild()
koloda = koloda.get_koloda_sobranna
piramidnaa_koloda = Piramida_koloda(kolichestvo).piram()
#koloda_ostatok = Piramida_koloda(kolichestvo).kolod()
Sobrannaa_piramida = Sobrannaa_piramida.piram_bild()

class UI(QWidget):
    def __init__(self):
        super(UI,self).__init__()
        self.ui = uic.loadUi(r'C:\Users\владислав\Pictures\колода\graf.ui')
        self.setWindowTitle('piram')
        self.ui.show()
        self.num = 0
        self.accard = None
        self.bind = {}
        self.lst = [self.ui.label, self.ui.label_5, self.ui.label_4, self.ui.label_6, self.ui.label_7, self.ui.label_8, self.ui.label_12,
               self.ui.label_11,
               self.ui.label_10, self.ui.label_9, self.ui.label_17, self.ui.label_16, self.ui.label_15, self.ui.label_14, self.ui.label_13,
               self.ui.label_23, self.ui.label_21, self.ui.label_22, self.ui.label_19, self.ui.label_20, self.ui.label_18, self.ui.label_24,
               self.ui.label_25, self.ui.label_26, self.ui.label_27, self.ui.label_31, self.ui.label_28, self.ui.label_32]

        z = 0
        while z <= 27:
            pixmap = QPixmap("{0}".format(piramidnaa_koloda[z]))
            self.lst[z].setPixmap(pixmap)
            z +=1

        self.startpos_x_y = []
        self.startpos = []
        self.cnt = 0

        for i in self.lst:
            self.startpos_x_y.append([i.x(),i.y()])
            self.startpos.append(i.pos())

        for i in self.lst:
            i.mouseMoveEvent = self.mouseMoveEvent
            i.mouseReleaseEvent = self.mouseReleaseEvent
            i.mousePressEvent = self.mousePressEvent


    def mouseMoveEvent(self, event):

            self.ui.label.move(self.ui.label.mapToParent(event.pos()))
            self.ui.label.raise_()


    def mousePressEvent(self, event):
        count = 0
        print(self.startpos_x_y[count])
        print(event.x(),event.y())
        for i in self.startpos_x_y:
            if event.x() in (range(i[0], i[0]+100)) and event.y() in range(i[1], i[1]+100):
                self.accard = self.lst[count]
                self.num = count
            count += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())

