# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import myLibrary as myLib


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    hypotenuse = myLib.getHypotenuse(4, 3)
    print("The hypotenuse from a triangle with sides 3 and 4 is: ", hypotenuse)
    rectangleArea = myLib.getRectangleArea(4, 3)
    print("The area from a rectangle with sides 3 and 4 is: ", rectangleArea)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
