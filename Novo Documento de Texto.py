print(' Formulario Familiar')
p=input('\n Nome do Pai: ')
import os
os.system('clear') or None
m=input('\n Nome da Mãe: ')
import os
os.system('clear') or None
vô=input('\n Nome do Avô: ')
import os
os.system('clear') or None
vó=input('\n Nome da Avó: ')
import os
os.system('clear') or None
irmao=input('\n Você tem Irmao(ã)?\n Sim ou Não: ')
if (irmao==('sim')) or (irmao==('Sim')):
    import os
    os.system('clear') or None
    nomeirmao=input('\n Nome do Irmao(ã): ')

    print('\n Lista de Familiares:\n\n','Pai:',p,'\n\n Mãe:',m,'\n\n Vô:',vô,'\n\n Vó:',vó,'\n\n Irmão(ã):',nomeirmao)
elif (irmao==('não')) or (irmao==('Não')):
    import os
    os.system('clear') or None
    print('\n Lista de Familiares:\n\n','Pai:',p,'\n\n Mãe:',m,'\n\n Vô:',vô,'\n\n Vó:',vó)
