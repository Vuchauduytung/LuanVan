import sys
import os

path = os.path.abspath(os.path.dirname(__file__))
main_path = os.path.abspath(os.path.join(path, os.pardir))
direct_path = os.path.abspath(os.path.join(main_path, "source", "GUIinput.py"))
os.system("python3 \"{path}\""\
    .format(path=direct_path))