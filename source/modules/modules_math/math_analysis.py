import math


def caculate_n(Temperature, Compression_ratio):
    n = 1
    i = 0
    while(i < 1000):
        m = 8.314/(19.806+0.002095*Temperature*(Compression_ratio**(n-1)+1))+1
        n = m
        i = i + 1
    return n


def dynamic_compression_ratio(Piston_journey, Late_closing_angle, Connecting_rod_length, Compression_ratio, Cylinder_diameter, load_pressure):
    # Cylinder_pressure = load_pressure*0.96
    SE = (Piston_journey*(1 + math.cos((Late_closing_angle*math.pi)/180))/2) + Connecting_rod_length - \
        math.sqrt((Connecting_rod_length**2)-((Piston_journey *
                  math.sin((Late_closing_angle*math.pi)/180))**2)/4)
    Ve = (math.pi*(Cylinder_diameter**2)*SE)/4
    Vc = (math.pi/(4*(Compression_ratio-1))) * \
        (Cylinder_diameter**2)*Piston_journey
    Dynamic_compression_ratio = (Ve+Vc)/Vc
    return Dynamic_compression_ratio


def volume(Piston_journey, Late_closing_angle, Connecting_rod_length, Compression_ratio, Cylinder_diameter, load_pressure, Temperature):
    Cylinder_pressure = load_pressure*0.96
    SE = (Piston_journey*(1 + math.cos((Late_closing_angle*math.pi)/180))/2) + Connecting_rod_length - \
        math.sqrt((Connecting_rod_length**2)-((Piston_journey *
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
        math.sqrt((Connecting_rod_length**2)-((Piston_journey *
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
    temperature_C = ((Temperature+20)-273) * \
        Dynamic_compression_ratio**(n0-1)+273
    temperature_F = temperature_C-273
    Compression_wattage = (((load_pressure*0.96)*10**5)
                            * 0.000145)*Dynamic_compression_ratio**n0

    return compression_pressure, temperature_C, temperature_F, Compression_wattage


def minimum_pressure(Dynamic_compression_ratio):
    Minimum_pressure = 14.7*Dynamic_compression_ratio + 14.7 + 5
    return Minimum_pressure


def Pressure_discharge(Piston_journey, Connecting_rod_length, Compression_ratio, Cylinder_diameter, load_pressure, Temperature, n):
    SE = ((Piston_journey*20/180)*(1 + math.cos((20*math.pi/2)/180))/2) + Connecting_rod_length - \
        math.sqrt((Connecting_rod_length**2) -
                  (((Piston_journey*20/180)*math.sin((20*math.pi)/180))**2)/4)
    Ve = (math.pi*(Cylinder_diameter**2)*SE)/4
    Vc = (math.pi/(4*(Compression_ratio-1))) * \
        (Cylinder_diameter**2)*Piston_journey
    Dynamic_compression_ratio = (Ve+Vc)/Vc
    n0 = (8.314/(19.806+0.002095*(Temperature+20)
          * (Dynamic_compression_ratio**(n-1)+1))+1)
    Pressure_discharge = (((load_pressure*0.96)*10**5)
                          * 0.000145)*Dynamic_compression_ratio**n0
    return Pressure_discharge


def minimum_pressure_load(load_pressure):
    Minimum_pressure_load = (((load_pressure*0.96)*10**5)*0.000145)
    return Minimum_pressure_load


def caculate(extTem, comp_rat, piston_jour, cyl_dm, rod_len, xup_cor, air_press):
    Temperature = extTem
    Dynamic_compression_ratio = dynamic_compression_ratio(Piston_journey=piston_jour,
                                                          Late_closing_angle=xup_cor,
                                                          Connecting_rod_length=rod_len,
                                                          Compression_ratio=comp_rat,
                                                          Cylinder_diameter=cyl_dm,
                                                          load_pressure=air_press)
    n = caculate_n(Temperature=Temperature,
                   Compression_ratio=comp_rat)
    load_pressure = air_press
    Volume = volume(Piston_journey=piston_jour,
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
    compression_pressure, temperature_C, temperature_F, Compression_wattage = Analysis(Temperature=Temperature,
                                                                                       Dynamic_compression_ratio=Dynamic_compression_ratio,
                                                                                       n=n,
                                                                                       load_pressure=load_pressure,
                                                                                       Volume=Volume,
                                                                                       n_dynamic=n_dynamic)
    return Compression_wattage, temperature_C, temperature_F, compression_pressure

def check_state(air_press: float, reality_pressure: dict, compression_pressure: float):
    # Pmax lay gia ti lon nhat trong .dat , Pmin lay gia trinho nhat trong .dat
    Pmax = reality_pressure["compress"]
    Pmin = reality_pressure["load"]
    Minimum_pressure_load = minimum_pressure_load(load_pressure=air_press)
    if 0.9*compression_pressure <= Pmax <= compression_pressure*1.1 and 0.8*Minimum_pressure_load <= Pmin <= Minimum_pressure_load*1.1:
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

def damage_in(Pmin, load_pressure):
    Minimum_pressure_load = minimum_pressure_load(load_pressure=load_pressure)
    if 0.8*Minimum_pressure_load <= Pmin <= Minimum_pressure_load*1.1:
        damage_in = 'Khí nạp bình thường.'
    elif Pmin < 0.8*Minimum_pressure_load:
        damage_in = 'Xuppap bị kẹt (không mở hoàn toàn).'
    elif Pmin > 0.62*Minimum_pressure_load:
        damage_in = 'Lọt khí qua xecmang (xecmang đóng không kín).'
    return damage_in