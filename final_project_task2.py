import turtle

def draw_pythagoras_tree(order, size):
    if order == 0:
        return
    else:
        # Draw the main trunk
        turtle.forward(size)
        turtle.left(45)
        draw_pythagoras_tree(order - 1, size * 0.6)  # Draw left branch

        turtle.right(90)
        draw_pythagoras_tree(order - 1, size * 0.6)  # Draw right branch

        turtle.left(45)
        turtle.backward(size)

def draw_pythagoras_tree_fractal(order, size=100):
    window = turtle.Screen()
    window.bgcolor("white")

    turtle.penup()
    turtle.goto(0, -size / 2)
    turtle.pendown()

    draw_pythagoras_tree(order, size)

    window.mainloop()

# Call the function
level = int(input("Enter the level of recursion: "))
draw_pythagoras_tree_fractal(level)
