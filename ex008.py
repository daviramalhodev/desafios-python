medida= float(input('Digite o valor em metros: '))
vmin= medida*1000
vcen= medida*100

print('{} metros equivale a {:.0f} centimetros e {:.0f} milimetros!'.format(medida, vcen, vmin))