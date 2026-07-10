"""Taiwan Market Entry Dashboard.

A beginner-friendly Streamlit project for evaluating whether a Thai product
could be a good fit for the Taiwan market.
"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


# Streamlit page settings must be the first Streamlit command in the file.
st.set_page_config(
    page_title="Taiwan Market Entry Dashboard",
    page_icon="🇹🇼",
    layout="wide",
)


# -----------------------------------------------------------------------------
# SAMPLE DATA
# Each product has business assumptions, competitor data, SWOT notes, a 4P
# strategy, and a customer persona. In a real project, these assumptions would
# be replaced with information from market research.
# -----------------------------------------------------------------------------
PRODUCT_DATA = {
    "Thai milk tea": {
        "demand_score": 8,
        "cultural_fit": 8,
        "competition_level": 8,
        "profit_margin_score": 7,
        "promotion_difficulty": 4,
        "estimated_cost": 32.0,
        "selling_price": 75.0,
        "target_customer": "Students and young professionals aged 16–30 who enjoy café culture and sweet drinks.",
        "main_competitors": "50 Lan, CoCo Fresh Tea & Juice, local bubble-tea shops",
        "competitors": [
            {"Competitor": "50 Lan", "Typical price (NT$)": 55, "Positioning": "Familiar local chain", "Key strength": "Convenient locations"},
            {"Competitor": "CoCo", "Typical price (NT$)": 65, "Positioning": "Trendy drink chain", "Key strength": "Large menu and brand awareness"},
            {"Competitor": "Independent Thai cafés", "Typical price (NT$)": 90, "Positioning": "Authentic Thai taste", "Key strength": "Strong cultural experience"},
        ],
        "swot": {
            "Strengths": "Distinctive orange color, recognizable Thai identity, and a rich flavor.",
            "Weaknesses": "High sugar content and dependence on imported tea ingredients.",
            "Opportunities": "Taiwan has a strong tea-drink culture and consumers enjoy new seasonal flavors.",
            "Threats": "A crowded beverage market and easy imitation by established drink chains.",
        },
        "marketing_4p": {
            "Product": "Offer classic Thai milk tea plus a less-sweet option with clear Thai branding.",
            "Price": "Use an accessible premium price of about NT$70–80 per cup.",
            "Place": "Start with pop-ups near universities, night markets, and delivery apps.",
            "Promotion": "Use short videos, Thai-food creators, and launch-week tasting coupons.",
        },
        "persona": {
            "Name": "Mei, the trend-seeking student",
            "Profile": "21 years old, university student in Taipei",
            "Needs": "An affordable, photogenic drink that feels new but still familiar",
            "Buying behavior": "Finds drinks on Instagram and TikTok; buys 2–3 café drinks each week",
            "Message": "A colorful taste of Thailand, made for your Taiwan tea break.",
        },
    },
    "Dried mango": {
        "demand_score": 7,
        "cultural_fit": 8,
        "competition_level": 6,
        "profit_margin_score": 7,
        "promotion_difficulty": 3,
        "estimated_cost": 58.0,
        "selling_price": 120.0,
        "target_customer": "Office workers, travelers, and health-aware snack buyers aged 25–45.",
        "main_competitors": "Taiwan dried-fruit brands, 7D, Philippine dried-mango imports",
        "competitors": [
            {"Competitor": "Local fruit brands", "Typical price (NT$)": 110, "Positioning": "Local and familiar", "Key strength": "Taiwan fruit reputation"},
            {"Competitor": "7D", "Typical price (NT$)": 135, "Positioning": "Imported premium snack", "Key strength": "Established dried-mango brand"},
            {"Competitor": "Supermarket private label", "Typical price (NT$)": 85, "Positioning": "Budget snack", "Key strength": "Low price"},
        ],
        "swot": {
            "Strengths": "Long shelf life, easy transport, and Thailand is known for tropical fruit.",
            "Weaknesses": "Some products contain high sugar and the category can look undifferentiated.",
            "Opportunities": "Growing demand for convenient snacks, gifts, and portion-controlled packs.",
            "Threats": "Strong Taiwanese fruit brands and price competition from other importers.",
        },
        "marketing_4p": {
            "Product": "Use resealable 100 g packs and highlight real Thai mango with a low-sugar option.",
            "Price": "Price near NT$110–130 to signal quality without becoming a luxury snack.",
            "Place": "Sell through supermarkets, convenience-store trials, marketplaces, and airport gift shops.",
            "Promotion": "Offer samples and communicate Thai origin, portability, and natural fruit content.",
        },
        "persona": {
            "Name": "Jason, the busy office snacker",
            "Profile": "34 years old, finance employee in New Taipei City",
            "Needs": "A convenient snack for work that feels healthier than candy",
            "Buying behavior": "Compares nutrition labels and buys snacks online in multipacks",
            "Message": "Real Thai mango for a naturally brighter afternoon break.",
        },
    },
    "Coconut water": {
        "demand_score": 7,
        "cultural_fit": 7,
        "competition_level": 6,
        "profit_margin_score": 6,
        "promotion_difficulty": 5,
        "estimated_cost": 38.0,
        "selling_price": 69.0,
        "target_customer": "Fitness enthusiasts and wellness-focused consumers aged 20–40.",
        "main_competitors": "Vita Coco, UFC, local sports drinks and bottled teas",
        "competitors": [
            {"Competitor": "Vita Coco", "Typical price (NT$)": 79, "Positioning": "Global wellness brand", "Key strength": "Strong international recognition"},
            {"Competitor": "UFC", "Typical price (NT$)": 59, "Positioning": "Thai mass market", "Key strength": "Competitive price and distribution"},
            {"Competitor": "Local sports drinks", "Typical price (NT$)": 35, "Positioning": "Everyday hydration", "Key strength": "Low price and convenience"},
        ],
        "swot": {
            "Strengths": "Natural hydration story and Thailand has strong coconut supply knowledge.",
            "Weaknesses": "Heavy packaging raises shipping cost and taste varies between brands.",
            "Opportunities": "Fitness, wellness, and clean-label trends support natural beverages.",
            "Threats": "Low-priced sports drinks and well-established imported coconut-water brands.",
        },
        "marketing_4p": {
            "Product": "Sell chilled pure coconut water in recyclable packs with no added sugar.",
            "Price": "Target NT$65–75, between local drinks and premium global brands.",
            "Place": "Focus on gyms, convenience stores, healthy supermarkets, and online cases.",
            "Promotion": "Partner with fitness instructors and emphasize natural electrolytes and Thai origin.",
        },
        "persona": {
            "Name": "Kevin, the active professional",
            "Profile": "29 years old, software designer and recreational runner in Taipei",
            "Needs": "A refreshing post-workout drink without artificial ingredients",
            "Buying behavior": "Shops at convenience stores after exercise and follows fitness creators",
            "Message": "Clean hydration from Thai coconuts—nothing extra needed.",
        },
    },
    "Skincare product": {
        "demand_score": 8,
        "cultural_fit": 7,
        "competition_level": 9,
        "profit_margin_score": 8,
        "promotion_difficulty": 8,
        "estimated_cost": 180.0,
        "selling_price": 520.0,
        "target_customer": "Beauty-conscious consumers aged 20–38 interested in gentle, tropical ingredients.",
        "main_competitors": "Taiwanese dermocosmetics, Korean beauty brands, Japanese skincare",
        "competitors": [
            {"Competitor": "Dr. Wu", "Typical price (NT$)": 750, "Positioning": "Taiwan dermocosmetic", "Key strength": "Trust and clinical image"},
            {"Competitor": "Korean beauty brands", "Typical price (NT$)": 480, "Positioning": "Trendy and innovative", "Key strength": "Influencer visibility"},
            {"Competitor": "Japanese drugstore brands", "Typical price (NT$)": 420, "Positioning": "Reliable everyday care", "Key strength": "Consumer familiarity"},
        ],
        "swot": {
            "Strengths": "Potentially high margin and a distinctive Thai botanical ingredient story.",
            "Weaknesses": "Low initial brand trust and product claims require careful evidence.",
            "Opportunities": "Consumers actively discover Asian beauty brands through social commerce.",
            "Threats": "Intense Korean, Japanese, and Taiwanese competition plus cosmetics regulations.",
        },
        "marketing_4p": {
            "Product": "Launch one hero moisturizer for humid weather with bilingual ingredients and testing information.",
            "Price": "Use an attainable premium price around NT$480–550.",
            "Place": "Begin on beauty marketplaces and social commerce before approaching retail chains.",
            "Promotion": "Use credible micro-influencer trials, before-and-after education, and sample sizes.",
        },
        "persona": {
            "Name": "Yuna, the ingredient-aware beauty shopper",
            "Profile": "27 years old, marketing specialist in Taichung",
            "Needs": "Gentle skincare suited to humid weather with transparent ingredients",
            "Buying behavior": "Reads reviews, watches beauty videos, and expects samples before committing",
            "Message": "Thai botanical care designed for comfortable, humid-weather skin.",
        },
    },
    "Eco-friendly tote bag": {
        "demand_score": 6,
        "cultural_fit": 8,
        "competition_level": 7,
        "profit_margin_score": 6,
        "promotion_difficulty": 5,
        "estimated_cost": 95.0,
        "selling_price": 250.0,
        "target_customer": "Students and urban shoppers aged 18–35 who value design and sustainability.",
        "main_competitors": "Local design markets, MUJI, lifestyle stores and online sellers",
        "competitors": [
            {"Competitor": "Local design markets", "Typical price (NT$)": 320, "Positioning": "Unique local design", "Key strength": "Artist story and originality"},
            {"Competitor": "MUJI", "Typical price (NT$)": 290, "Positioning": "Minimal and practical", "Key strength": "Trusted lifestyle brand"},
            {"Competitor": "Online budget sellers", "Typical price (NT$)": 120, "Positioning": "Low-cost utility", "Key strength": "Very low price"},
        ],
        "swot": {
            "Strengths": "Reusable, lightweight, and able to feature distinctive Thai design.",
            "Weaknesses": "Easy to copy and consumers may already own several tote bags.",
            "Opportunities": "Plastic reduction, design markets, and cross-border lifestyle shopping.",
            "Threats": "Many inexpensive substitutes and skepticism about vague green claims.",
        },
        "marketing_4p": {
            "Product": "Use durable recycled fabric, a practical inner pocket, and modern Thai artwork.",
            "Price": "Set a mid-market price around NT$230–280 and explain material quality.",
            "Place": "Test at design fairs, museum shops, university pop-ups, and online marketplaces.",
            "Promotion": "Tell the maker and material story; show reuse occasions instead of making vague claims.",
        },
        "persona": {
            "Name": "Lin, the conscious creative",
            "Profile": "24 years old, junior graphic designer in Kaohsiung",
            "Needs": "A useful everyday bag that expresses personal style and responsible values",
            "Buying behavior": "Visits weekend design markets and shares attractive purchases online",
            "Message": "Carry Thai creativity—and reuse it every day.",
        },
    },
}


# The five weights add up to 1.00 (or 100%).
WEIGHTS = {
    "Demand": 0.25,
    "Cultural fit": 0.20,
    "Competition": 0.20,
    "Profit margin": 0.20,
    "Promotion difficulty": 0.15,
}


def calculate_market_fit(
    demand, cultural_fit, competition_level, profit_margin, promotion_difficulty
):
    """Calculate a 0–100 market fit score from five 0–10 inputs."""

    # Competition and promotion difficulty are negative factors. A lower raw
    # number is better, so reverse each one before applying its weight.
    competition_score = 10 - competition_level
    promotion_score = 10 - promotion_difficulty

    weighted_score_out_of_10 = (
        demand * WEIGHTS["Demand"]
        + cultural_fit * WEIGHTS["Cultural fit"]
        + competition_score * WEIGHTS["Competition"]
        + profit_margin * WEIGHTS["Profit margin"]
        + promotion_score * WEIGHTS["Promotion difficulty"]
    )

    # The weighted result is out of 10, so multiply by 10 for a percentage-like
    # score from 0 to 100.
    return weighted_score_out_of_10 * 10, competition_score, promotion_score


def get_recommendation(market_fit_score, gross_margin):
    """Turn the two main results into a simple business recommendation."""

    if market_fit_score >= 75 and gross_margin >= 40:
        return (
            "GO — Strong pilot opportunity",
            "The product shows good market fit and enough gross-margin room. Start with a small Taiwan pilot and validate demand before scaling.",
            "success",
        )
    if market_fit_score >= 60 and gross_margin >= 25:
        return (
            "TEST — Enter carefully",
            "The opportunity is promising but has meaningful risks. Run a limited online launch or pop-up and improve the weakest factors.",
            "warning",
        )
    return (
        "REVIEW — Improve before entry",
        "The current assumptions show weak fit or limited margin. Adjust the product, price, positioning, or promotion plan before investing.",
        "error",
    )


def money(value):
    """Format a number as New Taiwan dollars."""

    return f"NT${value:,.2f}"


# -----------------------------------------------------------------------------
# PAGE HEADER AND PRODUCT SELECTOR
# -----------------------------------------------------------------------------
st.title("🇹🇼 Taiwan Market Entry Dashboard")
st.caption("Evaluate the entry potential of five Thai products using sample business assumptions.")

with st.sidebar:
    st.header("Product selection")
    selected_product = st.selectbox("Choose a Thai product", list(PRODUCT_DATA.keys()))
    st.info(
        "Learning tip: change the scores and prices to test different business scenarios. "
        "Each product keeps its scenario values while this browser session is open."
    )
    st.markdown("**Currency:** New Taiwan dollar (NT$)")

product = PRODUCT_DATA[selected_product]

st.subheader(selected_product)
st.write(f"**Target customer:** {product['target_customer']}")
st.write(f"**Main competitors:** {product['main_competitors']}")


# -----------------------------------------------------------------------------
# 1. MARKET FIT SCORE CALCULATOR
# -----------------------------------------------------------------------------
st.header("1. Market Fit Score Calculator")
st.write(
    "Score each factor from 0 to 10. Demand, cultural fit, and profit margin are positive; "
    "competition and promotion difficulty are negative."
)
st.caption(
    "Profit Margin Score is a 0–10 assessment of margin potential. The pricing section below "
    "calculates an actual gross-margin percentage from cost and price."
)

score_col1, score_col2 = st.columns(2)
with score_col1:
    demand = st.slider(
        "Demand Score (higher is better)", 0, 10, product["demand_score"], key=f"demand_{selected_product}"
    )
    cultural_fit = st.slider(
        "Cultural Fit (higher is better)", 0, 10, product["cultural_fit"], key=f"culture_{selected_product}"
    )
    profit_margin_score = st.slider(
        "Profit Margin Score (higher is better)", 0, 10, product["profit_margin_score"], key=f"margin_{selected_product}"
    )

with score_col2:
    competition_level = st.slider(
        "Competition Level (higher is worse)", 0, 10, product["competition_level"], key=f"competition_{selected_product}"
    )
    promotion_difficulty = st.slider(
        "Promotion Difficulty (higher is worse)", 0, 10, product["promotion_difficulty"], key=f"promotion_{selected_product}"
    )
    st.caption(
        "Negative-factor conversion: "
        f"competition becomes {10 - competition_level}/10 and promotion becomes {10 - promotion_difficulty}/10."
    )

market_fit_score, competition_score, promotion_score = calculate_market_fit(
    demand,
    cultural_fit,
    competition_level,
    profit_margin_score,
    promotion_difficulty,
)

metric_col1, metric_col2, metric_col3 = st.columns(3)
metric_col1.metric("Market Fit Score", f"{market_fit_score:.1f} / 100")
metric_col2.metric("Adjusted Competition Score", f"{competition_score} / 10")
metric_col3.metric("Adjusted Promotion Score", f"{promotion_score} / 10")

# Show all five factors in the same "higher is better" direction.
chart_data = pd.Series(
    {
        "Demand": demand,
        "Cultural fit": cultural_fit,
        "Low competition": competition_score,
        "Profit margin": profit_margin_score,
        "Easy promotion": promotion_score,
    }
)
fig, ax = plt.subplots(figsize=(8, 3.2))
# Sort first, then create the colors from that same sorted order. This keeps
# each color attached to the correct bar.
sorted_chart_data = chart_data.sort_values()
colors = ["#1f77b4" if value >= 6 else "#f39c12" for value in sorted_chart_data.values]
sorted_chart_data.plot(kind="barh", ax=ax, color=colors)
ax.set_xlim(0, 10)
ax.set_xlabel("Adjusted score (higher is better)")
ax.set_ylabel("")
ax.grid(axis="x", alpha=0.25)
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

with st.expander("See the score calculation"):
    st.code(
        f"""Demand:             {demand} × 25% = {demand * 0.25:.2f}
