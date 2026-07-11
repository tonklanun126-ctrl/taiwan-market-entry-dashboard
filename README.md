# Taiwan Market Entry Dashboard

A beginner-friendly business analytics dashboard that evaluates whether a Thai product may fit the Taiwan market. It connects simple Python analysis with international business tools such as market scoring, competitor analysis, pricing, SWOT, the 4Ps, customer personas, and entry recommendations.

> The product scores and market notes are sample assumptions for learning. A real market-entry decision would require current primary and secondary research.

## Overall project logic

The dashboard follows the same broad questions that a business would ask before entering a foreign market:

1. **What are we selling?** Choose one of six Thai products.
2. **Does the market look attractive?** Combine five important factors into a Market Fit Score.
3. **What evidence supports the idea?** Review starting assumptions and their confidence.
4. **Who already serves this market?** Compare the product with important competitors.
5. **Can the product make money?** Test contribution margin, scenarios, and break-even volume.
6. **How should we enter?** Review SWOT actions, 4P strategy, KPIs, personas, and compliance risks.
7. **What should we do next?** Receive a simple Go, Test, or Review recommendation.

The app includes sample data for:

- Low-Sugar Thai Coconut Crispy Rolls
- Thai milk tea
- Dried mango
- Coconut water
- Skincare product
- Eco-friendly tote bag

All prices are in New Taiwan dollars (NT$). The estimated cost is the **landed cost per unit in Taiwan**, which should include product cost, shipping, import costs, and packaging.

## Features

- Product selector
- Market evidence and confidence
- Editable Market Fit Score calculator
- Positive-direction factor chart
- Competitor comparison table
- Pricing, unit economics, and scenario analysis
- SWOT analysis and action plan
- 4P marketing strategy and pilot KPIs
- Compatible single and multiple customer personas
- Compliance and risk checklist
- Dynamic final recommendation and priority action

## Project files

```text
Taiwan Market Entry Dashboard/
├── app.py             # Streamlit dashboard and sample product data
├── requirements.txt   # Python packages needed by the app
└── README.md          # Project explanation and instructions
```

## How to run the project

### 1. Open a terminal in this project folder

```powershell
cd "path\to\CODEX PROJECT"
```

### 2. Create a virtual environment (recommended)

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can skip this step and use your normal Python installation.

### 4. Install the required packages

```powershell
python -m pip install -r requirements.txt
```

### 5. Start Streamlit

```powershell
python -m streamlit run app.py
```

Streamlit will show a local address, usually `http://localhost:8501`. Open it in a web browser. Stop the app by pressing `Ctrl+C` in the terminal.

## 1. How the Market Fit Score works

The app uses five business factors. Each input is scored from 0 to 10 and has a different weight:

| Factor | Weight | Meaning of a high score |
|---|---:|---|
| Demand | 25% | Better market-entry conditions |
| Cultural Fit | 20% | Better market-entry conditions |
| Competitive Opportunity | 20% | Better market-entry conditions |
| Profit Margin Potential | 20% | Better market-entry conditions |
| Promotion Ease | 15% | Better market-entry conditions |

The weights total 100%. The formula is:

```text
weighted_score =
    demand × 0.25
    + cultural_fit × 0.20
    + competitive_opportunity × 0.20
    + profit_margin_potential × 0.20
    + promotion_ease × 0.15

market_fit_score = weighted_score × 10
```

The weighted score is initially from 0 to 10. Multiplying it by 10 converts it to a final score from 0 to 100.

## 2. Why every visible factor uses the same direction

The original sample data stores competition level and promotion difficulty as negative conditions. The app converts those defaults before showing them:

```text
Competitive opportunity = 10 - competition level
Promotion ease = 10 - promotion difficulty
```

Every visible slider therefore follows one beginner-friendly rule: **higher means better market-entry conditions**.

## 3. How pricing and unit economics work

The calculator combines selling price and landed cost with retailer fees, marketing cost per unit, other variable cost, and monthly fixed cost.

- **Estimated landed cost:** total cost to get one unit ready for sale in Taiwan.
- **Selling price:** the amount paid by the Taiwan customer.

It calculates:

```text
Gross profit per unit = selling price - landed cost
Gross margin (%) = gross profit / selling price × 100
Retailer fee = selling price × retailer fee percentage
Total variable cost = landed cost + retailer fee + marketing + other variable cost
Contribution profit = selling price - total variable cost
Contribution margin = contribution profit / selling price × 100
Break-even units = monthly fixed cost / contribution profit
```

Gross profit only considers landed product cost. Contribution profit goes further by subtracting all variable selling costs. Net profit is what remains after contribution profit also covers fixed costs, tax, and other expenses. When contribution profit is zero or negative, break-even is not achievable under the current assumptions.

The **Profit Margin Score** in the Market Fit section is a broader 0–10 assessment of the product's margin potential. The pricing calculator separately produces an exact gross-margin percentage from the cost and price entered. In real analysis, the calculated result and market research would help the analyst choose a defensible 0–10 Profit Margin Score.

## 4. Connection to International Business / Business Administration

This project combines several important business subjects:

- **International business:** considers entry into a foreign market, cultural fit, imported-product costs, local competition, and localization.
- **Marketing:** uses segmentation, a customer persona, competitor positioning, and the 4P framework (Product, Price, Place, Promotion).
- **Strategy:** uses SWOT to connect internal strengths and weaknesses with external opportunities and threats.
- **Finance:** tests unit economics through landed cost, pricing, contribution margin, and break-even volume.
- **Business analytics:** turns several assumptions into a consistent score and uses scenario testing to support a decision.

The dashboard does not make the decision automatically. It organizes assumptions so a manager can discuss risks, compare options, and decide what research or pilot should happen next.

## 5. What I learned from this project

1. **Coding can turn business rules into a repeatable tool.** Python functions apply the same scoring and pricing formulas every time, while Streamlit makes the tool interactive.
2. **Business metrics must have a consistent direction and definition.** Positive-direction sliders make scoring easier to interpret, while contribution margin shows more than gross margin alone.
3. **Market entry requires more than a single number.** A useful recommendation combines demand and culture with competitors, costs, customers, risks, and a practical marketing plan.

## Beginner code guide

- `PRODUCT_DATA` is a Python dictionary containing the six sample products.
- `calculate_market_fit()` contains the weighted scoring formula.
- `get_recommendation()` converts the score and gross margin into a simple action.
- `st.selectbox`, `st.slider`, and `st.number_input` collect user inputs.
- pandas builds the competitor table.
- matplotlib creates the adjusted-factor bar chart.
- Streamlit recalculates the page automatically whenever an input changes.
