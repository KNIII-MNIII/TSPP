from Logic_class_structure import*

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication, QAction
import sys

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

from PyQt5.QtCore import QPoint
COM = Complected_Pyr().create_pyr()

'''
    This method realise a opportunity to take off the King card from the pyramid
    and from card stack
'''
def King_card_off(self):
    for i in fin_pyramid:
        for j in i:
            if j == pyramid_card[self.release_num]:
                self.v_1 = fin_pyramid.index(i)
                self.h_1 = i.index(j)
                if int(((fin_pyramid[self.v_1 + 1])[self.h_1 + 1])[:-2]) == 0 and int(
                        ((fin_pyramid[self.v_1 + 1])[self.h_1])[:-2]) == 0:
                    if int(((fin_pyramid[self.v_1])[self.h_1])[:-2]) == 13:
                        (fin_pyramid[self.v_1])[self.h_1] = ("0  ")
                        self.selectedcard_press.setVisible(False)
'''
    The main stack cards method, that compare cards in stack with cards in pyramid
'''
def Comparing_stack_pyr(self):
    if self.release_num < 28 and int((pyramid_card[self.release_num])[:-2]) + int((card_stack[self.z])[:-2]) == 13:
        for i in fin_pyramid:
            for j in i:
                if j == pyramid_card[self.release_num]:
                    self.v_1 = fin_pyramid.index(i)
                    self.h_1 = i.index(j)
                    if int(((fin_pyramid[self.v_1 + 1])[self.h_1 + 1])[:-2]) == 0 and int(((fin_pyramid[self.v_1 + 1])[self.h_1])[:-2]) == 0:
                        (fin_pyramid[self.v_1])[self.h_1] = ("0  ")
                        self.selectedcard_re.setVisible(False)
                        self.z += 1
                        pix_stack_card = QPixmap("{0}".format(card_stack[self.z]))
                        self.main_card_list[28].setPixmap(pix_stack_card)

'''
Method seems like last one but it`s compare cards in pyramid
'''
def Compearing_pyrCards(self):
    for i in fin_pyramid:
        for j in i:
            if j == pyramid_card[self.release_num]:
                self.v_1 = fin_pyramid.index(i)
                self.h_1 = i.index(j)
                self.van = int(((fin_pyramid[self.v_1 + 1])[self.h_1 + 1])[:-2])
                self.too = int(((fin_pyramid[self.v_1 + 1])[self.h_1])[:-2])
                if int(((fin_pyramid[self.v_1 + 1])[self.h_1 + 1])[:-2]) == 0 and int(((fin_pyramid[self.v_1 + 1])[self.h_1])[:-2]) == 0:
                    (fin_pyramid[self.v_1])[self.h_1] = ("0  ")
                    self.selectedcard_re.setVisible(False)
            elif j == pyramid_card[self.press_num]:
                self.v_1 = fin_pyramid.index(i)
                self.h_1 = i.index(j)
                if self.van == 0 and self.too == 0:
                    (fin_pyramid[self.v_1])[self.h_1] = ("0  ")
                    self.selectedcard_press.setVisible(False)



