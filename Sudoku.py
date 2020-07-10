import pygame
import solver

pygame.init()

WIN_WIDTH = 600

SCALE = WIN_WIDTH // 9
WIN_HEIGHT = WIN_WIDTH + SCALE//2.5

WINDOW = pygame.display.set_mode((WIN_WIDTH, int(WIN_HEIGHT)))
pygame.display.set_caption("Sudoku")

STAT_FONT = pygame.font.SysFont("comicsans", SCALE)

# Color Pallet
BLACK = [72, 72, 72]
GREY = [200, 200, 200]
TEXT = [160, 160, 160]
WHITE = [255, 255, 255]



class Board:
    def __init__(self):
        self.board = []

    def Pick_Board(self):
        self.board = [[0, 4, 2, 6, 0, 0, 0, 0, 3],
                      [0, 0, 0, 0, 0, 0, 7, 0, 0],
                      [5, 3, 8, 0, 0, 1, 6, 0, 2],
                      [0, 0, 5, 0, 0, 9, 0, 7, 0],
                      [0, 0, 0, 8, 0, 6, 0, 0, 0],
                      [0, 2, 0, 7, 0, 0, 1, 0, 0],
                      [8, 0, 4, 1, 0, 0, 2, 3, 6],
                      [0, 0, 1, 0, 0, 0, 0, 0, 0],
                      [3, 0, 0, 0, 0, 2, 8, 9, 0]]

        return self.board

    def Draw(self):
        WINDOW.fill(WHITE)
        for x in range(0, WIN_WIDTH, SCALE):
            pygame.draw.line(WINDOW, GREY, (x, 0), (x, WIN_WIDTH), 4)
            pygame.draw.line(WINDOW, GREY, (0, x), (WIN_WIDTH, x), 4)

        for x in range(0, WIN_WIDTH + 1, WIN_WIDTH // 3 - 1):
            pygame.draw.line(WINDOW, BLACK, (x, 0), (x, WIN_WIDTH), 8)
            pygame.draw.line(WINDOW, BLACK, (0, x), (WIN_WIDTH, x), 8)

        for row in range(len(self.Pick_Board())):
            for col in range(len(self.board[row])):
                text = STAT_FONT.render("{}".format(self.board[row][col] if self.board[row][col] > 0 else ""), 1, TEXT)
                Wgap = (SCALE - text.get_width()) // 2
                Hgap = (SCALE - text.get_height()) // 2
                WINDOW.blit(text, (col * SCALE + Wgap + 2, row * SCALE + Hgap+4))

        pygame.display.update()



def main():
    FPS = 10
    Clock = pygame.time.Clock()
    run = True

    board = Board()

    while run:
        Clock.tick(FPS)
        board.Draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == '__main__':
    main()
