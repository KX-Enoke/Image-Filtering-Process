#Milestone 3 [P8 - Task 1]; L8-18; 01/12/2019
#Authors: Teshwar Tarachand, Sebastien Grondin, Dylan Taylor
from Cimpl import *
from L8_18_image_filters import *


def display() -> str:
    """Authors: Teshwar Tarachand, Sebastien Grondin, Dylan Taylor
    Shows available effects that can be applied to an image. Takes user input
    and return the input in uppercase.
    """
    response = input("L)oad image   S)ave-as\n" +
                     "2)-tone   3)-tone   X)treme contrast   T)int sepia" +
                     "   P)osterize\n" +
                     "E)dge detect   I)mproved edge detect   V)ertical flip" +
                     "   H)orizontal flip\n" +
                     "Q)uit\n\n" +
                     ": ")
    response = response.upper()
    return response


filters_dict = {"L": "Load", "S": "Save-As", "2": two_tone_filter, "3":
                three_tone_filter, "X": extreme_contrast, "T": sepia, "P":
                posterize, "E": detect_edges, "I": detect_edges_better, "V":
                flip_vertical, "H": flip_horizontal}


def color_choosing():
    """Authors: Teshwar Tarachand
    Shows colours available for 2 and 3 tones. Returns the input if the
    colour is available. Otherwise, it asks to choose a different colour.
    """
    inp = "not input"
    color_list = ["black", "white", "red", "lime", "blue", "yellow", "cyan",
                  "magenta", "grey"]
    seperator = ', '
    while inp not in color_list:
        print(seperator.join(color_list))
        inp = input()
        if inp not in color_list:
            print("Error, choose a color again")
    return inp

go = True
color1 = 1
color2 = 1
color3 = 1
threshold = ""
image = "not image"
u_inp = ""

while (go == True):
    u_inp = display()

    if u_inp in filters_dict.keys():

        if u_inp == "L":
            image = load_image(choose_file())
            show(image)

        elif image == "not image":
            print("Please load an image first")

        elif u_inp == "E" or u_inp == "I":
            threshold = input("Please input the threshold : ")
            image = filters_dict[u_inp](image, float(threshold))

        elif u_inp == "2":
            print("Choose your first color: ")
            color1 = color_choosing()
            print("Choose your second color: ")
            color2 = color_choosing()
            image = filters_dict[u_inp](image, color1, color2)

        elif u_inp == "3":
            print("Choose your first color: ")
            color1 = color_choosing()
            print("Choose your second color: ")
            color2 = color_choosing()
            print("Choose your third color: ")
            color3 = color_choosing()
            image = filters_dict[u_inp](image, color1, color2, color3)

        elif u_inp == "S":
            save_as(image)

        else:
            image = filters_dict[u_inp](image)

    elif u_inp == "Q":
        print("Quitting")
        go = False

    else:
        print(u_inp)
        print("Please choose an effect again: ")
