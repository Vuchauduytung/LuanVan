import math

def n(Temperature,Compression_ratio):

    n = 1
    i = 0

    while(i<1000):
        m = 8.314/(19.806+0.002095*Temperature*(Compression_ratio**(n-1)+1))+1
        n = m
        i = i + 1
    return n     

def Dynamic_compression_ratio(Piston_journey,Late_closing_angle,Connecting_rod_length,Compression_ratio,Cylinder_diameter,Intake_pressure):
    
    Cylinder_pressure = Intake_pressure*0.96
    SE = (Piston_journey*(1 + math.cos((Late_closing_angle*math.pi)/180))/2) + Connecting_rod_length - math.sqrt((Connecting_rod_length**2)-((Piston_journey*math.sin((Late_closing_angle*math.pi)/180))**2)/4)
    Ve = (math.pi*(Cylinder_diameter**2)*SE)/4
    Vc = (math.pi/(4*(Compression_ratio-1)))*(Cylinder_diameter**2)*Piston_journey
    Dynamic_compression_ratio = (Ve+Vc)/Vc
    
    return Dynamic_compression_ratio

def Volume(Piston_journey,Late_closing_angle,Connecting_rod_length,Compression_ratio,Cylinder_diameter,Intake_pressure,Temperature):
    
    Cylinder_pressure = Intake_pressure*0.96
    SE = (Piston_journey*(1 + math.cos((Late_closing_angle*math.pi)/180))/2) + Connecting_rod_length - math.sqrt((Connecting_rod_length**2)-((Piston_journey*math.sin((Late_closing_angle*math.pi)/180))**2)/4)
    Ve = (math.pi*(Cylinder_diameter**2)*SE)/4
    Vc = (math.pi/(4*(Compression_ratio-1)))*(Cylinder_diameter**2)*Piston_journey
    Dynamic_compression_ratio = (Ve+Vc)/Vc
    Volume = (Dynamic_compression_ratio*Vc-Vc)/10**6
    n_dynamic = (Temperature/(Temperature+20))*(Dynamic_compression_ratio/(Dynamic_compression_ratio-1))*(Cylinder_pressure/Intake_pressure)
    
    return Volume

def n_dynamic(Piston_journey,Late_closing_angle,Connecting_rod_length,Compression_ratio,Cylinder_diameter,Intake_pressure,Temperature):
    
    Cylinder_pressure = Intake_pressure*0.96
    SE = (Piston_journey*(1 + math.cos((Late_closing_angle*math.pi)/180))/2) + Connecting_rod_length - math.sqrt((Connecting_rod_length**2)-((Piston_journey*math.sin((Late_closing_angle*math.pi)/180))**2)/4)
    Ve = (math.pi*(Cylinder_diameter**2)*SE)/4
    Vc = (math.pi/(4*(Compression_ratio-1)))*(Cylinder_diameter**2)*Piston_journey
    Dynamic_compression_ratio = (Ve+Vc)/Vc
    n_dynamic = (Temperature/(Temperature+20))*(Dynamic_compression_ratio/(Dynamic_compression_ratio-1))*(Cylinder_pressure/Intake_pressure)
    
    return n_dynamic
    
def Analysis(Temperature,Dynamic_compression_ratio,n,Intake_pressure,Volume,n_dynamic):

    n0 = (8.314/(19.806+0.002095*(Temperature+20)*(Dynamic_compression_ratio**(n-1)+1))+1)
    Compression_wattage = (Intake_pressure*Volume*n_dynamic*(Temperature+20)*((Volume**(n0-1))-1))/((n0-1)*Temperature)
    temperature_C = ((Temperature+20)-273)*Dynamic_compression_ratio**(n0-1)+273
    temperature_F = temperature_C-273
    compression_pressure = (((Intake_pressure*0.96)*10**5)*0.000145)*Dynamic_compression_ratio**n0
    
    return Compression_wattage,temperature_C,temperature_F,compression_pressure

def Minimum_pressure(Dynamic_compression_ratio):
    
    Minimum_pressure=14.7*Dynamic_compression_ratio + 14.7 +5
    
    return Minimum_pressure

def Pressure_discharge(Intake_pressure,Dynamic_compression_ratio,n):
    
    Pressure_discharge = (((Intake_pressure*0.96)*10**5)*0.000145)*Dynamic_compression_ratio**n
    
    return Pressure_discharge

def Minimum_pressure_intake(Intake_pressure):
    
    Minimum_pressure_intake=(((Intake_pressure*0.96)*10**5)*0.000145)
    
    return Minimum_pressure_intake