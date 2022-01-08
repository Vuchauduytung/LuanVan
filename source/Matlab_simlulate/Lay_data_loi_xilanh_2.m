path_P_l = fullfile(pwd,'..','simulate-input','data_P_xilanh_2.dat');
path_T_l = fullfile(pwd,'..','simulate-input','data_T_xilanh_2.dat');
% lay gia tri
a = 0;
ii = 0;
data_pmin = randn (721,1);
period = length(pmin_1);
for ii=1:period
        data_pmin (ii,1) = pmin_1(ii);
end
dlmwrite(path_P_l, data_pmin);
data_T = randn (721,1);

period = length(T_value_1);
for ii=1:period
        
        data_T (ii,1) = T_value_1(ii);
        
end
dlmwrite(path_T_l, data_T);
% Ve do thi
time = input('Nhap thoi gian:');
time_step =time*2;
p_v = zeros(1,time_step*period);
d = zeros(1,time_step*period);
for a = 1:period:time_step*period
    for ii = 1:period
        d (ii+a) = (ii+a)/period/2;
        p_v (ii+a) = pmin_1(ii);
    end
end
figure;
 axis([0    max(d)   min(pmin_1)-20     max(pmin_1)+20]);
 hold on
 plot(d,p_v,'-');
 grid on;
 box on;
 legend ('Duong ap suat chuan')
 xlabel('Chu trinh');
 ylabel('P (psi)');
 title('Do thi ');
