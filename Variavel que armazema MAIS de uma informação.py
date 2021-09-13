import os
al=input('\n Aluno: ')
if (al==('gabriel')):
    os.system('clear') or None
    print('\n Digite aqui suas notas\n')
    nta=int(input(' Primeiro Bimestre: ')),int(input(' Segundo Bimestre: ')), int(input(' Terceiro Bimestre: ')),int(input(' Quarto Bimestre: '))
    os.system('clear') or None
    print('\n Sua Média é:',(nta[0]+nta[1]+nta[2]+nta[3])/4)
elif (al==('igor')):
    os.system('clear') or None
    print('\n Digite aqui suas notas\n')
    nta=int(input(' Primeiro Bimestre: ')),int(input(' Segundo Bimestre: ')), int(input(' Terceiro Bimestre: ')),int(input(' Quarto Bimestre: '))
    os.system('clear') or None
    print('\n Sua Média é:',(nta[0]+nta[1]+nta[2]+nta[3])/4)
else:
    os.system('clear') or None
    print('\n Nome Incorreto')
print('-------------------\n Notas Registradas\n\n 1ºBimestre:',nta[0],'\n 2ºBimestre:',nta[1],'\n 3ºBimestre:',nta[2],'\n 4ºBimestre:',nta[3])
    