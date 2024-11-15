import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap

class VotingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Voting App")
        self.resize(400, 500)

        self.votes = {"Option 1": 0, "Option 2": 0, "Option 3": 0}
        self.voters = set()  # Set to track voters who have already voted

        layout = QVBoxLayout()

        # Voter ID input
        self.voter_id_input = QLineEdit(self)
        self.voter_id_input.setPlaceholderText("Enter your voter ID")
        
        # Create QLabel widgets to display the candidate pictures
        self.candidate1_pic = QLabel(self)
        self.candidate2_pic = QLabel(self)
        self.candidate3_pic = QLabel(self)

        # Load the images as QPixmaps and set them to the QLabel widgets
        self.candidate1_pic.setPixmap(QPixmap("selfie.png").scaled(150, 150))
        self.candidate2_pic.setPixmap(QPixmap("gray.png").scaled(150, 150))
        self.candidate3_pic.setPixmap(QPixmap("mirror.png").scaled(150, 150))

        self.option1_button = QPushButton("Vote for Option 1")
        self.option2_button = QPushButton("Vote for Option 2")
        self.option3_button = QPushButton("Vote for Option 3")
        self.result_label = QLabel("Votes: Option 1 = 0, Option 2 = 0, Option 3 = 0")

        self.option1_button.clicked.connect(lambda: self.vote("Option 1"))
        self.option2_button.clicked.connect(lambda: self.vote("Option 2"))
        self.option3_button.clicked.connect(lambda: self.vote("Option 3"))

        # Add widgets to the layout
        layout.addWidget(self.voter_id_input)
        layout.addWidget(self.candidate1_pic)
        layout.addWidget(self.option1_button)
        layout.addWidget(self.candidate2_pic)
        layout.addWidget(self.option2_button)
        layout.addWidget(self.candidate3_pic)
        layout.addWidget(self.option3_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def vote(self, option):
        voter_id = self.voter_id_input.text()
        if voter_id in self.voters:
            QMessageBox.warning(self, "Error", "You have already voted!")
        else:
            self.voters.add(voter_id)
            self.votes[option] += 1
            self.update_results()
            QMessageBox.information(self, "Thank You", "Your vote has been recorded.")
            self.voter_id_input.clear()

    def update_results(self):
        results = f"Votes: Option 1 = {self.votes['Option 1']}, Option 2 = {self.votes['Option 2']}, Option 3 = {self.votes['Option 3']}"
        self.result_label.setText(results)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VotingApp()
    window.show()
    sys.exit(app.exec_())
