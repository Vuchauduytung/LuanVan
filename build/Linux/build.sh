#!/bin/bash

pyinstaller --noconfirm --onedir --console \
    --icon "/home/tungvu/dev/thesis/LuanVan/source/icon/Logo-BK.ico" \
    --name "chuongtrinhchandoan" \
    --add-data "/home/tungvu/dev/thesis/LuanVan/source:source/" \
    "/home/tungvu/dev/thesis/LuanVan/main.py"
cd .. && cd .. && ln -s "build/Linux/dist/chuongtrinhchandoan/chuongtrinhchandoan"
