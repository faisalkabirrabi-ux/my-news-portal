import feedparser
import json

def fetch_news():
    news_sources = {
        "বাংলাদেশ": {
            "বিবিসি বাংলা": "https://www.bbc.com/bengali/index.xml",
            "সময় টিভি": "https://somoynews.tv/feed",
            "ইত্তেফাক": "https://www.ittefaq.com.bd/rss.xml",
            "বিডিনিউজ২৪": "https://bangla.bdnews24.com/?widgetName=rssfeed&widgetId=1151&getXmlFeed=true",
            "যুগান্তর": "https://www.jugantor.com/feed"
        },
        "আন্তর্জাতিক": {
            "আল জাজিরা": "https://www.aljazeera.com/xml/rss/all.xml",
            "BBC World": "http://feeds.bbci.co.uk/news/world/rss.xml"
        },
        "খেলাধুলা": {
            "ESPN Cricinfo": "https://www.espncricinfo.com/rss/content/story/feeds/0.xml",
            "BBC Sports": "https://www.bbc.com/sport/rss.xml"
        },
        "প্রযুক্তি": {
            "TechCrunch": "https://techcrunch.com/feed/",
            "Wired": "https://www.wired.com/feed/rss"
        }
    }
    
    all_data = {cat: [] for cat in news_sources.keys()}
    
    for category, sources in news_sources.items():
        for name, url in sources.items():
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries[:6]: # প্রতি পত্রিকা থেকে ৬টি তাজা খবর
                    all_data[category].append({
                        "title": entry.title,
                        "link": entry.link,
                        "source": name
                    })
            except Exception as e:
                print(f"Error with {name}: {e}")
    
    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    fetch_news()
