This project is designed to be able to retrieve YouTube information and interact with it through the terminal. The currently this Youtube terminal app is to be able to display your subscriptions and watch videos from said subscriptions. It requires Youtube Data API v3 which this README will go over how to enable later. The later goals of this app is to make the CLI interface smoother, give an option to watch in browser or in CLI, let the user choose what length videos they would like returned, and more features listed at the bottom of this README.

**Dependencies**

This project requires uv to run, its a wonderful package manager and virtual enviroment tool and more packed into one. It can be installed by a simple curl command or Powershell command on Windows

For Linux and MacOS

```curl -LsSf https://astral.sh/uv/install.sh | sh```
 
For Windows

```powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"```

**Enabling API Access**

The next piece of overhead for this is to enable access to Google's API, this is about a 5 minute process

1. Navigate to https://console.cloud.google.com

2. In the navigation pane on the lefthand side accessed by the three lines in the top left of the page, navigate to APIs & Services -> Credentials

3. Select 'Create New Project', it does not matter what you name it

4. Select 'Create credentials' a the top of the screen and select 'OAuth client ID'

5. Now we need to configure the consent screen, select the 'configure consent screen' at the right of the page. From here we can select 'Get Started' in the middle of the screen

6. We need to give a name to our app, 'YT Notifier' will work. Add your email as the support email below that and hit next, we will select 'External' for our audience, after hitting next we can enter our email address as the contact information for Google. Lastly we accept the user data policy and hit create

7. Navigate back to the APIs & Services -> Credentials and select 'Create credentials' -> 'OAuth client ID', choose 'Desktop app' for the Application Type and hit create, **don't close this page we will come back to it**

8. At the bottom of the OAuth client created box that pops up select 'Download JSON' and save it in the root of this project's directory, **make sure to rename it to YT.json**

9. If we attempt to authorize our script to make api calls we will get hit with an access denied. navigate back to the google cloud console, select the navigation pane and navigate to 'APIs & Services' -> 'OAuth consent screen'. That will take us to an overview of the app. from there navigate to the left and select 'Audience' -> '+ Add users' enter your email and save

10. Lastly if 'Youtube Data API v3' has not been used on your developer account it will need to be enabled Navigate back to the left navigation panel -> 'APIs & Services' -> 'Library' -> Scroll to 'Youtube' -> 'YouTube Data API v3' -> 'Enable'

**Potental Issues:**

If this error pops up
```
  File "/home/gaming/Boot.dev/github.com/Atleastfivecats/main.py", line 9, in main
    vids = client.get_videos_for_channel_ids([subs[0][2]])
                                              ~~~~^^^
IndexError: list index out of range
```

Then the account you authorized to use with the bot has no subscriptions

**Fix:**

Either add some subscriptions or delete the YT.pickle file and rerun the script to authorize a different account

------------------------------------------------------------------------------------------------------------

If the displayed videos are not the most recent videos uploaded from the channel then it is likely the newest videos are either too long or too short to be considered midform content and will not be displayed by the program. This is an issues we intend to fix down the line.

**TODO**

- Show more than 10 videos per channel
- Add the ability to page between videos
- Refactor UI to be cleaner
- Add more safety checks for improper input
- Add the option to display a different YouTube channel's videos
- Add the ability to see shortform (-4 min), midform (4 - 40 min), or longform content (40+ min)
- Potentially add a way to be notified of a new upload from a subscription

