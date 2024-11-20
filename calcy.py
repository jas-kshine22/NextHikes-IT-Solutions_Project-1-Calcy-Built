import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
import math

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title and dimensions
        self.setWindowTitle('Advanced Calculator')
        self.setGeometry(100, 100, 300, 400)

        # Initialize memory
        self.memory = 0

        # Create the UI components
        self.initUI()

    def initUI(self):
        # Create a vertical layout
        layout = QVBoxLayout()

        # Create the equation display area (screen)
        self.screen = QLineEdit()
        self.screen.setReadOnly(True)
        self.screen.setAlignment(Qt.AlignRight)
        layout.addWidget(self.screen)

        # Create grid layout for buttons
        grid = QGridLayout()

        # Define buttons in a 5x4 grid
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3),
            ('√', 4, 0), ('^', 4, 1), ('%', 4, 2), ('C', 4, 3),
            ('CE', 5, 0), ('M+', 5, 1), ('MR', 5, 2), ('MC', 5, 3)
        ]

        # Add buttons to the grid
        for btn_text, x, y, *span in buttons:
            button = QPushButton(btn_text)
            button.clicked.connect(self.on_button_click)
            grid.addWidget(button, x, y, *span)

        # Add grid layout to the main layout
        layout.addLayout(grid)

        # Set the layout for the window
        self.setLayout(layout)

    def on_button_click(self):
        # Get the sender of the signal (button clicked)
        button = self.sender()
        button_text = button.text()

        # Handle clear operations
        if button_text == 'C':
            self.screen.clear()
        elif button_text == 'CE':
            current_text = self.screen.text()
            self.screen.setText(current_text[:-1])  # Clear last entry

        # Handle memory operations
        elif button_text == 'M+':
            self.memory += float(self.screen.text())
            self.screen.clear()
        elif button_text == 'MR':
            self.screen.setText(str(self.memory))
        elif button_text == 'MC':
            self.memory = 0
            self.screen.clear()

        # Handle square root
        elif button_text == '√':
            try:
                result = math.sqrt(float(self.screen.text()))
                self.screen.setText(str(result))
            except Exception as e:
                self.screen.setText('Error')

        # Handle exponentiation
        elif button_text == '^':
            current_text = self.screen.text()
            self.screen.setText(current_text + '**')  # Use Python exponentiation operator

        # Handle percentage
        elif button_text == '%':
            try:
                result = float(self.screen.text()) / 100
                self.screen.setText(str(result))
            except Exception as e:
                self.screen.setText('Error')

        # If '=' is pressed, evaluate the equation
        elif button_text == '=':
            try:
                result = str(eval(self.screen.text()))
                self.screen.setText(result)
            except Exception as e:
                self.screen.setText('Error')

        # Otherwise, add the button text to the screen
        else:
            current_text = self.screen.text()
            new_text = current_text + button_text
            self.screen.setText(new_text)

# Main function to run the application
def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
