import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class VotingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Voting App")
        self.resize(300, 200)

        self.votes = {"Option 1": 0, "Option 2": 0, "Option 3": 0}

        layout = QVBoxLayout()

        self.option1_button = QPushButton("Vote for Option 1")
        self.option2_button = QPushButton("Vote for Option 2")
        self.option3_button = QPushButton("Vote for Option 3")
        self.result_label = QLabel("Votes: Option 1 = 0, Option 2 = 0, Option 3 = 0")

        self.option1_button.clicked.connect(lambda: self.vote("Option 1"))
        self.option2_button.clicked.connect(lambda: self.vote("Option 2"))
        self.option3_button.clicked.connect(lambda: self.vote("Option 3"))

        layout.addWidget(self.option1_button)
        layout.addWidget(self.option2_button)
        layout.addWidget(self.option3_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def vote(self, option):
        self.votes[option] += 1
        self.update_results()

    def update_results(self):
        results = f"Votes: Option 1 = {self.votes['Option 1']}, Option 2 = {self.votes['Option 2']}, Option 3 = {self.votes['Option 3']}"
        self.result_label.setText(results)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VotingApp()
    window.show()
    sys.exit(app.exec_())
