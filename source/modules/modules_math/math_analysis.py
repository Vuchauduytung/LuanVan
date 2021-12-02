import math


def caculate_n(Temperature, Compression_ratio):
    n = 1
    i = 0
    while(i < 1000):
        m = 8.314/(19.806+0.002095*Temperature*(Compression_ratio**(n-1)+1))+1
        n = m
        i = i + 1
    return n


def dynamic_compression_ratio(Piston_journey, Late_closing_angle, Connecting_rod_length, Compression_ratio, Cylinder_diameter, Intake_pressure):
    Cylinder_pressure = Intake_pressure*0.96
    SE = (Piston_journey*(1 + math.cos((Late_closing_angle*math.pi)/180))/2) + Connecting_rod_length - \
        math.sqrt((Connecting_rod_length**2)-((Piston_journey *
                  math.sin((Late_closing_angle*math.pi)/180))**2)/4)
    Ve = (math.pi*(Cylinder_diameter**2)*SE)/4
    Vc = (math.pi/(4*(Compression_ratio-1))) * \
        (Cylinder_diameter**2)*Piston_journey
    Dynamic_compression_ratio = (Ve+Vc)/Vc
    return Dynamic_compression_ratio


def volume(Piston_journey, Late_closing_angle, Connecting_rod_length, Compression_ratio, Cylinder_diameter, Intake_pressure, Temperature):
    Cylinder_pressure = Intake_pressure*0.96
    SE = (Piston_journey*(1 + math.cos((Late_closing_angle*math.pi)/180))/2) + Connecting_rod_length - \
        math.sqrt((Connecting_rod_length**2)-((Piston_journey *
                  math.sin((Late_closing_angle*math.pi)/180))**2)/4)
    Ve = (math.pi*(Cylinder_diameter**2)*SE)/4
    Vc = (math.pi/(4*(Compression_ratio-1))) * \
        (Cylinder_diameter**2)*Piston_journey
    Dynamic_compression_ratio = (Ve+Vc)/Vc
    Volume = (Dynamic_compression_ratio*Vc-Vc)/10**6
    n_dynamic = (Temperature/(Temperature+20))*(Dynamic_compression_ratio /
                                                (Dynamic_compression_ratio-1))*(Cylinder_pressure/Intake_pressure)
    return Volume


def n_dynamic_caculate(Piston_journey, Late_closing_angle, Connecting_rod_length, Compression_ratio, Cylinder_diameter, Intake_pressure, Temperature):
    Cylinder_pressure = Intake_pressure*0.96
    SE = (Piston_journey*(1 + math.cos((Late_closing_angle*math.pi)/180))/2) + Connecting_rod_length - \
        math.sqrt((Connecting_rod_length**2)-((Piston_journey *
                  math.sin((Late_closing_angle*math.pi)/180))**2)/4)
    Ve = (math.pi*(Cylinder_diameter**2)*SE)/4
    Vc = (math.pi/(4*(Compression_ratio-1))) * \
        (Cylinder_diameter**2)*Piston_journey
    Dynamic_compression_ratio = (Ve+Vc)/Vc
    n_dynamic = (Temperature/(Temperature+20))*(Dynamic_compression_ratio /
                                                (Dynamic_compression_ratio-1))*(Cylinder_pressure/Intake_pressure)
    return n_dynamic


def Analysis(Temperature, Dynamic_compression_ratio, n, Intake_pressure, Volume, n_dynamic):
    n0 = (8.314/(19.806+0.002095*(Temperature+20)
          * (Dynamic_compression_ratio**(n-1)+1))+1)
    Compression_wattage = (Intake_pressure*Volume*n_dynamic *
                           (Temperature+20)*((Volume**(n0-1))-1))/((n0-1)*Temperature) * 1000
    temperature_C = ((Temperature+20)-273) * \
        Dynamic_compression_ratio**(n0-1)+273
    temperature_F = temperature_C-273
    compression_pressure = (((Intake_pressure*0.96)*10**5)
                            * 0.000145)*Dynamic_compression_ratio**n0

    return Compression_wattage, temperature_C, temperature_F, compression_pressure


def Minimum_pressure(Dynamic_compression_ratio):
    Minimum_pressure = 14.7*Dynamic_compression_ratio + 14.7 + 5
    return Minimum_pressure


def Pressure_discharge(Piston_journey, Connecting_rod_length, Compression_ratio, Cylinder_diameter, Intake_pressure, Temperature, n):
    SE = ((Piston_journey*20/180)*(1 + math.cos((20*math.pi/2)/180))/2) + Connecting_rod_length - \
        math.sqrt((Connecting_rod_length**2) -
                  (((Piston_journey*20/180)*math.sin((20*math.pi)/180))**2)/4)
    Ve = (math.pi*(Cylinder_diameter**2)*SE)/4
    Vc = (math.pi/(4*(Compression_ratio-1))) * \
        (Cylinder_diameter**2)*Piston_journey
    Dynamic_compression_ratio = (Ve+Vc)/Vc
    n0 = (8.314/(19.806+0.002095*(Temperature+20)
          * (Dynamic_compression_ratio**(n-1)+1))+1)
    Pressure_discharge = (((Intake_pressure*0.96)*10**5)
                          * 0.000145)*Dynamic_compression_ratio**n0
    return Pressure_discharge


def Minimum_pressure_intake(Intake_pressure):
    Minimum_pressure_intake = (((Intake_pressure*0.96)*10**5)*0.000145)
    return Minimum_pressure_intake


def caculate(extTem, comp_rat, piston_jour, cyl_dm, rod_len, xup_cor, air_press):
    Temperature = extTem
    Dynamic_compression_ratio = dynamic_compression_ratio(Piston_journey=piston_jour,
                                                          Late_closing_angle=xup_cor,
                                                          Connecting_rod_length=rod_len,
                                                          Compression_ratio=comp_rat,
                                                          Cylinder_diameter=cyl_dm,
                                                          Intake_pressure=air_press)
    n = caculate_n(Temperature=Temperature,
                   Compression_ratio=comp_rat)
    Intake_pressure = air_press
    Volume = volume(Piston_journey=piston_jour,
                    Late_closing_angle=xup_cor,
                    Connecting_rod_length=rod_len,
                    Compression_ratio=comp_rat,
                    Cylinder_diameter=cyl_dm,
                    Intake_pressure=air_press,
                    Temperature=Temperature)
    n_dynamic = n_dynamic_caculate(Piston_journey=piston_jour,
                                   Late_closing_angle=xup_cor,
                                   Connecting_rod_length=rod_len,
                                   Compression_ratio=comp_rat,
                                   Cylinder_diameter=cyl_dm,
                                   Intake_pressure=air_press,
                                   Temperature=Temperature)
    Compression_wattage, temperature_C, temperature_F, compression_pressure = Analysis(Temperature,
                                                                                       Dynamic_compression_ratio,
                                                                                       n,
                                                                                       Intake_pressure,
                                                                                       Volume,
                                                                                       n_dynamic)
    return Compression_wattage, temperature_C, temperature_F, compression_pressure
