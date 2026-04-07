# Tabela ICMS interestadual (%) — baseada na tabela ANTT/CONFAZ
# Linha = Origem, Coluna = Destino

ESTADOS = ["AC","AL","AM","AP","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RN","RS","RJ","RO","RR","SC","SP","SE","TO","IM"]

# Matriz de alíquotas origem x destino
# Fonte: tabela ICMS 2021 (imagem fornecida)
ICMS_MATRIX = {
    "AC": {"AC":17,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "AL": {"AC":12,"AL":17,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "AM": {"AC":12,"AL":12,"AM":18,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "AP": {"AC":12,"AL":12,"AM":12,"AP":18,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "BA": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":18,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "CE": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":18,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "DF": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":18,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "ES": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":18,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "GO": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":17,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "MA": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":18,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "MT": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":17,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "MS": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":17,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "MG": {"AC":7,"AL":7,"AM":7,"AP":7,"BA":7,"CE":7,"DF":7,"ES":7,"GO":7,"MA":7,"MT":7,"MS":7,"MG":18,"PA":7,"PB":7,"PR":12,"PE":7,"PI":7,"RN":7,"RS":12,"RJ":12,"RO":7,"RR":7,"SC":12,"SP":12,"SE":7,"TO":7,"IM":4},
    "PA": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":17,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "PB": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":18,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "PR": {"AC":7,"AL":7,"AM":7,"AP":7,"BA":7,"CE":7,"DF":7,"ES":7,"GO":7,"MA":7,"MT":7,"MS":7,"MG":12,"PA":7,"PB":7,"PR":18,"PE":7,"PI":7,"RN":7,"RS":12,"RJ":12,"RO":7,"RR":7,"SC":12,"SP":12,"SE":7,"TO":7,"IM":4},
    "PE": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":18,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "PI": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":18,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "RN": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":18,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "RS": {"AC":7,"AL":7,"AM":7,"AP":7,"BA":7,"CE":7,"DF":7,"ES":7,"GO":7,"MA":7,"MT":7,"MS":7,"MG":12,"PA":7,"PB":7,"PR":12,"PE":7,"PI":7,"RN":7,"RS":17,"RJ":12,"RO":7,"RR":7,"SC":12,"SP":12,"SE":7,"TO":7,"IM":4},
    "RJ": {"AC":7,"AL":7,"AM":7,"AP":7,"BA":7,"CE":7,"DF":7,"ES":7,"GO":7,"MA":7,"MT":7,"MS":7,"MG":12,"PA":7,"PB":7,"PR":12,"PE":7,"PI":7,"RN":7,"RS":12,"RJ":17.5,"RO":7,"RR":7,"SC":12,"SP":12,"SE":7,"TO":7,"IM":4},
    "RO": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":17.5,"RR":12,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "RR": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":17,"SC":12,"SP":12,"SE":12,"TO":12,"IM":4},
    "SC": {"AC":7,"AL":7,"AM":7,"AP":7,"BA":7,"CE":7,"DF":7,"ES":7,"GO":7,"MA":7,"MT":7,"MS":7,"MG":12,"PA":7,"PB":7,"PR":12,"PE":7,"PI":7,"RN":7,"RS":12,"RJ":12,"RO":7,"RR":7,"SC":17,"SP":12,"SE":7,"TO":7,"IM":4},
    "SP": {"AC":7,"AL":7,"AM":7,"AP":7,"BA":7,"CE":7,"DF":7,"ES":7,"GO":7,"MA":7,"MT":7,"MS":7,"MG":12,"PA":7,"PB":7,"PR":12,"PE":7,"PI":7,"RN":7,"RS":12,"RJ":12,"RO":7,"RR":7,"SC":12,"SP":18,"SE":7,"TO":7,"IM":4},
    "SE": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":18,"TO":12,"IM":4},
    "TO": {"AC":12,"AL":12,"AM":12,"AP":12,"BA":12,"CE":12,"DF":12,"ES":12,"GO":12,"MA":12,"MT":12,"MS":12,"MG":12,"PA":12,"PB":12,"PR":12,"PE":12,"PI":12,"RN":12,"RS":12,"RJ":12,"RO":12,"RR":12,"SC":12,"SP":12,"SE":12,"TO":18,"IM":4},
    "IM": {"AC":4,"AL":4,"AM":4,"AP":4,"BA":4,"CE":4,"DF":4,"ES":4,"GO":4,"MA":4,"MT":4,"MS":4,"MG":4,"PA":4,"PB":4,"PR":4,"PE":4,"PI":4,"RN":4,"RS":4,"RJ":4,"RO":4,"RR":4,"SC":4,"SP":4,"SE":4,"TO":4,"IM":4},
}

def get_aliquota_icms(origem: str, destino: str) -> float:
    origem = origem.upper()
    destino = destino.upper()
    if origem not in ICMS_MATRIX:
        raise ValueError(f"Estado de origem inválido: {origem}")
    if destino not in ICMS_MATRIX[origem]:
        raise ValueError(f"Estado de destino inválido: {destino}")
    return ICMS_MATRIX[origem][destino]
