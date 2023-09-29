import sys
sys.path.append("Week_39")
from Week_39 import task1, task2, task3

def selectTask():
    return int(input("Select Task by writing the task number: "))

def doTask(input):
    if (input == 1):
        task1.harderSolution()
    elif (input == 2):
        task2.simpleSolution()
    elif (input == 3):
        task3.simpleSolution()


