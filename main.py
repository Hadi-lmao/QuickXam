
import sys
import json
import sqlite3

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QStackedWidget
)

from PySide6.QtCore import Qt

#=====================
#Functions
#=====================

    



#=====================
#APP
#=====================
app = QApplication(sys.argv)

#=====================
#Widgets
#=====================
sidebar = QWidget()
sidebar.setStyleSheet("""
    QWidget{
        border: 1px solid #403A32;
        border-radius: 10px;
    }
""")

home_btn = QPushButton("Home")
home_btn.setStyleSheet("""
    QPushButton{
        font-size: 20px;
        border: 0px solid #555555;
        color: #B8B0A3;
        padding: 6px;
    }
    QPushButton:hover{
        border: 1px solid #555555;
    }
""")

practice_btn = QPushButton("Practice")
practice_btn.setStyleSheet("""
    QPushButton{
        font-size: 20px;
        border: 0px solid #555555;
        color: #B8B0A3;
        padding: 6px;
    }QPushButton:hover{
        border: 1px solid #555555;
    }
""")

questions_btn = QPushButton("Questions")
questions_btn.setStyleSheet("""
    QPushButton{
        font-size: 20px;
        border: 0px solid #555555;
        color: #B8B0A3;
        padding: 6px;
    }
    QPushButton:hover{
        border: 1px solid #555555;
    }
""")

test_history_btn = QPushButton("Test History")
test_history_btn.setStyleSheet("""
    QPushButton{
        font-size: 20px;
        border: 0px solid #555555;
        color: #B8B0A3;
        padding: 6px;
    }
    QPushButton:hover{
        border: 1px solid #555555;
    }
""")


home = QWidget()
home.setStyleSheet("""
    QWidget{
        border: 1px solid #403A32;
        border-radius: 10px;
    }
""")

practice = QWidget()
practice.setStyleSheet("""
    QWidget{
        border: 1px solid #555555;
        border-radius: 10px;
    }
""")



sidebar_stack = QStackedWidget()

sidebar_label = QLabel("QuickXam")
sidebar_label.setAlignment(Qt.AlignCenter)
sidebar_label.setStyleSheet("""
    QLabel{
        font-size: 32px;
        font-weight: bold;
        border: 0px;
        color: #F5F1E8;
    }
""")


#=====================
#Connections
#=====================

home_btn.clicked.connect(
    lambda: sidebar_stack.setCurrentWidget(home)
)
practice_btn.clicked.connect(
    lambda: sidebar_stack.setCurrentWidget(practice)
)




#=====================
#Layout
#=====================
window = QWidget()
window.setStyleSheet("""
    QWidget{
        color: white;
        background: qlineargradient(
            x1: 0, y1: 0,
            x2: 1, y2: 1,
            stop: 0 #202020,
            stop: 1 #3a3a3a
        );
    }
""")

window.setWindowTitle("QuickXam")
window.resize(1000, 700)

layout = QHBoxLayout()
window.setLayout(layout)



#=====================
#Home Area
#=====================
home_layout = QVBoxLayout()
home.setLayout(home_layout)

#=====================
#Sidebar
#=====================
sidebar.setFixedWidth(200)
sidebar_layout = QVBoxLayout()
sidebar.setLayout(sidebar_layout)

sidebar_layout.addWidget(sidebar_label)
sidebar_layout.addWidget(home_btn)
sidebar_layout.addWidget(practice_btn)
sidebar_layout.addWidget(questions_btn)
sidebar_layout.addWidget(test_history_btn)
sidebar_layout.addStretch()

layout.addWidget(sidebar)
layout.addWidget(sidebar_stack)

sidebar_stack.addWidget(home)
sidebar_stack.addWidget(practice)


window.show()

sys.exit(app.exec())

