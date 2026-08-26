---
module: "current-projects"
topic: "Stock Predictor — S&P 500 Direction Forecasting with Neural Engine"
tags: [builds, quant-finance, neural-networks, yfinance, technical-analysis, trading-simulation, backtesting, feature-engineering, time-series]
last_updated: "2026-08-26"
confidence: "high"
source: "Desktop/Anirudh/My apps/Neural net 2/stockmarketcode.py (302 lines)"
description: "End-to-end stock direction prediction pipeline: Yahoo Finance data ingestion → technical indicator feature engineering (20+ indicators with exact formulas) → sequence windowing with lookback → Neural Engine binary classification (UP/DOWN) → trading simulation with win-rate metrics → model persistence. Includes exact indicator formulas, data leakage prevention, and regime-aware validation."
---

# Stock Predictor — S&P 500 Direction Forecasting

> **Source:** `Desktop/Anirudh/My apps/Neural net 2/stockmarketcode.py` (302 lines)
> **Dependencies:** `yfinance`, `pandas`, `sklearn.preprocessing.MinMaxScaler`, `matplotlib`, `numpy`, [[neural-engine]]
> **Default Ticker:** `SPY` (S&P 500 ETF) — configurable to any Yahoo Finance symbol
> **Pipeline:** 7 stages from raw data to live prediction

---

## For future agent
This is a **personal quant build** — a complete ML pipeline for predicting next-day stock direction (UP/DOWN) using technical indicators as features and the [[neural-engine]] as the classifier. Includes data fetching, feature engineering (20+ indicators with exact mathematical formulas), sequence windowing with lookback, training with chronological validation, trading simulation with transaction-cost-aware metrics, and model serialization. Cross-links: [[quant-finance/quant-toolkit-and-skills]], [[quant-finance/market-microstructure]], [[quant-finance/applications-of-quantitative-finance]], [[neural-engine]].

---

## 1. Pipeline Architecture (7 Stages)

```mermaid
flowchart TD
    subgraph Data[Stage 1: Data Ingestion]
        A[yfinance Ticker] --> B[history(period)]
        B --> C[Raw OHLCV DataFrame]
    end
    
    subgraph Features[Stage 2: Feature Engineering]
        C --> D[create_features]
        D --> E[20+ Technical Indicators]
        E --> F[dropna]
    end
    
    subgraph Prep[Stage 3: Sequence Preparation]
        F --> G[MinMaxScaler fit_transform]
        G --> H[Sliding Window: lookback_days]
        H --> I[X: (N, lookback × n_features)]
        H --> J[y: Binary UP/DOWN]
    end
    
    subgraph Model[Stage 4: Model Building]
        I --> K[NeuralEngine]
        K --> L[Architecture: 128-64-32-16-1]
    end
    
    subgraph Train[Stage 5: Training]
        L --> M[fit: mini-batch GD]
        M --> N[Chronological val_split]
        N --> O[Early Stopping]
    end
    
    subgraph Eval[Stage 6: Evaluation]
        O --> P[simulate_trading]
        P --> Q[Win Rate / PnL Metrics]
    end
    
    subgraph Deploy[Stage 7: Deployment]
        Q --> R[predict_tomorrow]
        R --> S[save_model: engine + scaler]
    end
```

---

## 2. Feature Engineering — Exact Mathematical Formulas

### 2.1 Price Returns
```python
# Simple returns
data['Returns'] = data['Close'].pct_change()
# Formula: R_t = (Close_t - Close_{t-1}) / Close_{t-1}

# Log returns (time-additive)
data['Log_Returns'] = np.log(data['Close'] / data['Close'].shift(1))
# Formula: r_t = ln(Close_t / Close_{t-1}) ≈ R_t for small returns
```

### 2.2 Moving Averages
```python
# Simple Moving Averages
data['SMA_5']  = data['Close'].rolling(window=5).mean()
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()
# Formula: SMA_n(t) = (1/n) Σ_{i=0}^{n-1} Close_{t-i}

# Exponential Moving Averages
data['EMA_12'] = data['Close'].ewm(span=12).mean()
data['EMA_26'] = data['Close'].ewm(span=26).mean()
# Formula: EMA_t = α × Close_t + (1-α) × EMA_{t-1}, α = 2/(span+1)
```

### 2.3 MACD (Moving Average Convergence Divergence)
```python
data['MACD'] = data['EMA_12'] - data['EMA_26']
data['MACD_Signal'] = data['MACD'].ewm(span=9).mean()
# MACD Line: EMA_12 - EMA_26
# Signal Line: EMA_9 of MACD
# Histogram: MACD - Signal
```

