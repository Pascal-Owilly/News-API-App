# Create a virtual environment
# import Flask from flask module
# Then initialize our app instance using the imported Flask
from distutils.log import debug
from importlib.resources import contents
from flask import Flask,render_template
from newsapi import NewsApiClient


app = Flask(__name__)
@app.route("/")
def home():
    # To get athorize we use the id and the api_key
    # We use sources provided by the news sites
    newsapi = NewsApiClient(api_key="88cdeb5bea694d6888cd2dda6e6fae00")
    all_news = newsapi.get_everything(sources = 'bbc-news, cnn,al-jazeera-english', page_size=60)

    # Fetching articles of the top newss headlines
    all_articles = all_news['articles']
    #  Get all articles

    # Creating empty lists to store the top headlines 
    news = []
    description = []
    images = []
    date_published = []
    news_url = []

# Use for loops to store all our contents
    for i in range(len(all_articles)):
        top_news_articles = all_articles[i]

        # apppend articles into the lists
        news.append(top_news_articles['title'])
        description.append(top_news_articles['description'])
        images.append(top_news_articles['urlToImage'])
        date_published.append(top_news_articles['publishedAt'])
        news_url.append(top_news_articles['url'])

        # Make a zip to find the contents directly
    articles = zip(news,description,images,date_published,news_url)



    # all_top_news = newsapi.get_everything(sources = 'bbc-news') 
    #  # Creating empty lists to store the top headlines 
   

# We now render this in our .html





    return render_template("index.html",articles=articles)  
   

if __name__=='__main__':
    app.run(debug=True)

