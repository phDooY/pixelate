import random


class Pixelate():
    def __init__(self, test_flag):
        self.test_flag = test_flag
        self.board = {}
        self.board_size = 0
        self.board_colors = 0
        self.win = False
        self.moves = 0

    def start(self):
        print 'Welcome to Pixelate'
        # Setup board
        while self.board_size not in range(5, 20):
            size_choice = raw_input('Please choose board size between 5 and 20:\n')
            try:
                self.board_size = int(size_choice)
            except ValueError:
                print 'Should be an integer'

        while self.board_colors not in range(3, 10):
            colors_choice = raw_input('Please choose number of colors between 3 and 10:\n')
            try:
                self.board_colors = int(colors_choice)
            except ValueError:
                print 'Should be an integer'

        self.generate_board()

        # Play
        while not self.win:
            self.visualize_board()
            self.make_step()
            self.moves += 1

        print 'Congratulations, you won in {} steps'.format(str(self.moves))

    def generate_board(self):
        for i in range(0, self.board_size**2):
            self.board.update({i: random.randrange(0, self.board_colors + 1)})

    def visualize_board(self):
        offset = 0
        limit = iteration = self.board_size
        print ' ' + ('_ ' * self.board_size)
        while iteration:
            row = []
            for i in range(offset, offset + limit):
                row.append(str(self.board[i]))
            print '|' + '|'.join(row) + '|'
            iteration -= 1
            offset += limit
        print ' ' + ('_ ' * self.board_size)

    def make_step(self):
        choice = None
        while choice not in range(0, self.board_colors):
            try:
                choice = int(raw_input('Make color choice between 0'
                                       ' and {}:\n'.format(str(self.board_colors - 1))))
            except ValueError:
                print 'Should be an integer'

        self.color_tiles(choice)

    def color_tiles(self, color):
        # TODO color tiles adjustent to origin into color of choice
        pass

    def link_to_origin(self):
        # TODO data structure for tiles linked to origin
        pass

    def check_win_condition(self):
        if len(set(self.board.values())) == 1:
            self.win = True

if __name__ == '__main__':
    game = Pixelate(False)
    game.start()
