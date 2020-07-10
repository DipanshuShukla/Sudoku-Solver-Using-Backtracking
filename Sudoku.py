import pygame
import solver
import copy

pygame.init()

WIN_WIDTH = 700

SCALE = WIN_WIDTH // 9
WIN_HEIGHT = WIN_WIDTH + SCALE//2

WINDOW = pygame.display.set_mode((WIN_WIDTH, int(WIN_HEIGHT)))
pygame.display.set_caption("Sudoku")

STAT_FONT = pygame.font.SysFont("comicsans", SCALE)
LABEL_FONT = pygame.font.SysFont("comicsans", int(SCALE//2.8))

# Color Pallet
BLACK = [72, 72, 72]
GREY = [200, 200, 200]
TEXT = [160, 160, 160]
ITEXT = [153, 102, 51]
WHITE = [255, 255, 255]



class Board:
    def __init__(self):
        self.board = []
        self.initBoard = []

    def Pick_Board(self):
        self.initBoard = [[0, 4, 2, 6, 0, 0, 0, 0, 3],
                      [0, 0, 0, 0, 0, 0, 7, 0, 0],
                      [5, 3, 8, 0, 0, 1, 6, 0, 2],
                      [0, 0, 5, 0, 0, 9, 0, 7, 0],
                      [0, 0, 0, 8, 0, 6, 0, 0, 0],
                      [0, 2, 0, 7, 0, 0, 1, 0, 0],
                      [8, 0, 4, 1, 0, 0, 2, 3, 6],
                      [0, 0, 1, 0, 0, 0, 0, 0, 0],
                      [3, 0, 0, 0, 0, 2, 8, 9, 0]]

        self.board = copy.deepcopy(self.initBoard)

    def Get_Board(self):
        return self.board

    def Draw(self):
        WINDOW.fill(WHITE)
        for x in range(0, WIN_WIDTH, SCALE):
            pygame.draw.line(WINDOW, GREY, (x, 0), (x, WIN_WIDTH), 4)
            pygame.draw.line(WINDOW, GREY, (0, x), (WIN_WIDTH, x), 4)

        for x in range(0, WIN_WIDTH + 1, WIN_WIDTH // 3 - 1):
            pygame.draw.line(WINDOW, BLACK, (x, 0), (x, WIN_WIDTH), 8)
            pygame.draw.line(WINDOW, BLACK, (0, x), (WIN_WIDTH, x), 8)

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                text = STAT_FONT.render("{}".format(self.board[row][col] if self.board[row][col] > 0 else ""), 1, TEXT)
                Wgap = (SCALE - text.get_width()) // 2
                Hgap = (SCALE - text.get_height()) // 2
                WINDOW.blit(text, (col * SCALE + Wgap + 2, row * SCALE + Hgap+4))

        for row in range(len(self.initBoard)):
            for col in range(len(self.initBoard[row])):
                text = STAT_FONT.render("{}".format(self.initBoard[row][col] if self.initBoard[row][col] > 0 else ""), 1, ITEXT)
                Wgap = (SCALE - text.get_width()) // 2
                Hgap = (SCALE - text.get_height()) // 2
                WINDOW.blit(text, (col * SCALE + Wgap + 2, row * SCALE + Hgap+4))

        text = LABEL_FONT.render("{}".format("Press SPACE to solve automatically."), 1, BLACK)
        WINDOW.blit(text, (int(SCALE*2.7), int(WIN_HEIGHT-SCALE//2.7)))

        pygame.display.update()



def main():
    FPS = 30
    Clock = pygame.time.Clock()
    run = True

    board = Board()
    board.Pick_Board()

    while run:
        Clock.tick(FPS)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            solver.Solve(board)

        board.Draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == '__main__':
    main()