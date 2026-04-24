# 📦 Análise de Consumo e Geração Automática de Pedidos

## 📌 Visão Geral

Este projeto automatiza a análise de consumo de materiais e a geração de pedidos mensais com base em dados históricos.

O sistema processa dados em Excel, filtra períodos específicos, calcula o consumo por produto e gera relatórios e visualizações para apoiar a tomada de decisão.

---

## 🎯 Objetivo

Eliminar processos manuais na análise de consumo e automatizar a criação de pedidos mensais de forma eficiente e padronizada.

---

## ⚙️ Funcionalidades

* 📥 Leitura e processamento de dados em Excel
* 📅 Filtro por um ou múltiplos meses
* 🧹 Tratamento e limpeza de dados
* 📊 Cálculo do consumo por produto
* 📄 Geração automática de pedidos (Excel)
* 📈 Visualização da distribuição de consumo (gráficos)

---

## 📁 Estrutura do Projeto

```bash
inventory-demand-analysis/
│
├── data/
│   └── BD_07_2025.xlsx
│
├── src/
│   ├── main.py
│   ├── processar_dados.py
│   ├── analise.py
│   └── visualizacao.py
│
├── outputs/
│   ├── pedidos.xlsx
│   └── distribuicao_produtos.png
│
├── README.md
└── requirements.txt
```

---

## 🚀 Como Executar

```bash
python src/main.py
```

---

## 📊 Saídas Geradas

* 📄 `pedidos.xlsx` → consolidação do consumo por produto
* 📈 `distribuicao_produtos.png` → gráfico de distribuição dos itens

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Matplotlib
* OpenPyXL

---

## 🧠 Conceitos Aplicados

* Análise de Dados
* ETL (Extração, Transformação e Carga)
* Tratamento de dados
* Agregação de informações
* Automação de processos
* Regras de negócio

---

## 💼 Valor de Negócio

* Redução de trabalho manual
* Padronização do processo de pedidos
* Maior confiabilidade nos dados
* Suporte à tomada de decisão baseada em dados

---

## 📌 Observações

* O sistema permite análise de múltiplos meses
* Apenas colunas específicas (produtos) são consideradas no cálculo
* O projeto simula um cenário real de controle de estoque e consumo

---

## 👨‍💻 Autor

Desenvolvido por **Lincolns Rocha**
