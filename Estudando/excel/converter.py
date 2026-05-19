import re
import pandas as pd

arquivo_sql = "modelo.sql"

with open(arquivo_sql, "r", encoding="utf-8") as f:
    sql = f.read()

dados = []

tabelas = re.findall(
    r'CREATE TABLE\s+(\w+)\s*\((.*?)\);',
    sql,
    re.S | re.I
)

for tabela, conteudo in tabelas:

    linhas = conteudo.splitlines()

    for linha in linhas:

        linha = linha.strip().rstrip(",")

        if not linha:
            continue

        if linha.upper().startswith("PRIMARY KEY"):
            continue

        if linha.upper().startswith("FOREIGN KEY"):
            continue

        partes = linha.split()

        if len(partes) < 2:
            continue

        campo = partes[0]

        # TIPAGEM INTELIGENTE
        if "email" in campo.lower():
            tipo = "email_field"

        elif "senha" in campo.lower():
            tipo = "password"

        elif "data" in campo.lower():
            tipo = "date"

        elif "descricao" in campo.lower() or "resumo" in campo.lower() or "comentario" in campo.lower():
            tipo = "text"

        elif "imagem" in campo.lower() or "repositorio" in campo.lower():
            tipo = "url"

        elif "nome" in campo.lower() or "titulo" in campo.lower() or "login" in campo.lower():
            tipo = "string"

        else:
            tipo = "integer"

        dados.append({
            "Tabela": tabela,
            "Campo": campo,
            "Tipo": tipo
        })

df = pd.DataFrame(dados)

df.to_excel("modelo_relacional.xlsx", index=False)

print("Planilha criada!")