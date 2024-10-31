import requests
import pandas as pd

# Base API endpoint for posts
url = "https://www.attackingfootball.com/wp-json/wp/v2/posts"
all_articles = []
page = 1

while True:
    # Request data with pagination parameters
    response = requests.get(url, params={"page": page, "per_page": 100})
    
    # Check if request was successful
    if response.status_code == 200:
        posts = response.json()
        
        # Break loop if no more posts are returned
        if not posts:
            break

        # Extract titles and URLs
        articles = [{"title": post.get("title", {}).get("rendered"), "url": post.get("link")} for post in posts]
        all_articles.extend(articles)
        
        # Go to the next page
        page += 1
    else:
        print("Failed to retrieve data from the API.")
        break

# Create a DataFrame for easy viewing and manipulation
articles_df = pd.DataFrame(all_articles)
print(articles_df)

# Save to a text file
with open("articles_list.txt", "w") as file:
    for article in all_articles:
        file.write(f"Title: {article['title']}\nURL: {article['url']}\n\n")

print("All articles saved to articles_list.txt")
