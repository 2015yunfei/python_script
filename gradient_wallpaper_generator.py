from PIL import Image


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def generate_gradient_image(color1, color2, width=1080, height=2340):
    gradient = Image.new('RGB', (width, height))

    # Generate gradient
    for y in range(height):
        # Interpolate colors
        r = int(color1[0] + (color2[0] - color1[0]) * y / height)
        g = int(color1[1] + (color2[1] - color1[1]) * y / height)
        b = int(color1[2] + (color2[2] - color1[2]) * y / height)

        # Draw horizontal line with interpolated color
        for x in range(width):
            gradient.putpixel((x, y), (r, g, b))

    return gradient


# Get user input for color1
color1_input = input("Enter color1 in hexadecimal format (e.g., #FF0000 for red): ")
color1 = hex_to_rgb(color1_input)

# Get user input for color2
color2_input = input("Enter color2 in hexadecimal format (e.g., #0000FF for blue): ")
color2 = hex_to_rgb(color2_input)

gradient_image = generate_gradient_image(color1, color2)

# Save the image
gradient_image.save("gradient_image.png")

# Display the image
gradient_image.show()
