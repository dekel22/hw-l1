from calculator import Calculator
from parsemathFile import ParsemathFile



calculator = Calculator()
parser = ParsemathFile()

parser.parse('C:\\Users\\dekel\\OneDrive\\Desktop\\aaa.txt')


while (not(parser.q.empty())):
    item = parser.q.get()
    print(calculator.calc(calculator.putNumbers(item)))
    parser.q.task_done()