Cultural fit:        {cultural_fit} × 20% = {cultural_fit * 0.20:.2f}
Low competition:    (10 - {competition_level}) × 20% = {competition_score * 0.20:.2f}
Profit margin:       {profit_margin_score} × 20% = {profit_margin_score * 0.20:.2f}
Easy promotion:     (10 - {promotion_difficulty}) × 15% = {promotion_score * 0.15:.2f}
--------------------------------------------------
Weighted score out of 10 = {market_fit_score / 10:.2f}
Market Fit Score = {market_fit_score:.1f} / 100""",
        language="text",
    )


# -----------------------------------------------------------------------------
# 2. COMPETITOR COMPARISON
# -----------------------------------------------------------------------------
st.header("2. Competitor Comparison")
st.write("Compare price, positioning, and competitive strengths before choosing a market position.")

competitor_df = pd.DataFrame(product["competitors"])

# The price widget appears later on the page, but Streamlit stores its current
# value in session_state. Reading it here keeps the earlier competitor table in
# sync with the user's latest pricing scenario after every rerun.
selling_price_key = f"price_{selected_product}"
current_selling_price = st.session_state.get(
    selling_price_key, float(product["selling_price"])
)
our_product_row = pd.DataFrame(
    [
        {
            "Competitor": f"Our {selected_product}",
            "Typical price (NT$)": current_selling_price,
            "Positioning": "Thai market entrant",
            "Key strength": "Thai origin and product story",
        }
    ]
)
comparison_df = pd.concat([our_product_row, competitor_df], ignore_index=True)
st.dataframe(comparison_df, use_container_width=True, hide_index=True)
st.caption(
    "Our product row uses the current scenario selling price. Competitor prices are sample values; "
    "verify current Taiwan prices before making a real decision."
)


# -----------------------------------------------------------------------------
# 3. PRICING AND PROFIT MARGIN CALCULATOR
# -----------------------------------------------------------------------------
st.header("3. Pricing and Profit Margin Calculator")
st.write(
    "Change the landed cost and Taiwan selling price. Landed cost should include the product, "
    "shipping, import costs, and packaging per unit."
)

price_col1, price_col2 = st.columns(2)
with price_col1:
    estimated_cost = st.number_input(
        "Estimated landed cost per unit (NT$)",
        min_value=0.0,
        value=float(product["estimated_cost"]),
        step=1.0,
        key=f"cost_{selected_product}",
    )
with price_col2:
    selling_price = st.number_input(
        "Selling price per unit (NT$)",
        min_value=0.0,
        value=float(product["selling_price"]),
        step=1.0,
        key=selling_price_key,
    )

gross_profit = selling_price - estimated_cost
gross_margin = (gross_profit / selling_price * 100) if selling_price > 0 else 0.0
# Markup divides by cost, so it has no defined value when cost is zero.
markup = (gross_profit / estimated_cost * 100) if estimated_cost > 0 else None

price_metric1, price_metric2, price_metric3 = st.columns(3)
price_metric1.metric("Gross profit per unit", money(gross_profit))
price_metric2.metric("Gross margin", f"{gross_margin:.1f}%")
price_metric3.metric(
    "Markup on cost", f"{markup:.1f}%" if markup is not None else "Not defined"
)

if markup is None:
    st.info("Markup is not defined when landed cost is zero because the formula would divide by zero.")

if selling_price <= estimated_cost:
    st.error("The selling price does not cover the landed cost. This product loses money before other operating expenses.")
elif gross_margin < 25:
    st.warning("The gross margin is positive but thin. There may be little room for marketing, staff, platform fees, and other expenses.")
else:
    st.success("The gross margin is positive. Remember that gross profit is not final net profit because operating expenses are not included.")

with st.expander("Gross margin and markup are different"):
    st.write(
        f"Gross profit = {money(selling_price)} − {money(estimated_cost)} = **{money(gross_profit)}**"
    )
    st.write(
        f"Gross margin = gross profit ÷ selling price = {money(gross_profit)} ÷ {money(selling_price)} = **{gross_margin:.1f}%**"
    )
    if markup is None:
        st.write(
            "Markup cannot be calculated because landed cost is **NT$0.00**. "
            "Division by zero is undefined."
        )
    else:
        st.write(
            f"Markup = gross profit ÷ cost = {money(gross_profit)} ÷ {money(estimated_cost)} = **{markup:.1f}%**"
        )


# -----------------------------------------------------------------------------
# 4–6. BUSINESS ANALYSIS SECTIONS
# -----------------------------------------------------------------------------
st.header("4. SWOT Analysis")
swot_col1, swot_col2 = st.columns(2)
with swot_col1:
    st.subheader("Strengths")
    st.write(product["swot"]["Strengths"])
    st.subheader("Weaknesses")
    st.write(product["swot"]["Weaknesses"])
with swot_col2:
    st.subheader("Opportunities")
    st.write(product["swot"]["Opportunities"])
    st.subheader("Threats")
    st.write(product["swot"]["Threats"])

st.header("5. 4P Marketing Strategy")
four_p_columns = st.columns(4)
for column, (label, note) in zip(four_p_columns, product["marketing_4p"].items()):
    with column:
        st.subheader(label)
        st.write(note)

st.header("6. Customer Persona")
persona = product["persona"]
st.subheader(persona["Name"])
persona_col1, persona_col2 = st.columns(2)
with persona_col1:
    st.write(f"**Profile:** {persona['Profile']}")
    st.write(f"**Needs:** {persona['Needs']}")
with persona_col2:
    st.write(f"**Buying behavior:** {persona['Buying behavior']}")
    st.write(f"**Suggested message:** “{persona['Message']}”")


# -----------------------------------------------------------------------------
# 7. FINAL RECOMMENDATION
# -----------------------------------------------------------------------------
st.header("7. Final Recommendation Summary")
recommendation, explanation, message_type = get_recommendation(market_fit_score, gross_margin)

if message_type == "success":
    st.success(f"**{recommendation}**\n\n{explanation}")
elif message_type == "warning":
    st.warning(f"**{recommendation}**\n\n{explanation}")
else:
    st.error(f"**{recommendation}**\n\n{explanation}")

summary_col1, summary_col2, summary_col3 = st.columns(3)
summary_col1.metric("Market fit", f"{market_fit_score:.1f}/100")
summary_col2.metric("Gross margin", f"{gross_margin:.1f}%")
summary_col3.metric("Profit per unit", money(gross_profit))

# Find the weakest adjusted factor so the user has one clear next action.
adjusted_factors = {
    "demand": demand,
    "cultural fit": cultural_fit,
    "competition position": competition_score,
    "profit margin potential": profit_margin_score,
    "promotion ease": promotion_score,
}
weakest_factor = min(adjusted_factors, key=adjusted_factors.get)
st.write(
    f"**Priority action:** Research and improve **{weakest_factor}**, currently the lowest adjusted factor "
    f"at {adjusted_factors[weakest_factor]}/10."
)
st.caption(
    "This dashboard is an educational portfolio project. Its sample assumptions are not a substitute for real customer, competitor, legal, and financial research."
)
