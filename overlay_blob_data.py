from PIL import Image, ImageDraw, ImageFont
import os

def add_overlay_to_image(
    input_image_path,
    output_image_path,
    text_to_add,
    position,  # A tuple (x, y)
    circleRadius,
    circleX,
    circleY,
    text_color=(255, 0, 0, 0),  # Default is Red (RGB)
    font_path=None,  # Path to a .ttf or .otf file
    font_size=20
):
    """
    Adds text to a bitmap image and saves the result.

    Args:
        input_image_path (str): The path to the input image file (e.g., 'my_image.bmp').
        output_image_path (str): The path to save the output image (e.g., 'output_with_text.bmp').
        text_to_add (str): The string of text to write on the image.
        position (tuple): The (x, y) coordinates for the top-left corner of the text.
        text_color (tuple): Single element touple [255]
        font_path (str, optional): The path to a TrueType font file. 
                                    If None, a default font is used.
        font_size (int): The size of the font.
    """
    try:
        # 1. Open the image
        print(input_image_path)
        img = Image.open(input_image_path)
    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_image_path}'")
        return
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    img.load()
    # 2. Create a drawing context
    draw = ImageDraw.Draw(img)

    # 3. Define the font
    font = None
    if font_path and os.path.exists(font_path):
        try:
            font = ImageFont.truetype(font_path, font_size)
        except Exception as e:
            print(f"Warning: Could not load custom font. Using default. Error: {e}")
            font = ImageFont.load_default()
    else:
        font = ImageFont.load_default()
        if font_path:
             print(f"Warning: Custom font path '{font_path}' not found. Using default font.")

    # 4. Add the text to the image
    print("Pos " + str(position))
    print("Txt " + text_to_add)
    print("Fill " + str(text_color))
    
    #draw.text((10, 10), "Hello", font=font, fill=(255))
    draw.text(position, text_to_add, fill=(255), font=font)
    
    print("Rad " + str(circleRadius))
    print("X " + str(circleX))
    print("Y " + str(circleY))
    draw.circle(xy=[circleX,circleY],radius = circleRadius,fill = None, outline = 255, width = 1)

    # 5. Save the modified image
    try:
        img.save(output_image_path)
        print(f"Successfully added text and saved to '{output_image_path}'")
    except Exception as e:
        print(f"Error saving image: {e}")

if __name__ == "__main__":
    # --- Example Usage ---

    # 1. Ensure you have an image file named 'original.bmp' in the same directory
    #    Or change the path below to your actual image file.

    input_file = 'C:\\Projects\\MBD\\TestImages\\Cam3\\FastForward_N944_3L\\test\\FastForward_N944_3L\\model2\\0_Camera3_1763035657.bmp'
    output_file = 'C:\\Projects\MBD\\TestImages\\Cam3\\FastForward_N944_3L\\test\\FastForward_N944_3L\\model2\\0_Camera5_1763031498_copy.bmp'
    custom_font_file = 'arial.ttf' # Change to the path of a .ttf font on your system

    # Example 1: Using a custom font (if available)
    add_overlay_to_image(
        input_image_path=input_file,
        output_image_path=output_file,
        text_to_add="Test Test test!\n  23312341 \n asdfasdf \n",
        position=(10, 10),
        circleRadius=55,
        circleX=75,
        circleY=100,
        text_color=(0, 0, 255, 255),  # Blue
        font_path=custom_font_file,
        font_size=5
    )
