<div align="center">

# 🚢 Predictive Export Intelligence & Logistics Optimization Platform

### AI-Powered Decision Intelligence Platform for Smart Export Planning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Machine%20Learning-XGBoost-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/AI-Agents-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/NLP-FinBERT-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/RAG-Enabled-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Under%20Development-yellow?style=for-the-badge">
</p>

</div>

---

# 📖 Project Overview

Predictive Export Intelligence & Logistics Optimization Platform is an AI-powered decision support system designed to help exporters make smarter business decisions.

The platform combines **Machine Learning, AI Agents, News Sentiment Analysis, and Retrieval-Augmented Generation (RAG)** to analyze historical commodity prices, international trade data, logistics information, and market news.

The objective is to help exporters:

- Predict future commodity prices
- Forecast export demand
- Optimize inventory
- Prioritize shipments
- Select the best shipping routes
- Analyze trade risks
- Maximize overall profit

---

# 🎯 Problem Statement

Global exporters often struggle with:

- Uncertain international demand
- Fluctuating commodity prices
- Manual export planning
- Limited warehouse capacity
- Shipping delays
- Trade restrictions
- Increasing logistics costs

Most export planning still depends on manual analysis and experience, leading to inventory mismanagement, delayed shipments, and reduced profitability.

This project aims to solve these challenges using Artificial Intelligence and Machine Learning.

---

# 🚀 Project Objectives

✔ Predict Commodity Prices

✔ Forecast Export Demand

✔ Inventory Optimization

✔ Smart Container Prioritization

✔ Route Optimization

✔ Trade Risk Analysis

✔ AI-powered Business Recommendations

✔ RAG-based Trade Intelligence Assistant

---

# 🏗️ Project Workflow

```text
                    Historical Datasets
                             │
        ┌────────────────────┼─────────────────────┐
        │                    │                     │
        ▼                    ▼                     ▼
 Commodity Prices      Commodity News       Trade Data
        │                    │
        └──────────────┬─────┘
                       │
              Data Cleaning (EDA)
                       │
             Feature Engineering
                       │
          News Sentiment Analysis
                 (FinBERT)
                       │
          Final Machine Learning Dataset
                       │
              XGBoost Prediction Model
                       │
                  AI Agent
                       │
             Business Recommendation
                       │
                 Export Dashboard
```

---

# 📂 Dataset Used

## 1. Commodity Price Dataset

Historical commodity prices from multiple years.

### Columns

- Date
- Commodity
- Price
- Open Price
- High Price
- Low Price
- Close Price
- Volume

---

## 2. Commodity News Dataset

Collected using **NewsAPI**.

### Columns

- Commodity
- Date
- Title
- Description
- Source

---

## 3. News Sentiment Dataset

Generated using FinBERT.

### Columns

- Commodity
- Date
- Sentiment
- Sentiment Score

---

## 4. Final Machine Learning Dataset

Created after merging commodity prices and news features.

Features include:

- Commodity
- Date
- Price
- Price Change
- Percentage Price Change
- Moving Average (MA7)
- Moving Average (MA30)
- Total News
- Average Sentiment
- Positive News
- Neutral News
- Negative News
- News Growth

Target Variable:

```
Next Price
```

---

# 📊 Exploratory Data Analysis (EDA)

Before training the Machine Learning model, several preprocessing steps were performed.

## Data Cleaning

- Removed duplicate news
- Removed missing values
- Standardized commodity names
- Converted date format
- Removed invalid records

---

## Feature Engineering

Created new features:

- Price Change
- Percentage Price Change
- MA7
- MA30
- Total News
- Average Sentiment
- Positive News Count
- Neutral News Count
- Negative News Count
- News Growth

---

## Dataset Merging

Merged commodity price dataset with sentiment dataset using:

- Commodity
- Date

---

## Target Variable Creation

Created:

```python
df["next_price"] = df["price"].shift(-1)
```

This becomes the target variable for Machine Learning.

---

# 🤖 Sentiment Analysis

Financial news sentiment is generated using **FinBERT**.

Model Used

