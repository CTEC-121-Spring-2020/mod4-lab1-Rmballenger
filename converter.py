# convert.py
# A Program to convert from F to C

from graphics import *


def main():
    # Create a window object
    win = GraphWin("Celsius Converter", 400, 300)

    # Create text objects
    celsiusTempString = "Celsius Temperature:   "
    fahrenheitTempString = "Fahrenheit Temperature:"

    # Create text boxes
    Text(Point(150, 50), celsiusTempString).draw(win)
    Text(Point(150, 250), fahrenheitTempString).draw(win)

    # Create center box
    Rectangle(Point(125, 100), Point(275, 200)).draw(win)

    # Create button text
    buttonText = Text(Point(200, 150), "Convert It")
    buttonText.draw(win)

    # Create input and output fields
    inputCelsiusField = Entry(Point(300, 50), 5)
    inputCelsiusField.setText("0.0")
    inputCelsiusField.draw(win)

    outputFahrenheitField = Text(Point(300, 250), "")
    outputFahrenheitField.draw(win)

    win.getMouse()

    celsiusTemperature = float(inputCelsiusField.getText())
    fahrenheit = 9.0/5.0 * celsiusTemperature + 32

    # Display results
    outputFahrenheitField.setText(round(fahrenheit, 2))

    buttonText.setText("Quit")

    win.getMouse()


main()
