n = t;
l = 0;
hLine = line(nan, nan, 'Color', 'blue');
data = zeros(2,n*length(pmin));
    for jj=1:length(pmin)
        if mod(jj,2)==0
            data(1,jj) = 20;
        else
            data(1,jj) = 18;
        end
        data(2,jj)=+jj/length(pmin);
    end
    for ii=1:n
        for jj=1:length(pmin)
            data(1,jj+ii*length(pmin))=pmin(jj);
            data(2,jj+ii*length(pmin))=ii+jj/length(pmin);
        end
    end