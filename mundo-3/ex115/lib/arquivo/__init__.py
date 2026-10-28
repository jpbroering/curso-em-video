from lib.interface import escreva, leiaInt

def arquivoExiste(caminho):
    try:
        a = open(caminho, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(caminho):
    try:
        a = open(caminho, 'x')
        a.close()
    except:
        print('HOUVE ALGUM ERRO AO CRIAR O ARQUIVO!')
    else:
        print('ARQUIVO CRIADO COM SUCESSO!')


def cadastrar(caminho, nome, idade):
    try:
        a = open(caminho, '+a')
    except:
        print('HOUVE ALGUM ERRO AO ABRIR O ARQUIVO!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
            print('PESSOA CADASTRADA COM SUCESSO!')
        except:
            print('HOUVE ALGUM ERRO AO ESCREVER NO ARQUIVO!')
    finally:
        a.close()


def listar(caminho):
    try:
        a = open(caminho, 'r')
    except:
        print('HOUVE ALGUM ERRO AO ABRIR O ARQUIVO!')
    else:
        escreva('PESSOAS CADASTRADAS')
        for linha in a:
            cadastro = linha.split(';')
            cadastro[1] = cadastro[1].replace('\n', '')
            print(f'{cadastro[0]:<30}{cadastro[1]:>3} anos')
    finally:
        a.close()