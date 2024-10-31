iimport requests
import pandas as pd

# API endpoint for posts
url = "https://www.attackingfootball.com/wp-json/wp/v2/posts"

# Request data
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    posts = response.json()
    
    # Extract titles and URLs
    articles = [{"title": post.get("title", {}).get("rendered"), "url": post.get("link")} for post in posts]
    
    # Create a DataFrame for easy viewing and manipulation
    articles_df = pd.DataFrame(articles)
    print(articles_df)
    
    # Save to a text file
    with open("articles_list.txt", "w") as file:
        for article in articles:
            file.write(f"Title: {article['title']}\nURL: {article['url']}\n\n")
    
    print("Articles saved to articles_list.txt")
else:
    print("Failed to retrieve data from the API.")
