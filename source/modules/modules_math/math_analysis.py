import math


def caculate_n(Temperature, Compression_ratio):
    n = 1
    i = 0
    while(i < 1000):
        m = 8.314/(19.806+0.002095*(Temperature+20)*(Compression_ratio**(n-1)+1))+1
        n = m
        i = i + 1
    return n


def dynamic_compression_ratio_caculate(Piston_journey, Late_closing_angle, Connecting_rod_length, Compression_ratio, Cylinder_diameter, load_pressure, Temperature):
    SE = (Piston_journey*(1 + math.cos((Late_closing_angle*math.pi)/180))/2) + Connecting_rod_length - \
        math.sqrt((Connecting_rod_length**2)+((Piston_journey *
                  math.sin((Late_closing_angle*math.pi)/180))**2)/4)
    Ve = (math.pi*(Cylinder_diameter**2)*SE)/4
    Vc = (math.pi/(4*(Compression_ratio-1))) * \
        (Cylinder_diameter**2)*Piston_journey
    Dynamic_compression_ratio = (Ve+Vc)/Vc
    return Dynamic_compression_ratio


def volume_caculate(Piston_journey, Late_closing_angle, Connecting_rod_length, Compression_ratio, Cylinder_diameter, load_pressure, Temperature):
    Cylinder_pressure = load_pressure*0.98
    SE = (Piston_journey*(1 + math.cos((Late_closing_angle*math.pi)/180))/2) + Connecting_rod_length - \
        math.sqrt((Connecting_rod_length**2)+((Piston_journey *
                  math.sin((Late_closing_angle*math.pi)/180))**2)/4)
    Ve = (math.pi*(Cylinder_diameter**2)*SE)/4
    Vc = (math.pi/(4*(Compression_ratio-1))) * \
        (Cylinder_diameter**2)*Piston_journey
    Dynamic_compression_ratio = (Ve+Vc)/Vc
    Volume = (Dynamic_compression_ratio*Vc-Vc)/10**6
    n_dynamic = (Temperature/(Temperature+20))*(Dynamic_compression_ratio /
                                                (Dynamic_compression_ratio-1))*(Cylinder_pressure/load_pressure)
    return Volume


def n_dynamic_caculate(Piston_journey, Late_closing_angle, Connecting_rod_length, Compression_ratio, Cylinder_diameter, load_pressure, Temperature):
    Cylinder_pressure = load_pressure*0.96
    SE = (Piston_journey*(1 + math.cos((Late_closing_angle*math.pi)/180))/2) + Connecting_rod_length - \
        math.sqrt((Connecting_rod_length**2)+((Piston_journey *
                  math.sin((Late_closing_angle*math.pi)/180))**2)/4)
    Ve = (math.pi*(Cylinder_diameter**2)*SE)/4
    Vc = (math.pi/(4*(Compression_ratio-1))) * \
        (Cylinder_diameter**2)*Piston_journey
    Dynamic_compression_ratio = (Ve+Vc)/Vc
    n_dynamic = (Temperature/(Temperature+20))*(Dynamic_compression_ratio /
                                                (Dynamic_compression_ratio-1))*(Cylinder_pressure/load_pressure)
    return n_dynamic


def Analysis(Temperature, Dynamic_compression_ratio, n, load_pressure, Volume, n_dynamic):
    n0 = (8.314/(19.806+0.002095*(Temperature+20)
          * (Dynamic_compression_ratio**(n-1)+1))+1)
    compression_pressure = (load_pressure*Volume*n_dynamic *
                           (Temperature+20)*((Volume**(n0-1))-1))/((n0-1)*Temperature) * 1000
    temperature_F = (((Temperature+20)) * \
        Dynamic_compression_ratio**(n0-1))+273
    temperature_C = temperature_F-273
    Compression_wattage = (((load_pressure*0.96)*10**5)
                            * 0.000145)*Dynamic_compression_ratio**n0

    return compression_pressure, temperature_C, temperature_F, Compression_wattage


def minimum_pressure(Dynamic_compression_ratio):
    Minimum_pressure = 14.7*Dynamic_compression_ratio + 14.7 + 5
    return Minimum_pressure


def minimum_pressure_load(load_pressure):
    Minimum_pressure_load = (((-load_pressure*0.98)*10**5)*0.000145)
    return Minimum_pressure_load

def pressure_discharge(load_pressure):
    pressure_discharge = (((load_pressure*0.98)*10**5)*0.000145)
    return pressure_discharge

