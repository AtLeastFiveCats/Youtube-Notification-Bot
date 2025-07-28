import sys
import webbrowser
import time
import os
from YT_API_calls import YouTubeAPICallsClient


# Bolding and underline prints to improve visibility
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

# Letters used for program navigation; vim power
CHOICES: dict[str, str] = {
    "q": "quitting the program",
    "n": "showing next results",
    "p": "showing next results",
    "m": "change videos duration to 4 to 20 min",
    "l": "change videos duration to above 20 min",
}


def hello_world() -> None:
    """Function to welcome user and let them know about basic functionality."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        f"{BOLD}{UNDERLINE}Welcome to the debloated, pro-attention span YT video chooser.{RESET}"
    )
    for key, value in CHOICES.items():
        print(f"Please use {key} for {value}.")


def print_results(list_to_print: list) -> None:
    """Function to print the fetched results for user in readable format."""
    for i, item in enumerate(list_to_print):
        print(f"{BOLD}{i + 1}. {item[0]}{RESET}: {item[1]}")


def make_a_decision(input_list: list, page: int = 0) -> str | int:
    """Function for making a decision with proper error handling."""
    current_page = (
        input_list[page * 10 : 10 + page * 10] if len(input_list) > 10 else input_list
    )
    while True:
        print_results(current_page)
        decision = input(
            "\nMake a selection from above choices by providing a number; use letters for program navigation: "
        ).lower()

        # Navigation, add strip to remove leading and trailing whitespaces
        if decision in CHOICES:
            return char_decision(decision.strip(), input_list, page)

        # Acutal choice made; adjust indexing right away and add current page
        if decision.isdigit() and 0 < int(decision) <= len(current_page):
            return page * 10 + int(decision) - 1

        print("Invalid selection. Try again.\n")


def char_decision(char: str, input_list: list, page: int) -> str | int:
    match char:
        case "q":
            sys.exit(0)
        case "n":
            if page == 4:
                print(
                    f"{BOLD}{UNDERLINE}There is max {page + 1} pages. Cannot go further.{RESET}"
                )
                return make_a_decision(input_list, page)
            page += 1
            return make_a_decision(input_list, page)
        case "p":
            if page == 0:
                print(
                    f"{BOLD}{UNDERLINE}Don't try to go below 0, that's simply rude.{RESET}"
                )
                return make_a_decision(input_list, page)
            page -= 1
            return make_a_decision(input_list, page)
        case "m":
            pass
        case "l":
            pass


def choose_video(video_list) -> None:
    # Make user choose videos from given channel, show only 10 newest
    current_videos = video_list
    current_video = make_a_decision(current_videos)

    # Again, we already know that videos choice has been made so just show it to user
    video_to_watch: str = current_videos[current_video][2]
    webbrowser.open(video_to_watch)
    # Add 0.5 s delay so the info about opening browser is printed in proper line
    time.sleep(0.5)


def main():
    hello_world()

    # Start YT client, fetch subscriptions and videos
    client = YouTubeAPICallsClient()
    subscriptions = client.get_subscriptions_info()
    if not subscriptions:
        raise Exception("The logged account has no subscriptions, too much grass boi.")
    videos = [client.get_videos_for_channel_id(sub[2]) for sub in subscriptions]

    # Puts main logic in a while loop for easy traversal
    while True:
        # Calling hello world again clears the terminal and displays options again
        hello_world()
        # Show logged user's subscriptions and ask which channel they wanna go to
        print(f"\n{BOLD}{UNDERLINE}Displaying current user's subscriptions:{RESET}")
        current_channel = make_a_decision(subscriptions)
        print(
            f"\n{BOLD}{UNDERLINE}Displaying {subscriptions[current_channel][0]}'s Videos:{RESET}"
        )
        choose_video(videos[current_channel])


if __name__ == "__main__":
    main()
