from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Меню")
main_window.resize(600, 200)

main_layout = QVBoxLayout()
layout1 = QVBoxLayout()
welcom_label = QLabel("Dino-Pong")
choose_label = QLabel("Виберіть рівень складності:")

button_easy = QPushButton("Легкий")
button_middle = QPushButton("Середный")
button_hard = QPushButton("Складний")

layout1.addWidget(welcom_label, alignment= Qt.AlignCenter)
layout1.addWidget(choose_label, alignment= Qt.AlignCenter)
layout1.addWidget(button_easy)
layout1.addWidget(button_middle)
layout1.addWidget(button_hard)

main_layout.addLayout(layout1)

def choose_button_easy():
    choose = 1
    # main_window.close()
    print(choose)
    return choose

def choose_button_middle():
    choose = 2
    # main_window.close()
    print(choose)
    return choose
def choose_button_hard():
    choose = 3
    # main_window.close()
    print(choose)
    return choose



first_choose = button_easy.clicked.connect(choose_button_easy)
first_choose = button_middle.clicked.connect(choose_button_middle)
first_choose = button_hard.clicked.connect(choose_button_hard)



if first_choose == 1:
    print("done")
    ball_speedx = 4
    ball_speedy = 4

if first_choose == 2:
    print("done2")
    ball_speedx = 5
    ball_speedy = 5

if first_choose == 3:
    print("done3")
    ball_speedx = 6
    ball_speedy = 6
   

main_window.setLayout(main_layout)
main_window.show()
app.exec_()