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
    "Low-Sugar Thai Coconut Crispy Rolls": {
        "demand_score": 8,
        "cultural_fit": 9,
        "competition_level": 6,
        "profit_margin_score": 8,
        "promotion_difficulty": 3,
        "estimated_cost": 55.0,
        "selling_price": 129.0,
        "package_size": "80 g resealable pack",
        "category": "Packaged snack",
        "target_customer": (
            "Health-aware students, office workers, and young professionals aged "
            "18–35 who enjoy convenient imported snacks."
        ),
        "main_competitors": (
            "Taiwanese rice crackers, Japanese premium biscuits, imported coconut "
            "chips, and other Thai snack brands."
        ),
        "competitors": [
            {
                "Competitor": "Local rice crackers",
                "Typical price (NT$)": 79,
                "Package size": "70–100 g",
                "Positioning": "Affordable local snack",
                "Key strength": "Familiar taste and strong distribution",
                "Weakness": "Limited Thai identity",
            },
            {
                "Competitor": "Imported coconut snacks",
                "Typical price (NT$)": 119,
                "Package size": "60–100 g",
                "Positioning": "Natural imported snack",
                "Key strength": "Health and tropical ingredient image",
                "Weakness": "Products can appear similar",
            },
            {
                "Competitor": "Japanese premium biscuits",
                "Typical price (NT$)": 149,
                "Package size": "70–120 g",
                "Positioning": "Premium gifting snack",
                "Key strength": "Strong quality perception",
                "Weakness": "Higher price",
            },
        ],
        "market_evidence": [
            {
                "Evidence": "Convenience and portability",
                "Reason": (
                    "The product is shelf-stable, lightweight, easy to carry, and suitable "
                    "for convenience-focused retail channels."
                ),
                "Impact": "Positive",
                "Confidence": "Medium",
            },
            {
                "Evidence": "Health-aware positioning",
                "Reason": (
                    "A lower-sugar recipe and transparent ingredient list support a "
                    "healthier-snacking and clean-label position."
                ),
                "Impact": "Positive",
                "Confidence": "Medium",
            },
            {
                "Evidence": "Thai product differentiation",
                "Reason": (
                    "Coconut, pandan, and black sesame flavors can create a recognizable "
                    "Thai identity while remaining familiar to Taiwan consumers."
                ),
                "Impact": "Positive",
                "Confidence": "Medium",
            },
            {
                "Evidence": "Imported-food competition",
                "Reason": (
                    "The product must compete with strong Taiwanese and Japanese snack "
                    "brands that already have consumer trust and retail distribution."
                ),
                "Impact": "Risk",
                "Confidence": "High",
            },
        ],
        "confidence_level": "Medium",
        "retailer_fee_percent": 15.0,
        "marketing_cost_per_unit": 8.0,
        "other_variable_cost": 4.0,
        "monthly_fixed_cost": 50000.0,
        "swot": {
            "Strengths": (
                "Shelf-stable, lightweight, easy to sample, and supported by a clear "
                "Thai coconut product story."
            ),
            "Weaknesses": (
                "A new brand has limited consumer trust, and coconut snacks can look "
                "similar without distinctive packaging."
            ),
            "Opportunities": (
                "Lower-sugar snacks, smaller portion sizes, imported-food discovery, "
                "online marketplaces, and premium supermarket trials."
            ),
            "Threats": (
                "Strong local and Japanese snack brands, retailer fees, price sensitivity, "
                "copycat products, and food-import compliance requirements."
            ),
        },
        "swot_actions": {
            "Strength action": (
                "Use product sampling and clear Thai-origin storytelling to make the "
                "taste and texture easy to understand."
            ),
            "Weakness action": (
                "Use distinctive packaging, transparent ingredients, and a resealable "
                "small pack to build trust."
            ),
            "Opportunity action": (
                "Test the product through online marketplaces and a limited pop-up before "
                "approaching large retailers."
            ),
            "Threat action": (
                "Track retailer fees, protect the packaging identity, and verify Taiwan "
                "food-label and import requirements before launch."
            ),
        },
        "marketing_4p": {
            "Product": (
                "An 80 g resealable pack of baked coconut crispy rolls. Launch Original "
                "Coconut first, followed by Pandan and Black Sesame."
            ),
            "Price": "Use an accessible-premium price of approximately NT$119–139 per pack.",
            "Place": (
                "Begin with e-commerce, Thai cultural events, university pop-ups, and "
                "premium supermarket trials."
            ),
            "Promotion": (
                "Use tasting samples, short texture-focused videos, Thai-origin stories, "
                "micro-influencers, and first-purchase coupons."
            ),
        },
        "marketing_kpis": {
            "Pilot duration": "14 days",
            "Sample target": "300 packs or tasting portions",
            "Purchase conversion target": "15% or higher",
            "Repeat purchase target": "20% or higher",
            "Average customer rating": "4.3/5 or higher",
            "Maximum customer acquisition cost": "NT$30",
        },
        "personas": [
            {
                "Name": "Mei, the health-aware student",
                "Profile": "22-year-old university student in Taipei",
                "Needs": "A portable snack that feels lighter than candy but is still enjoyable.",
                "Buying behavior": (
                    "Discovers products through short videos, checks price, and shares "
                    "attractive packaging with friends."
                ),
                "Message": "A lighter Thai coconut crunch for study breaks and busy days.",
            },
            {
                "Name": "Jason, the busy office snacker",
                "Profile": "32-year-old office employee in New Taipei City",
                "Needs": "A resealable afternoon snack with understandable ingredients.",
                "Buying behavior": (
                    "Compares nutrition labels and purchases snack multipacks online."
                ),
                "Message": "Real Thai coconut crunch, packed for your everyday break.",
            },
        ],
        "compliance_checklist": [
            "Confirm the Taiwan importer or local distribution partner",
            "Verify the correct customs classification",
            "Check commercial food-import inspection requirements",
            "Prepare Traditional Chinese ingredient and nutrition information",
            "Confirm allergen declarations for the final recipe",
            "Confirm country-of-origin and manufacturer information",
            "Verify shelf-life and storage instructions",
            "Avoid unsupported medical or health claims",
        ],
    },
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


