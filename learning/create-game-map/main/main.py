# MAIN
# System modules
import os

# User modules
from modules.Object2D import *

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.abspath(os.path.join(path, 'images'))
    
    canvas = Image2D(size = (800, 600), 
                     path = None)
    obj1_path = os.path.abspath(os.path.join(img_path, 'object1.png'))
    obj1_tagId = 'obj1'
    canvas.add_obj(path = obj1_path, 
                   pos = (50, 50), 
                   tagId = obj1_tagId)
    canvas.init(tagId = obj1_tagId)
    canvas.start()
    

if __name__ == "__main__":
    main()
    