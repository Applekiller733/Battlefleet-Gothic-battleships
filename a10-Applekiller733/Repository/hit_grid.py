

class Hit_Grid():
    def __init__(self):

        self.EMPTY = '.'
        self.HITEMPTY = '0'
        self.HITSHIP = '*'
        self.ATTEMPT = '!'

        self.board = []
        self.hits = []
        self.successful_hits = []
        self.empty_hits = []
        self.board_size = 10
        self.initialize_board()

    @property
    def hit_board(self):
        return self.board

    @property
    def hits_list(self):
        return self.hits

    @property
    def successful_hits_list(self):
        return self.successful_hits
    def add_hit(self, row, col):
        """
        Draws hit to hitboard and adds it to hit list
        :param row: row
        :param col: col
        """
        if self.isempty(row, col):
            self.board[row][col] = self.ATTEMPT
            self.hits.append([row, col])

    def draw_hit_on_board(self, row, col, type):
        """
        Draws final hit on board based on type param
        :param row: row
        :param col: col
        :param type: 1 if hit successful, anything else otherwise
        """
        if type == 1:
            self.board[row][col] = self.HITSHIP
        else:
            self.board[row][col] = self.HITEMPTY

    def initialize_board(self):
        """
        Initializes board with empty character
        :return:
        """
        self.board = [[self.EMPTY] * self.board_size for _ in range(self.board_size)]

    def debug_print_board(self):
        """
        Debug print
        :return:
        """
        for row in self.board:
            print(' '.join(row))

    def isempty(self, row, col):
        """
        Checks if cell empty
        :param row: row
        :param col: col
        :return:
        """
        try:
            return min(row, col) >= 0 and self.board[row][col] == self.EMPTY
        except IndexError:
            return 0