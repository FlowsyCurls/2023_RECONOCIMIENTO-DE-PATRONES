clear;
clc;
t=0:0.1:2*pi;
u1= sin(t);
u2= cos(t);
##t=t.^-1;
a=5;
b=10;
u= a.*u1 + b.*u2;     # entrada del sistema au1(t)+ bu2(t)
g = u.^(-1);                # evaluacion del sistema con la entrada g(t)=u(t)
g1 = a.*u1.^(-1);
g2 = b.*u2.^(-1);
g3=g1+g2;             # superposicion
result=round(g3-g);   # se redondea
if result == 0        # si la resta es cero es porque son iguales
  disp('Es un sistema lineal');
else
  disp('No es un sistema lineal');
end
subplot(2,1,1);
plot(t,g,"color", "red");     # Se grafica la funcion g
subplot(2,1,2);
plot(t,g3,"color", "green");  # Se grafica la funcion g3
