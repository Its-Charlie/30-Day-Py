#List of Hexadecimal Colors
import random

def list_of_hexa_colors(n):
    colors = []

    for i in range(n):
        color = "#"
        for j in range(6):
            color += random.choice("0123456789abcdef")
        colors.append(color)

    return colors

print(list_of_hexa_colors(5))


#List of RGB Colors

import random

def list_of_rgb_colors(n):
    colors = []

    for i in range(n):
        colors.append(
            f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"
        )

    return colors

print(list_of_rgb_colors(5))


#Generate Colors
import random

def generate_colors(color_type, n):
    colors = []

    if color_type == "hexa":
        for i in range(n):
            color = "#"
            for j in range(6):
                color += random.choice("0123456789abcdef")
            colors.append(color)

    elif color_type == "rgb":
        for i in range(n):
            colors.append(
                f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"
            )

    return colors

print(generate_colors("hexa",3))
print(generate_colors("rgb",3))