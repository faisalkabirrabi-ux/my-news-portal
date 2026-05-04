import feedparser
import json

def fetch_news():
    news_sources = {
        "bangla": {
            "Prothom Alo": "https://www.prothomalo.com/feed/topic/bangladesh",
            "Ittefaq": "https://www.ittefaq.com.bd/rss.xml"
        },
        "english": {
            "Daily Star": "https://www.thedailystar.net/rss.xml",
            "Dhaka Tribune": "https://www.dhakatribune.com/rss.xml"
        }
    }
    
    all_news = {"bangla": [], "english": []}
    
    for category, sources in news_sources.items():
        for name, url in sources.items():
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]: # প্রতি সোর্স থেকে ৫টি নিউজ
                all_news[category].append({
                    "title": entry.title,
                    "link": entry.link,
                    "source": name
                })
    
    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(all_news, f, ensure_ascii=False, indent=4)
    print("✅ News Updated!")

if __name__ == "__main__":
    fetch_news()
