import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-a", action='store_true')
parser.add_argument("-s", type=str)
parser.add_argument("-e", type=str)
parser.add_argument("-d", type=str)

args = parser.parse_args()


def parse_resolution(resolution: str):

    resolution_split = resolution.split("x")

    try:
        x, y, = int(resolution_split[0]), int(resolution_split[1])

    except IndexError:
        print("Invalid resolution", resolution)
        exit()
    except ValueError:
        print("Invalid resolution", resolution)
        exit()

    return x, y


def get_aspect(w, h):

    return (w/h)


def get_resolve_zoom (source_width, source_height, extraction_width, extraction_height, desqueeze = 1):

    desqueezed_ext_w = extraction_width*desqueeze
    source_aspect = get_aspect(source_width, source_height)

    source_w_as_169 = source_height*get_aspect(16, 9)

    if source_aspect<get_aspect(16, 9):

        entire_image_zoom = source_w_as_169/desqueezed_ext_w
        with_crop_zoom = source_width/desqueezed_ext_w

    else:

        entire_image_zoom = source_width/desqueezed_ext_w
        with_crop_zoom = source_w_as_169/desqueezed_ext_w

    return {"Scale Entire Image To Fit": entire_image_zoom, "Scale Full Frame With Crop": with_crop_zoom}


if __name__ == "__main__":

    if args.a:

        source = input("Type source resolution in the format 1920x1080:")

        extraction = input("Type extraction resolution in the format 1920x1080:")

        desqueeze = input("Type the anamorphic desqueeze factor:")

        if desqueeze == "":

            desqueeze = "1"

    else:

        source = args.s
        extraction = args.e
        desqueeze = args.d

    my_source_x, my_source_y = parse_resolution(source)
    my_ext_x, my_ext_y = parse_resolution(extraction)
    
    try:
        my_desqueeze = int(desqueeze.strip())
        
    except ValueError:
        print("Invalid desqueeze")
        exit()

    result = get_resolve_zoom(4448, 3096, 4448, 720)

    print("\n")

    for k, v in result.items():

        print(k, v,)
