# Perfect blue = hsv(240, 100, 100)


def hexToRGB(hex):
    return tuple(int(hex[i:i+2], 16) for i in (1,3,5))

def RGBtoHSV(rgb):

    #normalize
    red = rgb[0] / 255
    green = rgb[1] / 255
    blue = rgb[2] / 255

    cmax = max(red, green, blue)
    cmin = min(red, green, blue)

    delta = cmax - cmin

    #calculate hue
    hue = None
    if cmax == red:
        hue = 60 * (((green - blue) / delta ) % 6)
    elif cmax == green:
        hue = 60 * (((blue - red) / delta ) + 2)
    elif cmax == blue:
        hue = 60 * (((red - green) / delta ) + 4)

    #calculate saturation
    saturation = None
    if cmax == 0:
        saturation = 0
    else:
        saturation = delta / cmax * 100

    value = cmax * 100

    return (hue, saturation, value)


def main():
    color = "#F04C29"
    rgb = hexToRGB(color)
    hex = RGBtoHSV(rgb)

    print(rgb)
    print(hex)

if __name__ == "__main__":
    main()