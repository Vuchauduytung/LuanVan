disp('Exit Ctrl + C');
mS=zeros(1,721);
uk=S;
%ki nap
for k=1:270
    mS(k)=uk;
    uk=uk-(S/270);
end
%kì nen
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
        SE1 = ((0*(1+cosd(A))/2)+L-sqrt((L^2)+((0*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin_1(k)=((Pa*10^5)*0.000145)*ed1^n01;
        T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc)))+273;
end
for k = 20:47;
    if k == 20;
         SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
         Ve1 = (pi*(D^2)*SE1)/4;
         Vc1 = (pi/(4*(u-1)))*(D^2)*S;
         ed1 = (Ve1+Vc1)/Vc1;
         n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
         P_min=((Pa*10^5)*0.000145)*ed1^n01;
         pmin_1(k) = pmin_1(19);
     else
        SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
        pmin_1(k)=pmin_1(20)-P_min+((Pa*10^5)*0.000145)*ed1^n01;
    end
    T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc)))+273;
end
for k = 48:180;
        SE1 = ((0*(1+cosd(A))/2)+L-sqrt((L^2)+((0*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin_1(k)=((Pn*10^5)*0.000145)*ed1^n01;
        T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc)))+273;
end
for k = 181:270;
        pmin_1(k)=((Pn*10^5)*0.000145)*ed1^n01 + pmin_1(20)*(k-181)/45 ;
        T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc)))+273;
end
for k = 271:360;
        SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin_1(k)=((Pa*10^5)*0.000145)*ed1^n01;
        T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc)))+273;
end
for k = 361:450;
        SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin_1(k)=((Pa*10^5)*0.000145)*ed1^n01;
        T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc)))+273;
end
for k = 451:539;
        pmin_1(k)=((Pa*10^5)*0.000145)*ed1^n01-pmin_1(450)*(k-450)/50;
        T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc)))+273;
end
for k = 540:580;
     if k == 540;
         SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
         Ve1 = (pi*(D^2)*SE1)/4;
         Vc1 = (pi/(4*(u-1)))*(D^2)*S;
         ed1 = (Ve1+Vc1)/Vc1;
         n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
         P_min=pmin_1(540)-((Pa*10^5)*0.000145)*ed1^n01-20.5;
         pmin_1(k) = pmin_1(539)-pmin_1(539)*(k-539)/45;
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
        SE1 = ((0*(1+cosd(A))/2)+L-sqrt((L^2)+((0*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin_1(k)=((Pa*10^5)*0.000145)*ed1^n01;
        T_value_1(k)=(Tz*((abs(pmin_1(k))/Pc)))+273;
end
for k = 1:721;
    if T_value_1(k) < T;
    T_value_1(k) = T;   
    else
    T_value_1(k) = T_value_1(k);
    end
end
% Ve do thi
figure;
a = 0;
ii = 0;
axis on
period = length(pmin_1);
time = input('thoi gian do xylanh: ');
time_step = time*2;

 for a=1:period:time_step*period;
     for ii=1:period;
         plot(((ii+a)/period)/2 , pmin_1(ii), 'b.', 'MarkerSize', 10);
         hold on
     end
     pause(0.1);
 end
 axis([0  max(((ii+a)/period)/2)  (min(pmin)-20)  (max(pmin)+50)]);
 
% lay gia tri
data_pmin = randn (721,1);
period = length(pmin_1);
for ii=1:period
        data_pmin (ii,1) = pmin_1(ii);
end
dlmwrite('data\data_P.dat', data_pmin);
data_T = randn (721,1);

period = length(T_value_1);
for ii=1:period
        
        data_T (ii,1) = T_value_1(ii);
        
end
dlmwrite('data\data_T.dat', data_T);
