
GOOGLE_API_KEY = 'AIzaSyAZBo5jtrJFGb32Qf-gRadD3v7HRSM73HY'
NEWS_API_KEY = '59405fbcac10444f86caf44b1ac3e3d2'

import requests
import google.generativeai as genai

def fetch_news(topic):
    """ Fetches news articles based on the given topic. """
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': topic,
        'apiKey': NEWS_API_KEY,
        'language': 'en',
        'pageSize': 4
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['articles']
    else:
        return None


def generate(topic, articles):
    """Generates a concise summary based on multiple articles using a language model."""
    descriptions = '. '.join(
        [f"{article['title']}: {article['description']}" for article in articles if article['description']])
    prompt = f"Make a concise summary on the latest developments or latest news on {topic} and incorporate the following article summaries: {descriptions}"

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    text_summary = response.text

    text_summary = text_summary.replace('## ', '').replace('\n\n', '\n').replace('*', '')
    return text_summary


def summarize(topic):
    """ displays it in JSON format for the flask we are going to make """
    articles = fetch_news(topic)
    if articles:
        report = generate(topic, articles)
        sources = [{'title': article['title'], 'url': article['url']} for article in articles]
        final_summary = {
            "topic": topic,
            "concise_report": report,
            "sources": sources
        }
        return final_summary
    else:
        return {"error": "No articles found or failed to fetch articles."}


if __name__ == "__main__":
    print(summarize("Gen Ai in india"))
    #print(summarize("football")

