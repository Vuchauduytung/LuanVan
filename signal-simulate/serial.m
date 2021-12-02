% Test serial port

s = serial('COM2','BaudRate',9600,'Terminator','CR');  
fopen(s)  
s.BytesAvailableFcn = @Serial_int_Fcn;
fprintf(s,'Embedded Laboratory Serial Communication Tutorial');  
msg = fgets(s);  %get data from serial port  
fclose(s)  
delete(s)

function Serial_int_Fcn (hObject, eventdata)
    disp("Message receive");
end