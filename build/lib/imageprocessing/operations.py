from PIL import Image, ImageFilter

def blur_image(input_path, output_path):
    image = Image.open(input_path)
    blurred = image.filter(ImageFilter.BLUR)
    blurred.save(output_path)

def resize_image(input_path, output_path, size):
    image = Image.open(input_path)
    resized = image.resize(size)
    resized.save(output_path)
