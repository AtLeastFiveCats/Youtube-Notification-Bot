from YT_API_calls import YouTubeAPICallsClient


def main():
    client = YouTubeAPICallsClient()
    subs = client.get_subscriptions_info()
    print(subs)
    vids = client.get_videos_for_channel_ids([sub[2] for sub in subs])
    print(vids)


if __name__ == "__main__":
    main()
