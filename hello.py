#!/usr/bin/env python
#-*-coding:utf-8 -*-

'a test module'
__author__ = 'kevin'
import sys
def test():
    args=sys.argv
    if len(args) == 1:
        print 'hello, world.'
    elif len(args)==2:
        print 'hello, %s!' % args[1]
    else:
	print 'too many arguments!'

class Student(object):
    def __init__(self, name , score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print '%s:%s' % (self.__name, self.__score)
    def set_name(self, name):
        self.__name = name
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        self.__score = score

if __name__ == '__main__':
    test()
    student=Student('li', 89)
    student.print_score()
    student.set_name('zhangshan')
    student.score=90
    student.print_score()
