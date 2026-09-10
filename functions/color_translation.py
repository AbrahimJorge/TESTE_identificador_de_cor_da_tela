TRADUCOES_EXATAS = {
    "Navy Blue": "Azul Marinho",
    "Hot Pink": "Rosa Choque",
    "Sky Blue": "Azul Céu",
    "Forest Green": "Verde Floresta",
    "Steel Blue": "Azul Aço",
    "Light Blue": "Azul Claro",
    "Dark Blue": "Azul Escuro",
    "Light Green": "Verde Claro",
    "Dark Green": "Verde Escuro",
    "Light Red": "Vermelho Claro",
    "Dark Red": "Vermelho Escuro",
    "Sea Green": "Verde Mar",
    "Midnight Blue": "Azul Meia-Noite",
    "Dodger Blue": "Azul Dodger",
    "Cornflower Blue": "Azul Centáurea",
    "Dark Slate Blue": "Azul Ardósia Escuro",
    "Light Slate Gray": "Cinza Ardósia Claro",
    "Dark Slate Gray": "Cinza Ardósia Escuro"
}

DICIONARIO_GERAL = {
    "Red": "Vermelho", 
    "Blue": "Azul", 
    "Green": "Verde", 
    "Yellow": "Amarelo",
    "Black": "Preto", 
    "White": "Branco", 
    "Gray": "Cinza", 
    "Grey": "Cinza",
    "Orange": "Laranja", 
    "Purple": "Roxo", 
    "Pink": "Rosa", 
    "Brown": "Marrom",
    "Cyan": "Ciano", 
    "Magenta": "Magenta", 
    "Gold": "Dourado", 
    "Silver": "Prata",
    "Navy": "Marinho",
    "Teal": "Verde-azulado",
    "Olive": "Oliva",
    "Maroon": "Bordô",
    "Crimson": "Carmesim",
    "Indigo": "Índigo",
    "Violet": "Violeta",
    "Coral": "Coral",
    "Salmon": "Salmão",
    "Peach": "Pêssego",
    "Plum": "Ameixa",
    "Orchid": "Orquídea",
    "Turquoise": "Turquesa",
    "Khaki": "Caqui",
    "Beige": "Bege",
    "Ivory": "Marfim",
    "Slate": "Ardósia",
    "Aquamarine": "Água-marinha",
    "Lavender": "Lavanda",
    "Mint": "Menta",
    "Chocolate": "Chocolate",
    "Dark": "Escuro", 
    "Light": "Claro", 
    "Deep": "Forte", 
    "Pale": "Pálido",
    "Medium": "Médio",
    "Bright": "Brilhante",
    "Royal": "Real",
    "Antique": "Antigo"
}

def traduzir_cor(nome_em_ingles):
    """
    Traduz nomes de cores do inglês para o português de forma robusta.
    Tenta primeiro uma tradução exata e depois aplica substituições com ajustes gramaticais.
    """
    # 1. Tenta tradução exata
    if nome_em_ingles in TRADUCOES_EXATAS:
        return TRADUCOES_EXATAS[nome_em_ingles]
        
    nome_pt = nome_em_ingles
    
    # 2. Processa traduções gerais
    # Ordenar por tamanho da chave (maiores primeiro) ajuda a substituir palavras maiores antes
    for eng, pt in sorted(DICIONARIO_GERAL.items(), key=lambda item: len(item[0]), reverse=True):
        nome_pt = nome_pt.replace(eng, pt)
        
    # 3. Ajustes gramaticais
    # Como o inglês coloca o adjetivo antes (ex: Dark Blue), o replace simples gera "Escuro Azul".
    # Vamos reverter a ordem para os casos mais comuns.
    ajustes = {
        "Escuro Azul": "Azul Escuro",
        "Claro Azul": "Azul Claro",
        "Forte Azul": "Azul Forte",
        "Pálido Azul": "Azul Pálido",
        "Médio Azul": "Azul Médio",
        "Escuro Verde": "Verde Escuro",
        "Claro Verde": "Verde Claro",
        "Forte Verde": "Verde Forte",
        "Pálido Verde": "Verde Pálido",
        "Escuro Vermelho": "Vermelho Escuro",
        "Claro Vermelho": "Vermelho Claro",
        "Escuro Cinza": "Cinza Escuro",
        "Claro Cinza": "Cinza Claro",
        "Escuro Laranja": "Laranja Escuro",
        "Claro Laranja": "Laranja Claro",
        "Escuro Rosa": "Rosa Escuro",
        "Claro Rosa": "Rosa Claro",
        "Forte Rosa": "Rosa Forte",
        "Escuro Marrom": "Marrom Escuro",
        "Claro Marrom": "Marrom Claro",
        "Escuro Roxo": "Roxo Escuro",
        "Claro Roxo": "Roxo Claro"
    }
    
    for padrao, correcao in ajustes.items():
        if padrao in nome_pt:
            nome_pt = nome_pt.replace(padrao, correcao)

    return nome_pt
