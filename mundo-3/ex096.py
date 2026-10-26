def area(l, h):
    a = l * h
    print(f"A área de um terreno {l:.1f}x{h:.1f} é de {a:.1f}m².")

print("Controle de Terrenos".center(30))
print("-"*30)
lar = float(input("LARGURA (m): "))
comp = float(input("COMPRIMENTO (m): "))
area(lar, comp)