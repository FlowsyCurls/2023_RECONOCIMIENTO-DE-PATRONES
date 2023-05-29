





## 4.2

##%% Vectores
##x = [-9, 3, 5];
##y = [3, 0, -11];
##quiver(0, 0, x(1), x(2), 'b', 'LineWidth', 2); hold on;
##quiver(0, 0, y(1), y(2), 'r', 'LineWidth', 2); hold off;
##axis([-12 6 -12 4]);

##%% Plano
##n = [-33, -84, -9];
##p0 = [0, 0, -23.67];
##v = [-0.45, 0, 0] - [0, 0, -23.67];
##
##quiver3(p0(1), p0(2), p0(3), n(1), n(2), n(3), 'LineWidth', 2);
##hold on;
##surf([0, -0.45; 0, -0.45], [-84, -84; 0, 0], [-23.67, -23.67; 0, 0]);
##


##x = [-9, 3, 5];
##y = [3, 0, -11];
##plot([0, x(1)], [0, x(2)], 'b', 'LineWidth', 2); hold on;
##plot([0, y(1)], [0, y(2)], 'r', 'LineWidth', 2); hold off;
##axis([-12 6 -12 4]);













## 4.4
##format bank
##A = [1,4;-4,-7];
##[Valores_propios,Vectores_propios] = eig(A);
##printf("\n")
##Valores_propios
##Vectores_propios



## 4.5

#{
1 - Genere un set de datos aleatorio que consista en 4 variables (h1, h2, h3, h4)
con 20 muestras cada una. Muestre la matriz con las 20 muestras.

2 - Obtenga el valor esperado de cada una de las variables utilizando las
funciones de Octave.

3 - Obtenga la matriz de covarianza sin utilizar la funcion. Puede utilizar
la funcion cov.

4 - Explique cuales de las variables se relacionan mas y cuales se relacionan menos
#}

##% Generamos un set de datos aleatorios con 4 variables
##% y 20 muestras cada una
##data = randi([1, 50], 20, 4);
##
### Calculamos el valor esperado de cada variable.
##h1_mean = mean(data(:, 1));
##h2_mean = mean(data(:, 2));
##h3_mean = mean(data(:, 3));
##h4_mean = mean(data(:, 4));
##
##% Calculamos la matriz de covarianza
##matriz_cov = cov(data);
##
##% Hacemos el gráfico de la matriz de covarianza
##nombres_variables = {'h1', 'h2', 'h3', 'h4'};
##imagesc(matriz_cov);
####colormap(cool);
##colorbar;
##
##% Agregamos los nombres de las variables a los ejes x e y
##set(gca, 'XTickLabel', nombres_variables);
##set(gca, 'YTickLabel', nombres_variables);
##
##% Agregamos las etiquetas de los ejes x e y
##xlabel('Variables');
##ylabel('Variables');
##
##% Asignar el valor correspondiente
##for i = 1:4
##  for j = 1:4
##    text(i, j, sprintf('%.2f', matriz_cov(i,j)),
##    'HorizontalAlignment', 'center',
##    'VerticalAlignment', 'middle',
##    'FontSize', 14',
##    'Color', [1, 1, 1]);
##  end
##end



% Prints
##data
##disp(["h1_mean = " num2str(h1_mean)]);
##disp(["h2_mean = " num2str(h2_mean)]);
##disp(["h3_mean = " num2str(h3_mean)]);
##disp(["h4_mean = " num2str(h4_mean)]);
##matriz_cov


