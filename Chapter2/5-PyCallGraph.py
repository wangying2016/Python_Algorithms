# from pycallgraph import PyCallGraph
# from pycallgraph.output import GraphvizOutput
#
#
# class Banana:
#
#     def eat(self):
#         pass
#
#
# class Person:
#
#     def __init__(self):
#         self.no_bananas()
#
#     def no_bananas(self):
#         self.bananas = []
#
#
#     def add_bananas(self, banana):
#         self.bananas.append(banana)
#
#     def eat_bananas(self):
#         [banana.eat() for banana in self.bananas]
#         self.no_bananas()
#
#
# def main():
#     graphviz = GraphvizOutput()
#     graphviz.output_file = 'basic.png'
#
#     with PyCallGraph(output=graphviz):
#         person = Person()
#         for a in range(10):
#             person.add_bananas(Banana())
#         person.eat_bananas()
#
#
# if __name__ == '__main__':
#     main()
#

#!/usr/bin/env python
'''
This example demonstrates a simple use of pycallgraph.
'''
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


class Banana:

    def eat(self):
        pass


class Person:

    def __init__(self):
        self.no_bananas()

    def no_bananas(self):
        self.bananas = []

    def add_banana(self, banana):
        self.bananas.append(banana)

    def eat_bananas(self):
        [banana.eat() for banana in self.bananas]
        self.no_bananas()


def main():
    graphviz = GraphvizOutput()
    graphviz.output_file = 'basic.png'

    with PyCallGraph(output=graphviz):
        person = Person()
        for a in range(10):
            person.add_banana(Banana())
        person.eat_bananas()


if __name__ == '__main__':
    main()

a, b, c, d, e, f, g, h = range(8)
N = [
    {b, c, d, e, f},  # a
    {c, e},           # b
    {d},              # c
    {e},              # d
    {f},              # e
    {c, g, h},        # f
    {f, h},           # g
    {f, g}            # h
]
