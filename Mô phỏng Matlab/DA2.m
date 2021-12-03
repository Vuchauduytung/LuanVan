%ve do thi quan he e va n
%clc;
%khai báo tat ca các bien su dung
syms a b c x y k n m i p q f g n1 m1 name z u v po S D Vh A L W Po Pa SE ed Ve Vc T n0 Lc gct M1 w  pc pmin Tc Pc nb
% khai bao mang nhiet do T
x = zeros(1,23);
c=290;
for k=1:23 
    x(k) = c ;
    c=c+10;
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
%plot(y,b);
%grid on;
%box on;
%xlabel('Ty so nen e');
%ylabel('n');
%title('Do thi quan he giua ty so nen và n');
for i=1:2:23
        name=num2str(x(i));
        text(y(181),b(i,181),name);
end
%xac dinh
% khai báo giá tri
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
% công thuc tinh
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
%ki gian no
for k=1:180
    mS(k)=r;
    r=r-(S/180);
end
%ki xa
uk=0;
for k=181:360
    mS(k)=uk;
    uk=uk+(S/180);
end
%ki nap
for k=361:540
    mS(k)=uk;
    uk=uk-(S/180);
end
%kì nen
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
for k = 1:180;
    if (1<=k)&&(k<=41)
        SE1 = ((mS(k)*(1+cosd(do(k+40)))/2)+L-sqrt((L^2)-((mS(k)*sind(do(k+40)))^2)/4));
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
for k = 181:360;
       if (181<=k)&&(k<=201)&&(pmin(k)<=30)
        SE1 = ((mS(k)*(1+cosd(do(k-140)))/2)+L-sqrt((L^2)-((mS(k)*sind(do(k-140)))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=(((Pa*10^5)*0.000145)*ed1^n01);
       else
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
        end
end
for k = 361:378;
        SE1 = ((mS(k-196)*(1+cosd(do(k-320)))/2)+L-sqrt((L^2)-((mS(k)*sind(do(k-320)))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=(((Pa*10^5)*0.000145)*ed1^n01);
end
for k = 379:540;
        SE1 = ((mS(181)/2*(1+cosd(0))/2)+L-sqrt((L^2)-((mS(181)/2*sind(0))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
end
for k = 541:580; 
        SE1 = ((mS(k)*(1+cosd(do(k-525)))/2)+L-sqrt((L^2)-((mS(k)*sind(do(k-525)))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
end
for k = 581:630; 
        SE1 = ((mS(k)*(1+cosd(0))/2)+L-sqrt((L^2)-((mS(k)*sind(0))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
end
for k = 631:721;
    if (681<=k)&&(k<=721)
        SE1 = ((mS(k)*(1+cosd(do(k-680)))/2)+L-sqrt((L^2)-((mS(k)*sind(do(k-680)))^2)/4));
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
%duong ap suat
%subplot(2,2,3);
plot(pmin);
xlabel('Chu trinh');
ylabel('P (psi)');
title('Do thi ap suat chu trinh');  
% do thi cong nen Lac
% khai bao mang nhiet do T
x1 = zeros(1,23);
c = 290;
for k = 1:23
    x1(k) = c ;
    c = c+10;
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
for i = 1:23
        if T == x1(i)
           n2 = i;
        end
end
for k = 1:181
    Lac(1,k) = (Po*Vh1(k)*nv(k)*T*((Vh1(k)^(b(n2,k)-1))-1))/((b(n2,k)-1)*v);
    Lac(2,k) = -(Po*Vh1(k)*(nv(k)/y(k))*T*((y(k)^(b(n2,k)-1))-1))/((b(n2,k)-1)*v)-0.12;
end
%do thi cong nen Lac
%subplot(2,2,4)
%plot(Vh1,Lac);
%xlabel('The tich Vh');
%ylabel('Cong nen Lac');
%title('Do thi cong nen Lac');
