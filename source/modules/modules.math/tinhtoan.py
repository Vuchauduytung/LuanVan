import math
def n(T,e):

    nb = 1
    i = 0

    while(i<1000):
        m = 8.314/(19.806+0.002095*T*(e**(nb-1)+1))+1
        nb = m
        i = i + 1
    return nb       

def ed(S,A,L,e,D,Po):
    Pa = Po*0.96
    SE = (S*(1 + math.cos((A*math.pi)/180))/2) + L - math.sqrt((L**2)-((S*math.sin((A*math.pi)/180))**2)/4)
    Ve = (math.pi*(D**2)*SE)/4
    Vc = (math.pi/(4*(e-1)))*(D**2)*S
    ed = (Ve+Vc)/Vc
    return ed

def thetich(S,A,L,e,D,Po,T):
    Pa = Po*0.96
    SE = (S*(1 + math.cos((A*math.pi)/180))/2) + L - math.sqrt((L**2)-((S*math.sin((A*math.pi)/180))**2)/4)
    Ve = (math.pi*(D**2)*SE)/4
    Vc = (math.pi/(4*(e-1)))*(D**2)*S
    ed = (Ve+Vc)/Vc
    Vh1 = (ed*Vc-Vc)/10**6
    nv = (T/(T+20))*(ed/(ed-1))*(Pa/Po)
    return Vh1

def nd(S,A,L,e,D,Po,T):
    Pa = Po*0.96
    SE = (S*(1 + math.cos((A*math.pi)/180))/2) + L - math.sqrt((L**2)-((S*math.sin((A*math.pi)/180))**2)/4)
    Ve = (math.pi*(D**2)*SE)/4
    Vc = (math.pi/(4*(e-1)))*(D**2)*S
    ed = (Ve+Vc)/Vc
    nv=(T/(T+20))*(ed/(ed-1))*(Pa/Po)
    return nv
def phantich(T,ed,n,Po,Vh,nd):

    n0 = (8.314/(19.806+0.002095*(T+20)*(ed**(n-1)+1))+1)
    Lc = (Po*Vh*nd*(T+20)*((Vh**(n0-1))-1))/((n0-1)*T)
    Tc = ((T+20)-273)*ed**(n0-1)+273
    Tz = Tc-273
    Pc=(((Po*0.96)*10**5)*0.000145)*ed**n0
    return Lc,Tc,Tz,Pc