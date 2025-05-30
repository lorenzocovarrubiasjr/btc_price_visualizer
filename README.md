# 📈 BTC 30-Day Price Visualizer

This is a Python app that fetches the last 30 days of Bitcoin price data using the [CoinGecko API](https://www.coingecko.com/en/api), formats the data with `pandas`, and visualizes it with an interactive candlestick chart using `plotly`. The result is saved as an HTML file for easy viewing.

---
![Image Description](https://live.staticflickr.com/65535/54553957322_c5cb624134_b.jpg)

## 🚀 Features

- Fetches real-time BTC price data from CoinGecko
- Calculates and displays:
  - First price of the period
  - Last price
  - Minimum price
  - Maximum price
- Creates an interactive candlestick chart
- Exports the chart as a self-contained `.html` file

---

## 🧰 Tech Stack

- **Python**
- **[PyCoinGecko](https://pypi.org/project/pycoingecko/)** – API client for CoinGecko
- **[pandas](https://pandas.pydata.org/)** – For data formatting and analysis
- **[plotly](https://plotly.com/python/)** – For visualizing data as a candlestick chart

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/btc-30day-tracker.git
cd btc-30day-tracker
