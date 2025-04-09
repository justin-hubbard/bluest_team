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

def RGBtoXYZ(rgb):
    nR = rgb[0] / 255
    nG = rgb[1] / 255
    nB = rgb[2] / 255

    if ( nR > 0.04045 ): nR = pow(( nR + 0.055 ) / 1.055, 2.4)
    else: nR = nR / 12.92

    if ( nG > 0.04045 ): nG = pow(( nG + 0.055 ) / 1.055, 2.4)
    else: nG = nG / 12.92

    if ( nB > 0.04045 ): nB = pow(( nB + 0.055 ) / 1.055, 2.4)
    else:nB = nB / 12.92

    nR = nR * 100
    nG = nG * 100
    nB = nB * 100

    X = nR * 0.4124 + nG * 0.3576 + nB * 0.1805
    Y = nR * 0.2126 + nG * 0.7152 + nB * 0.0722
    Z = nR * 0.0193 + nG * 0.1192 + nB * 0.9505

    return (X, Y, Z)

def XYZtoLab(xyz):
    rX = xyz[0] / 95.047
    rY = xyz[1] / 100.00
    rZ = xyz[2] / 108.883

    if ( rX > 0.008856 ): rX = pow(rX, 1/3 )
    else: var_X = ( 7.787 * rX ) + ( 16 / 116 )

    if ( rY > 0.008856 ): rY = pow(rY, 1/3 )
    else: rY = ( 7.787 * rY ) + ( 16 / 116 )
    
    if ( rZ > 0.008856 ): rZ = pow(rZ, 1/3 )
    else: rZ = ( 7.787 * rZ ) + ( 16 / 116 )

    L = ( 116 * rY ) - 16
    a = 500 * ( rX - rY )
    b = 200 * ( rY - rZ )

    return (L, a, b)



def main():
    color = "#F04C29"
    rgb = hexToRGB(color)
    #hex = RGBtoHSV(rgb)

    xyz = RGBtoXYZ(rgb)
    lab = XYZtoLab(xyz)

    print(rgb)
    print(xyz)
    print(lab)

if __name__ == "__main__":
    main()