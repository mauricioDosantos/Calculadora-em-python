from functools import partial
from tkinter import*

#acumu e acumu1, são váriaveis que acumulam números, digitados pelo usuário.
acumu = []; acumu1 = []
#lista_operador recebe os operadores digitados.
lista_operador = [0]
#ultima_opsi_op recebe ultimo operador digítado.
ultima_opsi_op = 0

#Todos os prints é para saber por aonde está pasando e execultando o código.

#bt_click tem por primeira funcionalidade, limpar quaquer texto existente, definido por 001I até 001F.
#E tem por funcionalidade principal, adicionar texto na barra de texto, definido por 002I até 002F
#Foi usado uma variavel do tipo string, em que ela recebe dados por meio do .set e o .get junta o que ja tem na StringVar, chamada de texto.
#acumu.append é usado para receber o valor do botão em formato de string
#acumu só recebe números em formato de string, isto quer dizer que se printar ele aparece entre aspas(' ').
def bt_click (botao):
    #001I =================
    if len(acumu) > 0:
        print("Está limpo!")
    else:
        print("Limpando.")
        texto.set(" ")
    #001F =================
    #002I =================
    texto.set(texto.get() + botao["text"])
    acumu.append(botao["text"])
    #002F =================
    print('\n',acumu)

#Estava dando erro em utilizar o acumu, por isso t recebe acumu, podendo ser revisto o erro e retirado no futuro. 
t = acumu

#Esta função é responsavel por trabalhar com os operadores aritiméticos.
#Função inicia limpando a barra de texto,ultima_opsi_op recebe o operador da lista de operadores, para que a operação possa ser execultada somente quando estiver 2 números em acumu1.
#Ultima_opsi_op = Usado para execultar a operação quando estiver 2 elementos em acumu1.
#juntar_lis() é uma função para juntar a lista acumu, e transformala em número inteíro. Obs: sempre que digitado um oprador indica fim de um número.
#As estruturas condicionais, testam se ultima_opsi_op tem algum dos operadores aritiméticos.
#Toda vez que digitado um operador ele aguarda o proximo número a ser digitado.
def bt_click_operadores(botao):
    texto.set(" ")    
    ultima_opsi_op = lista_operador[0]
    lista_operador[0] = botao["text"]
    #junta a lista acumu, para todos os operadores
    juntar_lis(t)
    #========================
    if ultima_opsi_op == '+':
        print('Mais')
        if len(acumu1) == 2:
            #Aqui se chama a função soma().
            soma(acumu1)
        else:
            print("Falso")
         
    elif ultima_opsi_op == '-':
        print("Menos")
        if len(acumu1) == 2:
            #Aqui se chama a função menos().
            menos(acumu1)
        else:
            print("Falso")
          
    elif  ultima_opsi_op == '/':
        print("Divisao")
        if len(acumu1) == 2:
            #Aqui se chama a função divisao().
            divisao(acumu1)
        else:
            print("Falso")
        
    elif  ultima_opsi_op == '*':
        print("Multiplicaçao")
        if len(acumu1) == 2:
            #Aqui se chama a função multiplicacao().
            multiplicacao(acumu1)
        else:
            print("Falso")
        
    elif  ultima_opsi_op == "=":
        #No igual, se escreve o resultado da ultima soma.
        a = acumu1[0]
        texto.set(str(a))
        print("Mostrado o resultado!")
            
    else:
        return "Só para dar continuidade a execução do programa."

#Comando usado para juntar os números da lista, recebidos e colocados dentro dela por meio dos botões, lista essa chamada de acumu.
def juntar_lis(h):
    if len(acumu) < 1:
        return "Só, para sair do juntar Lista quando algum operador chamar e não tiver o que juntar, se não ele prossegue."
    print(acumu)
    #''.join() = usado para juntar strings que estão dentro de uma lista.
    a = ''.join(h)
    #acumu1 recebe o número que estava em string, juntado pelo join, e agora recebendo o como número inteiro.
    acumu1.append(int(a))
    print(acumu1)
    h.clear()    


#Área das funções dos operadores.
#Sempre ao apertar operador deve ter somente um operador na lista_operador.
#Funçao do operador de adição.
#Dentro da função, a variavel resultado recebe as posições de acumu1 em 0 e 1, e faz a soma.
#Resultado é escrito na tela, e a lista acumu1 é apagada e logo depois recebe o resultado.

#para não repetir comentario, todas as funções ue executam operação fazem a mesma coisa...
    