# The five positive-direction weights add up to 1.00 (or 100%).
WEIGHTS = {
    "Demand": 0.25,
    "Cultural fit": 0.20,
    "Competitive opportunity": 0.20,
    "Profit margin": 0.20,
    "Promotion ease": 0.15,
}


def calculate_market_fit(
    demand, cultural_fit, competitive_opportunity, profit_margin, promotion_ease
):
    """Calculate a 0–100 score from five positive-direction 0–10 inputs."""

    weighted_score_out_of_10 = (
        demand * WEIGHTS["Demand"]
        + cultural_fit * WEIGHTS["Cultural fit"]
        + competitive_opportunity * WEIGHTS["Competitive opportunity"]
        + profit_margin * WEIGHTS["Profit margin"]
        + promotion_ease * WEIGHTS["Promotion ease"]
    )

    return weighted_score_out_of_10 * 10


def calculate_unit_economics(
    landed_cost,
    selling_price,
    retailer_fee_percent,
    marketing_cost_per_unit,
    other_variable_cost,
    monthly_fixed_cost,
):
    """Return safe unit-economics results for one pricing scenario."""

    # Gross profit only subtracts landed product cost. Contribution profit also
    # subtracts the variable costs required to make one sale.
    gross_profit = selling_price - landed_cost
    gross_margin = (
        gross_profit / selling_price * 100 if selling_price > 0 else None
    )
    retailer_fee = selling_price * retailer_fee_percent / 100
    total_variable_cost = (
        landed_cost
        + retailer_fee
        + marketing_cost_per_unit
        + other_variable_cost
    )
    contribution_profit = selling_price - total_variable_cost
    contribution_margin = (
        contribution_profit / selling_price * 100 if selling_price > 0 else None
    )

    # Break-even cannot be calculated when each additional sale contributes
    # zero or a negative amount toward monthly fixed costs.
    if contribution_profit > 0:
        break_even_units = monthly_fixed_cost / contribution_profit
        break_even_units_per_day = break_even_units / 30
    else:
        break_even_units = None
        break_even_units_per_day = None

    return {
        "gross_profit": gross_profit,
        "gross_margin": gross_margin,
        "retailer_fee": retailer_fee,
        "total_variable_cost": total_variable_cost,
        "contribution_profit": contribution_profit,
        "contribution_margin": contribution_margin,
        "break_even_units": break_even_units,
        "break_even_units_per_day": break_even_units_per_day,
    }