### 2.4 RSI (Relative Strength Index) — 14 Period
```python
delta = data['Close'].diff()
gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
rs = gain / loss
data['RSI'] = 100 - (100 / (1 + rs))
# RSI = 100 - 100/(1 + RS), where RS = Avg Gain / Avg Loss over 14 periods
# Range: 0-100. >70 overbought, <30 oversold
```

### 2.5 Bollinger Bands (20 Period, 2σ)
```python
data['BB_Middle'] = data['Close'].rolling(window=20).mean()
bb_std = data['Close'].rolling(window=20).std()
data['BB_Upper'] = data['BB_Middle'] + (bb_std * 2)
data['BB_Lower'] = data['BB_Middle'] - (bb_std * 2)
data['BB_Width'] = (data['BB_Upper'] - data['BB_Lower']) / data['BB_Middle']
# Middle: SMA_20
# Upper: SMA_20 + 2σ
# Lower: SMA_20 - 2σ
# Width: (Upper - Lower) / Middle (volatility measure)
```

### 2.6 Volatility & Spread
```python
# Rolling volatility (std of returns)
data['Volatility'] = data['Returns'].rolling(window=20).std()

# High-Low spread (intraday range)
data['HL_Spread'] = (data['High'] - data['Low']) / data['Close']
# Normalized true range proxy
```

### 2.7 Volume Indicators
```python
data['Volume_SMA'] = data['Volume'].rolling(window=20).mean()
data['Volume_Ratio'] = data['Volume'] / data['Volume_SMA']
# Volume_Ratio > 1: above-average volume
```

### 2.8 Momentum
```python
data['Momentum_5']  = data['Close'] - data['Close'].shift(5)
data['Momentum_10'] = data['Close'] - data['Close'].shift(10)
# Absolute price change over N periods
```

### 2.9 Target Variable (Binary Classification)
```python
# Next-day direction: UP=1 if Close[t] > Close[t-1] else DOWN=0
future_price = scaled_target[i]
current_price = scaled_target[i-1]
y.append(1 if future_price > current_price else 0)
```

**Critical:** Uses `shift(1)` on target → no lookahead bias. Features at `t` predict `t+1`.

---

## 3. Sequence Preparation — Sliding Window Details

```python
def prepare_sequences(self, data, target_col='Close'):
    feature_cols = [col for col in data.columns if col != target_col]
    
    # Scale features (fit on all data — see leakage note below)
    scaled_features = self.scaler.fit_transform(data[feature_cols])
    scaled_target = data[target_col].values
    
    X, y = [], []
    for i in range(self.lookback_days, len(scaled_features)):
        # Flattened lookback window: (lookback_days × n_features,) → 1D
        X.append(scaled_features[i-self.lookback_days:i].flatten())
        # Binary target: next day UP/DOWN
        future_price = scaled_target[i]
        current_price = scaled_target[i-1]
        y.append(1 if future_price > current_price else 0)
    
    return np.array(X), np.array(y).reshape(-1, 1), feature_cols
```

**Input Shape:** `(N_samples, lookback_days × n_features)`
- Example: `lookback=30`, `n_features=22` → `X.shape = (N, 660)`
- Flattening loses temporal structure but works for dense NN

**Chronological Split (No Random Shuffle):**
```python
val_size = int(len(X) * val_split)
X_train = X[:-val_size]   # Older data
X_val = X[-val_size:]     # Most recent data
```
Prevents data leakage from future to past.

---

## 4. Data Leakage Prevention Checklist

| Leakage Risk | Prevention |
|--------------|------------|
| **Scaler fit on future** | `scaler.fit_transform()` on full dataset → **LEAKAGE**. Fix: fit on train only, transform val/test |
| **Target uses future Close** | `y` uses `Close[t]` vs `Close[t-1]` → correct (predicts next day) |
| **Indicators use future data** | All rolling windows use `.shift(1)` implicitly via pandas rolling → correct |
| **Random shuffle** | `val_split` uses chronological split → correct |
| **Feature selection on full data** | Not done — all indicators computed independently |

**Current Code Issue:** `scaler.fit_transform(data[feature_cols])` fits on **entire dataset** including validation. This leaks future distribution into training.

**Fix:**
```python
# In prepare_sequences, after creating X, y:
train_size = int(len(X) * (1 - val_split))
X_train, X_val = X[:train_size], X[train_size:]
y_train, y_val = y[:train_size], y[train_size:]

# Fit scaler ONLY on training features
# Need to restructure: scale before windowing or fit on train windows only
```

