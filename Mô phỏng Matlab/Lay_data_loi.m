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

%duong ap suat xylanh 1
disp('Exit Ctrl + C');
time = input('thoi gian do xylanh: ');
time = time*2;
a = 0;
ii = 0;
period = length(pmin_1);
fileID_1 = fopen('data\data_P_xylanh1.json','w');
fprintf(fileID_1, '{ "Data"');
fprintf(fileID_1, ':');
fprintf(fileID_1, '[');
time_step = (1/length(pmin_1))*1/2;
str = sprintf('{"xilanh":1, "time":%f, "pmin_1":%f}', 0, pmin_1(1));
fprintf(fileID_1, str);

time_time = 0;
for a=1:period:time*period
    for ii=1:period
        plot(((ii+a)/period)/2 , pmin_1(ii), 'b.', 'MarkerSize', 10);
        hold on;
        str = sprintf(', {"xilanh":1, "time":%f, "pmin_1":%f}', time_time, pmin_1(ii));
        time_time = time_time +time_step;
        fprintf(fileID_1, str);
    end
    pause(0.1);
end
fprintf(fileID_1, '] }');
fclose(fileID_1);

%xylanh2
fileID_2 = fopen('data\data_P_xylanh2.json','w');
fprintf(fileID_2, '{ "Data"');
fprintf(fileID_2, ':');
fprintf(fileID_2, '[');
time_step = (1/length(pmin_1))*1/2;
str = sprintf('{"xilanh":1, "time":%f, "pmin_1":%f}', 0, pmin_1(1));
fprintf(fileID_2, str);

time_time = 0;
for a=1:period:time*period
    for ii=1:period
        str = sprintf(', {"xilanh":1, "time":%f, "pmin_1":%f}', time_time, pmin_1(ii));
        time_time = time_time +time_step;
        fprintf(fileID_2, str);
    end
    pause(0.1);
end
fprintf(fileID_2, '] }');
fclose(fileID_2);

%xylanh3
fileID_3 = fopen('data\data_P_xylanh3.json','w');
fprintf(fileID_3, '{ "Data"');
fprintf(fileID_3, ':');
fprintf(fileID_3, '[');
time_step = (1/length(pmin_1))*1/2;
str = sprintf('{"xilanh":1, "time":%f, "pmin_1":%f}', 0, pmin_1(1));
fprintf(fileID_3, str);

time_time = 0;
for a=1:period:time*period
    for ii=1:period
        str = sprintf(', {"xilanh":1, "time":%f, "pmin_1":%f}', time_time, pmin_1(ii));
        time_time = time_time +time_step;
        fprintf(fileID_3, str);
    end
    pause(0.1);
end
fprintf(fileID_3, '] }');
fclose(fileID_3);

%xylanh4
fileID_4 = fopen('data\data_P_xylanh4.json','w');
fprintf(fileID_4, '{ "Data"');
fprintf(fileID_4, ':');
fprintf(fileID_4, '[');
time_step = (1/length(pmin_1))*1/2;
str = sprintf('{"xilanh":1, "time":%f, "pmin_1":%f}', 0, pmin_1(1));
fprintf(fileID_4, str);

time_time = 0;
for a=1:period:time*period
    for ii=1:period
        str = sprintf(', {"xilanh":1, "time":%f, "pmin_1":%f}', time_time, pmin_1(ii));
        time_time = time_time +time_step;
        fprintf(fileID_4, str);
    end
    pause(0.1);
end
fprintf(fileID_4, '] }');
fclose(fileID_4);
