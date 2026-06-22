import random
from news_fetch import fetch_news, filter_relevant

CORRIDOR_MAP = {
    "hormuz": "Hormuz", "iran": "Hormuz", "persian gulf": "Hormuz",
    "red sea": "Red Sea", "houthi": "Red Sea",
    "opec": "OPEC", "crude oil": "OPEC", "tanker": "Other",
    "sanctions": "Other"
}

def score_article(headline):
    h = headline.lower()
    corridor = "Other"
    for keyword, corr in CORRIDOR_MAP.items():
        if keyword in h:
            corridor = corr
            break
    
    if any(w in h for w in ["attack", "intensif", "surge", "down", "spike", "forced"]):
        score = round(random.uniform(7, 9.5), 1)
        severity = "high"
    elif any(w in h for w in ["consider", "discusses", "renewed", "meet"]):
        score = round(random.uniform(4, 6.9), 1)
        severity = "medium"
    else:
        score = round(random.uniform(2, 3.9), 1)
        severity = "low"
    
    return {"score": score, "corridor": corridor, "severity": severity, "reason": "Keyword-based scoring"}

if __name__ == "__main__":
    articles = filter_relevant(fetch_news())
    print("Scoring articles...\n")
    for article in articles:
        result = score_article(article["title"])
        print(f"Headline : {article['title']}")
        print(f"Score    : {result['score']}/10")
        print(f"Severity : {result['severity']}")
        print(f"Corridor : {result['corridor']}")
        print("-" * 60)