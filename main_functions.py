import webbrowser
import time
from YT_API_calls import YouTubeAPICallsClient

def choose_video(vids, decision = None):
    decision = input("Choose video to watch by providing a number (q to quit or r to return to subscriptions): ")
    if decision == "q":
        return str(decision)
    elif decision == "r":
        return str(decision)
    
    video_to_watch: str = vids[int(decision) - 1][2]
    webbrowser.open(video_to_watch)
    # Add 0.5 s delay so the info about opening browser is printed in proper line
    time.sleep(0.5)
    return choose_video(vids, int(decision))

