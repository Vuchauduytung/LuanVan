clear;
clc;
%ve do thi quan he e va n
%khai báo tat ca các bien su dung
syms a b c x y k n m i p q f g n1 m1 name z u v po S D Vh A L W Po Pa SE ed Ve Vc T n0 Lc gct M1 w  pc pmin Tc Pc nb
% khai bao mang nhiet do T
x = zeros(1,110);
c=290;
for k=1:110 
    x(k) = c ;
    c=c+1;
end
% khai báo mang ti so nén
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
%khai báo và tìm giá tri n
b=zeros(110,181);
nb=1;
for k=1:110
    for i=1:181
        for u=1:1000
m =8.314/(19.806+0.002095*x(k)*(y(i)^(nb-1)+1))+1;
nb=m;
        end
b(k,i)=m;
    end
end
    hold on
  plot(y,b);
  grid on;
  box on;
  xlabel('Ty so nen e');
  ylabel('n');
  title('Do thi quan he giua ty so nen và n');
 for i=1:10:110
         name=num2str(x(i));
         text(y(181),b(i,181),name);
 end
 hold off
%xac dinh
% khai báo giá tri
v = input('nhiet do To: '); %Nhiet do on dinh trong 3s 97*C
u = input('ty so nen cua dong co: '); %9.1
S = input('Hanh trinh piston: '); %76
D = input('Duong kinh xylanh: '); %75
L = input('Chieu dai thanh truyen: '); %133
A = input('Goc IVC: '); %40
A_1 = 20;
Po = 1; % Ap suat khi quyen
Pa = Po*0.96; % gioi han tren la ap suat khi quyen
Pn = -0.96*Po; % gioi han duoi la ap suat chan khong
% truy bat diem
if v>290
    for i = 1:110
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
% công thuc tinh
SE = (S*(1+cosd(A))/2)+L-sqrt((L^2)+((S*sind(A))^2)/4);
Ve = (pi*(D^2)*SE)/4;
Vc = (pi/(4*(u-1)))*(D^2)*S;
ed = (Ve+Vc)/Vc;
disp('ed= ');
disp(ed);
T = v+20;
n0 = (8.314/(19.806+0.002095*T*(ed^(p-1)+1))+1) ;
Vh1=((pi/4)*(D^2)*S)/10^9;
nv=(v/(T))*(ed/(ed-1))*(Pa/Po);
disp('n= ');
disp(n0) 
Lc = -(Po*10^2*Vh1*nv*T*((ed^(n0-1))-1))/((n0-1)*v);
Tc=T*ed^(n0-1);
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
mS=zeros(1,721000);
uk=S;
%ki nap
for k=1:270999
    mS(k)=uk;
    uk=uk-(S/270000);
end
%kì nen
bn=0;
for k=271000:360999
    mS(k)=bn;
    bn=bn+(S/90000);
end
%ki gian no
r=S;
for k=361000:4509999
    mS(k)=r;
    r=r-(S/90000);
end
%ki xa
uk =0;
for k=451000:721000
    mS(k)=uk;
    uk=uk+(S/270000);
