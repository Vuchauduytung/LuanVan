
%do thi ap suat 
syms pca
mS=zeros(1,721);
r=S*0.9;
%ki nap
for k=1:161
    mS(k)=r;
    r=r-(S/161);
end
for k=162:201
    mS(k)=r;
    r=r-(S/161);
end
%ki nen
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
%kì xa
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
for k = 1:161;
        SE1 = ((mS(181)/2*(1+cosd(0))/2)+L-sqrt((L^2)-((mS(181)/2*sind(0))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
end
for k = 162:201; 
        SE1 = ((mS(k)*(1+cosd(do(k-146)))/2)+L-sqrt((L^2)-((mS(k)*sind(do(k-146)))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
end
for k = 202:251; 
        SE1 = ((mS(k)*(1+cosd(0))/2)+L-sqrt((L^2)-((mS(k)*sind(0))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
end
for k = 252:342;
    if (681<=k)&&(k<=721)
        SE1 = ((mS(k)*(1+cosd(do(k-301)))/2)+L-sqrt((L^2)-((mS(k)*sind(do(k-301)))^2)/4));
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
for k = 343:522;
    if (343<=k)&&(k<=384)
        SE1 = ((mS(k)*(1+cosd(do(k-302)))/2)+L-sqrt((L^2)-((mS(k)*sind(do(k-302)))^2)/4));
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
for k = 523:702;
       if (523<=k)&&(k<=543)&&(pmin(k)<=30)
        SE1 = ((mS(k)*(1+cosd(do(k-522)))/2)+L-sqrt((L^2)-((mS(k)*sind(do(k-522)))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=(((Pa*10^5)*0.000145)*ed1^n01);
       else
        pmin(k)=((Pa*10^5)*0.000145)*ed1^n01;
        end
end
for k = 702:721;
        SE1 = ((mS(k-537)*(1+cosd(do(k-661)))/2)+L-sqrt((L^2)-((mS(k)*sind(do(k-661)))^2)/4));
        Ve1 = (pi*(D^2)*SE1)/4;
        Vc1 = (pi/(4*(u-1)))*(D^2)*S;
        ed1 = (Ve1+Vc1)/Vc1;
        n01 = (8.314/(19.806+0.002095*T*(ed1^(p-1)+1))+1) ;
        pmin(k)=(((Pa*10^5)*0.000145)*ed1^n01);
end
%duong ap suat
subplot(2,2,3);
plot(pmin);
xlabel('Chu trinh');
ylabel('P (psi)');
title('Do thi ap suat chu trinh');  
% do thi cong nen Lac
