import random 

dicionarioTemas = {
  "paises":["brasil", "cuba", "peru", "colombia"],
  "frutas":["abacaxi", "goiaba", "manga", "abacate"],
  "tech": ["programaçao", "computador", "python", "processador"]
}

while True:
  print("Jogo da Forca\nTemas: 1-paises | 2-Frutas | 3-tech | 4- Sair do Jogo")
  entrada = str(input("Digite uma opção: "))
 

  if entrada == "4":
    print("Você saiu do jogo :(")
    break 
  elif entrada == "1":
    palavra = random.choice(dicionarioTemas["paises"])
  elif entrada == "2":
    palavra = random.choice(dicionarioTemas["frutas"])
  elif entrada == "3":
    palavra = random.choice(dicionarioTemas["tech"])
  
  tentativas = ["-"]*len(palavra) 
  letrasErradas = [] 
  print("Vamos começar, sua palavra tem  " + str(len(palavra)) + " letras.\n")

  for i in range(18):
    
    print("".join(tentativas))#
    jogada = str(input("Digite uma letra: "))
    
    if jogada in palavra: 
      
      for j in range(len(palavra)):
        if palavra[j] == jogada:
          tentativas[j] = jogada
      resposta = "".join(tentativas)
      
      print("Forca: " + resposta + " Chances restantes: " + str(17 - i)) 
      if resposta == palavra: 
        print("Parabéns, você acertou a palavra é " + resposta + "!")
        break 

    else:
      letrasErradas +=[jogada] 
      resposta = "".join(tentativas)
      print("Forca: " + resposta + " Chances restantes: " + str(17-i)) 
      letrasJaUsadas = " ".join(letrasErradas)
      print("A letra " + jogada + " não está na palavra\n Letras erradas já digitadas: " + letrasJaUsadas) 

  else: 
    print("Você perdeu! Forca!") 

