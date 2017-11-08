import random
import os
import time

class Bulb(object):
    '''
        The lamp class
    '''
    def __init__(self):
        self.__state = False

    def is_on(self):
        return self.__state

    def switch(self):
        self.__state = not self.__state

    def __str__(self):
        char = '*' if self.is_on() else ' '
        return char

class Board(object):
    '''
        The class encapsulates matrix of lamp.
    '''
    def __init__(self, mat=5):
        self.lista = []
        self.__mat = mat
        for i in range(self.__mat):
            row = []
            for j in range(self.__mat):
                row.append(Bulb())
            self.lista.append(row)

    def print_board(self):
        for i in range(self.__mat):
            for j in range(self.__mat):
                print('%s ' % (self.lista[i][j], ), end='')
            print("")

    def pisca(self):
        '''
            Pisca de forma aleatoria
        '''
        while True:
            os.system('clear')
            self.print_board()
            row = random.randrange(self.__mat)
            col = random.randrange(self.__mat)
            self.lista[row][col].switch()
            time.sleep(0.6)

    def pisca_gradual(self):
        '''
            Switch the state of bulb gradually
        '''
        while  True:
            for row in range(self.__mat):
                for col in range(self.__mat):
                    os.system('clear')
                    self.lista[row][col].switch()
                    self.print_board()
                    time.sleep(0.6)
            
# Instance
b = Board()
b.pisca()
