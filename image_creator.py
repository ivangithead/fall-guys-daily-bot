from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from requests import get

footer_length = 50
footer_color  = (64, 64, 64)
price_color   = "white"
font = ImageFont.truetype("impact.ttf", 25)


def create_image(data: dict):
    image_bytes = get(data["image"])
    main_img = Image.open(BytesIO(image_bytes.content))
    main_img_x, main_img_y = main_img.size[0], main_img.size[1]  # For write the price

    new_image = Image.new("RGB", (main_img_x, main_img_y + footer_length), "black")
    watermark = Image.open('assets/watermark.png')

    """
    Watermarks generation
    """
    for bg_x in range(5, new_image.size[0], 200):
        for bg_y in range(10, new_image.size[1], 50):
            new_image.paste(watermark, (bg_x, bg_y), watermark)

    new_image.paste(main_img, (0, 0), main_img)

    """
    Draw footer
    """
    for footer_x in range(new_image.size[0]):
        for footer_y in range(main_img_y, main_img_y + footer_length):
            new_image.putpixel((footer_x, footer_y), footer_color)

    price_coords = (new_image.size[0] // 2, new_image.size[1] - footer_length // 1.25)

    drawer = ImageDraw.Draw(new_image)
    drawer.text(price_coords, str(data["price"]), font=font, fill=price_color)

    gem_image = Image.open("assets/gem_mark.png")
    new_image.paste(gem_image, (price_coords[0] - 30, int(price_coords[1]) + 2), gem_image)

    return new_image