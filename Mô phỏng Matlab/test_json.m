fileID = fopen('text.txt','w');
fprintf(fileID, '[');
str = sprintf('{"xilanh":1, "time":%f, "pmin":%f}', now, pmin(1));
fprintf(fileID, str);
for ii=2:length(pmin)
    str = sprintf(', {"xilanh":1, "time":%f, "pmin":%f}', now, pmin(ii));
    fprintf(fileID, str);
end
fprintf(fileID, ']');
fclose(fileID);