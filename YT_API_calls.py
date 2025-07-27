import os
import pickle
from dotenv import load_dotenv

# The Google APIs Client Libraries for Python
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


class YouTubeAPICallsClient:
    """YT client which makes API calls.
    For now it retrives current users subs list and videos for these channels."""

    def __init__(self) -> None:
        # Loading YT key and setting static variables
        load_dotenv()
        self.__yt_api_key: str = os.getenv("YOUTUBE_API_KEY", "")
        self.__client_secrets_file: str = "YT.json"
        self.__credentials_file: str = "YT.pickle"
        self.__api_service_name: str = "youtube"
        self.__api_version: str = "v3"
        self.__scopes: list[str] = ["https://www.googleapis.com/auth/youtube.readonly"]
        self.youtube = self.create_client(port=8080)

        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    def create_client(self, port):
        """Create YouTube API client; cache credential to avoid constant relog."""
        credentials = None

        # If there is credentials file, use it and avoid relog
        if os.path.exists(self.__credentials_file):
            print("Using existing credentials...")
            with open(self.__credentials_file, "rb") as token:
                credentials = pickle.load(token)

        # If there are no credentials, create them using browser authorization
        if not credentials:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                self.__client_secrets_file, self.__scopes
            )
            credentials = flow.run_local_server(port=port)

            # Save binary file for later user
            with open(self.__credentials_file, "wb") as token:
                print("Creating credentials binary...")
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
        self, channel_ids: list[str], max_results: int = 50, duration: str = "medium"
    ) -> list[list[str]]:
        """Get cleaned videos data for each channel ids: [title, description, video url]"""
        responses = []
        for channel_id in channel_ids:
            request = self.youtube.search().list(
                part="snippet",
                channelId=channel_id,
                maxResults=max_results,  # API default is 5
                order="date",
                type="video",  # other options: channel and playlist
                videoDuration=duration,  # short: 4min-, medium: 4-20min, long: 20min+
            )
            responses.append(request.execute())

        cleaned_videos: list[list[str]] = []
        for response in responses:
            for item in response["items"]:
                cleaned_videos.append(
                    [
                        item["snippet"]["title"],
                        item["snippet"]["description"],
                        f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                    ]
                )
        return cleaned_videos
