import sys
import os
from sha256 import sha256_hex

def main():
    
    if len(sys.argv) < 3:
        print('Como usar:')
        print(' Gerar: python autenticador.py gerar <documento>')
        print(' Verificar: python autenticador.py verificar <arquivo> <hash salvo>')
        exit()

    comando = sys.argv[1].lower()
    caminho = sys.argv[2]

    if not os.path.isfile(caminho):
        print('ERRO: Arquivo não encontrado')
        exit()

    with open(caminho, 'rb') as arquivo:
        conteudo = arquivo.read()

    hash_calculado = sha256_hex(conteudo)

    if comando == 'gerar':
        print(f'\nHash SHA256:\n{hash_calculado}')
        print('\nSalve o hash para validar o arquivo depois.')

    elif comando == 'verificar':
        if len(sys.argv) < 4:
            print('ERRO: Informe o hash')
            exit()

        hash_recebido = sys.argv[3].lower()

        print(f'\nHash do arquivo:\n{hash_calculado}')
        print(f'\nHash Informado:\n{hash_recebido}')

        if hash_calculado == hash_recebido:
            print('\nArquivo autentico')
        else:
            print('\nArquivo Invalido')

    else:
        print('ERRO: Comando invalido')
        
if __name__ == "__main__":
    main()