def get_recommendation(market_fit_score, contribution_margin):
    """Combine market fit and contribution margin into a pilot decision."""

    safe_margin = contribution_margin if contribution_margin is not None else -100

    if market_fit_score >= 75 and safe_margin >= 25:
        return (
            "GO — Strong pilot opportunity",
            "The assumptions support a pilot, but customer evidence and compliance checks are still required before scaling.",
            "success",
        )
    if market_fit_score >= 60 and safe_margin >= 15:
        return (
            "TEST — Run a limited Taiwan pilot",
            "The opportunity is promising, but the business should validate demand, repeat purchase, costs, and compliance through a controlled test.",
            "warning",
        )
    return (
        "REVIEW — Improve the business model",
        "Market fit or contribution economics are currently too weak. Improve the offer, price, costs, or evidence before investing.",
        "error",
    )


def money(value):
    """Format a number as New Taiwan dollars."""

    return f"NT${value:,.2f}"


def percent(value):
    """Format an optional percentage without causing zero-division errors."""

    return f"{value:.1f}%" if value is not None else "Not available"


def break_even_text(value):
    """Format an optional break-even result."""

    return f"{value:,.1f}" if value is not None else "Not achievable"


# -----------------------------------------------------------------------------
# PAGE HEADER AND PRODUCT SELECTOR
# -----------------------------------------------------------------------------
st.title("🇹🇼 Taiwan Market Entry Dashboard")
st.caption(
    "Evaluate six Thai products through market evidence, unit economics, "
    "strategy, and entry-risk analysis."
)

with st.sidebar:
    st.header("Product selection")
    selected_product = st.selectbox(
        "Choose a Thai product", list(PRODUCT_DATA.keys()), index=0
    )
    st.info(
        "Learning tip: change the scores and costs to test different scenarios. "
        "Each product keeps its values while this browser session is open."
    )
    st.markdown("**Currency:** New Taiwan dollar (NT$)")

product = PRODUCT_DATA[selected_product]

# Define the key before the competitor section. On each Streamlit rerun, this
# lets the table read the latest price entered later in the page.
selling_price_key = f"selling_price_{selected_product}"
current_selling_price = st.session_state.get(
    selling_price_key, float(product.get("selling_price", 0.0))
)


# -----------------------------------------------------------------------------
# 1. PRODUCT OVERVIEW
# -----------------------------------------------------------------------------
st.header("1. Product Overview")
st.subheader(selected_product)

overview_col1, overview_col2, overview_col3, overview_col4 = st.columns(4)
with overview_col1:
    st.metric("Category", product.get("category", "Not specified"))
with overview_col2:
    st.metric("Package size", product.get("package_size", "Varies by product"))
with overview_col3:
    with st.container(border=True):
        st.markdown("**Target customer**")
        st.write(product.get("target_customer", "Not specified"))
with overview_col4:
    with st.container(border=True):
        st.markdown("**Main competitors**")
        st.write(product.get("main_competitors", "Not specified"))


# -----------------------------------------------------------------------------
# 2. MARKET EVIDENCE
# -----------------------------------------------------------------------------
st.header("2. Market Evidence")
st.info(
    "The evidence and scores in this educational dashboard are starting assumptions. "
    "They should be validated with customer interviews, retailer data, competitor "
    "checks, and official regulations before a real investment decision."
)

market_evidence = product.get("market_evidence", [])
if market_evidence:
    st.dataframe(pd.DataFrame(market_evidence), width="stretch", hide_index=True)
else:
    st.write("Detailed market evidence has not yet been added for this sample product.")


# -----------------------------------------------------------------------------
# 3. COMPETITOR COMPARISON
# -----------------------------------------------------------------------------
st.header("3. Competitor Comparison")
st.write("Compare price, package, positioning, strengths, and weaknesses.")

