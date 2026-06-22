import streamlit as st
from news_fetch import fetch_news, filter_relevant
from risk_scorer import score_article
from scenario import SCENARIOS, run_scenario

st.set_page_config(page_title="Energy Risk Dashboard", layout="wide")

st.title("🛢️ India Energy Supply Chain — Risk Dashboard")
st.caption("AI-powered geopolitical risk monitoring & scenario analysis")

tab1, tab2 = st.tabs(["Live Risk Feed", "Scenario Modeller"])

# ── TAB 1: RISK FEED ──────────────────────────────────────────
with tab1:
    articles = filter_relevant(fetch_news())
    results = []
    for article in articles:
        result = score_article(article["title"])
        result["headline"] = article["title"]
        result["source"] = article["source"]
        results.append(result)
    results.sort(key=lambda x: x["score"], reverse=True)

    col1, col2, col3 = st.columns(3)
    high   = len([r for r in results if r["severity"] == "high"])
    medium = len([r for r in results if r["severity"] == "medium"])
    low    = len([r for r in results if r["severity"] == "low"])
    col1.metric("🔴 High Risk", high)
    col2.metric("🟡 Medium Risk", medium)
    col3.metric("🟢 Low Risk", low)

    st.divider()
    st.subheader("Live Risk Feed")
    for r in results:
        color = "🔴" if r["severity"] == "high" else "🟡" if r["severity"] == "medium" else "🟢"
        with st.expander(f"{color} [{r['score']}/10] {r['headline']}"):
            st.write(f"**Corridor:** {r['corridor']}")
            st.write(f"**Severity:** {r['severity']}")
            st.write(f"**Source:** {r['source']}")

# ── TAB 2: SCENARIO MODELLER ──────────────────────────────────
with tab2:
    st.subheader("Disruption Scenario Modeller")
    st.caption("Select a scenario to see cascading economic impacts")

    selected = st.selectbox("Choose a disruption scenario:", list(SCENARIOS.keys()))
    
    if st.button("Run Scenario"):
        s = run_scenario(selected)

        st.error(f"**{selected}**  \n{s['description']}")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Oil Price Increase", f"+{s['oil_price_increase']}%")
        col2.metric("Supply Reduction", f"-{s['supply_reduction']}%")
        col3.metric("India Impact", f"{s['india_impact_days']} days")
        col4.metric("Fuel Price Hike", f"+{s['fuel_price_hike']}%")

        st.divider()

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("**Affected Refiners**")
            for refiner in s["affected_refiners"]:
                st.write(f"• {refiner}")
            st.metric("GDP Impact", f"{s['gdp_impact']}%")

        with col_b:
            st.markdown("**Procurement Rerouting Recommendations**")
            for i, option in enumerate(s["rerouting_options"], 1):
                st.info(f"Option {i}: {option}")