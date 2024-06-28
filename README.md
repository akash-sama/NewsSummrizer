# News Summarizer Application

## Overview:
This application demonstrates a news generating site. The top 4 articles are retrieved from the News API and summarized using Google's Gemini API. The summarized news articles are then displayed in an attractive manner using a Flask application.

## Prerequisites:
To run this application, you need two API keys. As a standard best practice, they have been omitted here. You can obtain the keys for free from the following sources:

- **NEWS API**: [Get API Key](https://newsapi.org/)
- **GEMINI API**: [Get API Key](https://aistudio.google.com/app/apikey)

## Features:
- **News Retrieval**: Fetches the top 4 articles from the News API.
- **News Summarization**: Summarizes the articles using the Gemini API.
- **Flask Application**: Displays the summarized news in an attractive manner.



## Configuration:
Change the sum.py of the project and add your API keys:

    ```sh
    NEWS_API_KEY = your_news_api_key
    GEMINI_API_KEY = your_gemini_api_key
    ```

## Running the Application
1. Start the Flask application:
    ```sh
    flask run
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000` to view the summarized news articles.

## Usage Demo:
