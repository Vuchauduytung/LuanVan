path_P_l = fullfile(pwd,'..','output','Program','simulate-input','data_P_xilanh_4.dat');
path_T_l = fullfile(pwd,'..','output','Program','simulate-input','data_T_xilanh_4.dat');
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