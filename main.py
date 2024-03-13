import pygame
import numpy as np
import time

# Defining colors
BLACK = (0, 0, 0)
PURPLE = (160, 32, 240)

# Setting the dimensions of the grid cell
CELL_SIZE = 10

# Setting the number of rows and columns in the grid
ROWS = 50
COLS = 50

# Initialize the pygame library
pygame.init()

# Set the dimensions of the screen
SCREEN_SIZE = (COLS * CELL_SIZE, ROWS * CELL_SIZE)
screen = pygame.display.set_mode(SCREEN_SIZE)

# Set the title of the window
pygame.display.set_caption("Conway's Game of Life")

# Create the initial grid
grid = np.zeros((ROWS, COLS))


# Function to initialize the grid with random alive cells
def initialize_grid():
    for i in range(ROWS):
        for j in range(COLS):
            grid[i][j] = np.random.choice([0, 1])


# Function to draw the grid on the screen
def draw_grid():
    screen.fill(BLACK)
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, PURPLE, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()


# Function to count the number of live neighbors for a given cell
def count_neighbors(row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                if 0 <= row + i < ROWS and 0 <= col + j < COLS:
                    count += grid[row + i][col + j]
    return count


# Function to update the grid
def update_grid():
    new_grid = np.copy(grid)
    for i in range(ROWS):
        for j in range(COLS):
            neighbors = count_neighbors(i, j)
            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    grid[:] = new_grid[:]


# Main function
def main():
    initialize_grid()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_grid()
        update_grid()
        time.sleep(0.1)

    pygame.quit()


if __name__ == "__main__":
    main()
