import os
from dotenv import load_dotenv

# google api libs
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# loading YT key
load_dotenv()
YT_API_KEY: str = os.getenv("YOUTUBE_API_KEY")

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    print("Hello from youtube-notification-bot!")

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YT.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )

    credentials = flow.run_local_server(port=8080)

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials
    )

    request = youtube.subscriptions().list(part="snippet,contentDetails", mine=True)
    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()
