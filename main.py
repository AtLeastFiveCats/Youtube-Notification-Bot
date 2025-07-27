import webbrowser
import time
from YT_API_calls import YouTubeAPICallsClient
from main_functions import choose_video

# Bolding prints to improve visibility
BOLD = "\033[1m"
RESET = "\033[0m"


def main():
    # Start YT client
    client = YouTubeAPICallsClient()
    # Puts main logic in a while loop for easy traversal
    while True:

    # Get logged user's subscriptions and ask which channel they wanna go to
        subs = client.get_subscriptions_info()
        decision = (
        
                input(
                "Which channel would you like to see videos of? Please provide a number (q to quit): "
            )
                )
        if decision == "q":
            break
        print(f"Displaying {subs[int(decision) - 1][0]}'s Videos")
        vids = client.get_videos_for_channel_ids([subs[int(decision) - 1][2]])

        # Recursively call choose video until the user decides they want to q or r to subs
        decision = choose_video(vids)
        if type(decision) == int:
            choose_video(vids)
        elif str(decision) == "q":
            break
        # We could add a condition here for r, but the loop with repeat if r is returned anyway?

if __name__ == "__main__":
    main()
