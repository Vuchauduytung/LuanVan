# Method 3: Open with webbrowser

def open_c(compression_pressure, Pmax, Pmin, Minimum_pressure_intake, minimum_pressure ):
        # Pmax lay gia ti lon nhat trong .dat , Pmin lay gia trinho nhat trong .dat
    if 0.9*compression_pressure < Pmax < compression_pressure*1.1:
        value = 'Bình thường'
        path_open = "source\library\libary_fix\Open.txt"
        path = "source\library\libary_fix\Open.txt"
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

def open_in(compression_pressure, Pmax, Pmin, Minimum_pressure_intake, Minimum_pressure_charge ):
        # Pmax lay gia ti lon nhat trong .dat , Pmin lay gia trinho nhat trong .dat
    if 0.8*Minimum_pressure_intake < Pmin < Minimum_pressure_intake*1.1:
        value_in = 'Bình thường'
        path_open_in = "0"
        path_in = "0"
    else:
        value_in = 'Hư hỏng'
        path_open_in = "source\library\libary_fix\Tháo lắp động cơ.pdf"
        if 0.62*Minimum_pressure_charge < Pmin < 0.8*Minimum_pressure_charge:
            path_in = 'source\library\libary_fix\Hở xupap.pdf'
        elif Pmin < 0.62*Minimum_pressure_charge:
            path_in = 'source\library\libary_fix\Lọt khí xec măng.pdf'
        elif Pmin < Minimum_pressure_charge:
            path_in = 'source\library\libary_fix\Hư hỏng xylanh.pdf'
    return  value_in,path_open_in,path_in
