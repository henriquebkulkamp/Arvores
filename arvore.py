DataBaseArvores = []
Database = {}

def checarSeExiste(valor):
    existe = False
    for possibilidade in DataBaseArvores:
        if (valor == possibilidade):
            existe = True
            break
    return existe

def criarNoPrincipal(valor, proximoValor="None"):
    if (checarSeExiste(valor)):
        return
    
    DataBaseArvores.append(valor)

    Database[valor] = {
        "valor": valor,
        "proximoValor": proximoValor
        }
    
    return {
        "valor": valor,
        "proximosValores": proximoValor
    }

def criarFolha(caminho, valor, proximoValor = "None"): 
    if (not checarSeExiste(caminho[0])):
        return

    particao = Database[caminho[0]]

    for i in range( 1, len(caminho)-1 ):
        print(particao)
        particao = particao[caminho[i]]
    
    if particao["proximoValor"] == "None":
        particao["proximoValor"] = [{
            "valor": valor,
            "valorAnterior": caminho[ len(caminho)-1 ],
            "proximoValor": proximoValor
        }]
    else:
        particao["proximoValor"].append({
            "valor": valor,
            "valorAnterior": caminho[ len(caminho)-1 ],
            "proximoValor": proximoValor
        })

    return {
        "valor": valor,
        "valorAnterior": caminho[ len(caminho)-1 ],
        "proximosValor": proximoValor
    }



# ----------------------------------------------------------------
# AQUI TEM UNS VALORES HARDCODED PRA TESTA MESMO!
# criarNoPrincipal('Disco C')
# criarFolha('Disco C', 'Usuarios')
# criarFolha(['Disco C', 'Usuarios'], 'Henrique')
# criarFolha(['Disco C', 'Usuarios'], 'User 2')
# print(Database)
