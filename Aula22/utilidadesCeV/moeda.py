def aumentar(p,v = 0, formatacao = True):
    """ Função que calcula o aumento do preço
        INPUTS:
            p: preço
            v: taxa de aumento em porcento (o padrão é v = 0)
            formatacao: formatar o preco no modo moeda (padrão é True)
        OUTPUTS:
            p*(1+(0.01*v))   
    """
    novo = p*(1+(0.01*v))
    if formatacao:
        novo = moeda(novo)
    return novo
    

def diminuir(p,v = 0, formatacao = True):
    """ Função que calcula a diminuição do preço
        INPUTS:
            p: preço
            v: taxa de diminuição em porcento (o padrão é v = 0)
            formatacao: formatar o preco no modo moeda (padrão é True)
        OUTPUTS:
            p*(1-(0.01*v))   
    """
    novo = p*(1-(0.01*v))
    if formatacao:
        novo = moeda(novo)
    return novo
    
    
def dobro(p, formatacao = True):
    """ Função que calcula o dobro do preço
        INPUTS:
            p: preço
            formatacao: formatar o preco no modo moeda (padrão é True)
        OUTPUTS:
            2*p 
    """
    novo = 2*p
    if formatacao:
        novo = moeda(novo)
    return novo
    
        
def metade(p, formatacao = True):
    """ Função que calcula o aumento do preço
        INPUTS:
            p: preço
            formatacao: formatar o preco no modo moeda (padrão é True)
        OUTPUTS:
            0.5*p
    """
    novo = 0.5*p
    if formatacao:
        novo = moeda(novo)
    return novo

def moeda(p):
    """ Função que formata para moeda o preço
        INPUTS:
            p: preço
        OUTPUTS:
            novo: preço formatado no padrão moeda XX,XX
    """
    p = str(p)
    caracteres = p.split('.')
    p1 = caracteres[0]
    p2 = caracteres[1]
    if len(p2)<2:
        p2 = p2+'0'
    elif len(p2)>2:
        p2 = p2[0:2]
    novo = 'R$'+p1+','+p2
    return novo



def resumo(p, ta, td, formatacao = True):
    print('-'*30)
    print("RESUMO DO VALOR".center(30))
    # print("{: ^30}".format("RESUMO DO VALOR"))
    print('-'*30)
    
    #print(f"Preço analisado:".ljust(20), f" {moeda(p)}".rjust(5))
    print("{: <20}{: >5}".format("Dobro do preço:",dobro(p)))
    #print(f"Dobro do preço:".ljust(20),f"{dobro(p)}".rjust(5))
    print("{: <20}{: >5}".format("Metade do preço:",metade(p)))
    #print(f"Metade do preço:".ljust(20),f"{metade(p)}".rjust(5))
    print("{: <20}{: >5}".format(str(ta) + '% de aumento',aumentar(p,ta)))
    #print(f"{str(ta)}% de aumento".ljust(20),f"{aumentar(p,ta)}".rjust(5))
    print("{: <20}{: >5}".format(str(td) + '% de redução',diminuir(p,td)))
    #print(f"{str(ta)}% de redução".ljust(20),f"{diminuir(p,ta)}".rjust(5))
    
    
    
    
    






