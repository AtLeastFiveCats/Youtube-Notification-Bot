from YT_API_calls import YouTubeAPICallsClient


def main():
    client = YouTubeAPICallsClient()
    subs = client.get_subscriptions_info()
    # print(subs)
    # vids = client.get_videos_for_channel_ids([sub[2] for sub in subs])
    vids = client.get_videos_for_channel_ids([subs[0][2]])
    BOLD = "\033[1m"
    RESET = "\033[0m"
    for i, vid in enumerate(vids):
        print(f"\n{BOLD}{i + 1}. {vid[0]}{RESET}: {vid[1]}")


if __name__ == "__main__":
    main()
