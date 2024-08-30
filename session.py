import requests

def create_requests_session(cookies, user_agent):
    session = requests.Session()

    # Set cookies
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])

    # Set user-agent in headers
    session.headers.update({
        "User-Agent": user_agent,
        "x-csrftoken": session.cookies.get("csrftoken"),
        "x-ig-app-id": "936619743392459",
        "x-requested-with": "XMLHttpRequest",
    })

    return session

