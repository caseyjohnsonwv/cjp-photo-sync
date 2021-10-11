from PIL import Image

class AspectRatio:
    # categorization for pricing purposes, landscape/portrait is irrelevant
    __RATIOS__ = {
        4/5 : '4:5',
        5/4 : '4:5',
        1/1 : '1:1',
        3/4 : '4:3',
        4/3 : '4:3',
        9/16 : '16:9',
        16/9 : '16:9',
        2/3 : '3:2',
        3/2 : '3:2',
    }

    def get_aspect_ratio(image_path):
        im = Image.open(image_path)
        width, height = im.size
        true_ratio = ((width/height) * 100) // 1 / 100 # round to 2 decimals
        aspect_ratio = AspectRatio.__RATIOS__.get(true_ratio)
        return aspect_ratio # returns None if ratio not recognized
