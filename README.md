# Chương trình chẩn đoán áp suất nén tức thời không đánh lửa
# Các gói phần mềm cần thiết:
- Python
+ numpy
+ PyQt5
+ PyQt5Designer
+ matplotlib
+ asyncio
+ asyncqt
+ python-dotenv
+ openpyxl
## Cài đặt môi trường python:
1. Chạy file install_python.bat.
2. Chạy file python_setup.bat.
### Các thư mục con
1. source:
- Chứa tất cả các file code phục vụ cho main.py
2. build:
- Chứa các file dùng để build phần mềm từ source code
3. img:
- Chứa các hình ảnh dùng cho việc mô phỏng
## Cách build phần mềm từ source code:
1. Linux:
- Chạy dòng lệnh sau:
```
build/Linux/build.sh
```