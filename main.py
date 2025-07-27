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


def make_a_decision(input_list: list) -> str | int:
    """Function for making a decision with proper error handling."""
    print_results(input_list)
    decision = input(
        "Make a selection from above choices by providing a number; user letters for program navigation: "
    ).lower()
    return decision


def hello_world() -> None:
    """Function to welcome user and let them know about basic functionality."""
    choices: dict[str, str] = {
        "q": "quitting the program.",
        "quit": "quitting the program.",
        "n": "showing next results.",
        "p": "showing next results.",
    }
    print("Welcome to the debloated, pro-attention span YT video chooser.")
    for key, value in choices.items():
        print(f"Please use {key} for {value}")


def main():
    hello_world()

    # Start YT client, fetch subscriptions and videos
    client = YouTubeAPICallsClient()
    subscriptions = client.get_subscriptions_info()
    videos = [client.get_videos_for_channel_id(sub[2]) for sub in subscriptions]

    # Puts main logic in a while loop for easy traversal
    while True:
        # Show logged user's subscriptions and ask which channel they wanna go to
        current_channel = make_a_decision(subscriptions)
        if current_channel in ["q", "quit"]:
            break

        # We already know that channel has been properly chosen so adjust the indexing diff a give info to confirm choice
        current_channel = int(current_channel) - 1
        print(f"Displaying {subscriptions[current_channel][0]}'s Videos")

        # Make user choose videos from given channel, show only 10 newest
        current_videos = videos[current_channel][:10]
        current_video = make_a_decision(current_videos)
        if current_video in ["q", "quit"]:
            break

        # Again, we already know that videos choice has been made so just show it to user
        video_to_watch: str = current_videos[int(current_video) - 1][2]
        webbrowser.open(video_to_watch)
        # Add 0.5 s delay so the info about opening browser is printed in proper line
        time.sleep(0.5)


if __name__ == "__main__":
    main()