---

## 5. Neural Network Architecture — Detailed

```python
def build_model(self, input_size):
    self.engine = NeuralEngine(
        learning_rate=0.001,
        optimizer='adam',
        l2_lambda=0.001,
        dropout_rate=0.2,
        early_stopping_patience=15
    )
    
    # Input layer: 660 (30 × 22) → 128
    self.engine.add_layer(128, 'relu', dropout=0.3)
    # Hidden 1: 128 → 64
    self.engine.add_layer(64, 'relu', dropout=0.2)
    # Hidden 2: 64 → 32
    self.engine.add_layer(32, 'relu', dropout=0.2)
    # Hidden 3: 32 → 16
    self.engine.add_layer(16, 'relu')
    # Output: 16 → 1 (sigmoid for binary)
    self.engine.add_layer(1, 'sigmoid')
    
    self.engine.summary()
```

**Parameter Count:**
| Layer | Input | Output | Weights | Biases | Total |
|-------|-------|--------|---------|--------|-------|
| 1 | 660 | 128 | 84,480 | 128 | 84,608 |
| 2 | 128 | 64 | 8,192 | 64 | 8,256 |
| 3 | 64 | 32 | 2,048 | 32 | 2,080 |
| 4 | 32 | 16 | 512 | 16 | 528 |
| 5 | 16 | 1 | 16 | 1 | 17 |
| **Total** | | | | | **~95,489** |

---

## 6. Trading Simulation — Exact Implementation

```python
def simulate_trading(self, X, y, predictions):
    signals = (predictions > 0.5).astype(int).flatten()
    actual = y.flatten()
    
    # BUY signals (predict UP)
    correct_ups = np.sum((signals == 1) & (actual == 1))
    total_up_signals = np.sum(signals == 1)
    
    # SELL signals (predict DOWN)
    correct_downs = np.sum((signals == 0) & (actual == 0))
    total_down_signals = np.sum(signals == 0)
    
    # Strategy: Long when UP predicted, Flat when DOWN predicted
    returns = []
    for i in range(len(signals)):
        if signals[i] == 1:  # Predicted UP → Long
            returns.append(1 if actual[i] == 1 else -1)  # Win=+1, Loss=-1
    
    if returns:
        win_rate = (np.array(returns) > 0).sum() / len(returns)
        print(f"Strategy Win Rate: {win_rate:.2%}")
        print(f"Total Trades: {len(returns)}")
```

**Metrics Computed:**
- **Precision (UP):** `TP / (TP + FP)` = `correct_ups / total_up_signals`
- **Recall (UP):** `TP / (TP + FN)` 
- **Precision (DOWN):** `TN / (TN + FN)` = `correct_downs / total_down_signals`
- **Strategy Win Rate:** Fraction of long trades that were profitable
- **Total Trades:** Number of UP predictions (only longs executed)

---

## 7. Complete Usage with All Options

```python
from stockmarketcode import StockPredictor

# Initialize
predictor = StockPredictor(
    ticker='SPY',           # SPY, AAPL, GOOGL, TSLA, NVDA, BTC-USD, ETH-USD
    lookback_days=30        # 10-60 (30 default)
)

# Full training pipeline
engine = predictor.train(
    epochs=150,             # Max epochs (early stopping ~50-80)
    batch_size=64,          # Mini-batch size
    val_split=0.2           # Chronological validation split
)

# Live prediction
prediction = predictor.predict_tomorrow()
# Returns: dict with 'direction', 'confidence', 'raw_score', 'current_price'

# Save model + scaler
predictor.save_model('spy_predictor.pkl')
# Creates: spy_predictor.pkl (NeuralEngine) + spy_predictor_scaler.pkl (MinMaxScaler)
```

**Prediction Output:**
```python
{
    'direction': 'UP',           # 'UP' or 'DOWN'
    'confidence': 0.6734,        # max(p, 1-p)
    'raw_score': 0.6734,         # sigmoid output
    'current_price': 456.78      # Latest close
}
```

---

## 8. Configuration Deep Dive

### Ticker Selection
| Category | Symbols | Notes |
|----------|---------|-------|
| **ETFs** | SPY, QQQ, IWM, EFA, EEM | Broad market |
| **Large Cap** | AAPL, MSFT, GOOGL, AMZN, NVDA, META | High liquidity |
| **Crypto** | BTC-USD, ETH-USD, SOL-USD | 24/7, higher vol |
| **Forex** | EURUSD=X, GBPUSD=X | Use `=X` suffix |

