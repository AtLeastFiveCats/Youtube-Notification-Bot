from YT_API_calls import YouTubeAPICallsClient


def main():
    client = YouTubeAPICallsClient()
    subs = client.get_subscriptions_info()
    print(subs)


if __name__ == "__main__":
    main()
