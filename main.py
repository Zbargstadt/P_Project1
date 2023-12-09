from New_Lab9 import *

def main() -> None:
    '''
    Runs Program
    :return:
    '''
    application = QApplication([])
    window = Logic_Setup()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()