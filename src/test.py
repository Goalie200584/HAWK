

from tkinter import image_types
image_text = ["hello", 'this', '3', 'hello']

for line in image_text:
    for num in range(9):
        if image_text[1] == str(num):
            NAME = image_text[0]
        elif image_text[2] == str(num):
            NAME = image_text[0] + image_text[1]
        elif image_text[3] == str(num):
            NAME = image_text[0] + image_text[1] + image_text[2]


print(NAME)