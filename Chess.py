import pygame
pygame.init()

# Define the window dimensions
screen_width = 400
screen_height = 400

# Create the Pygame window
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Chess Game")

def draw_chessboard():
    dark_color = (139, 69, 19)
    light_color = (255, 228, 181)
    square_size = screen_width // 8

    for row in range(8):
        for col in range(8):
            color = dark_color if (row + col) % 2 == 0 else light_color
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

# Load chess piece images
b_pawn_img = pygame.image.load('pieces\\b_pawn.png')
b_rook_img = pygame.image.load('pieces\\b_rook.png')
b_knight_img = pygame.image.load('pieces\\b_knight.png')
b_queen_img = pygame.image.load('pieces\\b_queen.png')
b_bishop_img = pygame.image.load('pieces\\b_bishop.png')
b_king_img = pygame.image.load('pieces\\b_king.png')

w_pawn_img = pygame.image.load('pieces\w_pawn.png')
w_rook_img = pygame.image.load('pieces\w_rook.png')
w_knight_img = pygame.image.load('pieces\w_knight.png')
w_queen_img = pygame.image.load('pieces\w_queen.png')
w_bishop_img = pygame.image.load('pieces\w_bishop.png')
w_king_img = pygame.image.load('pieces\w_king.png')

def draw_piece(img, x, y):
    screen.blit(img, (x, y))

def board_setup():
    for i in range(8):
        draw_piece(w_pawn_img, i * 50, 50)
        draw_piece(b_pawn_img, i * 50, 300)

    draw_piece(w_rook_img, 0, 0)
    draw_piece(w_knight_img, 50, 0)
    draw_piece(w_bishop_img, 100, 0)
    draw_piece(w_queen_img, 150, 0)
    draw_piece(w_king_img, 200, 0)
    draw_piece(w_bishop_img, 250, 0)
    draw_piece(w_knight_img, 300, 0)    
    draw_piece(w_rook_img, 350, 0)

    draw_piece(b_rook_img, 0, 350)
    draw_piece(b_knight_img, 50, 350)
    draw_piece(b_bishop_img, 100, 350)
    draw_piece(b_queen_img, 150, 350)
    draw_piece(b_king_img, 200, 350)
    draw_piece(b_bishop_img, 250, 350)
    draw_piece(b_knight_img, 300, 350)    
    draw_piece(b_rook_img, 350, 350)


# Initialize piece locations
piece_locations = {
    w_pawn_img: [(i * 50, 50) for i in range(8)],
    b_pawn_img: [(i * 50, 300) for i in range(8)],
    w_rook_img: [(0, 0)],
    # Add more piece locations as needed
}

selected_piece = None

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for img, positions in piece_locations.items():
                for pos in positions:
                    px, py = pos
                    width, height = img.get_size()
                    if px <= x <= px + width and py <= y <= py + height:
                        selected_piece = img
                        positions.remove(pos)
                        break

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = event.pos
            for img, positions in piece_locations.items():
                if selected_piece == img:
                    positions.append((x - img.get_width() // 2, y - img.get_height() // 2))
                    selected_piece = None

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the chessboard
    draw_chessboard()

    # Draw the pieces using images
    board_setup()

    # Draw the selected piece if any
    if selected_piece:
        x, y = pygame.mouse.get_pos()
        screen.blit(selected_piece, (x - selected_piece.get_width() // 2, y - selected_piece.get_height() // 2))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()