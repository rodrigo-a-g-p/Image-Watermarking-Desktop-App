from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter.filedialog import askopenfilename


def add_watermark():
    upload_image_path = askopenfilename(title='Select Image')
    picture_name = upload_image_path.split('/')[-1][::-1].split('.')[1][::-1]

    img = Image.open(upload_image_path)
    width, height = img.size

    draw = ImageDraw.Draw(img)
    text = "rodrigoagponte"

    font_type = ImageFont.truetype('Tsushima.otf', 20)
    text_width, text_height = draw.textsize(text, font_type)

    # calculate the x,y coordinates of the text
    margin_side = 15
    margin_top = 10
    x = width - text_width - margin_side
    y = height - text_height - margin_top

    # draw watermark in the bottom-right corner
    draw.text((x, y), text, font=font_type)

    img.save(f'{picture_name}_with_watermark.png')


# Simple GUI
window = Tk()
window.title('Watermark Adder')
window.config(padx=50, pady=50)

# Display an image in the GUI
canvas = Canvas(height=600, width=600)
image = ImageTk.PhotoImage(Image.open('resources/watermark.png'))
canvas.create_image(300, 300, image=image)
canvas.grid(row=0, column=0)

# Create a button in the GUI
upload_image_button = Button(text='Upload Image', width=30, command=add_watermark)
upload_image_button.grid(row=1, column=0)


window.mainloop()