class UI(QWidget):

    def __init__(self):
        super(UI, self).__init__()
        self.ui = uic.loadUi(r'C:\Users\владислав\Pictures\колода\Dirty maket.ui')
        self.ui.show()
        self.press_num = 0
        self.release_num = 0
        self.selectedcard_press = None
        self.selectedcard_re = None


        self.main_card_list = [self.ui.label, self.ui.label_2, self.ui.label_3, self.ui.label_4, self.ui.label_5,self.ui.label_6,
                    self.ui.label_7, self.ui.label_8, self.ui.label_9, self.ui.label_10, self.ui.label_11, self.ui.label_12,
                    self.ui.label_13, self.ui.label_14, self.ui.label_15, self.ui.label_16, self.ui.label_17, self.ui.label_18,
                    self.ui.label_19, self.ui.label_20, self.ui.label_21, self.ui.label_22, self.ui.label_23, self.ui.label_24,
                    self.ui.label_25, self.ui.label_26, self.ui.label_27, self.ui.label_28, self.ui.label_29, self.ui.label_30,]



        z = 0
        self.z = 0
        while z <= 28:
            if z == 28:

                self.main_card_list[28].setPixmap(QPixmap("{0}".format(card_stack[self.z])))
                break
            pyr_pixmap = QPixmap("{0}".format(pyramid_card[z]))
            self.main_card_list[z].setPixmap(pyr_pixmap)
            z +=1
        self.ui.label_29.raise_()
        self.mouse_x_y = []
        self.card_x_y = []

        self.xpos = 0
        self.ypos = 0

        for i in self.main_card_list:
            self.mouse_x_y.append([i.x(),i.y()])
            self.card_x_y.append(i.pos())

        for i in self.main_card_list:
            i.mouseMoveEvent = self.mouseMoveEvent
            i.mouseReleaseEvent = self.mouseReleaseEvent
        self.ui.mousePressEvent = self.mousePressEvent


    def mousePressEvent(self, event):
        count = 0
        for i in self.mouse_x_y:
            if event.x() in range(i[0], i[0]+100) and event.y() in range(i[1], i[1]+100):
                self.selectedcard_press = self.main_card_list[count]
                self.press_num = count
            count += 1

        if self.selectedcard_press == self.main_card_list[29]:
            if self.z >= 22:
                self.z = 0
            self.z += 1
            pix_stack_card = QPixmap("{0}".format(card_stack[self.z]))
            self.main_card_list[28].setPixmap(pix_stack_card)
            pix_stack_card = QPixmap("{0}".format(card_stack[self.z +1 ]))
            self.ui.label_31.setPixmap(pix_stack_card)
            if self.z >= 22:
                self.z = 0

        elif self.selectedcard_press == self.main_card_list[28]:

            if int((card_stack[self.z])[:-2]) == 13:
                pix_stack_card = QPixmap("{0}".format(card_stack[self.z]))
                self.main_card_list[28].setPixmap(pix_stack_card)

        else:
            for i in fin_pyramid:
                for j in i:
                    if j == pyramid_card[self.release_num]:
                        self.v_1 = fin_pyramid.index(i)
                        self.h_1 = i.index(j)
                        if int(((fin_pyramid[self.v_1 + 1])[self.h_1 + 1])[:-2]) == 0 and int(
                                ((fin_pyramid[self.v_1 + 1])[self.h_1])[:-2]) == 0:
                            if int(((fin_pyramid[self.v_1])[self.h_1])[:-2]) == 13:
                                (fin_pyramid[self.v_1])[self.h_1] = ("0  ")
                                self.selectedcard_press.setVisible(False)





    def mouseMoveEvent(self, event):
        if self.selectedcard_press == self.main_card_list[29]:
            self.selectedcard_press.move(self.card_x_y[self.press_num])

        elif self.selectedcard_press == self.main_card_list[28]:
            self.xpos = event.x()
            self.ypos = event.y()
            center_point = QPoint(self.xpos - 30, self.ypos - 30)
            self.selectedcard_press.move(self.selectedcard_press.mapToParent(center_point))
            self.selectedcard_press.raise_()

        else:
            for i in fin_pyramid:
                for j in i:
                    if j == pyramid_card[self.press_num]:
                        v = fin_pyramid.index(i)
                        h = i.index(j)
                        if int(((fin_pyramid[v + 1])[h + 1])[:-2]) == 0 and int(((fin_pyramid[v + 1])[h])[:-2]) == 0:
                            self.xpos = event.x()
                            self.ypos = event.y()
                            center_point = QPoint(self.xpos-30, self.ypos-30)
                            self.selectedcard_press.move(self.selectedcard_press.mapToParent(center_point))
                            self.selectedcard_press.raise_()

    def mouseReleaseEvent(self, event):
        count = 0
        for i in self.mouse_x_y:
            if self.selectedcard_press.x() in range(i[0], i[0] + 60) and self.selectedcard_press.y() in range(i[1], i[1] + 78):
                self.selectedcard_re = self.main_card_list[count]
                self.release_num = count
            count += 1

        if self.selectedcard_press == self.main_card_list[29]:
            pix_stack_card = QPixmap("{0}".format(card_stack[self.z]))
            self.main_card_list[28].setPixmap(pix_stack_card)

        elif self.selectedcard_press == self.main_card_list[28]:
            if int((card_stack[self.z])[:-2]) == 13:
                self.z +=1
                pix_stack_card = QPixmap("{0}".format(card_stack[self.z]))
                self.ui.label_29.setPixmap(pix_stack_card)
                pix_stack_card = QPixmap("{0}".format(card_stack[self.z + 1]))
                self.ui.label_31.setPixmap(pix_stack_card)
                if self.z >= 22:
                    self.z = 0
            elif int((card_stack[self.z])[:-2]) != 13 and self.release_num < 29:
                Comparing_stack_pyr(self)
                pix_stack_card = QPixmap("{0}".format(card_stack[self.z + 1]))
                self.ui.label_31.setPixmap(pix_stack_card)


        else:
                if int((pyramid_card[self.release_num])[:-2]) + int((pyramid_card[self.press_num])[:-2]) == 13:
                    Compearing_pyrCards(self)

        if self.selectedcard_press.isVisible != False:
            self.selectedcard_press.move(self.card_x_y[self.press_num])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())

