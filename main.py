from random import randint
x = 27
y = 27
mines_left = 100
cells_left = x*y
field = [[" "] * (x+2) for i in range(y+2)]
field_show = [[0] * (x+2) for i in range(y+2)]
for x in range(1, len(field)-1):
    for y in range(1, len(field[0])-1):
        if randint(1, cells_left) <= mines_left:
            mines_left -= 1
            field[x][y] = 9
        else:
            field[x][y] = 0
        cells_left -= 1
def count_n(x, y):
    global field
    if field[x][y] != 9:
        count = 0
        if field[x-1][y-1] == 9:
            count += 1
        if field[x-1][y] == 9:
            count += 1
        if field[x-1][y+1] == 9:
            count += 1
        if field[x][y-1] == 9:
            count += 1
        if field[x][y+1] == 9:
            count += 1
        if field[x+1][y-1] == 9:
            count += 1
        if field[x+1][y] == 9:
            count += 1
        if field[x+1][y+1] == 9:
            count += 1
        field[x][y] = count
    return
for x in range(1, len(field)-1):
    for y in range(1, len(field[0])-1):
        count_n(x, y)
for i in field:
    print(i)
def check_neubours(x, y):
    if field[x - 1][y - 1] == 0 and field_show[x - 1][y - 1] == 0:
        field_show[x - 1][y - 1] = 1
        check_neubours(x-1, y-1)
    field_show[x - 1][y - 1] = 1

    if field[x - 1][y] == 0 and field_show[x - 1][y] == 0:
        field_show[x - 1][y] = 1
        check_neubours(x-1, y)
    field_show[x - 1][y] = 1

    if field[x - 1][y + 1] == 0 and field_show[x - 1][y + 1] == 0:
        field_show[x - 1][y + 1] = 1
        check_neubours(x-1, y+1)
    field_show[x - 1][y + 1] = 1

    if field[x][y - 1] == 0 and field_show[x][y - 1] == 0:
        field_show[x][y - 1] = 1
        check_neubours(x, y-1)
    field_show[x][y - 1] = 1

    if field[x][y + 1] == 0 and field_show[x][y + 1] == 0:
        field_show[x][y + 1] = 1
        check_neubours(x, y+1)
    field_show[x][y + 1] = 1

    if field[x + 1][y - 1] == 0 and field_show[x + 1][y - 1] == 0:
        field_show[x + 1][y - 1] = 1
        check_neubours(x+1, y-1)
    field_show[x + 1][y - 1] = 1

    if field[x + 1][y] == 0 and field_show[x + 1][y] == 0:
        field_show[x + 1][y] = 1
        check_neubours(x+1, y)
    field_show[x + 1][y] = 1

    if field[x + 1][y + 1] == 0 and field_show[x + 1][y + 1] == 0:
        field_show[x + 1][y + 1] = 1
        check_neubours(x+1, y+1)
    field_show[x + 1][y + 1] = 1


import pygame
time = 0
game_over = 0
pygame.init()
screen = pygame.display.set_mode((700, 580))
done = False
clock = pygame.time.Clock()
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if pygame.mouse.get_pressed()[0] == 1 and game_over == 0:
            position = pygame.mouse.get_pos()
            y = position[0]//20
            x = position[1]//20
            if y > 27:
                y = 0
            if x > 27:
                x = 0
            if field_show[x][y] == 0:
                field_show[x][y] = 1
                if field[x][y] == 0:
                    check_neubours(x, y)

        if pygame.mouse.get_pressed()[2] == 1 and game_over == 0:
            position = pygame.mouse.get_pos()
            x = position[0] // 20
            y = position[1] // 20
            if y > 27:
                y = 0
            if x > 27:
                x = 0
            if field_show[y][x] == 0:
                field_show[y][x] = 2
            elif field_show[y][x] == 2:
                field_show[y][x] = 0

    screen.fill((255, 255, 255))
    color = (0, 0, 0)
    for i in range(1, len(field)-1):
        for j in range(1, len(field[0])-1):
            pygame.draw.rect(screen, color, pygame.Rect(i*20, j*20, 21, 21), 1)

    # Выбираем шрифт, который мы будем использовать.
    # Стандартный шрифт, 25 точек.
    font = pygame.font.Font(None, 25)

    # Рисуем текст. "True" означает использовать сглаживание
    # Black -- цвет текста. Следующая строка создает образ текста
    # но не рисует его на экране.
    black = [0, 0, 255]
    green = [0, 255, 0]
    rad = [255, 0, 0]
    if game_over == 0:
        time += 1/60
    time_s = int(time)
    for i in range(len(field_show)):
        for j in range(len(field_show[0])):
            if field_show[i][j] == 1:
                if field[i][j] == 9:
                    # конец игры
                    game_over = 1
                    text = font.render("M", True, rad)
                    screen.blit(text, [3 + j * 20, 2 + i * 20])
                else:
                    text = font.render(str(field[i][j]), True, black)

    # Рисуем изображение текста на экран в точке (250, 250)
                    screen.blit(text, [6+j*20, 2+i*20])
            if field_show[i][j] == 2:
                text = font.render("F", True, green)
                screen.blit(text, [6 + j * 20, 2 + i * 20])
                # нарисовать флажок
    if game_over == 1:
        # красный экран, конец игры
        font = pygame.font.Font(None, 100)
        text = font.render("GAME OVER", True, rad)
        screen.blit(text, [100, 100])
        font = pygame.font.Font(None, 25)

    # время
    font = pygame.font.Font(None, 50)
    text = font.render(str(time_s), True, green)
    screen.blit(text, [600, 100])
    font = pygame.font.Font(None, 25)

    pygame.display.flip()
    clock.tick(60)
