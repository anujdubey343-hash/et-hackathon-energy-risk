SCENARIOS = {
    "Hormuz 30% Blockage": {
        "corridor": "Hormuz",
        "description": "Partial closure of Strait of Hormuz due to Iran-US standoff",
        "oil_price_increase": 22,
        "supply_reduction": 30,
        "india_impact_days": 18,
        "affected_refiners": ["Reliance", "BPCL", "HPCL"],
        "rerouting_options": [
            "Shift to West Africa sources (Nigeria, Angola) — +8 days transit",
            "Activate US SPR emergency allocation — covers 12 days",
            "Increase Russia pipeline imports via Central Asia — +15% volume",
        ],
        "gdp_impact": -0.4,
        "fuel_price_hike": 12,
    },
    "Red Sea Complete Suspension": {
        "corridor": "Red Sea",
        "description": "Full suspension of Red Sea shipping due to Houthi attacks",
        "oil_price_increase": 15,
        "supply_reduction": 20,
        "india_impact_days": 14,
        "affected_refiners": ["Reliance", "MRPL"],
        "rerouting_options": [
            "Cape of Good Hope rerouting — +14 days, +$2.1M per voyage",
            "Air freight for critical refined products",
            "Activate strategic petroleum reserves — 9.5 days cover",
        ],
        "gdp_impact": -0.2,
        "fuel_price_hike": 8,
    },
    "OPEC+ Emergency Cut": {
        "corridor": "OPEC",
        "description": "OPEC+ announces 2M barrel/day emergency production cut",
        "oil_price_increase": 18,
        "supply_reduction": 15,
        "india_impact_days": 10,
        "affected_refiners": ["All Indian refiners"],
        "rerouting_options": [
            "Increase US shale oil imports — spot market premium +$4/barrel",
            "Activate bilateral agreement with UAE for emergency supply",
            "Reduce non-essential refinery runs by 10%",
        ],
        "gdp_impact": -0.3,
        "fuel_price_hike": 10,
    },
}

def run_scenario(name):
    return SCENARIOS.get(name, None)