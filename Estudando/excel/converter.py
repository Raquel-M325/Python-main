import re
import pandas as pd

arquivo_sql = "modelo.sql"

with open(arquivo_sql, "r", encoding="utf-8") as f:
    sql = f.read()

dados = []

# captura CREATE TABLE
tabelas = re.findall(
    r'CREATE TABLE\s+(\w+)\s*\((.*?)\);',
    sql,
    re.S | re.I
)

for tabela, conteudo in tabelas:

    linhas = conteudo.splitlines()

    for linha in linhas:
        linha = linha.strip().rstrip(",")

        # ignora linhas vazias
        if not linha:
            continue

        # ignora FOREIGN KEY
        if linha.upper().startswith("FOREIGN KEY"):
            continue

        # ignora PRIMARY KEY isolada
        if linha.upper().startswith("PRIMARY KEY"):
            continue

        partes = linha.split()

        if len(partes) < 2:
            continue

        campo = partes[0]
        tipo = partes[1]

        pk = "PRIMARY KEY" in linha.upper()

        dados.append({
            "Tabela": tabela,
            "Campo": campo,
            "Tipo": tipo,
            "PK": "SIM" if pk else ""
        })

# dataframe
df = pd.DataFrame(dados)

# salva excel
df.to_excel("modelo_relacional.xlsx", index=False)

print("Planilha criada com sucesso!")