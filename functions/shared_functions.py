import pandas as pd
from scipy.spatial import KDTree
from collections import Counter
import ssl

import constants.constants as const
from functions.color_translation import traduzir_cor

def load_color_dataset():
    print("Baixando dataset de cores do GitHub (865 cores)...")
    try:
        # Corrige erro de certificado SSL
        ssl._create_default_https_context = ssl._create_unverified_context
        
        url_dataset = "https://raw.githubusercontent.com/codebrainz/color-names/master/output/colors.csv"
        df_cores = pd.read_csv(url_dataset, names=['Nome', 'Hex', 'R', 'G', 'B'])
        
        valores_rgb = df_cores[['R', 'G', 'B']].values
        nomes_cores = df_cores['Nome'].values
        
        const.arvore_cores = KDTree(valores_rgb)
        const.nomes_cores = nomes_cores
        
        print(f"Sucesso! {len(df_cores)} cores carregadas.")
        return True
    except Exception as e:
        print(f"Erro ao baixar ou processar o dataset: {e}")
        return False

def analyze_region(img_bgr, min_pixels=1, top_n=1):
    pixels_bgr = img_bgr.reshape(-1, 3)
    
    if len(pixels_bgr) < min_pixels: return None

    # Converte de BGR para RGB para comparar com o Dataset
    pixels_rgb = pixels_bgr[:, ::-1] 

    # Busca as cores mais próximas
    distancias, indices = const.arvore_cores.query(pixels_rgb)
    labels = const.nomes_cores[indices]
    
    total = len(labels)
    counter = Counter(labels)

    colors = []
    for label, count in counter.most_common(top_n):
        sel = labels == label
        mean_bgr = pixels_bgr[sel].mean(axis=0).astype(int)
        
        nome_traduzido = traduzir_cor(label)
        
        colors.append({
            "label": nome_traduzido,
            "count": int(count),
            "pct": count / total * 100.0,
            "bgr": (int(mean_bgr[0]), int(mean_bgr[1]), int(mean_bgr[2])),
        })

    return {"total": total, "colors": colors}
