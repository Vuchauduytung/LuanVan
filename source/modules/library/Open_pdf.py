# Method 3: Open with webbrowser

def open_c(compression_pressure, Pmax, P_in, Minimum_pressure_intake, minimum_pressure ):
        # Pmax lay gia ti lon nhat trong .dat , P_in lay gia trinho nhat trong .dat
    if 0.9*compression_pressure < Pmax < compression_pressure*1.1:
        value = 'Bình thường'
        path_open = "0"
        path = "0"
    else:
        value = 'Hư hỏng'
        path_open = "source\library\libary_fix\Tháo lắp động cơ.pdf"
        if Pmax < minimum_pressure:
            path = 'source\library\libary_fix\Gãy xéc măng, gãy xupap lủng piston.pdf'
        elif minimum_pressure < Pmax <0.62*compression_pressure:
            path = 'source\library\libary_fix\Hở giăng nắp máy.pdf'
        elif 0.62*compression_pressure < Pmax <0.8*compression_pressure:
            path = 'source\library\libary_fix\Hở xupap.pdf'
        elif Pmax > compression_pressure:
            path = 'source\library\libary_fix\Xilanh không đều.pdf'
        elif Pmax < 0.9*compression_pressure:
            path = 'source\library\libary_fix\Xilanh không đều.pdf'
    return  value,path_open,path

def open_in(compression_pressure, Pmax, P_in, Minimum_pressure_intake, Minimum_pressure_charge ):
    Minimum_pressure_load = Minimum_pressure_intake
    Pressure_discharge = Minimum_pressure_charge
    if 0.8*Minimum_pressure_intake < P_in < Minimum_pressure_intake*1.1:
        value_in = 'Bình thường'
        path_open_in = "0"
        path_in = "0"
    else:
        value_in = 'Hư hỏng'
        path_open_in = "source\library\libary_fix\Tháo lắp động cơ.pdf"
        if 0.62*Minimum_pressure_charge < P_in < 0.8*Minimum_pressure_charge:
            path_in = 'source\library\libary_fix\Hở xupap.pdf'
        elif P_in < 0.62*Minimum_pressure_charge:
            path_in = 'source\library\libary_fix\Lọt khí xec măng.pdf'
        elif P_in < Minimum_pressure_charge:
            path_in = 'source\library\libary_fix\Hư hỏng xylanh.pdf'
        elif P_in > 1.1*Minimum_pressure_load:
            damage_in = "source\library\libary_fix\Hở xupap.pdf"
        elif 0.8*Pressure_discharge <= P_in <= Pressure_discharge*1.1:
            damage_in = 'source\library\libary_fix\Hở xupap.pdf'
    return  value_in,path_open_in,path_in