def caculate(extTem, comp_rat, piston_jour, cyl_dm, rod_len, xup_cor, air_press):
    Temperature = extTem
    n = caculate_n(Temperature=Temperature,
                   Compression_ratio=comp_rat)
    load_pressure = air_press
          
    dynamic_compression_ratio = dynamic_compression_ratio_caculate(Piston_journey=piston_jour,
                                                            Late_closing_angle=xup_cor,
                                                            Connecting_rod_length=rod_len,
                                                            Compression_ratio=comp_rat,
                                                            Cylinder_diameter=cyl_dm,
                                                            load_pressure=air_press,
                                                            Temperature=Temperature)
    
    Volume = volume_caculate(Piston_journey=piston_jour,
                    Late_closing_angle=xup_cor,
                    Connecting_rod_length=rod_len,
                    Compression_ratio=comp_rat,
                    Cylinder_diameter=cyl_dm,
                    load_pressure=air_press,
                    Temperature=Temperature)
    n_dynamic = n_dynamic_caculate(Piston_journey=piston_jour,
                                   Late_closing_angle=xup_cor,
                                   Connecting_rod_length=rod_len,
                                   Compression_ratio=comp_rat,
                                   Cylinder_diameter=cyl_dm,
                                   load_pressure=air_press,
                                   Temperature=Temperature)
    compression_pressure, temperature_F, temperature_C, Compression_wattage = Analysis(Temperature=Temperature,
                                                                                       Dynamic_compression_ratio=dynamic_compression_ratio,
                                                                                       n=n,
                                                                                       load_pressure=load_pressure,
                                                                                       Volume=Volume,
                                                                                       n_dynamic=n_dynamic)
    return n, dynamic_compression_ratio , temperature_F, Compression_wattage

def check_state(air_press: float, reality_pressure: dict, compression_pressure: float):
    Pmax = reality_pressure["compress"]
    P_out = reality_pressure["discharge"]
    P_in = reality_pressure["load"]
    Minimum_pressure_load = minimum_pressure_load(load_pressure=air_press)
    pressure_discharge = pressure_discharge(load_pressure=air_press)
    if 0.9*compression_pressure <= Pmax <= compression_pressure*1.1 and 0.8*pressure_discharge <= P_out <= pressure_discharge*1.1 and 0.8*Minimum_pressure_load <= P_in <= Minimum_pressure_load*1.1:
        return True
    else:
        return False

def damage(comp_rat, piston_jour, cyl_dm, rod_len, xup_cor, air_press, Pci, compression_pressure):
    Dynamic_compression_ratio = dynamic_compression_ratio(Piston_journey=piston_jour,
                                                          Late_closing_angle=xup_cor,
                                                          Connecting_rod_length=rod_len,
                                                          Compression_ratio=comp_rat,
                                                          Cylinder_diameter=cyl_dm,
                                                          load_pressure=air_press)
    Minimum_pressure = 14.7*comp_rat + 14.7 + 5
    if 0.9*compression_pressure <= Pci <= compression_pressure*1.1:
        damage_c ='Áp suất nén bình thường'
    elif Pci < Minimum_pressure:
        damage_c ='Gãy xéc măng, gãy xupap hay bị lủng piston.'
    elif Minimum_pressure < Pci <0.62*compression_pressure:
        damage_c = 'Hở gioăng nắp máy.'
    elif 0.62*compression_pressure < Pci <0.8*compression_pressure:
        damage_c = 'Hở xupap.'
    elif Pci > compression_pressure:
        damage_c = 'Buồng đốt bị bám mụi than, kẹt xupap xả.'
    elif Pci < 0.9*compression_pressure:
        damage_c = 'Các xy lanh mòn không đều.'
    return damage_c

def damage_out(load_pressure):
    
    Pressure_discharge = (((load_pressure*0.96)*10**5)
                          * 0.000145)
    
    pressure_discharge = pressure_discharge(load_pressure=load_pressure)
    
    if 0.8*pressure_discharge <= P_out <= pressure_discharge*1.1:
        damage_out = 'Khí xả bình thường.'
    elif 0.62*Pressure_discharge < P_out < 0.8*Pressure_discharge:
        damage_out = 'Xilanh mòn không đều.'
    elif P_out < 0.62*Pressure_discharge:
        damage_out = 'Cam mở sai thời điểm.'
    elif P_out < 2*Pressure_discharge:
        damage_out = "Hở xupap xả"
    elif P_out > 1.1*Pressure_discharge:
        damage_out = "Xupap nạp mở sai thời điểm"
    elif P_out > 5*Pressure_discharge:
        damage_out = "Kẹt xupap xả"
    return damage_out

def damage_in(load_pressure):
    Minimum_pressure_load = (((-load_pressure*0.98)*10**5)
                             *0.000145)
    Pressure_discharge = (((load_pressure*0.96)*10**5)
                          * 0.000145)
    if 0.8*Minimum_pressure_load <= P_in <= Minimum_pressure_load*1.1:
        damage_in = 'Khí nạp bình thường.'
    elif 0.62*Minimum_pressure_load < P_in < 0.8*Minimum_pressure_load:
        damage_in = 'Xuppap nạp hở (không mở hoàn toàn).'
    elif P_in < 0.62*Minimum_pressure_load:
        damage_in = 'Cam mở sai thời điểm.'
    elif P_in > 1.1*Minimum_pressure_load:
        damage_in = "Xupap nạp hở"
    elif 0.8*Pressure_discharge <= P_in <= Pressure_discharge*1.1:
        damage_in = 'Lỗi thời điểm đóng mở xupap'
    return damage_in