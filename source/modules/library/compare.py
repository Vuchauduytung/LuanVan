def compare_c(compression_pressure, Pmax, Pmin, Minimum_pressure_intake, minimum_pressure ):
        # Pmax lay gia ti lon nhat trong .dat , Pmin lay gia trinho nhat trong .dat
    if 0.8*compression_pressure < Pmax < compression_pressure*1.1:
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
    
def compare_in(compression_pressure, Pmax, Pmin, Minimum_pressure_intake ):            
    if 0.8*compression_pressure < Pmax < compression_pressure*1.1:
        value_in = 'Bình thường'
        damage_in = 'Bình thường'
    else:
        value_in = 'Hư hỏng'
        if Pmin < 0.8*Minimum_pressure_intake:
            damage_in = 'Xuppap bị kẹt (không mở hoàn toàn).'
        elif Pmin > 0.62*Minimum_pressure_intake:
            damage_in = 'Lọt khí qua xecmang (xecmang đóng không kín).'
    return  value_in, damage_in