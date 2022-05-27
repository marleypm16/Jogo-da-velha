game=[['-','-','-'],['-','-','-'],['-','-','-']]
jogador= 'X'
gamerunning= True

#funçao para mostrar o jogo

def mostrarGame(game):
    print(game[0][0] + "|" + game[0][1] + "|" + game[0][2])
    print(game[1][0] + "|" + game[1][1] + "|" + game[1][2])
    print(game[2][0] + "|" + game[2][1] + "|" + game[2][2])


#perguntar ao jogador aonde ele vai colocar sua letra

def ask_Player(game):
    linha=int(input("Qual Linha Você deseja colocar ? Escolha de 0 a 2"))
    coluna=int(input("Qual Coluna Você deseja colocar ? Escolha de 0 a 2"))
    #verifico se a casa ja foi usada
    if game[linha][coluna] =='-':
        game[linha][coluna] = jogador

    elif game[linha][coluna] == jogador:
        print("Esta casa ja foi usada")


#Verificar Vitória

def verificar_Diagonal(game):
    global gamerunning
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != '-':
        gamerunning = False
        print("Vitória")
        mostrarGame(game)
    elif game[0][2] == game[1][1] == game[2][0] and game[0][2] != '-':
        gamerunning = False
        print("Vitória")
        mostrarGame(game)

def Verificar_Horizontal(game):
    global gamerunning

    if game[0][0] == game[0][1] == game[0][2] and game[0][0] != '-':
        gamerunning= False
        print('Vitória')
        mostrarGame(game)
    elif game[1][0] == game[1][1] == game[1][2] and game[1][0] != '-':
        gamerunning= False
        print('Vitória')
        mostrarGame(game)
    elif game[2][0] == game[2][1] == game[2][2] and game[2][0] != '-':
        gamerunning= False
        print('Vitória')
        mostrarGame(game)
def Verificar_Vertical(game):        
    global gamerunning
    if game[0][0] == game[1][0] == game[2][0] and game[0][0] != '-':
        gamerunning= False
        print('Vitória')
    elif game[0][1] == game[1][1] == game[2][1] and game[0][1] != '-':
        gamerunning= False
        print('Vitória')
        mostrarGame(game)   
    elif game[0][2] == game[1][2] == game[2][2] and game[0][2] != '-':
        gamerunning= False
        print('Vitória')
        mostrarGame(game)          

#verificar empate

def Empate(game):
    global gamerunning
    for i in game:
        if '-' not in i:
            gamerunning = False
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
    