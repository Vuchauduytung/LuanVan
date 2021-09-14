# Import the required libraries
from tkinter import *
from PIL import Image, ImageTk
import os

# path = os.path.abspath(os.path.dirname(__file__))
# img_path = os.path.abspath(os.path.join(path, 'images', 'object.png'))

# # Create an instance of tkinter frame
# win = Tk()

# # Set the size of the tkinter window
# win.geometry("700x350")

# # Define a Canvas widget
# canvas = Canvas(win, width=600, height=400, bg="white")
# canvas.pack(pady=20)

# # Add Images to Canvas widget
# image = ImageTk.PhotoImage(Image.open(img_path))
# img = canvas.create_image(250, 120, anchor=NW, image=image)

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    img_path = os.path.abspath(os.path.join(path, 'images', 'object.png'))

    # Create an instance of tkinter frame
    win = Tk()

    # Set the size of the tkinter window
    win.geometry("700x350")

    # Define a Canvas widget
    canvas = Canvas(win, width=600, height=400, bg="white")
    canvas.pack(pady=20)

    # Add Images to Canvas widget
    image = ImageTk.PhotoImage(Image.open(img_path))
    img = canvas.create_image(250, 120, anchor=NW, image=image, tags = 'obj')
    
    # Bind the move function
    win.bind("<Left>", catch_button(lam = left, 
                                    canvas = canvas, 
                                    tagId = 'obj'))
    win.bind("<Right>", catch_button(lam = right, 
                                    canvas = canvas, 
                                    tagId = 'obj'))
    win.bind("<Up>", catch_button(lam = up, 
                                    canvas = canvas, 
                                    tagId = 'obj'))
    win.bind("<Down>", catch_button(lam = down, 
                                    canvas = canvas, 
                                    tagId = 'obj'))
    win.mainloop()


def left(e, canvas, tagId):
   x = -20
   y = 0
   canvas.move(tagId, x, y)

def right(e, canvas, tagId):
   x = 20
   y = 0
   canvas.move(tagId, x, y)

def up(e, canvas, tagId):
   x = 0
   y = -20
   canvas.move(tagId, x, y)

def down(e, canvas, tagId):
   x = 0
   y = 20
   canvas.move(tagId, x, y)
   
def catch_button(lam, canvas, tagId):
    return lambda e : lam(e = e, 
                          canvas = canvas, 
                          tagId = tagId)

if __name__ == "__main__":
    main()