competitor_df = pd.DataFrame(product.get("competitors", []))
our_product_row = pd.DataFrame(
    [
        {
            "Competitor": f"Our {selected_product}",
            "Typical price (NT$)": current_selling_price,
            "Package size": product.get("package_size", "Varies by product"),
            "Positioning": "Thai market entrant",
            "Key strength": "Thai origin and product story",
            "Weakness": "New brand with limited local awareness",
        }
    ]
)
comparison_df = pd.concat([our_product_row, competitor_df], ignore_index=True)
st.dataframe(comparison_df, width="stretch", hide_index=True)
st.caption(
    "Our product row uses the current scenario price. Competitor prices are "
    "category-level sample estimates and should be checked before a real launch."
)


# -----------------------------------------------------------------------------
# 4. PRICING AND UNIT ECONOMICS
# -----------------------------------------------------------------------------
st.header("4. Pricing and Unit Economics")
st.write(
    "Test how product cost, channel fees, marketing, and other variable costs "
    "affect the profit contributed by each sale."
)

price_col1, price_col2, price_col3 = st.columns(3)
with price_col1:
    landed_cost = st.number_input(
        "Landed cost per unit (NT$)",
        min_value=0.0,
        value=float(product.get("estimated_cost", 0.0)),
        step=1.0,
        key=f"landed_cost_{selected_product}",
        help="Product, shipping, import, and packaging cost per unit—not the final total business cost.",
    )
with price_col2:
    selling_price = st.number_input(
        "Selling price per unit (NT$)",
        min_value=0.0,
        value=float(product.get("selling_price", 0.0)),
        step=1.0,
        key=selling_price_key,
    )
with price_col3:
    retailer_fee_percent = st.number_input(
        "Retailer or platform fee (%)",
        min_value=0.0,
        value=float(product.get("retailer_fee_percent", 15.0)),
        step=1.0,
        key=f"retailer_fee_{selected_product}",
    )

cost_col1, cost_col2, cost_col3 = st.columns(3)
with cost_col1:
    marketing_cost_per_unit = st.number_input(
        "Marketing cost per unit (NT$)",
        min_value=0.0,
        value=float(product.get("marketing_cost_per_unit", 5.0)),
        step=1.0,
        key=f"marketing_cost_{selected_product}",
    )
with cost_col2:
    other_variable_cost = st.number_input(
        "Other variable cost per unit (NT$)",
        min_value=0.0,
        value=float(product.get("other_variable_cost", 3.0)),
        step=1.0,
        key=f"other_cost_{selected_product}",
    )
with cost_col3:
    monthly_fixed_cost = st.number_input(
        "Monthly fixed cost (NT$)",
        min_value=0.0,
        value=float(product.get("monthly_fixed_cost", 30000.0)),
        step=1000.0,
        key=f"fixed_cost_{selected_product}",
    )

economics = calculate_unit_economics(
    landed_cost,
    selling_price,
    retailer_fee_percent,
    marketing_cost_per_unit,
    other_variable_cost,
    monthly_fixed_cost,
)

unit_row1 = st.columns(4)
unit_row1[0].metric("Gross profit per unit", money(economics["gross_profit"]))
unit_row1[1].metric("Gross margin", percent(economics["gross_margin"]))
unit_row1[2].metric("Retailer fee per unit", money(economics["retailer_fee"]))
unit_row1[3].metric("Total variable cost", money(economics["total_variable_cost"]))

unit_row2 = st.columns(4)
unit_row2[0].metric(
    "Contribution profit per unit", money(economics["contribution_profit"])
)
unit_row2[1].metric("Contribution margin", percent(economics["contribution_margin"]))
unit_row2[2].metric(
    "Break-even units/month", break_even_text(economics["break_even_units"])
)
unit_row2[3].metric(
    "Break-even units/day", break_even_text(economics["break_even_units_per_day"])
)

if selling_price <= 0:
    st.warning("Margins cannot be calculated when the selling price is zero.")
elif economics["contribution_profit"] <= 0:
    st.error(
        "Break-even is not achievable under the current assumptions because "
        "contribution profit per unit is zero or negative."
    )
else:
    st.success(
        "Each sale contributes toward monthly fixed costs. Use the scenario table "
        "below to see how sensitive this result is."
    )

