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
            damage_c = 'Hở xupap.'
        elif Pmax > compression_pressure:
            damage_c = 'Buồng đốt bị bám mụi than, kẹt xupap xả.'
        elif Pmax < 0.9*compression_pressure:
            damage_c = 'Các xy lanh mòn không đều.'
    return value, damage_c   
    
def compare_in(compression_pressure, Pmax, Pmin, Minimum_pressure_intake, Minimum_pressure_charge ):            
    if 0.8*Minimum_pressure_intake < Pmin < Minimum_pressure_intake*1.1:
        value_in = 'Bình thường'
        damage_in = 'Bình thường'
    else:
        value_in = 'Hư hỏng'
        if 0.62*Minimum_pressure_charge < Pmin < 0.8*Minimum_pressure_charge:
            damage_in = 'Xuppap bị kẹt (không mở hoàn toàn).'
        elif Pmin < 0.62*Minimum_pressure_charge:
            damage_in = 'Lọt khí qua xecmang (xecmang đóng không kín).'
        elif Pmin < Minimum_pressure_charge:
            damage_in = "Xylanh hư hỏng"
    return  value_in, damage_in

def compare_out(compression_pressure, Pmax, P_out, Minimum_pressure_intake, Minimum_pressure_charge ):
    
    Minimum_pressure_load = Minimum_pressure_intake
    Pressure_discharge = Minimum_pressure_charge        
    if 0.8*Minimum_pressure_intake < P_out < Minimum_pressure_intake*1.1:
        value_out = 'Bình thường'
        damage_out = 'Bình thường'
    else:
        if 0.8*pressure_discharge <= P_out <= pressure_discharge*1.1:
            damage_out = 'Khí nạp bình thường.'
        elif 0.62*Pressure_discharge < P_out < 0.8*Pressure_discharge:
            damage_out = 'Xuppap bị kẹt (không mở hoàn toàn).'
        elif P_out < 0.62*Pressure_discharge:
            damage_out = 'Cam mở sai thời điểm.'
        elif P_out < 2*Pressure_discharge:
            damage_out = "Hở xupap xả"
        elif P_out > 1.1*Pressure_discharge:
            damage_out = "Xupap nạp mở sai thời điểm"
        elif P_out > 5*Pressure_discharge:
            damage_out = "Kẹt xupap xả"
    return value_out, damage_out

def compare_in(compression_pressure, Pmax, P_in, Minimum_pressure_intake, Minimum_pressure_charge ):
    
    Minimum_pressure_load = Minimum_pressure_intake
    Pressure_discharge = Minimum_pressure_charge        
    if 0.8*Minimum_pressure_intake < P_in < Minimum_pressure_intake*1.1:
        value_in = 'Bình thường'
        damage_in = 'Bình thường'
    else:
        if 0.8*Minimum_pressure_load <= P_in <= Minimum_pressure_load*1.1:
            damage_in = 'Khí nạp bình thường.'
        elif 0.62*Minimum_pressure_load < P_in < 0.8*Minimum_pressure_load:
            damage_in = 'Xuppap nạp hở (không mở hoàn toàn).'
        elif P_in < 0.62*Minimum_pressure_load:
            damage_in = 'Cam mở sai thời điểm.'
        elif P_in > 1.1*Minimum_pressure_load:
            damage_in = "Xupap nạp nh"
        elif 0.8*Pressure_discharge <= P_in <= Pressure_discharge*1.1:
            damage_in = 'Lỗi thời điểm đóng mở xupap'
    return value_in, damage_in