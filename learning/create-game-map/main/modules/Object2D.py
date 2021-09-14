from tkinter import *
import numpy as np

class Image2D:
    ctrl = {
            'Left' : (-1, 0),
            'Right' : (1, 0),
            'Up' : (0, -1),
            'Down' : (0, 1)
        }
    key_sen = 10
    def __init__(self, size, path = None):
        self.root = Tk()
        self.root.title('Create game image object')
        self.root.geometry('800x600')  
        w = size[0]
        h = size[1]
        self.tags = {}
        self.label = Label(self.root, text = '')
        self.canvas = Canvas(self.root, 
                            width = w,
                            height = h,
                            bg = 'white')
        self.canvas.pack(pady = 20)
        if path is not None:
            img = PhotoImage(file = path)
            self.img = self.canvas.create_image(0,
                                                0, 
                                                anchor = NW,
                                                image = img,
                                                tags = 'back_ground')
            self.label = Label(self.root, text = '')
            self.label.pack(pady = 20)
            
    def add_obj(self, path, pos = (0,0), tagId = 'obj'):
        img = PhotoImage(file = path)
        self.canvas.create_image(pos[0],
                                 pos[1], 
                                 anchor = NW,
                                 image = img,
                                 tags = tagId)
        self.tags.update({
            tagId : {
                'img' : img
            }
        })
            
    def drag(self, tagId, x, y):
        (x1, y1, x2, y2) = self.canvas.bbox(tagId)
        if x > x1 and x < x2 and y > y1 and y < y2:
            self.label.config(text = "Obj1 coordinates: \nx= {x_value}, y= {y_value}"\
                .format(x_value = x, 
                        y_value = y))  
            self.canvas.delete(tagId)  
            img = self.tags.get(tagId).get('img')
            self.canvas.create_image(x,
                                     y, 
                                     image = img,
                                     tags = tagId)
            
    def move(self, key, tagId):
        xAmount, yAmount = np.array(self.ctrl.get(key)) * self.key_sen
        self.canvas.move(tagId, xAmount, yAmount)
        
    def catch_key(self, key, tagId):
        return lambda e : self.move(key = key, 
                                    tagId = tagId)  
    
    def catch_mouse(self, tagId):
        return lambda e : self.drag(tagId = tagId, 
                                    x = e.x, 
                                    y = e.y)  
        
    def key_init(self, tagId = 'all'):
        self.root.bind("<Left>", self.catch_key(key = 'Left', 
                                                  tagId = tagId))
        self.root.bind("<Right>", self.catch_key(key = 'Right', 
                                                   tagId = tagId))
        self.root.bind("<Up>", self.catch_key(key = 'Up', 
                                                tagId = tagId))
        self.root.bind("<Down>", self.catch_key(key = 'Down', 
                                                  tagId = tagId))     
        
    def mouse_init(self, tagId = 'all'):
        self.canvas.bind('<B1-Motion>', self.catch_mouse(tagId)) 
    
    def init(self, tagId = 'all'):
        self.key_init(tagId = tagId)
        self.mouse_init(tagId = tagId)
        
    def start(self):
        self.root.mainloop()