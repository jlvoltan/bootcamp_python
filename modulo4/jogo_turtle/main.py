import turtle



def Tela(tamanhoX,tamanhoY):
    '''Serve para setar a janela do jogo'''
    tela=turtle.Screen()
    tela.title("Turtle")
    tela.bgcolor(0.5,0,0.5)
    tela.setup(width=tamanhoX,height=tamanhoY)
    tela.tracer(0)
    return tela

def Controladores():
    """Serve para os jogadores escolherem se usaram um retangulo ou um classsic para
    rebater a bola"""
    print("Escolha os controladores:")
    print("1- barra")
    print("2- classic")
    opcao_A = opcao_B =0
    while ((opcao_A !=1) and (opcao_A !=2)) or ((opcao_B !=1) and (opcao_B !=2)):
        opcao_A= int(input("Digite o número do objeto para A: "))
        opcao_B= int(input("Digite o número do objeto para B: "))
    print("Jogador A use as teclas 8 e 2")
    print("Jogador B use as teclas seta para cima e seta para baixo")
    if(opcao_A == 1):
        objetoA="square"
    else:
     objetoA="classic"
    if(opcao_B == 1):
        objetoB="square"
    else:
        objetoB="classic"
    return objetoA,objetoB

def Controlador(objeto, jogador):
    """Serve para criar os controladores na posição correta e com o objeto que o jogador escolheu"""
    barra = turtle.Turtle()
    barra.speed(0)
    barra.shape(objeto)
    barra.color('black')
    barra.shapesize(stretch_wid=4, stretch_len=1)
    barra.penup()
    if(jogador==1): posicaoX=-355
    else: posicaoX=355
    barra.goto(posicaoX, 0)
    return barra

def Circulo():
    """Serve para criar a bola e sua velocidade"""
    circulo = turtle.Turtle()
    circulo.speed(0)
    circulo.shape('circle')
    circulo.color('red')
    circulo.penup()
    circulo.goto(0, 0)

    #Setando a velocidade/movimento da bola
    print("Escolha a dificuldade:")
    print("1-Fácil,2- Médio 3- Difícil")
    escolhaVelocidade = int(input("Número: "))
    if(escolhaVelocidade==1): velocidade=0.15
    elif(escolhaVelocidade==2): velocidade=0.25
    elif (escolhaVelocidade == 3):velocidade = 0.35
    circulo.dx=circulo.dy= velocidade
    return circulo

#Placar
def CriaPlacar():
    valor_placar = [0, 0]
    placar = turtle.Turtle()
    placar.speed()
    placar.color("black")
    placar.penup() #O movimentyo da caneta
    placar.hideturtle()
    placar.goto(0, -280)
    placar = AtualizaPlacar(placar, valor_placar)
    return placar, valor_placar

def AtualizaPlacar(placar, valor_placar):
    '''Serve para atualizar o placar'''
    placar.clear()
    placar.write("Jogador A: {} x Jogador B: {}".format(valor_placar[0], valor_placar[1]), align="center",font=("Arial", 32, "normal"))
    return placar

# funcao para o movimento
def movimento(barra, movimento):
    y=barra.ycor()
    if (movimento): y+= 10 #Subida usei 1
    else: y-=10          #Descida usei 0
    barra.sety(y)
    return barra

def sair():
    global continuar
    continuar=False
# recebendo Teclas

def EscutaTecla(tela):
    tela.listen()
    tela.onkeypress(barra_A_cima, "8")
    tela.onkeypress(barra_A_baixo, "2")
    tela.onkeypress(barra_B_cima, "Up")
    tela.onkeypress(barra_B_baixo, "Down")
    tela.onkeypress(sair, "Escape")

#funcoes para o movimento
#Barra A
#cima
def barra_A_cima():movimento(barra_A, 1)
#baixo
def barra_A_baixo():movimento(barra_A, 0)

#Barra B
#cima
def barra_B_cima(): movimento(barra_B, 1)
#baixo
def barra_B_baixo():movimento(barra_B, 0)



if __name__ == '__main__':
    tela = Tela(800, 600)
    objetoA,objetoB= Controladores()
    barra_A = Controlador(objetoA, 1)
    barra_B = Controlador(objetoB, 2)
    circulo = Circulo()

    # pontuacao
    placar, valor_placar=CriaPlacar()

    # recebendo dados do teclado
    continuar = True
    EscutaTecla(tela)
    print("Aperte **Esc** para sair!")

    while (continuar):
        tela.update()

        # adicionando o movimento da bola
        circulo.setx(circulo.xcor() + circulo.dx)
        circulo.sety(circulo.ycor() + circulo.dy)

        # definindo limites da imagem
        if circulo.ycor() > 290:
            circulo.sety(290)
            circulo.dy = circulo.dy * -1   # reverte o movimento quanto bate na borda
        if circulo.ycor() < -290:
            circulo.sety(-290)
            circulo.dy = circulo.dy * -1  # reverte o movimento quanto bate na borda
        if circulo.xcor() > 390:
            circulo.goto(0, 0)
            circulo.dx = circulo.dx * -1 # PONTO!! Bopla retorna ao meio de campo e reverte o movimento
            valor_placar[0] += 1
            AtualizaPlacar(placar,valor_placar)
        if circulo.xcor() < -390:
            circulo.goto(0, 0)
            circulo.dx = circulo.dx * -1  # PONTO!! Bopla retorna ao meio de campo e reverte o movimento
            valor_placar[1] += 1
            AtualizaPlacar(placar,valor_placar)

        #Vendo se a bola não foi rebatida
        if (circulo.xcor() > 350 and circulo.xcor() < 360) and (circulo.ycor() < barra_B.ycor() + 40 and circulo.ycor() > barra_B.ycor() - 40):
            circulo.setx(350)
            circulo.dx = circulo.dx * -1

        if (circulo.xcor() < -350 and circulo.xcor() > -360) and (circulo.ycor() < barra_A.ycor() + 40 and circulo.ycor() > barra_A.ycor() - 40):
            circulo.setx(-350)
            circulo.dx = circulo.dx * -1
    print("Fim de Jogo!!")
    print("Jogador A: {} x Jogador B: {}".format(valor_placar[0], valor_placar[1]))

    