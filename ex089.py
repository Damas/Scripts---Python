ficha = list()

while True:
    nome = str(input('Digite o nome: '))
    nota1 = int(input('Digite a nota: '))
    nota2 = int(input('Digite a nota: '))
    
    media = (nota1 + nota2) / 2
    
    ficha.append([nome,[nota1,nota2], media])
    resp = str(input('Quer continuar? S/N: '))
    if resp in 'Nn':
        break
print('-' * 35)
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":>8}')
print('-' * 35)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<15}{a[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Mostra nota de qual aluno? (999 interrompe) '))
    if opc == 999:
        break
    if opc == (len(ficha) - 1):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('\n \033[32m >>>>>>>>>>>>>>>>>>>>>>> VOLTE SEMPRE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')
        