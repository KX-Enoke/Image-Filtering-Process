from Cimpl import * 

# L8-18-P2-RED.py

def red_channel(image: Image) -> Image:
    """Author: Teshwar Tarachand
    Returns a red channel copy of a given image. In other words, this 
    function will filter out the blues and greens of the image.
     
    >>>image = load_image(choose_file())
    >>>red_channel(image)
    """
    red_image = copy(image)
    
    for x, y, (r, g, b) in image:
        rouge = create_color(r, g == 0, b == 0)
        set_color(red_image, x, y, rouge)
    show(red_image)
    return(red_image)

# L8-18-P2-GREEN.py
        
def green_channel(image: Image) -> Image:
    """Author: Sebastien Grondin
    Returns a green channel copy of a given image. In other words, this 
    function will filter out the blues and reds of the image.
    
    >>>image = load_image(choose_file())
    >>>green_channel(image)
    """ 
    green_image = copy(image)
    
    for x, y, (r, g, b) in image:
        vert = create_color(r == 0, g, b == 0)
        set_color(green_image, x, y, vert)
    show(green_image)
    return(green_image)

# L8-18-P2-BLUE.py

def blue_channel(image: Image) -> Image:
    """Author: Dylan Taylor
    Returns a blue channel copy of a given image. In other words, this 
    function will filter out the green and reds of the image.
    
    
    >>>image = load_image(choose_file())
    >>>blue_channel(image)
    """
    blue_image = copy(image)
    
    for x, y, (r, g, b) in image:
        bleu = create_color(r == 0, g == 0, b)
        set_color(blue_image, x, y, bleu)
    show(blue_image)
    return(blue_image)


# L8-18-P5-Vertical_Flip.py

def flip_vertical(image: Image) -> Image:
    """Author: Sebastien Grondin
    Returns and shows a flipped, on the vertical axis, copy of a given image.

    >>>image = load_image(choose_file())
    >>>flip_vertical(image)
    """

    new_image = copy(image)
    width_pixels = get_width(image)
    height_pixels = get_height(image)

    for y in range(height_pixels):
        for x in range(width_pixels):
            pix_color = get_color(image, x, y)
            set_color(new_image, width_pixels - 1 - x, y, pix_color)
    show(new_image)
    return new_image

# L8-18-P5-Improved_Edge_Detection.py

def detect_edges_better(original: Image, threshold: float) -> Image:
    """Author: Teshwar Tarachand
    Returns and shows the improved edge detected version of a given image and
    threshhold value.

    >>> image = load_image(choose_file())
    >>> detect_edges_better(image, 10)
    """
    image = copy(original)
    height = get_height(image)
    width = get_width(image)

    for x, y, (r, g, b) in image:
        pixel1 = get_color(original, x, y)
        brightness1 = (pixel1[0] + pixel1[1] + pixel1[2]) // 3

        if y != (height-1):
            pixel2 = get_color(original, x, y + 1)
            brightness2 = (pixel2[0] + pixel2[1] + pixel2[2]) // 3
            contrast_Below = abs(brightness1 - brightness2)

        if x != (width - 1):
            pixel3 = get_color(original, x + 1, y)
            brightness3 = (pixel3[0] + pixel3[1] + pixel3[2]) // 3
            contrast_Beside = abs(brightness1 - brightness3)

        if contrast_Below > threshold or contrast_Beside > threshold:
            high_image = create_color(0, 0, 0)
            set_color(image, x, y, high_image)
        else:
            low_image = create_color(255, 255, 255)
            set_color(image, x, y, low_image)

    show(image)
    return image

# L8-18-P5-Horizontal_Flip.py

