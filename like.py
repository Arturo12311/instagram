def like_post(session, media_id):
    url = "https://www.instagram.com/graphql/query/"

    headers = {
        "content-type": "application/json",
        "x-csrftoken": session.cookies.get("csrftoken"),
        "x-ig-app-id": "936619743392459",
        "x-fb-friendly-name": "usePolarisLikeMediaLikeMutation",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    }

    payload = {
        "variables": {
            "media_id": media_id
        },
        "doc_id": "8244673538908708"
    }

    response = session.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"Successfully liked the post {media_id}!")
    else:
        print(f"Failed to like the post {media_id}. Status Code: {response.status_code}")
        print("Response:", response.text)
