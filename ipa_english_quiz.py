###################################
# Author: Vinicius OA
# Company: English Methods
# Social media: ---

import io
from time import sleep
from termcolor import colored
from random import shuffle

arquivo = io.open('ipa_english_renew.txt','r', encoding='utf8')
linhas = arquivo.readlines()
palavras_parser = [palavra.strip('\n').split() for palavra in linhas] #lista das palavras

print ("Bem vindo ao English Quiz da English Methods. Se voce nao esta familiarizado com os simbolos de transcricao, " 
       "Segue os mais importantes\nˈ = Estresse principal, ou seja, enfatico\n. = separacao silabica\nˌ = estresse secundario" 
       " da palavra\n")

sleep(8)

### funcao que retorna uma *lista* do fonema desejado ###
def lista_palavra_fonema(vog_conso,pergunta_fonema,opcao_lista_return):
    consoantes = ('h','r','w','ŋ','ð','θ','l','n','j', 't̬')
    vogais = ('ə','ɝ','ɚ','ʌ','ɑː')
    lista_fonemas_inicio = []
    lista_fonemas_meio = []
    lista_fonemas_final = []
    for buscar_palavra in palavras_parser:
        try:
            if vog_conso == 1:
                if consoantes[pergunta_fonema-1] in buscar_palavra[0]:
                    if consoantes[pergunta_fonema-1] in buscar_palavra[0][0] or consoantes[pergunta_fonema-1] in \
                            buscar_palavra[0][1]:
                        lista_fonemas_inicio.append(buscar_palavra)

                    elif consoantes[pergunta_fonema-1] in buscar_palavra[0][-1]:
                        lista_fonemas_final.append(buscar_palavra)

                    else:
                        lista_fonemas_meio.append(buscar_palavra)

            else:
                if vogais[pergunta_fonema-1] in buscar_palavra[0]:
                    if vogais[pergunta_fonema-1] in buscar_palavra[0][0] or vogais[pergunta_fonema-1] in \
                            buscar_palavra[0][1]:
                        lista_fonemas_inicio.append(buscar_palavra)

                    elif vogais[pergunta_fonema-1] in buscar_palavra[0][-1]:
                        lista_fonemas_final.append(buscar_palavra)

                    else:
                        lista_fonemas_meio.append(buscar_palavra)

        except IndexError:
            continue

    if opcao_lista_return == 1:
        return lista_fonemas_inicio

    elif opcao_lista_return == 2:
        return lista_fonemas_final

    elif opcao_lista_return == 3:
        return lista_fonemas_meio

    else:
        return (lista_fonemas_inicio+lista_fonemas_meio+lista_fonemas_final)

###################################################################

