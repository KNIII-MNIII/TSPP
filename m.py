from Logic_class_structure import*
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication, QAction
import sys
import os
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QPoint
COM = Complected_Pyr().create_pyr()
class UI(QWidget):
    def __init__(self):
        super(UI,self).__init__()
        self.ui = uic.loadUi(r'C:\Users\владислав\Pictures\колода\graf.ui')
        self.setWindowTitle('piram')
        self.ui.show()
        self.numeration = 0
        self.numeration_2 = 0
        self.card_m = None
        self.card_n = None
        self.bind = {}
        self.nu = 1

        self.lst = [self.ui.label, self.ui.label_5, self.ui.label_4, self.ui.label_6, self.ui.label_7, self.ui.label_8, self.ui.label_12,
               self.ui.label_11,
               self.ui.label_10, self.ui.label_9, self.ui.label_17, self.ui.label_16, self.ui.label_15, self.ui.label_14, self.ui.label_13,
               self.ui.label_23, self.ui.label_21, self.ui.label_22, self.ui.label_19, self.ui.label_20, self.ui.label_18, self.ui.label_24,
               self.ui.label_25, self.ui.label_26, self.ui.label_27, self.ui.label_31, self.ui.label_28, self.ui.label_32, self.ui.label_33, self.ui.label_34,self.ui.label_35,self.ui.label_36]

        self.lst_extra = []
        self.ui.label_35.raise_()
        z = 0
        self.z = 0
        while z <= 28:
            if z == 28:
                pixmap_P = QPixmap("{0}".format(card_stack[self.z]))
                self.lst[28].setPixmap(pixmap_P)
                break
            pixmap = QPixmap("{0}".format(pyramid_card[z]))
            self.lst[z].setPixmap(pixmap)
            z +=1
        self.k = None

        self.startpos_x_y = []
        self.startpos = []
        self.cnt = 0
        self.xpos = 0
        self.ypos = 0

        for i in self.lst:
            self.startpos_x_y.append([i.x(),i.y()])
            self.startpos.append(i.pos())

        for i in self.lst:
            i.mouseMoveEvent = self.mouseMoveEvent
            i.mouseReleaseEvent = self.mouseReleaseEvent
        self.ui.mousePressEvent = self.mousePressEvent


    def mousePressEvent(self, event):
        count = 0
        for i in self.startpos_x_y:
            if event.x() in range(i[0], i[0]+100) and event.y() in range(i[1], i[1]+120):
                self.card_m = self.lst[count]
                self.numeration = count
            count += 1

        if self.card_m == self.lst[29]:
            if self.z >= 23:
                self.z = 0

            self.z += 1
            pixmap_P = QPixmap("{0}".format(card_stack[self.z]))
            self.lst[28].setPixmap(pixmap_P)
            self.z -=1
            pixmap_P = QPixmap("{0}".format(card_stack[self.z]))
            self.lst[30].setPixmap(pixmap_P)
            self.z -= 1
            pixmap_P = QPixmap("{0}".format(card_stack[self.z]))
            self.lst[31].setPixmap(pixmap_P)
            self.z +=2

            if self.nu == 0:
                self.z += 2
                pixmap_P = QPixmap("{0}".format(card_stack[self.z]))
                self.lst[28].setPixmap(pixmap_P)
                self.z -= 1
                pixmap_P = QPixmap("{0}".format(card_stack[self.z]))
                self.lst[30].setPixmap(pixmap_P)
                self.z -= 2
                pixmap_P = QPixmap("{0}".format(card_stack[self.z]))
                self.lst[31].setPixmap(pixmap_P)
                self.z += 3
                self.nu = 1



        elif self.card_m == self.lst[28]:
            if int((card_stack[self.z])[:-2]) == 13:
                pixmap_P = QPixmap("{0}".format(card_stack[self.z]))
                self.lst[28].setPixmap(pixmap_P)

        elif self.card_m == self.lst[30]:
            print(int((card_stack[self.z - 1])[:-2]))

        elif self.card_m == self.lst[31]:
            pass

        else:
            for i in fin_pyramid:
                for j in i:
                    if j == pyramid_card[self.numeration]:
                        self.v_1 = fin_pyramid.index(i)
                        self.h_1 = i.index(j)
                        if int(((fin_pyramid[self.v_1 + 1])[self.h_1 + 1])[:-2]) == 0 and int(((fin_pyramid[self.v_1 + 1])[self.h_1])[:-2]) == 0:
                            if int(((fin_pyramid[self.v_1])[self.h_1])[:-2]) == 13:
                                (fin_pyramid[self.v_1])[self.h_1] = ("0  ")
                                self.card_m.setVisible(False)


    def mouseMoveEvent(self, event):
        if self.card_m == self.lst[29]:
            self.card_m.move(self.startpos[self.numeration])

        elif self.card_m == self.lst[28]:
            self.xpos = event.x()
            self.ypos = event.y()
            center_point = QPoint(self.xpos - 50, self.ypos - 60)
            self.card_m.move(self.card_m.mapToParent(center_point))
            self.card_m.raise_()

        elif self.card_m == self.lst[30]:
            self.xpos = event.x()
            self.ypos = event.y()
            center_point = QPoint(self.xpos - 50, self.ypos - 60)
            self.card_m.move(self.card_m.mapToParent(center_point))
            self.card_m.raise_()

        elif self.card_m == self.lst[31]:
            self.card_m.move(self.startpos[self.numeration])

        else:
            for i in fin_pyramid:
                for j in i:
                    if j == pyramid_card[self.numeration]:
                        v = fin_pyramid.index(i)
                        h = i.index(j)
                        if int(((fin_pyramid[v + 1])[h + 1])[:-2]) == 0 and int(((fin_pyramid[v + 1])[h])[:-2]) == 0:
                            self.xpos = event.x()
                            self.ypos = event.y()
                            center_point = QPoint(self.xpos-50, self.ypos-60)
                            self.card_m.move(self.card_m.mapToParent(center_point))
                            self.card_m.raise_()


    def mouseReleaseEvent(self, event):
        count = 0
        for i in self.startpos_x_y:
            if self.card_m.x() in range(i[0], i[0] + 100) and self.card_m.y() in range(i[1], i[1] + 120):
                self.card_n = self.lst[count]
                self.numeration_2 = count
            count += 1

        if self.card_m == self.lst[29]:
            pixmap_P = QPixmap("{0}".format(card_stack[self.z]))
            self.lst[28].setPixmap(pixmap_P)

        if self.card_m == self.lst[31]:
            pixmap_P = QPixmap("{0}".format(card_stack[self.z-2]))
            self.lst[31].setPixmap(pixmap_P)

        elif self.card_m == self.lst[28]:
            if int((card_stack[self.z])[:-2]) == 13:
                pixmap_P = QPixmap("{0}".format(card_stack[self.z+1]))
                self.lst[28].setPixmap(pixmap_P)
                self.z +=1
                if self.z >= 23:
                    self.z = 0
            elif int((card_stack[self.z])[:-2]) != 13 and self.numeration_2 < 29 :
                if self.numeration_2 < 28 and int((pyramid_card[self.numeration_2])[:-2]) + int((card_stack[self.z])[:-2]) == 13 :
                    for i in fin_pyramid:
                        for j in i:
                            if j == pyramid_card[self.numeration_2] :
                                self.v_1 = fin_pyramid.index(i)
                                self.h_1 = i.index(j)
                                if int(((fin_pyramid[self.v_1 + 1])[self.h_1 + 1])[:-2]) == 0 and int(((fin_pyramid[self.v_1 + 1])[self.h_1])[:-2]) == 0:
                                    (fin_pyramid[self.v_1])[self.h_1] = ("0  ")
                                    self.card_n.setVisible(False)
                                    self.z +=1
                                    pixmap_P = QPixmap("{0}".format(card_stack[self.z]))
                                    self.lst[28].setPixmap(pixmap_P)

        elif self.card_m == self.lst[30]:
            if int((card_stack[self.z-1])[:-2]) == 13:
                pixmap_P = QPixmap("{0}".format(card_stack[self.z]))
                self.lst[30].setPixmap(pixmap_P)
                self.z -=2
                pixmap_P = QPixmap("{0}".format(card_stack[self.z]))
                self.lst[31].setPixmap(pixmap_P)
                self.z += 3
                pixmap_P = QPixmap("{0}".format(card_stack[self.z]))
                self.lst[28].setPixmap(pixmap_P)
                if self.z >= 23:
                    self.z = 0
            elif int((card_stack[self.z-1])[:-2]) != 13 and self.numeration_2 < 29 :
                if self.numeration_2 < 28 and int((pyramid_card[self.numeration_2])[:-2]) + int((card_stack[self.z-1])[:-2]) == 13 :
                    for i in fin_pyramid:
                        for j in i:
                            if j == pyramid_card[self.numeration_2]:
                                self.v_1 = fin_pyramid.index(i)
                                self.h_1 = i.index(j)
                                if int(((fin_pyramid[self.v_1 + 1])[self.h_1 + 1])[:-2]) == 0 and int(((fin_pyramid[self.v_1 + 1])[self.h_1])[:-2]) == 0:
                                    (fin_pyramid[self.v_1])[self.h_1] = ("0  ")
                                    self.card_n.setVisible(False)
                                    self.z -=1
                                    pixmap_P = QPixmap("{0}".format(card_stack[self.z-1]))
                                    self.lst[30].setPixmap(pixmap_P)
                                    self.z -=1
                                    pixmap_P = QPixmap("{0}".format(card_stack[self.z-1]))
                                    self.lst[31].setPixmap(pixmap_P)
                                    self.nu = 0
        else:
            if self.card_n == self.lst[28]:
                self.card_m.move(self.startpos[self.numeration])
            elif self.numeration_2 < 29:
                if int((pyramid_card[self.numeration_2])[:-2]) + int((pyramid_card[self.numeration])[:-2]) == 13 :
                    for i in fin_pyramid:
                        for j in i:
                            if j == pyramid_card[self.numeration]:
                                self.v_1 = fin_pyramid.index(i)
                                self.h_1 = i.index(j)
                                if int(((fin_pyramid[self.v_1 + 1])[self.h_1 + 1])[:-2]) == 0 and int(
                                        ((fin_pyramid[self.v_1 + 1])[self.h_1])[:-2]) == 0:
                                    if int(((fin_pyramid[self.v_1])[self.h_1])[:-2]) == 13:
                                         (fin_pyramid[self.v_1])[self.h_1] = ("0  ")
                                         self.card_m.setVisible(False)
                            if j == pyramid_card[self.numeration_2]:
                                self.v_1 = fin_pyramid.index(i)
                                self.h_1 = i.index(j)
                                self.van = int(((fin_pyramid[self.v_1 + 1])[self.h_1 + 1])[:-2])
                                self.too = int(((fin_pyramid[self.v_1 + 1])[self.h_1])[:-2])
                                if int(((fin_pyramid[self.v_1 + 1])[self.h_1 + 1])[:-2]) == 0 and int(((fin_pyramid[self.v_1 + 1])[self.h_1])[:-2]) == 0:
                                    (fin_pyramid[self.v_1])[self.h_1] = ("0  ")
                                    self.card_n.setVisible(False)
                            elif j == pyramid_card[self.numeration]:
                                self.v_1 = fin_pyramid.index(i)
                                self.h_1 = i.index(j)
                                if self.van == 0 and self.too == 0:
                                    (fin_pyramid[self.v_1])[self.h_1] = ("0  ")
                                    self.card_m.setVisible(False)
        if self.card_m.isVisible != False:
            self.card_m.move(self.startpos[self.numeration])
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())
