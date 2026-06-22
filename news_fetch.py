def fetch_news():
    articles = [
        {"title": "Houthi attacks intensify on Red Sea shipping lanes", "source": "Reuters"},
        {"title": "OPEC+ considers emergency output cut amid tensions", "source": "Bloomberg"},
        {"title": "Iran sanctions renewed by US Treasury Department", "source": "BBC"},
        {"title": "Strait of Hormuz traffic down 15% after standoff", "source": "Al Jazeera"},
        {"title": "Crude oil prices surge on Persian Gulf security fears", "source": "Reuters"},
        {"title": "Indian refiners forced to spot market as tanker rates spike", "source": "ET"},
        {"title": "Red Sea rerouting adds 14 days to Asia-Europe shipping", "source": "Lloyd's"},
        {"title": "G7 discusses coordinated response to oil supply threats", "source": "BBC"},
    ]
    return articles

def filter_relevant(articles):
    KEYWORDS = ["Hormuz", "Red Sea", "OPEC", "Iran", "crude oil", "tanker", "sanctions", "Houthi", "Persian Gulf"]
    relevant = []
    for article in articles:
        for keyword in KEYWORDS:
            if keyword.lower() in article["title"].lower():
                relevant.append(article)
                break
    return relevant

if __name__ == "__main__":
    all_news = fetch_news()
    relevant_news = filter_relevant(all_news)

    print(f"Total articles: {len(all_news)}")
    print(f"Relevant articles: {len(relevant_news)}")
    print("\nRelevant headlines:")
    for article in relevant_news:
        print(f"  - {article['title']}")