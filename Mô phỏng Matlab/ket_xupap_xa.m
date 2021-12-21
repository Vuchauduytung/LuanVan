% c�ng thuc tinh
SE = (S*(1+cosd(A))/2)+L-sqrt((L^2)+((S*sind(A))^2)/4);
Ve = (pi*(D^2)*SE)/4;
Vc = (pi/(4*(u-1)))*(D^2)*S;
ed = (Ve+Vc)/Vc;
T = v+20;
n0 = (8.314/(19.806+0.002095*T*(ed^(p-1)+1))+1) ;
Vh1=(ed*Vc-Vc)/10^6;
nv=(v/(T))*(ed/(ed-1))*(Pa/Po);
Pc_1=((Pa*10^5)*0.000145)*ed^n0*0.7;
disp('Pc_1 loi = ')
disp(Pc_1);
Tc=T*ed^(n0-1)*0.7;
Tz=(Tc-273);
disp(Tc)
%ki nap
mS=zeros(1,721);
uk=S;
%ki nap
for k=1:270
    mS(k)=uk;
    uk=uk-(S/270);
end
%k� nen
bn=0;
for k=271:360
    mS(k)=bn;
    bn=bn+(S/90);
end
%ki gian no
r=S;
for k=361:450
    mS(k)=r;
    r=r-(S/90);
end
%ki xa
uk =0;
for k=451:721
    mS(k)=uk;
    uk=uk+(S/270);
end
%truong hop 1
pmin_1 = zeros(1,721);
T_value_1 =zeros(1,721);
for k = 1:19;
        SE1 = ((1*(1+cosd(A))/2)+L-sqrt((L^2)+((1*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin_1(k)=((Pa*10^5)*0.000145)*ed1^n01;
        T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc_1)))+273;
end
for k = 20:47;
         SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
         Ve1 = (pi*(D^2)*SE1)/4;
         Vc1 = (pi/(4*(u-1)))*(D^2)*S;
         ed1 = (Ve1+Vc1)/Vc1;
         n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
    if k < 22000;
         P_min=((Pa*10^5)*0.000145)*ed1^n01;
         pmin_1(k) = pmin_1(19);
    else
        pmin_1(k)=pmin_1(20)-P_min+((Pa*10^5)*0.000145)*ed1^n01;
    end
    T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc_1)))+273;
end
for k = 48:180;
        SE1 = ((1*(1+cosd(A))/2)+L-sqrt((L^2)+((1*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin_1(k)=((Pn*10^5)*0.000145)*ed1^n01;
        T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc_1)))+273;
end
for k = 181:270;
        pmin_1(k)=((Pn*10^5)*0.000145)*ed1^n01 + pmin_1(20)*(k-180)/45;
        T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc_1)))+273;
end
for k = 271:360;
        SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin_1(k)=((Pa*10^5)*0.000145)*ed1^n01*0.7;
        T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc_1)))+273;
end
for k = 361:450;
        SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin_1(k)=(((Pa*10^5)*0.000145)*ed1^n01*0.7);
        T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc_1)))+273;
end
for k = 451:539;
        pmin_1(k)=(((Pa*10^5)*0.000145)*ed1^n01-pmin_1(450)*(k-450)/26)*0.8;
        T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc_1)))+273;
end
for k = 540:580;
     if k <= 541;
         SE1 = ((mS(k)*(1+cosd(0))/2)+L-sqrt((L^2)+((mS(k)*sind(0))^2)/4));
         Ve1 = (pi*(D^2)*SE1)/4;
         Vc1 = (pi/(4*(u-1)))*(D^2)*S;
         ed1 = (Ve1+Vc1)/Vc1;
         n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
         P_min=pmin_1(451)-pmin_1(451)*(k-451)/60-((Pa*10^5)*0.000145)*ed1^n01;
         pmin_1(k) = pmin_1(539)-pmin_1(539)*(k-539)/5;
     else
        SE1 = ((mS(k)*(1+cosd((k-541)))/2)+L-sqrt((L^2)+((mS(k)*sind((k-541)))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
        pmin_1(k)=P_min+((Pa*10^5)*0.000145)*ed1^n01;
     end
     T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc)))+273;
end
for k = 581:721;
        SE1 = ((0*(1+cosd(0))/2)+L-sqrt((L^2)+((0*sind(0))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
    if k <= 671000;
        pmin_1(k)=pmin_1(k-310)*0.9;
    else
        pmin_1(k)=((Pa*10^5)*0.000145)*ed1^n01;
    end
    T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc_1)))+273;
end
for k = 1:721;
    if T_value_1(k) < T;
    T_value_1(k) = T;   
    else
    T_value_1(k) = T_value_1(k);
    end
end
hold on 
cla;
 plot(truc_khuyu,pmin,'-');
 plot(truc_khuyu,T_value,'-');
 plot(pmin_1,'--');
 plot(T_value_1,'--');
 legend ('Duong ap suat chuan','Duong nhiet do chuan','Duong ap suat loi','Duong nhiet do loi')