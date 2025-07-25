import os
from dotenv import load_dotenv

# The Google APIs Client Libraries for Python
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Loading YT key and setting static variables
load_dotenv()
YT_API_KEY: str = os.getenv("YOUTUBE_API_KEY", "")
CLIENT_SECRETS_FILE: str = "YT.json"
API_SERVICE_NAME: str = "youtube"
API_VERSION: str = "v3"
SCOPES: list[str] = ["https://www.googleapis.com/auth/youtube.readonly"]

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRETS_FILE, SCOPES
)
credentials = flow.run_local_server(port=8080)
youtube = googleapiclient.discovery.build(
    API_SERVICE_NAME, API_VERSION, credentials=credentials
)

# Get subscriptions list JSON response file
request = youtube.subscriptions().list(part="snippet,contentDetails", mine=True)
response = request.execute()

# Prepare cleaned subs info: title / description / channel ID
subscriptons = response.get("items", [])
cleaned_subscriptions: list = []
print(f"Found {len(subscriptons)} subscriptions")
for sub in subscriptons:
    sub_data = sub["snippet"]
    cleaned_subscriptions.append(
        [
            sub_data["title"],
            sub_data["description"],
            sub_data["resourceId"]["channelId"],
        ]
    )
print(cleaned_subscriptions)