```
ProsusAI/finbert
```

Sentiment Values

| Sentiment | Value |
|-----------|-------|
| Positive | 1 |
| Neutral | 0 |
| Negative | -1 |

---

# 🧠 Machine Learning Model

## Current Model

### XGBoost Regressor

Purpose:

Predict future commodity prices.

### Input Features

- Price
- MA7
- MA30
- Price Change
- Total News
- Average Sentiment
- Positive News
- Neutral News
- Negative News
- News Growth

Target

```
Next Price
```

---

# 🤖 AI Agents

## Commodity Price Prediction Agent

Functions

- Reads latest commodity news
- Extracts useful information
- Predicts future commodity price
- Explains prediction

---

## Hugging Face AI Agent

Model

```
HuggingFaceH4/zephyr-7b-beta
```

Functions

- Business Recommendation
- Price Explanation
- Market Analysis

---

# ⚙️ Technologies Used

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Machine Learning | XGBoost |
| NLP | FinBERT |
| AI Agent | Groq Llama 3.3 |
| LLM | Hugging Face |
| Data Processing | Pandas |
| Numerical Computing | NumPy |
| Visualization | Matplotlib |
| Notebook | Jupyter |
| Version Control | Git & GitHub |

---

# ✅ Current Progress

Completed Modules

- Commodity Price Prediction
- Data Collection
- Data Cleaning
- Feature Engineering
- News Sentiment Analysis
- XGBoost Model
- AI Agent

---

# 🚀 Future Modules

## Demand Forecasting

Predict future demand for each country.

Model

- XGBoost
- LSTM

---

## Inventory Optimization

Predict warehouse inventory requirements.

Model

- Random Forest

---

## Container Prioritization

Prioritize export containers based on:

- Profit
- Delivery Deadline
- Customer Priority

Model

- XGBoost

---

## Route Optimization

Recommend best shipping route.

Algorithms

- Dijkstra
- A*

---

## Trade Risk Prediction

Analyze:

- Inflation
- GDP
- Political Stability
- Exchange Rate

Model

- XGBoost

---

## Country Segmentation

Cluster countries according to:

- Trade Volume
- Demand
- Revenue

Model

- K-Means Clustering

---

## Logistics Anomaly Detection

Detect:

- Shipping Delays
- Abnormal Costs
- Fraud

Model

- Isolation Forest

---

## RAG Trade Intelligence Assistant

Answer exporter questions such as:

- Which country should I export to?
- Which commodity is profitable?
- Current trade policies
- Latest market trends

---

# 📈 Machine Learning Roadmap

| Module | Model |
|----------|--------|
| Commodity Price Prediction | XGBoost |
| Demand Forecasting | LSTM / XGBoost |
| Inventory Optimization | Random Forest |
| Container Prioritization | XGBoost |
| Trade Risk Prediction | XGBoost |
| Country Segmentation | K-Means |
| Route Optimization | Dijkstra |
| Logistics Anomaly Detection | Isolation Forest |

---

# 📦 Installation

```bash
git clone https://github.com/yourusername/Predictive-Export-Intelligence.git

cd Predictive-Export-Intelligence

pip install -r requirements.txt
```

---

# ▶️ Run

```bash
python collect_news.py

python clean_news.py

python sentiment.py

python feature_engineering.py

python create_final_dataset.py

python commodity_agent.py
```

---

# 📌 Future Scope

- AI-powered Export Planning
- Multi-Agent Decision Support
- Global Demand Prediction
- Real-time Commodity Forecasting
- Smart Logistics Planning
- Route Optimization
- Risk Monitoring
- Interactive Dashboard
- RAG-based Export Assistant

---

# 👨‍💻 Author

## Mohasin Nadaf

🎓 B.Tech – D. Y. Patil College of Engineering & Technology, Kolhapur

🎓 PG-Diploma in Big Data Analytics (DBDA), C-DAC Mumbai

💻 Machine Learning | Data Engineering | AI Agents | Generative AI

---

<div align="center">

### ⭐ If you found this project useful, please consider giving it a Star ⭐

</div>
