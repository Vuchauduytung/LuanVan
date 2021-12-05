disp('press Ctrl-C to exit');
hLine = line(nan, nan, 'Color', 'red');
i = 0;
while 1
    apsuat = 18;
    X = get(hLine, 'XData');
    Y = get(hLine, 'YData');
    x = [X i];
    y = [Y apsuat];
    set(hLine, 'XData', x, 'YData', y);
    i = i+1;
    pause(0.1);
    apsuat = 20;
    X = get(hLine, 'XData');
    Y = get(hLine, 'YData');
    x = [X i];
    y = [Y apsuat];
    set(hLine, 'XData', x, 'YData', y);
    i = i+1;
    pause(0.1);
end