end
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
T_value =zeros(1,721000);
pmin = zeros(1,721000);
truc_khuyu =zeros(1,721000);
for k = 1:19999;
        SE1 = ((0*(1+cosd(A))/2)+L-sqrt((L^2)+((0*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
        T_value(k)=(Tz*((abs(pmin(k))/Pc)))+273;
end
for k = 20000:47999;
    if k == 20000;
         SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
         Ve1 = (pi*(D^2)*SE1)/4;
         Vc1 = (pi/(4*(u-1)))*(D^2)*S;
         ed1 = (Ve1+Vc1)/Vc1;
         n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
         P_min=((Pa*10^5)*0.000145)*ed1^n01;
         pmin(k) = pmin(19999);
     else
        SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
        pmin(k)=pmin(20000)-P_min+((Pa*10^5)*0.000145)*ed1^n01;
    end
    T_value(k)=(Tz*((abs(pmin(k))/Pc)))+273;
end
for k = 48000:180999;
        SE1 = ((0*(1+cosd(A))/2)+L-sqrt((L^2)+((0*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pn*10^5)*0.000145)*ed1^n01;
        T_value(k)=(Tz*((abs(pmin(k))/Pc)))+273;
end
for k = 181000:270999;
        pmin(k)=((Pn*10^5)*0.000145)*ed1^n01 + pmin(20000)*(k-181000)/45000 ;
        T_value(k)=(Tz*((abs(pmin(k))/Pc)))+273;
end
for k = 271000:360999;
        SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
        T_value(k)=(Tz*((abs(pmin(k))/Pc)))+273;
end
for k = 361000:450999;
        SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
        T_value(k)=(Tz*((abs(pmin(k))/Pc)))+273;
end
for k = 451000:539999;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01-pmin(450000)*(k-450000)/50000;
        T_value(k)=(Tz*((abs(pmin(k))/Pc)))+273;
end
for k = 540000:580999;
     if k <= 541999;
         SE1 = ((mS(k)*(1+cosd(A))/2)+L-sqrt((L^2)+((mS(k)*sind(A))^2)/4));
         Ve1 = (pi*(D^2)*SE1)/4;
         Vc1 = (pi/(4*(u-1)))*(D^2)*S;
         ed1 = (Ve1+Vc1)/Vc1;
         n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
         P_min=pmin(451000)-pmin(451000)*(k-451000)/38000-((Pa*10^5)*0.000145)*ed1^n01;
         pmin(k) = pmin(539999)-pmin(539999)*(k-539999)/5000;
     else
        SE1 = ((mS(k)*(1+cosd((k-541000)/1000))/2)+L-sqrt((L^2)+((mS(k)*sind((k-541000)/1000))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
        pmin(k)=P_min+((Pa*10^5)*0.000145)*ed1^n01;
     end
     T_value(k)=(Tz*((abs(pmin(k))/Pc)))+273;
end
for k = 581000:721000;
        SE1 = ((0*(1+cosd(A))/2)+L-sqrt((L^2)+((0*sind(A))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
        T_value(k)=(Tz*((abs(pmin(k))/Pc)))+273;
end
for k = 1:721000;
    if T_value(k) < T;
    T_value(k) = T;   
    else
    T_value(k) = T_value(k);
    end
end
axis on
for k = 1:721000;
    truc_khuyu (k) =k*0.001;
end
% khai bao mang nhiet do T
x1 = zeros(1,23);
c = 290;
for k = 1:110
    x1(k) = c ;
    c = c+1;
end
Vh1 = zeros(1,181);
for i=1:181
    Vh1(i)=(y(i)*Vc-Vc)/10^6;
end
nv = zeros(1,181);
for i = 1:181
nv(i)=(v/(T))*(y(i)/(y(i)-1))*(Pa/Po);
end
Lac = zeros(2,181);
n2=0;
for i = 1:110
        if T == x1(i)
           n2 = i;
        end
end
for k = 1:181
    Lac(1,k) = (Po*Vh1(k)*nv(k)*T*((Vh1(k)^(b(n2,k)-1))-1))/((b(n2,k)-1)*v);
    Lac(2,k) = -(Po*Vh1(k)*(nv(k)/y(k))*T*((y(k)^(b(n2,k)-1))-1))/((b(n2,k)-1)*v)-0.12;
end
%do thi cong nen Lac
figure;
plot(Vh1,Lac);
xlabel('The tich Vh');
ylabel('Cong nen Lac');
title('Do thi cong nen Lac');
%duong ap suat
 figure;
 axis([0    max(truc_khuyu)   min(pmin)-150     max(T_value)+150]);
 hold on
 plot(truc_khuyu,pmin,'-');
 plot(truc_khuyu,T_value,'-');
 grid on;
 box on;
 legend ('Duong ap suat chuan','Duong nhiet do chuan')
 xlabel('Chu trinh');
 ylabel('P (psi) va Nhiet do (K)');
 title('Do thi ');