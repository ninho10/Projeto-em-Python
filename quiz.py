# MEU QUIZ EM PYTHON

print(" Quiz do Paulo ")
answer_user = input("você que jogar ?  (S/N) ")
print(answer_user)


if answer_user != "S":
    quit()     # para termina o porgrama

print(" Começando o jogo.....")
print("Qual e meu (nome)? \n (A) Pedro \n (B) Paulo \n (C) ninho \n ")
resposta1 = input(" Resposta : ")

if resposta1 == "B":
    print("Parabens Correto")
else:
    print("Esta Errada !")

print("Qual e minha (idade)? \n (A) 35 \n (B) 30 \n (C) 34 \n ")
resposta2 = input(" Resposta : ")

if resposta2 == "C":
    print("Parabens Correto")
else:
    print("Esta Errada !")