# Method 3: Open with webbrowser
import os

def open_c(main_path, compression_pressure, Pmax, minimum_pressure):
        # Pmax lay gia ti lon nhat trong .dat , P_in lay gia trinho nhat trong .dat
    if 0.9*compression_pressure < Pmax < compression_pressure*1.1:
        value = 'Bình thường'
        path_open = "0"
        path = "0"
    else:
        value = 'Hư hỏng'
        path_open = "library/libary_fix/Tháo lắp động cơ.pdf"
        if Pmax < minimum_pressure:
            path = 'library/libary_fix/Gãy xéc măng, gãy xupap lủng piston.pdf'
        elif minimum_pressure < Pmax <0.62*compression_pressure:
            path = 'library/libary_fix/Hở giăng nắp máy.pdf'
        elif Pmax > compression_pressure:
            path = 'library/libary_fix/Xilanh không đều.pdf'
        elif Pmax < 0.9*compression_pressure:
            path = 'library/libary_fix/Xilanh không đều.pdf'
    abs_path_open = os.path.abspath(os.path.join(main_path, path_open))
    abs_path = os.path.abspath(os.path.join(main_path, path))
    return  value,abs_path_open,abs_path

def open_in(main_path, 
            P_in,
            Minimum_load_pressure,
            Minimum_charge_pressure):
    Minimum_pressure_load = Minimum_load_pressure
    Pressure_discharge = Minimum_charge_pressure 
    if 1.1*Minimum_pressure_load <= P_in <= Minimum_pressure_load*0.8:
        value_in = 'Bình thường'
        path_open_in = "0"
        path_in = "0"
    else:
        value_in = 'Hư hỏng'
        path_open_in = "library/libary_fix/Tháo lắp động cơ.pdf"
        if 0.8*Minimum_pressure_load < P_in < 0.62*Minimum_pressure_load:
            path_in = 'library/libary_fix/Hở xupap.pdf'
        elif P_in < 1.4*Minimum_pressure_load:  #P_in < P_compress_end
            path_in = 'library/libary_fix/Xilanh không đều.pdf'
        elif P_in > 0.62*Minimum_pressure_load:
            path_in = 'library/libary_fix/Lọt khí xec măng.pdf'
        elif P_in < Minimum_charge_pressure:
            path_in = 'library/libary_fix/Hư hỏng xylanh.pdf'
        elif P_in < 1.1*Minimum_pressure_load:
            path_in = "library/libary_fix/Hở xupap.pdf"
        elif 0.8*Pressure_discharge <= P_in <= Pressure_discharge*1.1:
            path_in = 'library/libary_fix/Hở xupap.pdf'
    abs_path_open_in = os.path.abspath(os.path.join(main_path, path_open_in))
    abs_path_in = os.path.abspath(os.path.join(main_path, path_in))
    return  value_in, abs_path_open_in, abs_path_in

def open_out(main_path, P_out,P_out_st,P_compress_end, Minimum_charge_pressure):
    Pressure_discharge = Minimum_charge_pressure        
    if 0.8*Minimum_charge_pressure < P_out < Minimum_charge_pressure*1.1:
        value_out = 'Bình thường'
        path_open_out = "0"
        path_out = "0"
    else:
        value_out= 'Hư hỏng'
        path_open_out = "library/libary_fix/Tháo lắp động cơ.pdf"
        if P_out_st > 5*Pressure_discharge:
            path_out = "library/libary_fix/Hở xupap.pdf"
        elif 0.62*Pressure_discharge < P_out < 0.8*Pressure_discharge:
            path_out = 'library/libary_fix/Xilanh không đều.pdf'
        elif P_out < 0.62*Pressure_discharge:
            path_out = 'library/libary_fix/Hở giăng nắp máy.pdf'
        elif P_compress_end < 2*Pressure_discharge:
            path_out = "library/libary_fix/Hở xupap.pdf"
        elif P_out > 1.1*Pressure_discharge:
            path_out = "library/libary_fix/Hở xupap.pdf"
    abs_path_open_out = os.path.abspath(os.path.join(main_path, path_open_out))
    abs_path_out = os.path.abspath(os.path.join(main_path, path_out))
    return value_out, abs_path_open_out,abs_path_out

