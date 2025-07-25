import os
from dotenv import load_dotenv

# loading YT key
load_dotenv()
YT_API_KEY: str = os.getenv("YOUTUBE_API_KEY")


def main():
    print(YT_API_KEY)
    print("Hello from youtube-notification-bot!")


if __name__ == "__main__":
    main()
