disp('press Ctrl-C to exit');
i = 0;
t = 0;
hLine = line(nan, nan, 'Color', 'blue');
while 1
    axis([0  i+1  0  300]);
    if i<0.9;
        apsuat = 18;
        X = get(hLine, 'XData');
        Y = get(hLine, 'YData');
        x = [X i];
        y = [Y apsuat];
        set(hLine, 'XData', x, 'YData', y);
        i = i+1/length(pmin);
        pause(0.01);
        apsuat = 20;
        X = get(hLine, 'XData');
        Y = get(hLine, 'YData');
        x = [X i];
        y = [Y apsuat];
        set(hLine, 'XData', x, 'YData', y);
        i = i+1/length(pmin);
        pause(0.01);
    else i > 0.9;
        for ii=1:i
            for jj=1:length(pmin)
                X = get(hLine, 'XData');
                Y = get(hLine, 'YData');
                m = ii+jj/length(pmin);
                x = [X m];
                y = [Y pmin(jj)];
                set(hLine, 'XData', x, 'YData', y);
                pause(0.005);
            end
        end
        i = i+1;
        %disp(i);
        pause(1);
    end
    t = single(i);
end