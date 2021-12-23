def compare_c(compression_pressure, Pmax, Pmin, Minimum_pressure_intake, minimum_pressure ):
        # Pmax lay gia ti lon nhat trong .dat , Pmin lay gia trinho nhat trong .dat
    if 0.9*compression_pressure < Pmax < compression_pressure*1.1:
        value = 'Bình thường'
        damage_c = "Bình thường"
    else:
        value = 'Hư hỏng'
        if Pmax < minimum_pressure:
            damage_c ='Gãy xéc măng, gãy xupap hay bị lủng piston.'
        elif minimum_pressure < Pmax <0.62*compression_pressure:
            damage_c = 'Hở gioăng nắp máy.'
        elif 0.62*compression_pressure < Pmax <0.8*compression_pressure:
            damage_c = 'Các xy lanh mòn không đều'
        elif Pmax > compression_pressure:
            damage_c = 'Buồng đốt bị bám mụi than, kẹt xupap xả.'
        elif Pmax < 0.9*compression_pressure:
            damage_c = 'Các xy lanh mòn không đều.'
    return value, damage_c   
    

def compare_out(compression_pressure, Pmax, P_out,P_out_st,P_compress_end, Minimum_pressure_intake, Minimum_pressure_charge ):
    
    Minimum_pressure_load = Minimum_pressure_intake
    Pressure_discharge = Minimum_pressure_charge        
    if 0.8*Minimum_pressure_charge < P_out < Minimum_pressure_charge*1.1:
        value_out = 'Bình thường'
        damage_out = 'Bình thường'
    else:
        value_out= 'Hư hỏng'
        if P_out_st > 5*Pressure_discharge:
            damage_out = "Kẹt xupap xả"
        elif 0.8*Pressure_discharge <= P_out <= Pressure_discharge*1.1:
            damage_out = 'Khí xả bình thường.'
        elif 0.62*Pressure_discharge < P_out < 0.8*Pressure_discharge:
            damage_out = 'Xilanh mòn không đều.'
        elif P_out < 0.62*Pressure_discharge:
            damage_out = 'Cam mở sai thời điểm.'
        elif P_compress_end < 2*Pressure_discharge:
            damage_out = "Hở xupap xả"
        elif P_out > 1.1*Pressure_discharge:
            damage_out = "Xupap mở sai thời điểm"
    return value_out, damage_out

def compare_in(compression_pressure, Pmax, P_in, Minimum_pressure_intake, P_compress_end, Minimum_pressure_charge ):
    
    Minimum_pressure_load = Minimum_pressure_intake
    Pressure_discharge = Minimum_pressure_charge        
    if 1.1*Minimum_pressure_load <= P_in <= Minimum_pressure_load*0.8:
        value_in = 'Bình thường'
        damage_in = 'Bình thường'
    else:
        value_in= 'Hư hỏng'
        if 1.1*Minimum_pressure_load <= P_in <= Minimum_pressure_load*0.8:
            damage_in = 'Khí nạp bình thường.'
        elif 0.8*Minimum_pressure_load < P_in < 0.62*Minimum_pressure_load:
            damage_in = 'Xupap nạp hở.'
        elif P_in < 1.4*Minimum_pressure_load:  #P_in < P_compress_end
            damage_in = 'Xilanh mòn không đều.'
        elif P_in < 1.1*Minimum_pressure_load:
            damage_in = "Xupap nạp hở"
        elif P_in > 0.62*Minimum_pressure_load:
            damage_in = 'Cam mở sai thời điểm.'
        elif 0.8*Pressure_discharge <= P_in <= Pressure_discharge*1.1:
            damage_in = 'Lỗi thời điểm đóng mở xupap'
    return value_in, damage_in

