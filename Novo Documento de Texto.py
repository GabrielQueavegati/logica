print(' Formulario Familiar')
p=input('\n Nome do Pai: ')
import os
os.system('clear') or None
m=input('\n Nome da M�e: ')
import os
os.system('clear') or None
v�=input('\n Nome do Av�: ')
import os
os.system('clear') or None
v�=input('\n Nome da Av�: ')
import os
os.system('clear') or None
irmao=input('\n Voc� tem Irmao(�)?\n Sim ou N�o: ')
if (irmao==('sim')) or (irmao==('Sim')):
    import os
    os.system('clear') or None
    nomeirmao=input('\n Nome do Irmao(�): ')

    print('\n Lista de Familiares:\n\n','Pai:',p,'\n\n M�e:',m,'\n\n V�:',v�,'\n\n V�:',v�,'\n\n Irm�o(�):',nomeirmao)
elif (irmao==('n�o')) or (irmao==('N�o')):
    import os
    os.system('clear') or None
    print('\n Lista de Familiares:\n\n','Pai:',p,'\n\n M�e:',m,'\n\n V�:',v�,'\n\n V�:',v�)
