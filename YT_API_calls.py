import os
from dotenv import load_dotenv

# The Google APIs Client Libraries for Python
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Loading YT key and setting static variables
load_dotenv()

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


class YouTubeAPICallsClient:
    def __init__(self) -> None:
        self.__yt_api_key: str = os.getenv("YOUTUBE_API_KEY", "")
        self.__client_secrets_file: str = "YT.json"
        self.__api_service_name: str = "youtube"
        self.__api_version: str = "v3"
        self.__scopes: list[str] = ["https://www.googleapis.com/auth/youtube.readonly"]
        self.youtube = self.create_client(port=8080)

    def create_client(self, port):
        """Create and authenticate YouTube API client"""
        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            self.__client_secrets_file, self.__scopes
        )
        credentials = flow.run_local_server(port=port)
        return googleapiclient.discovery.build(
            self.__api_service_name, self.__api_version, credentials=credentials
        )

    def get_subscriptions_info(self) -> list[list[str]]:
        """Get cleaned subscription data: [title, description, channel_id]"""
        request = self.youtube.subscriptions().list(
            part="snippet,contentDetails", mine=True
        )
        response = request.execute()

        # Prepare cleaned subs info: title / description / channel ID
        subscriptions = response.get("items", [])
        cleaned_subscriptions: list = []
        print(f"Found {len(subscriptions)} subscriptions")
        for sub in subscriptions:
            sub_data = sub["snippet"]
            cleaned_subscriptions.append(
                [
                    sub_data["title"],
                    sub_data["description"],
                    sub_data["resourceId"]["channelId"],
                ]
            )
        return cleaned_subscriptions

    def get_videos_for_channel_ids(self, channel_ids: list[str]):
        responses = []
        for channel_id in channel_ids:
            request = self.youtube.channels().list(
                part="snippet,contentDetails,statistics", id=channel_id, maxResults=5
            )
            responses.append(request.execute())
        return responses
