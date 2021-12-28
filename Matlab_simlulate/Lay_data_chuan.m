SE = (S*(1+cosd(A))/2)+L-sqrt((L^2)+((S*sind(A))^2)/4);
Ve = (pi*(D^2)*SE)/4;
Vc = (pi/(4*(u-1)))*(D^2)*S;
ed = (Ve+Vc)/Vc;
T = v+20;
n0 = (8.314/(19.806+0.002095*T*(ed^(p-1)+1))+1) ;
Vh1=(ed*Vc-Vc)/10^6;
nv=(v/(T))*(ed/(ed-1))*(Pa/Po);
Lc = (Po*Vh1*nv*T*((Vh1^(n0-1))-1))/((n0-1)*v);
Tc=T*ed^(n0-1);
Tz=Tc-273;
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
pmin_c = zeros(1,721);
T_value_c =zeros(1,721);
for k = 1:19;
        SE1 = ((0*(1+cosd(A))/2)+L-sqrt((L^2)+((0*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin_c(k)=((Pa*10^5)*0.000145)*ed1^n01;
        T_value_c(k)=(Tz*((abs(pmin_c(k))/Pc)))+273;
end
for k = 20:47;
    if k == 20;
         SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
         Ve1 = (pi*(D^2)*SE1)/4;
         Vc1 = (pi/(4*(u-1)))*(D^2)*S;
         ed1 = (Ve1+Vc1)/Vc1;
         n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
         P_min=((Pa*10^5)*0.000145)*ed1^n01;
         pmin_c(k) = pmin_c(19);
     else
        SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
        pmin_c(k)=pmin_c(20)-P_min+((Pa*10^5)*0.000145)*ed1^n01;
    end
    T_value_c(k)=(Tz*((abs(pmin_c(k))/Pc)))+273;
end
for k = 48:180;
        SE1 = ((0*(1+cosd(A))/2)+L-sqrt((L^2)+((0*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin_c(k)=((Pn*10^5)*0.000145)*ed1^n01;
        T_value_c(k)=(Tz*((abs(pmin_c(k))/Pc)))+273;
end
for k = 181:270;
        pmin_c(k)=((Pn*10^5)*0.000145)*ed1^n01 + pmin_c(20)*(k-181)/45 ;
        T_value_c(k)=(Tz*((abs(pmin_c(k))/Pc)))+273;
end
for k = 271:360;
        SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin_c(k)=((Pa*10^5)*0.000145)*ed1^n01;
        T_value_c(k)=(Tz*((abs(pmin_c(k))/Pc)))+273;
end
for k = 361:450;
        SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin_c(k)=((Pa*10^5)*0.000145)*ed1^n01;
        T_value_c(k)=(Tz*((abs(pmin_c(k))/Pc)))+273;
end
for k = 451:539;
        pmin_c(k)=((Pa*10^5)*0.000145)*ed1^n01-pmin_c(450)*(k-450)/50;
        T_value_c(k)=(Tz*((abs(pmin_c(k))/Pc)))+273;
end
for k = 540:580;
     if k == 540;
         SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
         Ve1 = (pi*(D^2)*SE1)/4;
         Vc1 = (pi/(4*(u-1)))*(D^2)*S;
         ed1 = (Ve1+Vc1)/Vc1;
         n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
         P_min=pmin_c(540)-((Pa*10^5)*0.000145)*ed1^n01-20.5;
         pmin_c(k) = pmin_c(539)-pmin_c(539)*(k-539)/45;
     else
        SE1 = ((mS(k)*(1+cosd((k-541)))/2)+L-sqrt((L^2)+((mS(k)*sind((k-541)))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
        pmin_c(k)=P_min+((Pa*10^5)*0.000145)*ed1^n01;
     end
     T_value_c(k)=(Tz*((abs(pmin_c(k))/Pc)))+273;
end
for k = 581:721;
        SE1 = ((0*(1+cosd(A))/2)+L-sqrt((L^2)+((0*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin_c(k)=((Pa*10^5)*0.000145)*ed1^n01;
        T_value_c(k)=(Tz*((abs(pmin_c(k))/Pc)))+273;
end
for k = 1:721;
    if T_value_c(k) < T;
    T_value_c(k) = T;   
    else
    T_value_c(k) = T_value_c(k);
    end
end
path_P_1 = fullfile(pwd,'..','output','Program','simulate-input','data_P_xilanh_1.dat');
path_T_1 = fullfile(pwd,'..','output','Program','simulate-input','data_T_xilanh_1.dat');
path_P_2 = fullfile(pwd,'..','output','Program','simulate-input','data_P_xilanh_2.dat');
path_T_2 = fullfile(pwd,'..','output','Program','simulate-input','data_T_xilanh_2.dat');
path_P_3 = fullfile(pwd,'..','output','Program','simulate-input','data_P_xilanh_3.dat');
path_T_3 = fullfile(pwd,'..','output','Program','simulate-input','data_T_xilanh_3.dat');
path_P_4 = fullfile(pwd,'..','output','Program','simulate-input','data_P_xilanh_4.dat');
path_T_4 = fullfile(pwd,'..','output','Program','simulate-input','data_T_xilanh_4.dat');
% lay gia tri
a = 0;
ii = 0;
data_pmin = randn (721,1);
period = length(pmin_c);
for ii=1:period
        data_pmin (ii,1) = pmin_c(ii);
end
dlmwrite(path_P_1, data_pmin);
for ii=1:period
        data_pmin (ii,1) = pmin_c(ii);
end
dlmwrite(path_P_2, data_pmin);

data_T = randn (721,1);
period = length(T_value_c);
for ii=1:period
        
        data_T (ii,1) = T_value_c(ii);
        
end
dlmwrite(path_T_1, data_T);
for ii=1:period
        
        data_T (ii,1) = T_value_c(ii);
        
end
dlmwrite(path_T_2, data_T);
% lay gia tri
data_pmin = randn (721,1);
period = length(pmin_c);
for ii=1:period
        data_pmin (ii,1) = pmin_c(ii);
end
dlmwrite(path_P_3, data_pmin);
for ii=1:period
        data_pmin (ii,1) = pmin_c(ii);
end
dlmwrite(path_P_4, data_pmin);

data_T = randn (721,1);
period = length(T_value_c);
for ii=1:period
        
        data_T (ii,1) = T_value_c(ii);
        
end
dlmwrite(path_T_3, data_T);
for ii=1:period
        
        data_T (ii,1) = T_value_c(ii);
        
end
dlmwrite(path_T_4, data_T);