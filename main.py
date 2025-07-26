import webbrowser
import time
from YT_API_calls import YouTubeAPICallsClient

# Bolding prints to improve visibility
BOLD = "\033[1m"
RESET = "\033[0m"


def main():
    # Start YT client, grab subs and vids
    client = YouTubeAPICallsClient()
    subs = client.get_subscriptions_info()
    # print(subs)
    # vids = client.get_videos_for_channel_ids([sub[2] for sub in subs])
    decision = input("Which channel would you like to see videos of? Please provide a number: ") 
    vids = client.get_videos_for_channel_ids([subs[int(decision) - 1][2]])
    # Print vids nicely for user to choose
    for i, vid in enumerate(vids):
        print(f"\n{BOLD}{i + 1}. {vid[0]}{RESET}: {vid[1]}")
    # Loop for user to keep opening videos they want
    while True:
        decision = input("Choose video to watch by providing a number (q to quit): ")
        if decision == "q":
            break
        video_to_watch: str = vids[int(decision) - 1][2]
        webbrowser.open(video_to_watch)
        # Add 0.5 s delay so the info about opening browser is printed in proper line
        time.sleep(0.5)


if __name__ == "__main__":
    main()