def flip_horizontal(image: Image) -> Image:
    """Author: Tarachand Teshwar
    Takes in an image, and flips it along the horizontal axis. Returns and 
    shows the flipped image.

    >>>image = load_image(choose_file())
    >>>flip_horizontal(image)
    """
    new_image = copy(image)
    width = get_width(image)
    height = get_height(image)

    for y in range(height // 2):
        for x in range(width):
            left = get_color(image, x, y)
            right = get_color(image, x, height - 1 - y)
            set_color(new_image, x, height - 1 - y, left)
            set_color(new_image, x, y, right)

    show(new_image)
    return new_image

# L8-18-P5-Edge_Detection.py

def detect_edges(image: Image, threshold: float) -> Image:
    """Author: Dylan Taylor
    Takes in an image and a threshold value. Returns and shows an image that 
    looks like it has been drawn as a pencil sketch. 
    
    >>>image = load_image(choose_file())
    >>>detect_edges(image, 10)
    """
    height = get_height(image)
    for x, y, (r, g, b) in image:
        if y != (height-1):
            pixel1 = get_color(image, x, y)
            brightness1 = (pixel1[0] + pixel1[1] + pixel1[2]) / 3
            pixel2 = get_color(image, x, y + 1)
            brightness2 = (pixel2[0] + pixel2[1] + pixel2[2]) / 3
            contrast = (abs(brightness1 - brightness2))
            if contrast > threshold:
                high_image = create_color(0, 0, 0)
                set_color(image, x, y, high_image)
            elif contrast < threshold:
                low_image = create_color(255, 255, 255)
                set_color(image, x, y, low_image)
    
    show(image)
    return(image)

# L8-18-P4-Two_Tone_Filter.py

colours = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), 
           (255, 255, 0), (0, 255, 255), (255, 0, 255), (128, 128, 128)]
list1 = [("black", 1), ("white", 2), ("red", 3), ("lime", 4), ("blue", 5), 
         ("yellow", 6), ("cyan", 7), ("magenta", 8), ("grey", 9)]


def two_tone_filter(image: Image, colour1: str, colour2: str) -> Image:
    """Author: Dylan Taylor
    Returns and shows a two toned varient of a given image and two selected 
    colours. It will iterate through every pixel altering it according to its 
    brightness.
    
    >>>image = load_image(choose_file())
    >>>two_tone_filter(image, "black", "white")
    """
    for i in range(len(list1)):
        colour, number = list1[i]
        if colour1 == colour:
            colour1 = number
    for i in range(len(list1)):
        colour, number = list1[i]
        if colour2 == colour:
            colour2 = number
    
    new_image = copy(image)
    c1 = int(colour1) - 1
    c2 = int(colour2) - 1
    
    r1 = colours[c1][0]
    g1 = colours[c1][1]
    b1 = colours[c1][2]
    r2 = colours[c2][0]
    g2 = colours[c2][1]
    b2 = colours[c2][2]    
    for x, y, (r, g, b) in image:
        brightness = (r + g + b) / 3
        if brightness <= 127:
            (r, g, b) = (r1, g1, b1)
            toned_image = create_color(r, g, b)
            set_color(new_image, x, y, toned_image)
        else:
            (r, g, b) = (r2, g2, b2)
            toned_image = create_color(r, g, b)
            set_color(new_image, x, y, toned_image)
    show(new_image)
    return new_image

# L8-18-P4-Three_Tone_Filter.py

colours = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), 
           (255, 255, 0), (0, 255, 255), (255, 0, 255), (128, 128, 128)]
list1 = [("black", 1), ("white", 2), ("red", 3), ("lime", 4), ("blue", 5), 
         ("yellow", 6), ("cyan", 7), ("magenta", 8), ("grey", 9)]


