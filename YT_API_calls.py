import os
import pickle
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
        self.__credentials_file: str = "YT.pickle"
        self.__api_service_name: str = "youtube"
        self.__api_version: str = "v3"
        self.__scopes: list[str] = ["https://www.googleapis.com/auth/youtube.readonly"]
        self.youtube = self.create_client(port=8080)

    def create_client(self, port):
        """Create and authenticate YouTube API client"""
        credentials = None

        if os.path.exists(self.__credentials_file):
            print("load cred")
            with open(self.__credentials_file, "rb") as token:
                credentials = pickle.load(token)

        if not credentials:
            # Get credentials and create an API client
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                self.__client_secrets_file, self.__scopes
            )
            credentials = flow.run_local_server(port=port)
            with open(self.__credentials_file, "wb") as token:
                print("write cred")
                pickle.dump(credentials, token)

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
        cleaned_subscriptions: list[list[str]] = []
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

    def get_videos_for_channel_ids(
        self, channel_ids: list[str], max_results: int = 10
    ) -> list[list[str]]:
        """Get cleaned videos data for each channel ids: [title, description, video_id]"""
        responses = []
        for channel_id in channel_ids:
            request = self.youtube.search().list(
                part="snippet",
                channelId=channel_id,
                maxResults=max_results,  # default is 5
                type="video",  # other options: channel and playlist
                videoDuration="medium",  # short: 4min-, medium: 4-20min, long: 20min+
            )
            responses.append(request.execute())

        cleaned_videos: list[list[str]] = []
        for response in responses:
            for item in response["items"]:
                cleaned_videos.append(
                    [
                        item["snippet"]["title"],
                        item["snippet"]["description"],
                        item["id"]["videoId"],
                    ]
                )

        return cleaned_videos
