import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    
    level = int(input("Введіть рівень рекурсії (бажано 1-5): "))

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Koch Snowflake")

    t = turtle.Turtle()
    t.speed(0)
    t.color("red")

    
    size = 300

    t.penup()
    t.goto(-150, 90)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, level, size)
        t.right(120)
    
    screen.mainloop()

if __name__ == "__main__":
    main()
