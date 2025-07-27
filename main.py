import webbrowser
import time
from YT_API_calls import YouTubeAPICallsClient

# Bolding prints to improve visibility
BOLD = "\033[1m"
RESET = "\033[0m"


def print_results(list_to_print: list) -> None:
    """Function to print the fetched results for user in readable format."""
    for i, item in enumerate(list_to_print):
        print(f"\n{BOLD}{i + 1}. {item[0]}{RESET}: {item[1]}")


def choose_channel(subscriptions: list) -> str | int:
    print_results(subscriptions)
    decision = input(
        "Which channel would you like to see videos of? Please provide a number: "
    )
    if decision == "q":
        return "q"
    print(f"Displaying {subscriptions[int(decision) - 1][0]}'s Videos")
    return int(decision)


def choose_video(videos: list) -> str | None:
    print_results(videos)
    decision = input("Choose video to watch by providing a number (q to quit): ")
    if decision == "q":
        return decision

    video_to_watch: str = videos[int(decision) - 1][2]
    webbrowser.open(video_to_watch)
    # Add 0.5 s delay so the info about opening browser is printed in proper line
    time.sleep(0.5)


def main():
    # Start YT client, fetch subscriptions and videos
    client = YouTubeAPICallsClient()
    subscriptions = client.get_subscriptions_info()
    videos = [client.get_videos_for_channel_id(sub[2]) for sub in subscriptions]

    # Puts main logic in a while loop for easy traversal
    while True:
        # Show logged user's subscriptions and ask which channel they wanna go to
        current_channel = choose_channel(subscriptions)
        if current_channel == "q":
            break

        current_video = choose_video(videos[current_channel - 1])
        if current_video == "q":
            break


if __name__ == "__main__":
    main()
