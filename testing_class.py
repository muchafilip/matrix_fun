from matrix_class_final import Matrix
import re

assert hasattr(Matrix, 'multiply'), "something went wrong"


def ask_user(message):
    print(message)
    matrix = []
    while True:
        row = input()
        if row != '' and re.match("^[0-9 \r\n]+$", row):
            try:
                matrix.append(list(map(int, row.split(' '))))
            except ValueError:
                print('invalid character, try again')
                row = input()
        else:
            return matrix


def main():
    m1 = Matrix(ask_user('enter rows for m1 and press enter'))
    m2 = Matrix(ask_user('enter rows for m2 and press enter'))
    print('Result:')
    [print(i) for i in m1.multiply(m2)]


if __name__ == "__main__":
    main()