def three_tone_filter(image: Image, colour1: str, colour2: str, 
                      colour3: str) -> Image:
    """Author: Dylan Taylor
    Returns and shows a two toned varient of a given image and three selected 
    colours. It will iterate through every pixel altering it according to its 
    brightness.
    
    >>>image = load_image(choose_file())
    >>>three_tone_filter(image, "black", "white", "red")
    """
    for i in range(len(list1)):
        colour, number = list1[i]
        if colour1 == colour:
            colour1 = number
    for i in range(len(list1)):
        colour, number = list1[i]
        if colour2 == colour:
            colour2 = number
    for i in range(len(list1)):
        colour, number = list1[i]
        if colour3 == colour:
            colour3 = number

    new_image = copy(image)
    c1 = int(colour1) - 1
    c2 = int(colour2) - 1
    c3 = int(colour3) - 1

    r1 = colours[c1][0]
    g1 = colours[c1][1]
    b1 = colours[c1][2]
    r2 = colours[c2][0]
    g2 = colours[c2][1]
    b2 = colours[c2][2]
    r3 = colours[c3][0]
    g3 = colours[c3][1]
    b3 = colours[c3][2]
    for x, y, (r, g, b) in image:
        brightness = (r + g + b) / 3
        if brightness <= 84:
            (r, g, b) = (r1, g1, b1)
            toned_image = create_color(r, g, b)
            set_color(new_image, x, y, toned_image)
        elif brightness >= 85 and brightness <= 170:
            (r, g, b) = (r2, g2, b2)
            toned_image = create_color(r, g, b)
            set_color(new_image, x, y, toned_image)
        elif brightness >= 171 and brightness <= 255:
            (r, g, b) = (r3, g3, b3)
            toned_image = create_color(r, g, b)
            set_color(new_image, x, y, toned_image)
    show(new_image)
    return new_image


# L8-18-P4-Sepia.py

def grayscale(image: Image) -> Image:
    """
    Return a grayscale copy of image.

    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image


def sepia(image: Image) -> Image:
    """Author: Teshwar Tarachand, Dylan Taylor, Sebastien Grondin
    Returns and shows an image with a sepia tinting filter applied to it.

    >>>image = load_image(choose_file())
    >>>sepia(image)
    """

    new_image = copy(image)
    gray_image = grayscale(new_image)

    for x, y, (r, g, b) in gray_image:
        ReGrBl = get_color(gray_image, x, y)
        RGB = ReGrBl[1]

        if RGB < 63:
            R = RGB * 1.1
            B = RGB * 0.9
            tint = create_color(R, RGB, B)
            set_color(gray_image, x, y, tint)

        elif RGB >= 63 and RGB <= 191:
            R = RGB * 1.15
            B = RGB * 0.85
            tint = create_color(R, RGB, B)
            set_color(gray_image, x, y, tint)

        elif RGB > 191:
            R = RGB * 1.08
            B = RGB * 0.93
            tint = create_color(R, RGB, B)
            set_color(gray_image, x, y, tint)

    show(gray_image)
    return gray_image

# L8-18-P4-Posterizing.py

def _adjust_component(quad: int) -> int:
    """Author: Teshwar Tarachand
    Finds the range and returns the mid point of a given pixel's RGB values.
    Meant to be used within other functions.
    """
    if quad <= 63:
        quad = 31
        return quad

    elif quad >= 64 and quad <= 127:
        quad = 95
        return quad

    elif quad >= 128 and quad <= 191:
        quad = 159
        return quad

    elif quad >= 192 and quad <= 255:
        quad = 233
        return quad


def posterize(image: Image) -> Image:
    """Author: Teshwar Tarachand
    Returns and shows a posterized copy of a given image.

    >>>image = load_image(choose_file())
    >>>posterize(image)
    """
    image = copy(image)

    for x, y, (r, g, b) in image:
        final_colour = create_color(_adjust_component(r), _adjust_component(g),
                                    _adjust_component(b))
        set_color(image, x, y, final_colour)
    show(image)
    return(image)

# L8-18-P4-Extreme_Contrast.py

def extreme_contrast(image:Image)->Image:
    """Author: Sebastien Grondin
    Returns and shows the extreme contrast varient of a given image.

    >>> image = load_image(choose_file())
    >>> extreme_contrast(image)
    """ 
    new_image = copy(image)
    
    for x, y, (r, g, b) in new_image:
        new_red = 0
        new_green = 0
        new_blue = 0
        
        if r >= 128:
            new_red = 255
            
        if g >= 128:
            new_green = 255
            
        if b >= 128:
            new_blue = 255    
        
        final_colour = create_color(new_red, new_green, new_blue)
        set_color(new_image, x, y, final_colour)
        
    show(new_image)
    return(new_image)
