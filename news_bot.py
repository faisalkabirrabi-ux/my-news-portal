import feedparser
import json

def fetch_news():
    # সব ক্যাটাগরির নিউজের RSS লিঙ্ক এখানে দেওয়া হয়েছে
    news_sources = {
        "bangla": {
            "বিবিসি বাংলা": "https://www.bbc.com/bengali/index.xml",
            "সময় টিভি": "https://somoynews.tv/feed",
            "ইত্তেফাক": "https://www.ittefaq.com.bd/rss.xml",
            "বিডিনিউজ২৪": "https://bangla.bdnews24.com/?widgetName=rssfeed&widgetId=1151&getXmlFeed=true"
        },
        "english": {
            "Daily Star": "https://www.thedailystar.net/rss.xml",
            "Dhaka Tribune": "https://www.dhakatribune.com/rss.xml"
        },
        "international": {
            "Al Jazeera": "https://www.aljazeera.com/xml/rss/all.xml",
            "Reuters World": "https://www.reutersagency.com/feed/?best-topics=world",
            "BBC World": "http://feeds.bbci.co.uk/news/world/rss.xml"
        }
    }
    
    all_data = {"bangla": [], "english": [], "international": []}
    
    for category, sources in news_sources.items():
        for name, url in sources.items():
            try:
                feed = feedparser.parse(url)
                # প্রতি সোর্স থেকে ৫টি করে লেটেস্ট নিউজ নেওয়া হচ্ছে
                for entry in feed.entries[:5]:
                    all_data[category].append({
                        "title": entry.title,
                        "link": entry.link,
                        "source": name
                    })
            except Exception as e:
                print(f"Error fetching from {name}: {e}")
    
    # ডাটাগুলো news.json ফাইলে সেভ করা হচ্ছে
    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)
    print("✅ All News Updated Successfully!")

if __name__ == "__main__":
    fetch_news()
