import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Intersecting Circles Structure")

# Turtle for circles
t = turtle.Turtle()
t.speed(0.55)
t.hideturtle()
t.up()

# Turtle for labels
label_t = turtle.Turtle()
label_t.hideturtle()
label_t.up()
label_t.color("black")

# Labels and colors (outermost to innermost)
labels = [
    "Artificial Intelligence (AI)",
    "Machine Learning (ML)",
    "Deep Learning",
    "Generative AI",
    "Large Language Models (LLM)",
    "ChatGPT"
]
colors = ["#133B5C", "#1E5F74", "#1597BB", "#76ADC8", "#A3BFFA", "#EAF1FF"]

# Custom font sizes for each label
font_sizes = [14, 13, 12, 12, 6, 10]

# Custom label Y-offsets (multipliers of radius)
label_y_multipliers = [0.77, 0.75, 0.65, 0.6, 0.55, 0.5]

# Base radius and step between circles
base_radius = 500
radius_step = 80
intersection_y = -base_radius  # All circles touch this Y-coordinate at bottom

# Draw intersecting circles and labels
for i in range(len(labels)):
    radius = base_radius - i * radius_step
    center_y = intersection_y + radius
    center_x = 0

    # Draw filled circle
    t.goto(center_x, center_y - radius)
    t.setheading(0)
    t.down()
    t.fillcolor(colors[i])
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.up()

    # Calculate label Y-position using custom multiplier
    label_y = center_y + radius * label_y_multipliers[i]
    label_t.goto(center_x, label_y)
    label_t.write(labels[i], align="center", font=("Arial", font_sizes[i], "bold"))

    time.sleep(0.5)  # Optional animation delay

# Keep the window open
screen.mainloop()
