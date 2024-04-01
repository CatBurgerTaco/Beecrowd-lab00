A, B, C = input().split()
A, B, C = float(A), float(B), float(C)

print("TRIANGULO: "+str('{:.3f}'.format((A*C)/2)))
print("CIRCULO: "+str('{:.3f}'.format((C**2)*3.14159)))
print("TRAPEZIO: "+str('{:.3f}'.format(((A + B)*C)/2)))
print("QUADRADO: "+str('{:.3f}'.format(B**2)))
print("RETANGULO: "+str('{:.3f}'.format(A*B)))