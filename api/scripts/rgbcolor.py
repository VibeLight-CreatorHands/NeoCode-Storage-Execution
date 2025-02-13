def rgb_to_color_name(r: int, g: int, b: int):
    if r == 255 and g == 0 and b == 0:
        return "Red"
    elif r == 0 and g == 255 and b == 0:
        return "Green"
    elif r == 0 and g == 0 and b == 255:
        return "Blue"
    else:
        return "Unknown color"

if __name__ == "__main__":
    r = int(input("Enter red value (0-255): "))
    g = int(input("Enter green value (0-255): "))
    b = int(input("Enter blue value (0-255): "))
    print(f"The color is: {rgb_to_color_name(r, g, b)}")
