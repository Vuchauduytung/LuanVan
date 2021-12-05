% clc; clear all; close all
%duong ap suat
figure;
a = 0;
ii = 0;
i =0;
time_step = now;
period = 721;
fileID = fopen('data_off.json','a');
hLine = line(nan, nan, 'Color', 'blue');
fprintf(fileID, '[');
str = sprintf('{"xilanh":"off", "time":%f, "pmin":%f}', time_step, 18);
fprintf(fileID, str);
for a=0:period:Inf
    for ii=1:period
        X = get(hLine, 'XData');
        Y = get(hLine, 'YData');
        if mod(ii,2)==0
                apsuat = 20;
            else
                apsuat = 18;
        end
        x = [X ii];
        y = [Y apsuat];
        set(hLine, 'XData', x, 'YData', y);
        str = sprintf(', {"xilanh":"off", "time":%f, "pmin":%f}', time_step + 0.0007, apsuat);
        fprintf(fileID, str);
        pause(0.1);
    end
    pause(0.1);
end
fprintf(fileID, ']');
fclose(fileID);