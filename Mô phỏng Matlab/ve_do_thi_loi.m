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
 axis([0  max(((ii+a)/period)/2)  (min(pmin_1)-20)  (max(pmin_1)+50)]);
 
% lay gia tri
data_pmin = randn (721,1);
period = length(pmin_1);
for ii=1:period
        data_pmin (ii,1) = pmin_1(ii);
end
dlmwrite('data\data_P_l.dat', data_pmin);
data_T = randn (721,1);

period = length(T_value_1);
for ii=1:period
        
        data_T (ii,1) = T_value_1(ii);
        
end
dlmwrite('data\T_value_l.dat', data_T);