with st.expander("Understand the profit measures"):
    st.markdown(
        """
- **Gross profit** subtracts only landed product cost from selling price.
- **Gross margin** shows gross profit as a percentage of selling price.
- **Contribution profit** also subtracts retailer fees, unit marketing, and other variable costs.
- **Contribution margin** shows contribution profit as a percentage of selling price.
- **Net profit** is what remains after contribution profit also covers fixed costs, tax, and any other expenses.

Landed cost is important, but it is not the final total cost of operating the business.
"""
    )

st.subheader("Scenario Analysis")
scenario_settings = [
    {
        "Scenario": "Optimistic",
        "landed_cost": landed_cost * 0.90,
        "selling_price": selling_price * 1.05,
        "retailer_fee_percent": max(0.0, retailer_fee_percent - 2),
    },
    {
        "Scenario": "Base case",
        "landed_cost": landed_cost,
        "selling_price": selling_price,
        "retailer_fee_percent": retailer_fee_percent,
    },
    {
        "Scenario": "Conservative",
        "landed_cost": landed_cost * 1.15,
        "selling_price": selling_price * 0.95,
        "retailer_fee_percent": retailer_fee_percent + 3,
    },
]

scenario_rows = []
for scenario in scenario_settings:
    scenario_result = calculate_unit_economics(
        scenario["landed_cost"],
        scenario["selling_price"],
        scenario["retailer_fee_percent"],
        marketing_cost_per_unit,
        other_variable_cost,
        monthly_fixed_cost,
    )
    scenario_rows.append(
        {
            "Scenario": scenario["Scenario"],
            "Selling price": money(scenario["selling_price"]),
            "Landed cost": money(scenario["landed_cost"]),
            "Gross margin": percent(scenario_result["gross_margin"]),
            "Contribution profit": money(scenario_result["contribution_profit"]),
            "Contribution margin": percent(scenario_result["contribution_margin"]),
            "Break-even units per month": break_even_text(
                scenario_result["break_even_units"]
            ),
        }
    )

st.dataframe(pd.DataFrame(scenario_rows), width="stretch", hide_index=True)


# -----------------------------------------------------------------------------
# 5. MARKET FIT SCORE
# -----------------------------------------------------------------------------
st.header("5. Market Fit Score")
st.write(
    "All factors use one direction: **higher score = better market-entry conditions**."
)

# Stored competition and promotion values describe difficulty, so convert their
# defaults once for the positive-direction sliders shown to the user.
competitive_opportunity_default = 10 - int(product.get("competition_level", 5))
promotion_ease_default = 10 - int(product.get("promotion_difficulty", 5))

fit_col1, fit_col2 = st.columns(2)
with fit_col1:
    demand = st.slider(
        "Demand", 0, 10, int(product.get("demand_score", 5)),
        key=f"demand_{selected_product}",
        help="Higher score = better market-entry conditions",
    )
    cultural_fit = st.slider(
        "Cultural Fit", 0, 10, int(product.get("cultural_fit", 5)),
        key=f"culture_{selected_product}",
        help="Higher score = better market-entry conditions",
    )
    profit_margin_potential = st.slider(
        "Profit Margin Potential", 0, 10,
        int(product.get("profit_margin_score", 5)),
        key=f"profit_potential_{selected_product}",
        help="Higher score = better market-entry conditions",
    )
with fit_col2:
    competitive_opportunity = st.slider(
        "Competitive Opportunity", 0, 10, competitive_opportunity_default,
        key=f"opportunity_{selected_product}",
        help="Higher score = better market-entry conditions",
    )
    promotion_ease = st.slider(
        "Promotion Ease", 0, 10, promotion_ease_default,
        key=f"promotion_ease_{selected_product}",
        help="Higher score = better market-entry conditions",
    )

market_fit_score = calculate_market_fit(
    demand,
    cultural_fit,
    competitive_opportunity,
    profit_margin_potential,
    promotion_ease,
)
st.metric("Market Fit Score", f"{market_fit_score:.1f} / 100")

