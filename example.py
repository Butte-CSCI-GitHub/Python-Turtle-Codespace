import sys
from turtle import Turtle

def main():

    pen: Turtle = Turtle()

    for _ in range(4):
        pen.forward(100)
        pen.right(90)
    
    input()

if __name__ == '__main__':
    sys.exit(main())
