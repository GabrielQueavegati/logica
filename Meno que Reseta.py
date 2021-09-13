controle=True
while controle:
    import os
    os.system('clear') or None
    
    print('\n Boas Vindas')
    
    RST=input('\n Você Deseja:\n 1-Sacar\n 2-Depositar\n 3-Sair\n\n Digite aqui: ')
    if (RST==('Sacar')) or (RST==('sacar')) or (RST==('1')):
        import os
        os.system('clear') or None
        
        print('\n Saque com Sucesso ')
        controle=False
    elif (RST==('Depositar')) or (RST==('depositar')) or (RST==('2')):
        import os
        os.system('clear') or None
        
        print('\n Saque com Sucesso ')
        controle=False
    elif (RST==('Sair')) or (RST==('sair')) or (RST==('3')):
        controle=False
        import os
        os.system('clear') or None
    