fit_factors = pd.Series(
    {
        "Demand": demand,
        "Cultural Fit": cultural_fit,
        "Competitive Opportunity": competitive_opportunity,
        "Profit Margin Potential": profit_margin_potential,
        "Promotion Ease": promotion_ease,
    }
)
sorted_fit_factors = fit_factors.sort_values()
factor_colors = [
    "#1f77b4" if value >= 7 else "#f39c12"
    for value in sorted_fit_factors.values
]
fig, ax = plt.subplots(figsize=(8, 3.4))
sorted_fit_factors.plot(kind="barh", ax=ax, color=factor_colors)
ax.set_xlim(0, 10)
ax.set_xlabel("Score (higher is better)")
ax.set_ylabel("")
ax.grid(axis="x", alpha=0.25)
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

with st.expander("See the score calculation"):
    st.code(
        f"""Demand:                   {demand} × 25% = {demand * 0.25:.2f}
Cultural Fit:              {cultural_fit} × 20% = {cultural_fit * 0.20:.2f}
Competitive Opportunity:  {competitive_opportunity} × 20% = {competitive_opportunity * 0.20:.2f}
Profit Margin Potential:   {profit_margin_potential} × 20% = {profit_margin_potential * 0.20:.2f}
Promotion Ease:            {promotion_ease} × 15% = {promotion_ease * 0.15:.2f}
--------------------------------------------------------
Market Fit Score = {market_fit_score:.1f} / 100""",
        language="text",
    )

with st.expander("Market Fit scoring guide"):
    st.markdown(
        """
- **0–3:** Weak or unsupported
- **4–6:** Possible, but meaningful risks remain
- **7–8:** Good initial fit
- **9–10:** Strong fit supported by evidence
"""
    )

weakest_factor = fit_factors.idxmin()
weakest_factor_score = int(fit_factors.min())


# -----------------------------------------------------------------------------
# 6. SWOT AND ACTION PLAN
# -----------------------------------------------------------------------------
st.header("6. SWOT and Action Plan")
swot = product.get("swot", {})
swot_items = [
    ("Strengths", swot.get("Strengths", "Not yet defined")),
    ("Weaknesses", swot.get("Weaknesses", "Not yet defined")),
    ("Opportunities", swot.get("Opportunities", "Not yet defined")),
    ("Threats", swot.get("Threats", "Not yet defined")),
]
for row_start in range(0, 4, 2):
    swot_columns = st.columns(2)
    for column, (label, note) in zip(
        swot_columns, swot_items[row_start : row_start + 2]
    ):
        with column:
            with st.container(border=True):
                st.subheader(label)
                st.write(note)

st.subheader("Action Plan")
swot_actions = product.get("swot_actions", {})
if swot_actions:
    action_columns = st.columns(2)
    for index, (label, action) in enumerate(swot_actions.items()):
        with action_columns[index % 2]:
            st.markdown(f"**{label}**")
            st.write(action)
else:
    st.write("A detailed action plan has not yet been added for this product.")


# -----------------------------------------------------------------------------
# 7. 4P MARKETING STRATEGY AND KPIs
# -----------------------------------------------------------------------------
st.header("7. 4P Marketing Strategy and KPIs")
four_p = product.get("marketing_4p", {})
four_p_columns = st.columns(4)
for column, label in zip(four_p_columns, ["Product", "Price", "Place", "Promotion"]):
    with column:
        with st.container(border=True):
            st.subheader(label)
            st.write(four_p.get(label, "Not yet defined"))

st.subheader("Pilot Marketing KPIs")
marketing_kpis = product.get("marketing_kpis", {})
if marketing_kpis:
    kpi_columns = st.columns(3)
    for index, (label, value) in enumerate(marketing_kpis.items()):
        kpi_columns[index % 3].metric(label, value)
else:
    st.write("Pilot KPIs have not yet been defined for this product.")


# -----------------------------------------------------------------------------
# 8. CUSTOMER PERSONAS
# -----------------------------------------------------------------------------
st.header("8. Customer Personas")

# New products can contain a list; older records keep their original dictionary.
personas = product.get("personas", [])
if not personas and product.get("persona"):
    personas = [product.get("persona")]

