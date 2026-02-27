nota1 = int(input("digite sua primeira nota: "))
nota2 = int(input("digite sua segunda nota: "))
nota3 = int(input("digite sua terceira nota: "))
media =  (nota1 + nota2 + nota3) / 3
if media < 5:
    categoria = "reprovado"
elif media < 10:
    categoria = "aprovado"
else :
    categoria = "nota perfeita"
print (f"voce foi {categoria}")
