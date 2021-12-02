% Test serial port

s = serial('COM2','BaudRate',9600,'Terminator','CR');  
fopen(s)  
fprintf(s,'Embedded Laboratory Serial Communication Tutorial');  
% msg = fgets(s);  %get data from serial port  
s.BytesAvailableFcn = @Serial_int_Fcn;
while 1 
end
fclose(s)
delete(s)

function Serial_int_Fcn (hObject, eventdata)
    disp("Receive message");
end