if personas:
    persona_columns = st.columns(min(len(personas), 2))
    for index, persona in enumerate(personas):
        with persona_columns[index % len(persona_columns)]:
            with st.container(border=True):
                st.subheader(persona.get("Name", "Unnamed persona"))
                st.write(f"**Profile:** {persona.get('Profile', 'Not specified')}")
                st.write(f"**Needs:** {persona.get('Needs', 'Not specified')}")
                st.write(
                    f"**Buying behavior:** "
                    f"{persona.get('Buying behavior', 'Not specified')}"
                )
                st.write(f"**Message:** “{persona.get('Message', 'Not specified')}”")
else:
    st.write("Customer personas have not yet been added for this product.")


# -----------------------------------------------------------------------------
# 9. COMPLIANCE AND RISK CHECKLIST
# -----------------------------------------------------------------------------
st.header("9. Compliance and Risk Checklist")
compliance_items = product.get("compliance_checklist", [])
if compliance_items:
    checklist_columns = st.columns(2)
    for index, item in enumerate(compliance_items):
        with checklist_columns[index % 2]:
            st.checkbox(
                item,
                value=False,
                disabled=True,
                key=f"compliance_{selected_product}_{index}",
            )
else:
    st.write("A detailed compliance checklist has not yet been added for this product.")

st.warning(
    "This is an educational checklist, not legal advice. The business must confirm "
    "the latest Taiwan food-import, inspection, labeling, ingredient, allergen, tax, "
    "and customs requirements with official authorities and qualified local partners."
)


# -----------------------------------------------------------------------------
# 10. FINAL RECOMMENDATION
# -----------------------------------------------------------------------------
st.header("10. Final Recommendation")
recommendation, explanation, message_type = get_recommendation(
    market_fit_score, economics["contribution_margin"]
)
confidence_level = product.get(
    "confidence_level", "Low" if not market_evidence else "Medium"
)

if message_type == "success":
    st.success(f"**{recommendation}**\n\n{explanation}")
elif message_type == "warning":
    st.warning(f"**{recommendation}**\n\n{explanation}")
else:
    st.error(f"**{recommendation}**\n\n{explanation}")

summary_row1 = st.columns(4)
summary_row1[0].metric("Market Fit Score", f"{market_fit_score:.1f}/100")
summary_row1[1].metric("Gross Margin", percent(economics["gross_margin"]))
summary_row1[2].metric(
    "Contribution Margin", percent(economics["contribution_margin"])
)
summary_row1[3].metric(
    "Contribution Profit/Unit", money(economics["contribution_profit"])
)

summary_row2 = st.columns(3)
summary_row2[0].metric(
    "Break-even Units/Month", break_even_text(economics["break_even_units"])
)
summary_row2[1].metric(
    "Weakest Market Fit Factor", f"{weakest_factor} ({weakest_factor_score}/10)"
)
summary_row2[2].metric("Confidence Level", confidence_level)

st.subheader("Conditions required before GO")
conditions_before_go = [
    "Test at least 300 packs or tasting portions",
    "Achieve at least 15% sample-to-purchase conversion",
    "Achieve at least 20% repeat purchase intention or repeat purchases",
    "Maintain contribution margin above 25%",
    "Receive an average customer score of at least 4.3/5",
    "Complete the food-import and labeling compliance review",
]
for condition in conditions_before_go:
    st.markdown(f"- {condition}")

st.write(
    f"**Priority action:** Strengthen **{weakest_factor}**, currently the lowest "
    f"Market Fit factor at {weakest_factor_score}/10, and validate it with evidence."
)

with st.expander("Sources, assumptions, and research limits"):
    st.markdown(
        """
**Research references to consult**

- USDA Foreign Agricultural Service — *Taiwan Retail Foods Annual 2025*
- Taiwan Food and Drug Administration — *Food Guidance, Laws and Regulations*
- Taiwan Ministry of Economic Affairs retail statistics

**Limits of this educational dashboard**

- Competitor prices are sample estimates, not verified current quotations.
- Costs and channel fees are sample assumptions, not supplier or retailer contracts.
- Regulations must be checked again with official authorities and qualified local partners before a real launch.
- Scores represent an initial hypothesis, not proven market demand.
- This project does not claim regulatory approval, a retailer agreement, or guaranteed sales.
"""
    )

st.caption(
    "Educational portfolio project: validate every commercial, customer, and "
    "regulatory assumption before investing."
)
