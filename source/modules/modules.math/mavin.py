#area VIN
def char_vin_1(num_vin):
    char_Vin = list(num_vin)
    
    if ord(char_Vin[0]) == ord('A') or ord(char_Vin[0]) == ord('B') or ord(char_Vin[0]) == ord('C') or ord(char_Vin[0]) == ord('D') :
        area_vin = 'Africa'
    elif ord(char_Vin[0]) == ord('E') or ord(char_Vin[0]) == ord('F') or ord(char_Vin[0]) == ord('G') or ord(char_Vin[0]) == ord('H'):
        area_vin = 'Africa'
    elif ord(char_Vin[0]) == ord('J') or ord(char_Vin[0]) == ord('K') or ord(char_Vin[0]) == ord('L') or ord(char_Vin[0]) == ord('M'):
        area_vin ='Asia'
    elif ord(char_Vin[0]) == ord('N') or ord(char_Vin[0]) == ord('O') or ord(char_Vin[0]) == ord('P') or ord(char_Vin[0]) == ord('Q'):
        area_vin ='Asia'
    elif ord(char_Vin[0]) == ord('R'):
        area_vin = 'Asia'
    elif ord(char_Vin[0]) == ord('S') or ord(char_Vin[0]) == ord('T') or ord(char_Vin[0]) == ord('U') or ord(char_Vin[0]) == ord('V'):
        area_vin = 'Europe'
    elif ord(char_Vin[0]) == ord('W') or ord(char_Vin[0]) == ord('X') or ord(char_Vin[0]) == ord('Y') or ord(char_Vin[0]) == ord('Z'):
        area_vin = 'Europe'
    return area_vin
num_vin ='W23'
char = char_vin_1(num_vin)
print(char)
# def char_vin_three_num(num_vin):
#     char_Vin = list(num_vin)
#     if ord(char_Vin[:2]) == ord('AF'):
#         manu_car = 'Ford South Africa'
#     elif ord(char_Vin[:2]) == ord('AA'):
#         manu_car = 'Volkswagen South Africa'
#     return manu_car
# num_vin ='AFAGFH'
# char = char_vin_three_num(num_vin)
# print(char)
