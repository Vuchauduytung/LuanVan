<<<<<<< HEAD:Matlab_simlulate/Lay_data_loi_xilanh_1.m
time = input('Thoi gian do: ');
for i=0:time
    pause(1);
end
path_P_l = fullfile(pwd,'..','output','Program','simulate-input','data_P_xilanh_1.dat');
path_T_l = fullfile(pwd,'..','output','Program','simulate-input','data_T_xilanh_1.dat');
=======
path_P_l = fullfile(pwd,'..','simulate-input','data_P_xilanh_1.dat');
path_T_l = fullfile(pwd,'..','simulate-input','data_T_xilanh_1.dat');
>>>>>>> a93e8137d591719a21b858b5e906395a0125dd84:build/Linux/dist/chuongtrinhchandoan/source/Matlab_simlulate/Lay_data_loi_xilanh_1.m
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
% ve do thi
figure;
time_step = time*2;
time_line= zeros(1,time_step*period);
pre = zeros(1,time_step*period);
T_line = zeros(1,time_step*period);
 for a=1:period:time_step*period;
     for ii=1:period;
         time_line (ii+a)=((ii+a)/period)/2;
         pre (ii+a)= pmin_1(ii);
         T_line (ii+a)= T_value_1(ii);
     end
     pause(0.1);
 end
axis([0  max(time_line)  (min(pmin_1)-20)  (max(pmin_1)+50)]);
grid on;
box on;
hold on
plot(time_line,pre,'-');
legend ('Duong ap suat')
xlabel('Thoi gian (s)');
ylabel('P (psi)');
title('Do thi ap suat');