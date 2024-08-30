import requests

def search_posts(session, query, rank_token, next_max_id):
    url = "https://www.instagram.com/api/v1/fbsearch/search_engine_result_page/"
    params = {
        "query": query,
    }
    if rank_token: 
        params["rank_token"] = rank_token
        params["next_max_id"] = next_max_id

    response = session.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract media IDs
        media_ids = []
        for section in data.get('sections', []):
            for layout_content in section.get('layout_content', {}).values():
                if isinstance(layout_content, list):
                    for item in layout_content:
                        media_id = item.get('media', {}).get('pk')
                        if media_id and media_id not in media_ids:
                            media_ids.append(media_id)

        # Ensure unique media IDs and update pagination parameters
        next_max_id = data.get('next_max_id')
        rank_token = data.get('rank_token')

        return media_ids, rank_token, next_max_id

    else:
        print(f"Failed to retrieve posts. Status Code: {response.status_code}")
        return [], None, None