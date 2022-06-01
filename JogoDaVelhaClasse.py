
class Jogodavelha:

    #funcao para mostrar o jogo 
    def __init__(self,jogo,jogador):
        self.jogo = jogo
        self.jogador = jogador
        
    
    def mostrarJogo(self):
        print(self.jogo[0] + '|' + self.jogo[1] + '|' + self.jogo[2])
        print(self.jogo[3] + '|' + self.jogo[4] + '|' + self.jogo[5])
        print(self.jogo[6] + '|' + self.jogo[7] + '|' + self.jogo[8])
    
    #input para colocar a letra em uma das posições
    def ask_player(self):

        ask=int(input("Onde você deseja colocar sua letra? Escolha de 1 a 9 :"))

        if self.jogo[ask-1] == '-':
            self.jogo[ask-1] = self.jogador
        
        #Verificar erro:
           
        elif self.jogo[ask - 1] == self.jogador:
            print("Essa casa ja foi usada")

    #Verificar vitoria:

    def VerificarDiagonal(self):

        if self.jogo[0] == self.jogo[4] == self.jogo[8] and self.jogo[8] != '-' or self.jogo[2] == self.jogo[4] == self.jogo[6] and self.jogo[6] != '-':
            return True

    def verificarHorizontal(self):
        if self.jogo[0] == self.jogo[1] == self.jogo[2] and self.jogo[2] != '-' or self.jogo[3] == self.jogo[4] == self.jogo[5] and self.jogo[5] != '-' or self.jogo[6] == self.jogo[7] == self.jogo[8] and self.jogo[8] != '-':
            return True

    def verificarVertical(self):
        if self.jogo[0] == self.jogo[3] == self.jogo[6] and self.jogo[6] != '-' or self.jogo[1] == self.jogo[4] == self.jogo[7] and self.jogo[7] != '-' or self.jogo[2] == self.jogo[6] == self.jogo[8] and self.jogo[8] != '-':
            return True
    #Verificar empate
    def empate(self):
        if '-' not in self.jogo:
            print("Empate")
            return True
    #Trocar jogadores
    def trocarJogador(self):
            if self.jogador == 'X':
                self.jogador= 'O'
            else:
                self.jogador = 'X'

    #Começar o game
    def startGame(self):
        while JogoEmAndamento:
            self.mostrarJogo()
            self.ask_player()
            if self.VerificarDiagonal() or self.verificarHorizontal() or self.verificarVertical():
                print("Vitória")
                self.mostrarJogo()
                break
            if self.empate():
                self.mostrarJogo()
                break
            self.trocarJogador()
JogoEmAndamento= True 
game= Jogodavelha(['-','-','-','-','-','-','-','-','-'],'X')
game.startGame()


        
        


        
    



