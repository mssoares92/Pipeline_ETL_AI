
import pandas as pd
from google import genai # Importação da nova biblioteca

# --- CONFIGURAÇÃO ---
GOOGLE_API_KEY ="GOOGLE_API_KEY"
# Inicializa o cliente na nova versão
client = genai.Client(api_key=GOOGLE_API_KEY)

# Verifique se esta URL termina com output=csv
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRLsMkYhtnAG51XMKpbeWaLIvO1jdxgWOHkfP2T43sRuGuS02rthmEVrOPrMH9ai4OGgYBp4BSL-zUR/pub?gid=0&single=true&output=csv"

# --- 1. EXTRACT ---
def extract():
    df = pd.read_csv(SHEET_URL)
    # FILTRO: Somente limites de 1000 para cima
    df_filtrado = df[df['limite'] >= 1000].copy()
    return df_filtrado

# --- 2. TRANSFORM ---
def transform(row):
    limite = row['limite']
    
    # Nova lógica de definição de categoria
    if 1000 <= limite < 5000:
        categoria = "Ouro"
        perfil = "Vantagens Ouro (foco em descontos em parceiros e anuidade zero)"
    elif 5000 <= limite < 10000:
        categoria = "Platinum"
        perfil = "Vantagens Platinum (foco em seguros de viagem e concierge)"
    else: # Acima de 10000
        categoria = "Black"
        perfil = "Vantagens Black (foco em salas VIP e pontuação turbinada)"

    prompt = (
        f"Você é um gerente de conta do Santander. O cliente {row['nome']} "
        f"possui limite de R$ {limite:.2f} e categoria {categoria}. "
        f"Crie uma frase de impacto (máximo 120 caracteres) destacando os benefícios e indicando qual das categorias ele se encaixa{categoria}."
    )
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception:
        return f"Aproveite as vantagens do seu cartão {categoria}!"

# --- EXECUÇÃO ---
df = extract()

if df.empty:
    print("Nenhum cliente qualificado para as categorias Ouro, Platinum ou Black.")
else:
    print(f"Processando {len(df)} clientes qualificados...")
    df['mensagem_personalizada'] = df.apply(transform, axis=1)

    print("\n--- Resultado da Segmentação de Cartões ---")
    # Removi o .head() para você ver TODOS os clientes no terminal
    print(df[['nome', 'limite', 'mensagem_personalizada']])
    
    df.to_csv('resultado_segmentado_cartoes.csv', index=False)