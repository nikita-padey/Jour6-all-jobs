#Job2

def draw_triangle(height):

    if height < 1:
        print("La hauteur doit être d'au moins 1.")
        return

    for i in range(height):
        spaces = ' ' * (height - i - 1)
        
        if i == 0:
            inside = ''
        elif i == height - 1:
            inside = '_' * (2 * i)
        else:
            inside = ' ' * (2 * i)
        
        line = spaces + '/' + inside + '\\'
        
        print(line)

draw_triangle(5)
