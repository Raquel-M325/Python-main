import re
import pandas as pd

arquivo_sql = "modelo.sql"

with open(arquivo_sql, "r", encoding="utf-8") as f:
    sql = f.read()

tabelas = []

create_tables = re.findall(
    r'CREATE TABLE (\w+)\s*\((.*?)\);',
    sql,
    re.S | re.I
)

for tabela, conteudo in create_tables:
    linhas = conteudo.split(",")

    for linha in linhas:
        linha = linha.strip()

        if linha.upper().startswith("FOREIGN KEY"):
            continue

        partes = linha.split()

        if len(partes) >= 2:
            campo = partes[0]
            tipo = partes[1]

            pk = "PRIMARY KEY" in linha.upper()

            tabelas.append({
                "Tabela": tabela,
                "Campo": campo,
                "Tipo": tipo,
                "PK": "Sim" if pk else ""
            })

df = pd.DataFrame(tabelas)

df.to_excel("modelo_relacional.xlsx", index=False)

print("Planilha criada com sucesso!")