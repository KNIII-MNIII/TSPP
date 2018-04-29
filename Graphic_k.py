from Object_k import*
from PyQt5.QtWidgets import *
import sys
import os
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QPoint
class UI(QWidget):
    def __init__(self):
        super(UI,self).__init__()
        self.ui = uic.loadUi(r'C:\Users\владислав\Pictures\курсач\graf_kovor.ui')
        self.setWindowTitle('piram')
        self.ui.show()
        self.numeration = 0
        self.numeration_2 = 0
        self.card_m = None
        self.card_n = None
        self.bind = {}
        self.nu = 1

        self.ui.Button.clicked.connect(self.Button_click)

        self.lst_tuz = [self.ui.label, self.ui.label_2, self.ui.label_3, self.ui.label_4]
        self.lst_pole = [self.ui.label_5, self.ui.label_6, self.ui.label_7,
               self.ui.label_8,
               self.ui.label_9, self.ui.label_10, self.ui.label_11, self.ui.label_12, self.ui.label_13, self.ui.label_14, self.ui.label_15,
               self.ui.label_16, self.ui.label_17, self.ui.label_18, self.ui.label_19, self.ui.label_20, self.ui.label_21, self.ui.label_22,
               self.ui.label_23, self.ui.label_24, self.ui.label_25]


        self.kol_vo_kart = 0
        z = 0
        self.z = 0
        while z <= 19:
            pixmap = QPixmap("{0}".format(kovor_card_K[z]))
            self.lst_pole[z].setPixmap(pixmap)
            z +=1
        z = 0
        while z <= 3:
            pixmap = QPixmap("{0}".format(kovor_card_T[z]))
            self.lst_tuz[z].setPixmap(pixmap)
            z += 1

        self.z = 0
        pixmap = QPixmap("{0}".format(card_stack[self.z]))
        self.ui.label_25.setPixmap(pixmap)
        self.startpos_x_y = []
        self.startpos = []
        self.startpos_x_y_T = []
        self.startpos_T = []
        self.cnt = 0
        self.xpos = 0
        self.ypos = 0

        for i in self.lst_pole:
            self.startpos_x_y.append([i.x(),i.y()])
            self.startpos.append(i.pos())

        for i in self.lst_pole:
            i.mouseMoveEvent = self.mouseMoveEvent
            i.mouseReleaseEvent = self.mouseReleaseEvent
            self.ui.mousePressEvent = self.mousePressEvent

        for j in self.lst_tuz:
            self.startpos_x_y_T.append([j.x(), j.y()])
            self.startpos_T.append(j.pos())

        for j in self.lst_tuz:
            j.mouseMoveEvent = self.mouseMoveEvent
            j.mouseReleaseEvent = self.mouseReleaseEvent
            self.ui.mousePressEvent = self.mousePressEvent

    print(kovor_card_K)
    def mousePressEvent(self, event):
        count = 0
        for i in self.startpos_x_y:
            if event.x() in range(i[0], i[0] + 100) and event.y() in range(i[1], i[1] + 120):
                self.card_m = self.lst_pole[count]
                self.numeration = count
            count += 1

        if self.card_m == self.lst_pole[20]:
            pixmap = QPixmap("{0}".format(card_stack[self.z]))
            self.card_m.setPixmap(pixmap)


    def mouseMoveEvent(self, event):
            self.xpos = event.x()
            self.ypos = event.y()
            center_point = QPoint(self.xpos - 50, self.ypos - 60)
            self.card_m.move(self.card_m.mapToParent(center_point))
            self.card_m.raise_()

    def mouseReleaseEvent(self, event):
        count = 0
        for j in self.startpos_x_y_T:
            if self.card_m.x() in range(j[0], j[0] + 100) and self.card_m.y() in range(j[1], j[1] + 120):
                self.card_n = self.lst_tuz[count]
                self.numeration_2 = count
            count += 1
        if (int((kovor_card_K[self.numeration])[:-2]) -1 == int((kovor_card_T[self.numeration_2])[:-2])) and ((kovor_card_K[self.numeration])[-1:])  == ((kovor_card_T[self.numeration_2])[-1:]):
            kovor_card_T[self.numeration_2] = kovor_card_K[self.numeration]
            pixmap = QPixmap("{0}".format(kovor_card_K[self.numeration]))
            self.lst_tuz[self.numeration_2].setPixmap(pixmap)

            kovor_card_K[self.numeration] = card_stack[self.z]

            pixmap = QPixmap("{0}".format(card_stack[self.z]))
            self.lst_pole[self.numeration].setPixmap(pixmap)
            self.z += 1
            pixmap = QPixmap("{0}".format(card_stack[self.z]))
            self.ui.label_25.setPixmap(pixmap)
            self.kol_vo_kart +=1
        if self.card_m.isVisible != False:
            self.card_m.move(self.startpos[self.numeration])

    def Button_click(self):
        k1 = card_stack[self.kol_vo_kart:]
        kovor_card_K.extend(k1)
        set(kovor_card_K)
        random.shuffle((kovor_card_K))
        random.shuffle((card_stack))

        self.lst_tuz = [self.ui.label, self.ui.label_2, self.ui.label_3, self.ui.label_4]
        self.lst_pole = [self.ui.label_5, self.ui.label_6, self.ui.label_7,
                         self.ui.label_8,
                         self.ui.label_9, self.ui.label_10, self.ui.label_11, self.ui.label_12, self.ui.label_13,
                         self.ui.label_14, self.ui.label_15,
                         self.ui.label_16, self.ui.label_17, self.ui.label_18, self.ui.label_19, self.ui.label_20,
                         self.ui.label_21, self.ui.label_22,
                         self.ui.label_23, self.ui.label_24, self.ui.label_25]

        self.kol_vo_kart = 0
        z = 0
        self.z = 0
        while z <= 19:
            pixmap = QPixmap("{0}".format(kovor_card_K[z]))
            self.lst_pole[z].setPixmap(pixmap)
            z += 1
        z = 0
        while z <= 3:
            pixmap = QPixmap("{0}".format(kovor_card_T[z]))
            self.lst_tuz[z].setPixmap(pixmap)
            z += 1
        self.z = 0
        pixmap = QPixmap("{0}".format(card_stack[self.z]))
        self.ui.label_25.setPixmap(pixmap)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())