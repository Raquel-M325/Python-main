from telethon import TelegramClient

# Obtenha suas credenciais gratuitas em https://my.telegram.org
api_id = 0  # Substitua pelo seu api_id
api_hash = '0'

client = TelegramClient('sessao_pesquisa', api_id, api_hash)

async def analisar_membros():
    # Substitua pelo nome de usuário do grupo ou link
    grupo = await client.get_entity('https://t.me/potilivre') 
    
    membros = await client.get_participants(grupo)
    
    total = len(membros)
    deletados = 0
    bots = 0
    ativos = 0
    
    for m in membros:
        if m.deleted:
            deletados += 1
        elif m.bot:
            bots += 1
        else:
            ativos += 1
            
    print(f"--- RELATÓRIO DO GRUPO ---")
    print(f"Total registrado: {total}")
    print(f"Contas Deletadas: {deletados}")
    print(f"Bots: {bots}")
    print(f"Membros Humanos Ativos (N real): {ativos}")

with client:
    client.loop.run_until_complete(analisar_membros())


