% Definir la cuadrícula de valores x e y
[x, y] = meshgrid(-10:0.5:10);

% Calcular el valor de z para cada par de valores (x,y)
z = (84*x - 15*y + 786)/168;

% Graficar el plano con un colormap distinto
surf(x, y, z, 'EdgeColor', 'none');
colormap(spring);

% Dividir el vector (84,-15,-168) por 10 para reducir su longitud
v = [84, -15, -168]/10;

% Agregar el vector (84,-15,-168)/10 al gráfico
hold on;  % para que el vector se dibuje en el mismo gráfico
quiver3(0, 0, 0, v(1), v(2), v(3), 'LineWidth', 2, 'Color', 'k');

% Definir los límites de los ejes para ampliar la vista del plano y el vector
xlim([-10, 10]);
ylim([-10, 10]);
zlim([-10, 10]);


% agregar etiquetas a los ejes y título al gráfico
xlabel('x');
ylabel('y');
zlabel('z');
title('Plano 84x - 15y - 168z - 786 = 0');

