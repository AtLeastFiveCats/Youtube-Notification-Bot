import webbrowser
import time
from YT_API_calls import YouTubeAPICallsClient

# Bolding prints to improve visibility
BOLD = "\033[1m"
RESET = "\033[0m"


def print_results(list_to_print: list) -> None:
    for i, item in enumerate(list_to_print):
        print(f"\n{BOLD}{i + 1}. {item[0]}{RESET}: {item[1]}")


def choose_video(vids) -> str | None:
    decision = input("Choose video to watch by providing a number (q to quit): ")
    if decision == "q":
        return decision

    video_to_watch: str = vids[int(decision) - 1][2]
    webbrowser.open(video_to_watch)
    # Add 0.5 s delay so the info about opening browser is printed in proper line
    time.sleep(0.5)


def main():
    # Start YT client
    client = YouTubeAPICallsClient()
    # Puts main logic in a while loop for easy traversal
    while True:
        # Get logged user's subscriptions and ask which channel they wanna go to
        subs = client.get_subscriptions_info()
        print_results(subs)
        decision = input(
            "Which channel would you like to see videos of? Please provide a number: "
        )
        if decision == "q":
            break

        print(f"Displaying {subs[int(decision) - 1][0]}'s Videos")
        vids = client.get_videos_for_channel_ids([subs[int(decision) - 1][2]])
        print_results(vids)
        choose_video(vids)
        if decision == "q":
            break


if __name__ == "__main__":
    main()
