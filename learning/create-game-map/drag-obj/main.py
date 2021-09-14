from tkinter import *
import os

path = os.path.abspath(os.path.dirname(__file__))
img_path = os.path.abspath(os.path.join(path, 'images', 'object.png'))
    
root = Tk()
root.title('Demo drag')
root.geometry('800x600')    
    
w = 600
h = 400
x = w/2
y = h/2
my_canvas = Canvas(root, 
                    width = w,
                    height = h,
                    bg = 'white')
my_canvas.pack(pady = 20)
    
img = PhotoImage(file = img_path)
my_image = my_canvas.create_image(260,
                                125, 
                                anchor = NW,
                                image = img,
                                tags = 'obj')
my_label = Label(root, text = '')
# my_label.pack(pady = 20)

def main():
    my_canvas.bind('<B1-Motion>', move)
    # my_canvas.focus('obj')
    root.mainloop()

    
def move(event):
    global my_canvas, my_label, my_image
    (x1, y1, x2, y2) = my_canvas.bbox('obj')
    if event.x > x1 and event.x < x2 and event.y > y1 and event.y < y2:
        my_label.config(text = "Coordinates: \nx= {x_value}, y= {y_value}"\
            .format(x_value = event.x, 
                    y_value = event.y))  
        my_canvas.delete('obj')  
        my_image = my_canvas.create_image(event.x,
                                        event.y, 
                                        image = img,
                                        tags = 'obj')
    

    

if __name__ == '__main__':
    main()    