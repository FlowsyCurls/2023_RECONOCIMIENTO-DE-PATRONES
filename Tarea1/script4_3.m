% Definir la función
f = @(x,y) log(x.^2 + y.^2);

% Definir los límites de la malla
x = linspace(-3,3,50);
y = linspace(-3,3,50);
[X,Y] = meshgrid(x,y);

% Calcular el gradiente
[Gx, Gy] = gradient(f(X,Y));

% Graficar la superficie
figure;
surf(X,Y,f(X,Y));
title('Superficie de f(x,y)');

% Graficar los vectores gradiente
hold on;
quiver(X,Y,Gx,Gy, 'color', 'red', 'linewidth', 1.5);
grad1 = [double(subs(Gx, [X, Y], [-6, 1])), double(subs(Gy, [X, Y], [-6, 1]))];
quiver(-6, 1, grad1(1), grad1(2), 'color', 'blue', 'linewidth', 3);
grad2 = [double(subs(Gx, [X, Y], [4, -2])), double(subs(Gy, [X, Y], [4, -2]))];
quiver(4, -2, grad2(1), grad2(2), 'color', 'yellow', 'linewidth', 3);
hold off;
title('Gradiente de f(x,y)');
legend('Superficie de f(x,y)', 'Gradiente de f(x,y)', 'Gradiente en (-6,1)', 'Gradiente en (4,-2)');

