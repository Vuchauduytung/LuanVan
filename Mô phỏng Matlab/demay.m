% clc; clear all; close all
%ve do thi quan he e va n
%clc;
%khai b�o tat ca c�c bien su dung
close all;
syms a b c x y k n m i p q f g n1 m1 name z u v po S D Vh A L W Po Pa SE ed Ve Vc T n0 Lc gct M1 w  pc pmin Tc Pc nb
% khai bao mang nhiet do T
x = zeros(1,23);
c=290;
for k=1:23 
    x(k) = c ;
    c=c+10;
end
% khai b�o mang ti so n�n
y=zeros(1,181);
a=1.5;
for i=1:181
y(i) = a;
a = a + 0.1;
end
% mang ti so nen tuong duong de truy bat diem
s=zeros(1,181);
w=15;
for i=1:181
s(i) = w;
w = w + 1;
end
%khai b�o v� t�m gi� tri n
b=zeros(23,181);
nb=1;
for k=1:23
    for i=1:181
        for u=1:1000
m =8.314/(19.806+0.002095*x(k)*(y(i)^(nb-1)+1))+1;
nb=m;
        end
b(k,i)=m;
    end
end
% ve do thi
for i=1:2:23
        name=num2str(x(i));
        text(y(181),b(i,181),name);
end
%xac dinh
% khai b�o gi� tri
v = input('nhiet do To: '); %300
u = input('ty so nen cua dong co: '); %9.1
S = input('Hanh trinh piston: '); %75
D = input('Duong kinh xylanh: '); %76
Vh = input('Dung tich xylanh: '); %1343
A = input('Goc dong muon xuppap: '); %40
L = input('Chieu dai thanh truyen: '); %133
W = input('cong suat cuc dai: '); %68.4
Po = input('Ap suat khi nap: '); %1
Pa = Po*0.96;
Pa = Po*0.96;
% truy bat diem
if v>290
    for i = 1:23
        if v == x(i)
        n1 = i;
        end
    end
   for k=1:181
       if (u*10)==s(k)
        q=(s(k)/10);
        m1=k;
       end
   end
   p=b(n1,m1);
   text(q,p,'*');
% c�ng thuc tinh
SE = (S*(1+cosd(A))/2)+L-sqrt((L^2)-((S*sind(A))^2)/4);
Ve = (pi*(D^2)*SE)/4;
Vc = (pi/(4*(u-1)))*(D^2)*S;
ed = (Ve+Vc)/Vc;
disp(ed)
T = v+20;
n0 = (8.314/(19.806+0.002095*T*(ed^(p-1)+1))+1) ;
Vh1=(ed*Vc-Vc)/10^6;
nv=(v/(T))*(ed/(ed-1))*(Pa/Po);
disp('n= ');
disp(n0) 
Lc = (Po*Vh1*nv*T*((Vh1^(n0-1))-1))/((n0-1)*v);
Tc=(T-273)*ed^(n0-1)+273;
Tz=Tc-273;
Pc=((Pa*10^5)*0.000145)*ed^n0;
disp('Ap suat truoc xuppap: Pa= ')
disp(Pa);
disp('Lc = ')
disp(Lc*1000);
disp('Tc = ')
disp(Tc);
disp(Tz);
disp('Pc = ')
disp(Pc);
else 
    disp('khong co gia tri')
end
%do thi ap suat 
syms pca
mS=zeros(1,721);
r=S;
%ki nap
for k=1:180
    mS(k)=r;
    r=r-(S/180);
end
%k� nen
uk=0;
for k=181:360
    mS(k)=uk;
    uk=uk+(S/180);
end
%ki gian no
for k=361:540
    mS(k)=uk;
    uk=uk-(S/180);
end
%ki xa
bn=0;
for k=541:721
    mS(k)=bn;
    bn=bn+(S/180);
end
%goc quay truc khuyu
ksm=zeros(1,721);
m=0;
for k=1:721
    ksm(k)=m;
    m=m+1;
end
%goc dong mo xuppap
do=zeros(1,(2*A+1));
tm=0;
for k=1:A
    do(k)=tm;
    tm=tm+1;
end
for k=A+1:(2*A)
    do(k)=tm;
    tm=tm-1;
end
%xac dinh
T = v+20;
pmin = zeros(1,721);
for k = 1:18;
        SE1 = ((mS(k+164)*(1+cosd(do(k+40)))/2)+L-sqrt((L^2)-((mS(k+360)*sind(do(k+40)))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=(((Pa*10^5)*0.000145)*ed1^n01);
end
for k = 19:180;
        SE1 = ((mS(181)/2*(1+cosd(0))/2)+L-sqrt((L^2)-((mS(181)/2*sind(0))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
end
for k = 181:220; 
        SE1 = ((mS(k)*(1+cosd(do(k-165)))/2)+L-sqrt((L^2)-((mS(k)*sind(do(k-165)))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
end
for k = 221:270; 
        SE1 = ((mS(k)*(1+cosd(0))/2)+L-sqrt((L^2)-((mS(k)*sind(0))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
end
for k = 271:360;
    if (321<=k)&&(k<=360)
        SE1 = ((mS(k)*(1+cosd(do(k-320)))/2)+L-sqrt((L^2)-((mS(k)*sind(do(k-320)))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
    else
        SE1 = ((mS(k)*(1+cosd(0))/2)+L-sqrt((L^2)-((mS(k)*sind(0))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
    end
end
for k = 361:540;
    if (361<=k)&&(k<=401)
        SE1 = ((mS(k)*(1+cosd(do(k-320)))/2)+L-sqrt((L^2)-((mS(k)*sind(do(k-320)))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
    else
        SE1 = ((mS(k)*(1+cosd(0))/2)+L-sqrt((L^2)-((mS(k)*sind(0))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
    end
end
for k = 541:721;
       if (541<=k)&&(k<=561)&&(pmin(k)<=30)
        SE1 = ((mS(k)*(1+cosd(do(k-500)))/2)+L-sqrt((L^2)-((mS(k)*sind(do(k-500)))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=(((Pa*10^5)*0.000145)*ed1^n01);
       else
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
        end
end
%duong ap suat
disp('Exit Ctrl + C');
figure;
a = 0;
ii = 0;
period = length(pmin);
fileID = fopen('F:\HK211\Luận Văn\data\data_P.json','w');
fprintf(fileID, '{ "Data"');
fprintf(fileID, ':');
fprintf(fileID, '[');
time_step = (1/length(pmin))*1/2;
str = sprintf('{"xilanh":1, "time":%f, "pmin":%f}', 0, pmin(1));
fprintf(fileID, str);
time = input('thoi gian do :');
time = time*2;
time_time = 0;
for a=1:period:time*period
    for ii=1:period
        plot(((ii+a)/period)/2 , pmin(ii), 'b.', 'MarkerSize', 10);
        hold on;
        str = sprintf(', {"xilanh":1, "time":%f, "pmin":%f}', time_time, pmin(ii));
        time_time = time_time +time_step;
        fprintf(fileID, str);
    end
    pause(0.1);
end
fprintf(fileID, ']');
fprintf(fileID, '}')
fclose(fileID);

% save dat
data_pmin = randn (721,1);
period = length(pmin);
time_step = 0.0007;
time = now;
for ii=1:period
        
        data_pmin (ii,1) = pmin(ii);
        
        time = time + time_step;
end
dlmwrite('F:\HK211\Lu?n V?n\data\data.dat', data_pmin);
