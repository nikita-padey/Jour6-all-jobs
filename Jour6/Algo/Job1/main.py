#Job1

def draw_rectangle(width, height):
    if width < 2 or height < 1:
        print("Les dimensions sont trop petites pour dessiner un rectangle.")
        return
    print('|' + '-' * (width - 2) + '|')

    for i in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    print('|' + '-' * (width - 2) + '|')
draw_rectangle(10, 5)
