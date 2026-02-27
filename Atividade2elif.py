nota1 = int(input("digite sua primeira nota: "))
nota2 = int(input("digite sua segunda nota: "))
nota3 = int(input("digite sua terceira nota: "))
media =  (nota1 + nota2 + nota3) / 3
if media < 5.:
    categoria = "reprovado F"
elif media < 6:
    categoria = "aprovado F"
elif media < 7.:
    categoria = "aprovado D"
elif media < 8.:
    categoria = "aprovado C"
elif media < 9.:
    categoria = "aprovado B"
elif media < 10.:
    categoria = "aprovado A"
else :
    categoria = "nota perfeita A"
print (f"voce foi {categoria}")
