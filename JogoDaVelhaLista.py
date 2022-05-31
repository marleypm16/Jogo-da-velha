# fazer a variavel com meu jogo, vitoria, jogador, jogorodando


jogo= ['-','-','-','-','-','-','-','-','-']
JogoEmAndamento= True
jogador = 'X'
#funcao para mostrar o jogo 

def MostrarJogo(jogo):
    print(jogo[0] + "|" + jogo[1] + "|" + jogo[2])
    print(jogo[3] + '|' + jogo[4] + "|" +jogo[5])
    print(jogo[6] + '|' + jogo[7] + "|" +jogo[8])

#Perguntar ao jogador onde ele vai colocar sua letra

def ask_player(game):
    ask= int(input(" Em qual posição voce quer inserir? Escolha de 1 a 9 :"))
    if game[ask -1] == '-':
        game[ask - 1] = jogador


#Verificar vitorias

def check_Horizontal(jogo):
    vitoria= jogo[0] == jogo[1] == jogo[2] and jogo[0] !='-' or jogo[3] ==  jogo[4] == jogo[5] and jogo[3] != '-' or jogo[6] ==  jogo[7] == jogo[8] and jogo[6] != '-'
    if vitoria:
        return True
        

def check_Vertical(jogo):
    vitoria= jogo[0] == jogo[3] == jogo[6] and jogo[0]!= '-' or jogo[1] ==  jogo[4] == jogo[7] and jogo[1] !='-' or jogo[2] ==  jogo[5] == jogo[8] and jogo[2] != '-'
    if vitoria:
        return True



def check_Diagonal(jogo):
    vitoria= jogo[0] == jogo[4] == jogo[8] and jogo[0] != '-' or jogo[2] ==  jogo[4] == jogo[6] and jogo[2] != '-'
    if vitoria:
        return True



#Empate

def Empate(jogo):
    if '-' not in jogo:
        return True

#Trocar Jogadores


def Trocar_Jogadores(jogador):
    if jogador == 'X':
        return 'O'
    else:
        return 'X'


while JogoEmAndamento:
    MostrarJogo(jogo)
    ask_player(jogo)
    if check_Diagonal(jogo) or check_Horizontal(jogo) or check_Vertical(jogo):
        MostrarJogo(jogo)
        print('Vitória')
        JogoEmAndamento= False

    if Empate(jogo):
        print("Empate.")
        MostrarJogo(jogo)
        JogoEmAndamento = False
   
    jogador=Trocar_Jogadores(jogador)


