import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Definição das dimensões da tela
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

# Criação da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Cobrinha")

clock = pygame.time.Clock()

# Função para desenhar a cobra na tela
def draw_snake(snake):
    for pos in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

# Função para desenhar a comida na tela
def draw_food(food):
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

# Função principal do jogo
def main():
    snake = [(WIDTH/2, HEIGHT/2)]
    dx, dy = BLOCK_SIZE, 0
    food = (random.randrange(0, WIDTH-BLOCK_SIZE, BLOCK_SIZE), random.randrange(0, HEIGHT-BLOCK_SIZE, BLOCK_SIZE))
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE

        snake_head = (snake[0][0] + dx, snake[0][1] + dy)
        snake.insert(0, snake_head)

        if snake_head == food:
            food = (random.randrange(0, WIDTH-BLOCK_SIZE, BLOCK_SIZE), random.randrange(0, HEIGHT-BLOCK_SIZE, BLOCK_SIZE))
            score += 10
        else:
            snake.pop()

        screen.fill(BLACK)
        draw_snake(snake)
        draw_food(food)

        if (snake_head[0] < 0 or snake_head[0] >= WIDTH or
            snake_head[1] < 0 or snake_head[1] >= HEIGHT or
            snake_head in snake[1:]):
            font = pygame.font.Font(None, 36)
            text = font.render("Game Over! Score: {}".format(score), True, WHITE)
            text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            return

        pygame.display.flip()
        clock.tick(10)  # Velocidade da cobra

if __name__ == "__main__":
    main()
