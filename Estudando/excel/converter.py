import re
import pandas as pd

arquivo_sql = "modelo.sql"

with open(arquivo_sql, "r", encoding="utf-8") as f:
    sql = f.read()

sql = re.sub(r'--.*', '', sql)

tabelas = re.findall(
    r'CREATE\s+TABLE\s+(\w+)\s*\((.*?)\);',
    sql,
    flags=re.S | re.I
)

dados = []

for tabela, conteudo in tabelas:

    linhas = conteudo.splitlines()

    pk_global = []
    fk_info = []

    pk_match = re.search(
        r'PRIMARY\s+KEY\s*\((.*?)\)',
        conteudo,
        re.I | re.S
    )

    if pk_match:
        pk_global = [
            campo.strip()
            for campo in pk_match.group(1).split(",")
        ]

    fk_matches = re.findall(
        r'FOREIGN\s+KEY\s*\((.*?)\)\s*REFERENCES\s*(\w+)\s*\((.*?)\)',
        conteudo,
        re.I
    )

    for campo_fk, tabela_ref, campo_ref in fk_matches:
        fk_info.append(
            (
                campo_fk.strip(),
                tabela_ref.strip(),
                campo_ref.strip()
            )
        )

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

        campo = partes[0].strip()
        tipo_original = partes[1].strip()

        pk = "SIM" if campo in pk_global else ""

        fk = ""

        for campo_fk, tabela_ref, campo_ref in fk_info:
            if campo_fk == campo:
                fk = f"{tabela_ref}({campo_ref})"
                break

        nulo = "NAO" if "NOT NULL" in linha.upper() else "SIM"

        unique = "SIM" if "UNIQUE" in linha.upper() else ""

        identity = (
            "SIM"
            if "AUTO_INCREMENT" in linha.upper()
            else ""
        )

        default = ""

        default_match = re.search(
            r'DEFAULT\s+([^,\s]+)',
            linha,
            re.I
        )

        if default_match:
            default = default_match.group(1)

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
            "Tipo de dado": tipo_original,
            "Nulo": nulo,
            "PK": pk,
            "FK": fk,
            "Unique": unique,
            "Identity": identity,
            "Default": default,
            "Restrições": ", ".join(restricoes)
        })

df = pd.DataFrame(dados)

ordem_colunas = [
    "Tabela",
    "Campo",
    "Descrição",
    "Tipo de dado",
    "Nulo",
    "PK",
    "FK",
    "Unique",
    "Identity",
    "Default",
    "Restrições"
]

df = df[ordem_colunas]

df.to_excel(
    "dicionario_de_dados.xlsx",
    index=False
)

print("Dicionário de dados gerado com sucesso!")