def soma(s):
    resultado = s[0] + s[1]
    texto.set(str(resultado))
    print('\n',resultado)
    acumu1.clear()
    acumu1.append(resultado)

#funçao do operador de menos.
def menos(m):
    resultado = m[0] - m[1]
    texto.set(str(resultado))
    acumu1.clear()
    acumu1.append(resultado)

#funçao do operador de multiplicacao.
def multiplicacao(n):
    resultado = n[0] * n[1]
    texto.set(str(resultado))
    acumu1.clear()
    acumu1.append(resultado)

#funçao do operador de divisao.
def divisao(d):
    resultado = d[0] / d[1]
    texto.set(str(resultado))
    acumu1.clear()
    acumu1.append(resultado)

#Botão C que limpa todas listas e label.
def limpeza_de_lista_e_label():
    texto.set(" ")
    acumu.clear()
    acumu1.clear()
    lista_operador[0] = 0
    ultima_opsi_op2 = 0


#=================  Tela Principal  ================= 
ja = Tk()
texto = StringVar()

ja.title("CALCULADORA TI_BUGADO")
#var = StringVar()



#escrito da tela
lb = Label(ja, text="__________________CALCULADORA_______________________________")
lb.place(x=100, y=70)

#parte a recer e calcular os numeros, caixa de texto.
lb2 = Label(ja, textvar = texto)
lb2.place(x=100, y=90)


#area dos botões
bt1 = Button(ja, text="1", width=10, bg="blue")
bt1["command"] = partial(bt_click, bt1)
bt1.place(x=100, y=130)

bt2 = Button(ja, text="2", width=10, bg="blue")
bt2["command"] = partial(bt_click, bt2)
bt2.place(x=100, y=160)

bt3 = Button(ja, text="3", width=10, bg="blue")
bt3["command"] = partial(bt_click, bt3)
bt3.place(x=100, y=190)

bt4 = Button(ja, text="4", width=10, bg="blue")
bt4["command"] = partial(bt_click, bt4)
bt4.place(x=184, y=130)

bt5 = Button(ja, text="5", width=10, bg="blue")
bt5["command"] = partial(bt_click, bt5)
bt5.place(x=184, y=160)

bt6 = Button(ja, text="6", width=10, bg="blue")
bt6["command"] = partial(bt_click, bt6)
bt6.place(x=184, y=190)

bt7 = Button(ja, text="7", width=10, bg="blue")
bt7["command"] = partial(bt_click, bt7)
bt7.place(x=268, y=130)

bt8 = Button(ja, text="8", width=10, bg="blue")
bt8["command"] = partial(bt_click, bt8)
bt8.place(x=268, y=160)

bt9 = Button(ja, text="9", width=10, bg="blue")
bt9["command"] = partial(bt_click, bt9)
bt9.place(x=268, y=190)

bt0 = Button(ja, text="0", width=10, bg="blue")
bt0["command"] = partial(bt_click, bt0)
bt0.place(x=100, y=220)

#botao igual
bt_igual = Button(ja, text="=", width=10, bg="grey")
bt_igual["command"] = partial(bt_click_operadores, bt_igual)
bt_igual.place(x=184, y=220)

#botao sair
bt_sair = Button(ja, text="SAIR", width=10, bg="red",command=quit)
bt_sair.place(x=268, y=220)

#x, y na linha de cada fileira
#botoes dos operadores soma, subtraçao,mutiplicação e divisão
bt_mais = Button(ja, text="+", width=10, bg="orange")
bt_mais["command"] = partial(bt_click_operadores, bt_mais)
bt_mais.place(x=352, y=130)

bt_menos = Button(ja, text="-", width=10, bg="orange")
bt_menos['command'] = partial(bt_click_operadores, bt_menos)
bt_menos.place(x=352, y=160)

bt_mult = Button(ja, text="*", width=10, bg="orange")
bt_mult['command'] = partial(bt_click_operadores, bt_mult)
bt_mult.place(x=352, y=190)

bt_div = Button(ja, text="/", width=10, bg="orange")
bt_div['command'] = partial(bt_click_operadores, bt_div)
bt_div.place(x=352, y=220)

#Botão Que limpa o label e as listas.
bt_c = Button(ja, text="C", width=10, bg="red")
bt_c["command"] = partial(limpeza_de_lista_e_label)
bt_c.place(x=352, y=90)

ja.geometry("500x400+50+50")
ja.mainloop
#=================  Fim da Tela Principal ================= 