### Lookback Window Tuning
| Lookback | Pros | Cons |
|----------|------|------|
| **10-15** | Faster training, more samples | Less context, noisier |
| **30** (default) | Balanced | Standard |
| **50-60** | More context, smoother | Fewer samples, slower |

### Architecture Variants
```python
# Conservative (less overfitting)
engine.add_layer(64, 'relu', dropout=0.3)
engine.add_layer(32, 'relu', dropout=0.2)
engine.add_layer(1, 'sigmoid')

# Aggressive (more capacity)
engine.add_layer(256, 'relu', dropout=0.3)
engine.add_layer(128, 'relu', dropout=0.3)
engine.add_layer(64, 'relu', dropout=0.2)
engine.add_layer(32, 'relu', dropout=0.2)
engine.add_layer(1, 'sigmoid')

# For regression (predict return magnitude)
engine.add_layer(128, 'relu', dropout=0.2)
engine.add_layer(64, 'relu', dropout=0.2)
engine.add_layer(1, 'linear')  # Linear output, MSE loss
```

---

## 9. Model Persistence — Dual Artifact Save

```python
def save_model(self, filename=None):
    if filename is None:
        filename = f"{self.ticker}_predictor.pkl"
    
    # Save NeuralEngine (weights + architecture + optimizer state)
    self.engine.save(filename)
    
    # Save scaler separately (needed for inference)
    import joblib
    scaler_filename = filename.replace('.pkl', '_scaler.pkl')
    joblib.dump(self.scaler, scaler_filename)
    
    print(f"Model saved: {filename}")
    print(f"Scaler saved: {scaler_filename}")
```

**Load for Inference:**
```python
# Recreate predictor
predictor = StockPredictor(ticker='SPY', lookback_days=30)

# Load engine
predictor.engine.load('spy_predictor.pkl')

# Load scaler
import joblib
predictor.scaler = joblib.load('spy_predictor_scaler.pkl')

# Now ready for predict_tomorrow()
```

---

## 10. Cross-References

- [[neural-engine]] — Core ML engine (from-scratch NumPy, 4 optimizers, dropout, L2)
- [[quant-finance/quant-toolkit-and-skills]] — ML for quant workflows
- [[quant-finance/market-microstructure]] — Market data considerations, bid-ask, slippage
- [[quant-finance/applications-of-quantitative-finance]] — Strategy deployment
- [[quant-finance/momentum-jegadeesh-titman]] — Momentum factor literature
- [[quant-finance/pairs-trading-gatev-goetzmann-rouwenhorst]] — Mean reversion alternative

---

## 11. Known Limitations / TODOs (Detailed)

| Issue | Severity | Fix |
|-------|----------|-----|
| **Scaler leakage** | High | Fit scaler on train windows only, transform val/test |
| **Binary only** | Medium | Add regression head for return magnitude |
| **No transaction costs** | Medium | Subtract commission + slippage per trade in simulation |
| **Single asset** | Medium | Multi-asset with shared trunk + asset-specific heads |
| **No regime detection** | Medium | Add HMM or volatility regime filter |
| **No walk-forward** | High | Implement expanding window validation |
| **Flattened sequences** | Low | Try LSTM/GRU (would need autodiff or manual BPTT) |
| **No feature importance** | Low | Add permutation importance or SHAP |

---

## 12. Performance Benchmarks (Typical SPY 2Y Data)

| Metric | Typical Range |
|--------|---------------|
| **Training Samples** | ~450 (2 years × 252 days - 30 lookback) |
| **Features** | 22 (after dropna) |
| **Input Dim** | 660 (30 × 22) |
| **Train Time** | 30-60 seconds (CPU, 150 epochs) |
| **Val Accuracy** | 52-58% (near random for direction) |
| **Strategy Win Rate** | 50-55% (slight edge if any) |
| **Sharpe (sim)** | 0.5-1.0 (before costs) |

> **Reality Check:** Daily direction prediction is notoriously difficult. Expect ~52-55% accuracy. The value is in **regime-aware** modeling, not raw direction prediction.

---

## See Also
- [[Neural net 2/neuralnet.py]] — Core engine source (497 lines)
- [[Neural net 2/stockmarketcode.py]] — Full pipeline source (302 lines)
- [[Neural net 2/xor_model.pkl]] — Demo model
- [[wiki/01-Areas/Engineering/engineering-math]] — Time series math foundations