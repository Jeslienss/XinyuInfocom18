clear
clc

tab = csvread('matres.csv');
tab = tab(:, 3:14);

[a, b] = size(tab);
res = [];
for i = 1:a
    temp = find(tab(i, :) <= 0.5);
    if ~isempty(temp)
        res = [res, temp(1) + 1];
    end
end

mean(res)
