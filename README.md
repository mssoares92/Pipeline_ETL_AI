# Pipeline ETL: Análise de Crédito com Gemini AI 🚀

Projeto desenvolvido para o desafio Pipeline ETL Analise de Dados | TOTVS e DIO.

## 🛠️ Tecnologias
- **Python** (Pandas)
- **Google Gemini API** (IA Generativa para mensagens personalizadas)
- **Google Sheets** (Fonte de dados)

## 📋 Fluxo ETL
1. **Extract**: Leitura de dados de uma planilha Google Sheets (CSV). Filtragem de clientes com limite > 1000.
2. **Transform**: Classificação dos clientes em categorias (Ouro, Platinum, Black) e geração de mensagens de marketing via IA.
3. **Load**: Exportação dos resultados para um novo arquivo CSV.
