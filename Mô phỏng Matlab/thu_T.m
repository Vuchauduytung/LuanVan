%ve do thi quan he e va n
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
subplot(2,1,1);
plot(y,b);
grid on;
box on;
xlabel('Ty so nen e');
ylabel('n');
title('Do thi quan he giua ty so nen và n');
for i=1:2:23
        name=num2str(x(i));
        text(y(181),b(i,181),name);
end
%xac dinh
% khai báo giá tri
v = 370; %Nhiet do on dinh trong 3s 97*C
c = input('Gioi han tren nhiet do: ');
l = input('Gioi han duoi nhiet do: ');
u = input('ty so nen cua dong co: '); %9.1
S = input('Hanh trinh piston: '); %75
D = input('Duong kinh xylanh: '); %76
L = input('Chieu dai thanh truyen: '); %133
A = input('Goc xuppap xa: '); %40
A_1 = 20;
Po = 1; % Ap suat khi quyen
Pa = Po*0.96; % gioi han tren la ap suat khi quyen
Pn = -0.96*Po; % gioi han duoi la ap suat chan khong
%goc quay truc khuyu
ksm=zeros(1,721);
m=0;
for k=1:721
    ksm(k)=m;
    m=m+1;
end
j = 0;
pmin = zeros((l-c)/10,721);
for v = c:10:l;
    j =j+1;
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
    disp('ed= ');
    disp(ed);
    SE = (S*(1+cosd(0))/2)+L-sqrt((L^2)-((S*sind(0))^2)/4);
    Ve = (pi*(D^2)*SE)/4;
    Vc = (pi/(4*(u-1)))*(D^2)*S;
    ed = (Ve+Vc)/Vc;
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
    disp('Lc = ')
    disp(Lc*1000);
    disp('Pc = ')
    disp(Pc);
    else 
        disp('khong co gia tri')
    end
    %do thi ap suat 
    syms pca
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
    %xac dinh
    for k = 1:19;
            SE1 = ((0*(1+cosd(0))/2)+L-sqrt((L^2)-((0*sind(0))^2)/4));
            Ve1 = (pi*(D^2)*SE1)/4;
            Vc1 = (pi/(4*(u-1)))*(D^2)*S;
            ed1 = (Ve1+Vc1)/Vc1;
            n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
            pmin(j,k)=((Pa*10^5)*0.000145)*ed1^n01;
    end
    for k = 20:39;
        if k < 22;
             SE1 = ((mS(k)*(1+cosd(0))/2)+L-sqrt((L^2)-((mS(k)*sind(0))^2)/4));
             Ve1 = (pi*(D^2)*SE1)/4;
             Vc1 = (pi/(4*(u-1)))*(D^2)*S;
             ed1 = (Ve1+Vc1)/Vc1;
             n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
             P_min=((Pa*10^5)*0.000145)*ed1^n01;
             pmin(j,k) = pmin(j,19);
         else
            SE1 = ((mS(k)*(1+cosd(k-381))/2)+L-sqrt((L^2)-((mS(k)*sind(k-381))^2)/4));
            Ve1 = (pi*(D^2)*SE1)/4;
            Vc1 = (pi/(4*(u-1)))*(D^2)*S;
            ed1 = (Ve1+Vc1)/Vc1;
            n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
            pmin(j,k)=pmin(j,20)-P_min+((Pa*10^5)*0.000145)*ed1^n01;
        end
    end
    for k = 40:240;
            SE1 = ((0*(1+cosd(0))/2)+L-sqrt((L^2)-((0*sind(0))^2)/4));
            Ve1 = (pi*(D^2)*SE1)/4;
            Vc1 = (pi/(4*(u-1)))*(D^2)*S;
            ed1 = (Ve1+Vc1)/Vc1;
            n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
            pmin(j,k)=((Pn*10^5)*0.000145)*ed1^n01;
    end
    for k = 241:270;
            pmin(j,k)=((Pn*10^5)*0.000145)*ed1^n01 + pmin(j,20)*(k-240)/17 ;
    end
    for k = 271:360;
            SE1 = ((mS(k)*(1+cosd(0))/2)+L-sqrt((L^2)-((mS(k)*sind(0))^2)/4));
            Ve1 = (pi*(D^2)*SE1)/4;
            Vc1 = (pi/(4*(u-1)))*(D^2)*S;
            ed1 = (Ve1+Vc1)/Vc1;
            n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
            pmin(j,k)=((Pa*10^5)*0.000145)*ed1^n01;
    end
    for k = 361:450;
            SE1 = ((mS(k)*(1+cosd(0))/2)+L-sqrt((L^2)-((mS(k)*sind(0))^2)/4));
            Ve1 = (pi*(D^2)*SE1)/4;
            Vc1 = (pi/(4*(u-1)))*(D^2)*S;
            ed1 = (Ve1+Vc1)/Vc1;
            n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
            pmin(j,k)=((Pa*10^5)*0.000145)*ed1^n01;
    end
    for k = 451:499;
            pmin(j,k)=((Pa*10^5)*0.000145)*ed1^n01-pmin(j,450)*(k-450)/26;
    end
    for k = 500:540;
         if k == 500;
             SE1 = ((mS(k)*(1+cosd(0))/2)+L-sqrt((L^2)-((mS(k)*sind(0))^2)/4));
             Ve1 = (pi*(D^2)*SE1)/4;
             Vc1 = (pi/(4*(u-1)))*(D^2)*S;
             ed1 = (Ve1+Vc1)/Vc1;
             n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
             P_min=((Pa*10^5)*0.000145)*ed1^n01;
             pmin(j,k) = pmin(j,450)-pmin(j,450)*(k-450)/26;
         else
            SE1 = ((mS(k)*(1+cosd(k-500))/2)+L-sqrt((L^2)-((mS(k)*sind(k-500))^2)/4));
            Ve1 = (pi*(D^2)*SE1)/4;
            Vc1 = (pi/(4*(u-1)))*(D^2)*S;
            ed1 = (Ve1+Vc1)/Vc1;
            n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1);
            pmin(j,k)=pmin(j,500)-P_min+((Pa*10^5)*0.000145)*ed1^n01;
         end
    end
    for k = 541:721;
            SE1 = ((0*(1+cosd(0))/2)+L-sqrt((L^2)-((0*sind(0))^2)/4));
            Ve1 = (pi*(D^2)*SE1)/4;
            Vc1 = (pi/(4*(u-1)))*(D^2)*S;
            ed1 = (Ve1+Vc1)/Vc1;
            n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
            pmin(j,k)=((Pa*10^5)*0.000145)*ed1^n01;
    end
end
%duong ap suat
subplot(2,1,2);
hold on
plot(ksm,pmin);
xlabel('Chu trinh');
ylabel('P (psi)');
title('Do thi ap suat chu trinh');