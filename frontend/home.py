from PySide6.QtWidgets import QLabel, QVBoxLayout ,QWidget


def create_home_page():
    page = QWidget()
    page.setStyleSheet("""
    QWidget{
        border: 1px solid #555555;
        border-radius: 10px;
    }
""")

    layout = QVBoxLayout()

    label = QLabel("Home")
    layout.addWidget(label)
    layout.addStretch()

    page.setLayout(layout)

    return page