while True:
    try:
        pergunta1 = int(input('\nQual fonema tu gostarias de praticar? Se for consoantes/vogais, digite e envie '
                              +colored(' 1','yellow')+'.\nNo entanto,' 
                             ' se quiser treinar a n-th palavras mais comuns, digite e envie '+ colored('2\n','yellow')+
                              '(Envie) => '))

        if pergunta1 not in range(1,3):
            print (colored("\nFavor, envie apenas 1 ou 2.\n",'red'))
            sleep(2)

        else:
            if pergunta1 != 2:
                flag = True
                while True:
                    if flag == True:
                        print ("\n"+("Consoantes".center(130))+"\n\n1 - [h]\t\t2 - [r]\t\t3 - [w]\t\t4 - [ŋ]\t\t5 - [ð]\t\t" 
                                    "6 - [θ]\t\t7 - [l] (Dark L)\t\t8 - [n] (Final de palavras)\t\t9 - [j]\t\t10 - [t̬]\n")
                        pergunta_fonema = int(input("\nDigite e envie a opcao da consoante que queres treinar. Caso queira"  
                                        " treinar"+colored(' vogais','cyan')+", envie "+colored(' 0','yellow')+
                                        ". Se quiser voltar, envie "+colored(' -1','yellow')+".\n(Envie) => "))

                        if pergunta_fonema == 0:
                            flag = False

                        elif pergunta_fonema == -1:
                            break

                        elif pergunta_fonema > 10 or pergunta_fonema < 1:
                            print (colored("\nenvie apenas as opções disponiveis.\n",'red'))
                            sleep(1.5)

                        else:
                            while True:
                                pergunta2 = int(input("\n\nVocê deseja palavras que começam com o fonema escolhido"+
                                            colored(' [1]','yellow')+", terminam com ela"+colored(' [2]','yellow')+
                                             ", esteja no meio"+colored(' [3]','yellow')+" ou que contenha o fonema"+
                                           colored(' [4]','yellow')+"?\nDigite e envie a opção. Caso queira voltar, envie "+
                                            colored(' 0','yellow')+".\n(Envie) => "))

                                if pergunta2 == 0:
                                    break

                                elif pergunta2 > 4 or pergunta2 < 0:
                                    print(colored("\nenvie apenas as opções disponiveis.\n",'red'))
                                    sleep(1.5)

                                else:
                                    recebe_fonemas = lista_palavra_fonema(1,pergunta_fonema,pergunta2)
                                    shuffle(recebe_fonemas)
                                    acertos = 0
                                    erros = 0
                                    if len(recebe_fonemas) != 0:
                                        for palavra_quiz in recebe_fonemas:
                                            print (colored('\n\n'+palavra_quiz[0],'yellow'))
                                            recebe_resposta = input("\nQual palavra a transcricao fonetica acima corresponde? " 
                                                                    "Caso queira encerrar o quiz, digite 'sair'\n(Envie) =>")

                                            if recebe_resposta.lower() == palavra_quiz[1]:
                                                acertos += 1
                                                print (colored('\nParabens! voce acertou!','green'))
                                                print ("Voce ja acertou: "+colored(str(acertos)+"\n",'green')+"Voce ja errou: "+
                                                       colored(str(erros)+"\n",'red'))

                                                sleep(2)

                                            elif recebe_resposta.lower().strip("'") == 'sair':
                                                print ("\nSeu saldo final ficou:\n"+"Acertos: "+colored(str(acertos)+"\n",'green')+
                                                       "Erros: "+colored(str(erros)+"\n",'red'))

                                                sleep(2)
                                                break

                                            else:
                                                erros += 1
                                                print (colored('\nInfelizmente, voce errou\nA resposta certa é: '+
                                                               palavra_quiz[1]+'\n','red'))
                                                print("Voce ja acertou: " + colored(str(acertos) + "\n",'green') + "Voce ja errou: "
                                                      + colored(str(erros) + "\n", 'red'))

                                                sleep(2)

                                    else:
                                        print(colored('\nInfelizmente não possuimos palavras com essa opcao', 'red'))
                                        sleep(1.5)

                    elif flag != None:
                        while True:
                            print ("\n"+("Vogais".center(60))+"\n\n1 - [ə]\t\t2 - [ɝ]\t\t3 - [ɚ]\t\t4 - [ʌ]\t\t5 - [ɑː]\n\n")
                            pergunta_fonema2 = int(input("Digite e envie a opcao da vogal que queres treinar. Caso queira " 
                                                         "treinar "+colored('consoantes','cyan')+", envie "+colored(' 0','yellow')+". Para sair, envie "+colored(' -1','yellow')+
                                                    "\n(Envie) => "))

                            if pergunta_fonema2 == 0:
                                flag = True
                                break

                            elif pergunta_fonema2 == -1:
                                flag = None
                                break

                            elif pergunta_fonema2 > 5 or pergunta_fonema2 < 0:
                                print("envie apenas as opções disponiveis.")
                                sleep(2)

                            else:
                                while True:
                                    pergunta2 = int(input("\n\nVocê deseja palavras que começam com o fonema escolhido" +
                                                 colored(' [1]','yellow') + ", terminam com ela" + colored(' [2]', 'yellow') +
                                                 ", esteja no meio" + colored(' [3]','yellow') + " ou que contenha o fonema" +
                                                 colored(' [4]','yellow') + "?\nDigite e envie a opção. Caso queira voltar, " 
                                                 "envie " + colored(' 0', 'yellow') + ".\n(Envie) => "))

                                    if pergunta2 == 0:
                                        break

                                    elif pergunta2 > 4 or pergunta2 < 0:
                                        print(colored("\nenvie apenas as opções disponiveis.\n", 'red'))
                                        sleep(1.5)
                                        continue

                                    else:
                                        recebe_fonemas = lista_palavra_fonema(2, pergunta_fonema2, pergunta2)
                                        shuffle(recebe_fonemas)
                                        acertos = 0
                                        erros = 0
                                        if len(recebe_fonemas) != 0:
                                            for palavra_quiz in recebe_fonemas:
                                                print(colored('\n\n' + palavra_quiz[0], 'yellow'))
                                                recebe_resposta = input("\nQual palavra a transcricao fonetica acima corresponde?" 
                                                                        " Caso queira encerrar o quiz, digite 'sair'\n(Envie) =>")

                                                if recebe_resposta.lower() == palavra_quiz[1]:
                                                    acertos += 1
                                                    print(colored('\nParabens! voce acertou!\n', 'green'))
                                                    print("Voce ja acertou: " + colored(str(acertos) + "\n",'green') +
                                                          "Voce ja errou: " + colored(str(erros) + "\n", 'red'))
                                                    sleep(2)

                                                elif recebe_resposta.lower().strip("'") == 'sair':
                                                    print("\nSeu saldo final ficou:\n" + "Acertos: " + colored(str(acertos) +
                                                    "\n", 'green') + "Erros: " + colored(str(erros) + "\n", 'red'))
                                                    sleep(2)
                                                    break

                                                else:
                                                    erros += 1
                                                    print(colored('\nInfelizmente, voce errou\nA resposta certa é: ' +
                                                                  palavra_quiz[1] + '\n', 'red'))
                                                    print("Voce ja acertou: " + colored(str(acertos) + "\n",'green') +
                                                          "Voce ja errou: " + colored(str(erros) + "\n", 'red'))
                                                    sleep(2)

                                        else:
                                            print(colored('\nInfelizmente não possuimos palavras com essa opcao','red'))
                                            sleep(2)

                    else:
                        break

            else:
                while True:
                    pergunta3 = input("\nVoce quer treinar quantas 'x' palavras mais comuns? Digite e envie uma " 
                                 "quantidade.\nCaso queira voltar, envie "+colored(' 0', 'yellow') +"\nEntretanto, se quiser" 
                                 " mandar uma sequencia/range, envie:"+colored('{x-y} como 10-20', 'yellow')+'\nNosso dicionario possui 10 mil ' 
                                 "palavras, quanto mais perto de 0 for a sequencia/range, mais" +colored(' frequentes ', 'yellow')+ "sao tais palavras no ingles"
                                 "\n(Envie) => ")


                    if int(pergunta3) == 0:
                        break

                    elif pergunta3 not in str(list(range(1,100001))) and '-' not in pergunta3:
                        print ("\n"+colored("Quantidade nao possivel",'red'))
                        sleep(1.5)

                    else:
                        nova_lista_palavra = palavras_parser[:int(pergunta3)] if '-' not in pergunta3 else palavras_parser[(int(pergunta3[0:pergunta3.find('-')]))-1:int(pergunta3[pergunta3.find('-')+1:])]
                        shuffle(nova_lista_palavra)
                        acertos = 0
                        erros = 0
                        for contador, palavra in enumerate(nova_lista_palavra):
                            if contador != pergunta3:
                                print(colored('\n\n' + palavra[0], 'yellow'))
                                recebe_resposta = input("\nQual palavra a transcricao fonetica acima corresponde?" 
                                                " Caso queira encerrar o quiz, digite 'sair'\n(Envie) =>")

                                if recebe_resposta.lower() == palavra[1]:
                                    acertos += 1
                                    print(colored('\nParabens! voce acertou!\n', 'green'))
                                    print("Voce ja acertou: " + colored(str(acertos) + "\n", 'green') +
                                        "Voce ja errou: " + colored(str(erros) + "\n", 'red'))
                                    sleep(2)

                                elif recebe_resposta.lower().strip("'") == 'sair':
                                    print("\nSeu saldo final ficou:\n" + "Acertos: " + colored(str(acertos) +
                                    "\n",'green') + "Erros: " + colored(str(erros) + "\n", 'red'))
                                    sleep(2)
                                    break

                                else:
                                    erros += 1
                                    print(colored('\nInfelizmente, voce errou\nA resposta certa é: ' +
                                            palavra_quiz[1] + '\n', 'red'))
                                    print("Voce ja acertou: " + colored(str(acertos) + "\n", 'green') +
                                            "Voce ja errou: " + colored(str(erros) + "\n", 'red'))
                                    sleep(2)

                            else:
                                break

    except ValueError:
        print (colored("\nFavor, apenas envie o numero das opcoes ou as mesmas na sintaxe correta.\n",'red'))
        sleep(2)

    except (KeyboardInterrupt, EOFError):
        break
