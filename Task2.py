import turtle

# Функція для рекурсивного малювання однієї сторони сніжинки Коха
def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)

# Функція для малювання сніжинки Коха
def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

# Функція для запиту рівня рекурсії у користувача
def get_user_input():
    while True:
        try:
            order = int(input("Введіть рівень рекурсії (не робіть більше 6): "))
            if order >= 0:
                return order
            else:
                print("Рівень рекурсії має бути невід'ємним числом.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    # Отримуємо рівень рекурсії від користувача
    recursion_level = get_user_input()

    # Налаштовуємо Turtle для малювання
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.penup()
    t.goto(-150, 100)  # Початкове положення для малювання
    t.pendown()

    # Малюємо сніжинку Коха
    koch_snowflake(t, recursion_level, 500)
    turtle.done()
