from login import login_with_selenium
from session import create_requests_session
from search import search_posts
from like import like_post
import time

USERNAME = "yknfjguzizojlqyrid@nbmbb.com"
PASSWORD = "password123123"

def main():
    # Login with Selenium and get the driver, cookies, and user agent
    driver, cookies, user_agent = login_with_selenium(USERNAME, PASSWORD)

    # Initiate requests session with cookies and user agent
    session = create_requests_session(cookies, user_agent)

    # Now you can quit the Selenium driver since you've got all you need
    driver.quit()

    # Initial search query
    query = "awsome"
    rank_token = None
    next_max_id = None

    # Set to track liked posts
    liked_posts = set()
    total_likes = 0

    while True:
        # Perform the search query
        media_ids, rank_token, next_max_id = search_posts(session, query, rank_token, next_max_id)
        print("\n---\nNEW BATCH OF POSTS AQUIRED")

        # Like each post in the extracted media IDs if not already liked
        for media_id in media_ids:
            if media_id not in liked_posts:
                like_post(session, media_id)
                liked_posts.add(media_id)
                total_likes += 1
                time.sleep(2)  # Delay between likes to mimic human behavior
            
        print(f"total likes: {total_likes}")

        # If there's no more data, break the loop
        if not next_max_id:
            break

if __name__ == "__main__":
    main()
