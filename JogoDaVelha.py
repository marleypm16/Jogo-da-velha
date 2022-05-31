


game=[['-','-','-'],['-','-','-'],['-','-','-']]
gamerunning= True
jogador = 'X'

#funçao para mostrar o jogo

def mostrarGame(game):
    print(game[0][0] + "|" + game[0][1] + "|" + game[0][2])
    print(game[1][0] + "|" + game[1][1] + "|" + game[1][2])
    print(game[2][0] + "|" + game[2][1] + "|" + game[2][2])


#perguntar ao jogador aonde ele vai colocar sua letra

def ask_Player(game):
    linha=int(input("Qual Linha Você deseja colocar ? Escolha de 0 a 2 :"))
    coluna=int(input("Qual Coluna Você deseja colocar ? Escolha de 0 a 2 :"))
    #verifico se a casa ja foi usada
    if game[linha][coluna] =='-':
        game[linha][coluna] = jogador

    elif game[linha][coluna] == jogador:
        print("Esta casa ja foi usada")


#Verificar Vitória

def verificar_Diagonal(game):
    vitoria = game[0][0] == game[1][1] == game[2][2] and game[0][0] != '-' or game[0][2] == game[1][1] == game[2][0] and game[0][2] != '-' 
    if vitoria:
        print("Vitória")
        mostrarGame(game)
    return True


def Verificar_Horizontal(game):

    vitoria=game[0][0] == game[0][1] == game[0][2] and game[0][0] != '-' or game[1][0] == game[1][1] == game[1][2] and game[1][0] != '-' or game[2][0] == game[2][1] == game[2][2] and game[2][0] != '-'

    if vitoria:
        print("Vitória")
        mostrarGame(game)
    return True


def Verificar_Vertical(game):       
    vitoria = game[0][0] == game[1][0] == game[2][0] and game[0][0] != '-' or game[0][1] == game[1][1] == game[2][1] and game[0][1] != '-' or game[0][2] == game[1][2] == game[2][2] and game[0][2] != '-'
    if vitoria:
        print("Vitória")
        mostrarGame(game)
    return True

vitoria= verificar_Diagonal(game) or Verificar_Horizontal(game) or Verificar_Vertical(game)      
     
#verificar empate



def Empate(game):
    for lista in game:
        traço=[]
        for linha in lista:
            traço.append(linha)
        if '-' not in traço:
            print("Empate")
            mostrarGame(game)




#Troca de jogadores

def switch_Player():
    global jogador
    if jogador == 'X':
        jogador = 'O'
    else:
        jogador = 'X'

while gamerunning:
    mostrarGame(game)
    ask_Player(game)
    verificar_Diagonal(game)
    Verificar_Horizontal(game)
    Verificar_Vertical(game)
    Empate(game)
    switch_Player()
        
    