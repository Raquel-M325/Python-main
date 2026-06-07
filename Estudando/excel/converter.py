import re
import pandas as pd

arquivo_sql = "modelo.sql"

with open(arquivo_sql, "r", encoding="utf-8") as f:
    sql = f.read()

# Remove comentários
sql = re.sub(r'--.*', '', sql)

# Captura tabelas
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

    # Captura PRIMARY KEY
    pk_match = re.search(
        r'PRIMARY\s+KEY\s*\((.*?)\)',
        conteudo,
        flags=re.I | re.S
    )

    if pk_match:
        pk_global = [
            campo.strip()
            for campo in pk_match.group(1).split(",")
        ]

    # Captura FOREIGN KEY
    fk_matches = re.findall(
        r'FOREIGN\s+KEY\s*\((.*?)\)\s*REFERENCES\s*(\w+)\s*\((.*?)\)',
        conteudo,
        flags=re.I
    )

    for campo_fk, tabela_ref, campo_ref in fk_matches:
        fk_info.append({
            "campo": campo_fk.strip(),
            "tabela": tabela_ref.strip(),
            "referencia": campo_ref.strip()
        })

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

        tipo_match = re.match(
            r'^\w+\s+([A-Z]+(?:\(\d+(?:,\d+)?\))?)',
            linha,
            flags=re.I
        )

        if tipo_match:
            tipo_completo = tipo_match.group(1).upper()
        else:
            tipo_completo = partes[1].upper()

        tamanho = ""

        tamanho_match = re.search(
            r'\((.*?)\)',
            tipo_completo
        )

        if tamanho_match:
            tamanho = tamanho_match.group(1)

        tipo_dado = re.sub(
            r'\(.*\)',
            '',
            tipo_completo
        )

        pk = "SIM" if campo in pk_global else ""

        fk = ""

        for item in fk_info:
            if item["campo"] == campo:
                fk = f'{item["tabela"]}({item["referencia"]})'
                break

        nulo = "NAO" if "NOT NULL" in linha.upper() else "SIM"

        unique = "SIM" if "UNIQUE" in linha.upper() else ""

        identity = ""

        if campo.lower().startswith("id_"):
            identity = "SIM"

        default = ""

        default_match = re.search(
            r'DEFAULT\s+([^,\s]+)',
            linha,
            flags=re.I
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
            "Tipo de dado": tipo_dado,
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

colunas = [
    "Tabela",
    "Campo",
    "Descrição",
    "Tipo de dado",
    "Tamanho",
    "Nulo",
    "PK",
    "FK",
    "Unique",
    "Identity",
    "Default",
    "Restrições"
]

df = df[colunas]

df.to_excel(
    "dicionario_de_dados.xlsx",
    index=False
)

print("Dicionário de dados gerado com sucesso!")