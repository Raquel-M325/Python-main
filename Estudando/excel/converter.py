import re
import pandas as pd

arquivo_sql = "modelo.sql"

with open(arquivo_sql, "r", encoding="utf-8") as f:
    sql = f.read()

tabelas = re.findall(
    r'CREATE TABLE\s+(\w+)\s*\((.*?)\);',
    sql,
    re.S | re.I
)

dados = []

for tabela, conteudo in tabelas:

    linhas = conteudo.splitlines()

    pk_global = []
    fk_info = []

    # PK composta
    pk_match = re.search(r'PRIMARY KEY\s*\((.*?)\)', conteudo, re.I)
    if pk_match:
        pk_global = [x.strip() for x in pk_match.group(1).split(",")]

    # FK
    fk_matches = re.findall(
        r'FOREIGN KEY\s*\((.*?)\)\s*REFERENCES\s*(\w+)\s*\((.*?)\)',
        conteudo,
        re.I
    )

    for f in fk_matches:
        fk_info.append((f[0].strip(), f[1], f[2].strip()))

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
        tipo_original = partes[1].upper()

        # TIPOS INTELIGENTES
        if "email" in campo.lower():
            tipo = "email"
        elif "senha" in campo.lower():
            tipo = "password_hash"
        elif "data" in campo.lower():
            tipo = "datetime"
        elif "descricao" in campo.lower() or "resumo" in campo.lower() or "comentario" in campo.lower():
            tipo = "text"
        elif "imagem" in campo.lower() or "repositorio" in campo.lower():
            tipo = "url"
        elif "nome" in campo.lower() or "titulo" in campo.lower():
            tipo = "varchar"
        else:
            tipo = "integer"

        # tamanho estimado
        tamanho = ""
        if tipo == "varchar":
            tamanho = "255"
        elif tipo == "email":
            tamanho = "255"
        elif tipo == "password_hash":
            tamanho = "255"
        elif tipo == "text":
            tamanho = "max"
        elif tipo == "integer":
            tamanho = "11"

        # PK
        pk = "SIM" if (campo in pk_global or "PRIMARY KEY" in linha.upper()) else ""

        # FK
        fk = ""
        for f in fk_info:
            if f[0] == campo:
                fk = f"{f[1]}({f[2]})"

        # UNIQUE (heurística simples)
        unique = "SIM" if "email" in campo.lower() else ""

        # NULL
        nulo = "NAO" if "NOT NULL" in linha.upper() else "SIM"

        # identity (auto incremento)
        identity = "SIM" if "id" in campo.lower() else ""

        # default
        default = ""

        # restrições
        restricoes = []
        if pk:
            restricoes.append("PRIMARY KEY")
        if fk:
            restricoes.append("FOREIGN KEY")
        if unique:
            restricoes.append("UNIQUE")

        dados.append({
            "Tabela": tabela,
            "Campo": campo,
            "Descrição": "",
            "Tipo de dado": tipo,
            "Tamanho": tamanho,
            "Nulo": nulo,
            "PK": pk,
            "FK": fk,
            "Unique": unique,
            "Identity": identity,
            "Default": default,
            "Restrições": ", ".join(restricoes)
        })

df = pd.DataFrame(dados)

df.to_excel("dicionario_de_dados.xlsx", index=False)

print("Dicionário de dados gerado com sucesso!")