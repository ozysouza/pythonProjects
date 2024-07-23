from turtle import Turtle, Screen
import random
import colorgram

t = Turtle()
screen = Screen()

# def extract_colors(image_path, num_colors):
#     colors = colorgram.extract(image_path, num_colors)
#     rgb_tuples = []
#
#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         rgb_tuples.append((r, g, b))
#     return rgb_tuples
# return [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
#
#
# color_list = extract_colors("download.jpeg", 30)

colors_list = [(5, 12, 35), (40, 21, 16), (130, 89, 54), (202, 137, 119), (235, 211, 82), (188, 137, 161), (216, 83, 67), (80, 6, 20), (33, 139, 65), (147, 86, 105), (193, 77, 101), (29, 87, 29), (220, 176, 210), (74, 107, 141), (152, 136, 65), (20, 207, 180), (12, 72, 28), (132, 158, 180), (7, 62, 139), (114, 188, 158), (86, 133, 173), (125, 8, 28), (18, 204, 220), (242, 204, 6), (236, 172, 164), (133, 223, 208)]
screen.colormode(255)
t.penup()
t.hideturtle()
t.speed(0)

t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    t.dot(20, random.choice(colors_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


# s = Screen()
# t.shape("turtle")
# # t.pensize(3)

# s.colormode(255)
#

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b


# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         t.color(random_color())
#         t.circle(100)
#         t.setheading(t.heading() + size_of_gap)
#
#
# draw_spirograph(1)


# directions = [0, 90, 180, 270]
#
# for _ in range(200):
#     t.color(random_color())
#     t.forward(30)
#     t.setheading(random.choice(directions))


# num_sides = 3
# is_not_over = True
#
# while is_not_over:
#     t.color(random.choice(colors))
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         t.forward(100)
#         t.right(angle)
#
#     num_sides += 1
#     if num_sides == 10:
#         is_not_over = False

screen.exitonclick()
