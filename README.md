# Reddit Auto Post Commenter
An Azure Function that comments all new posts in a specifc subreddit.

All of the core code is located in [__init__.py](./CommentRedditPost/__init__.py).

You will need to create a reddit app to use this bot.
All of the actions performed by this script will appear as if they were done by you.
You can create the reddit bot by following these steps:

1. Navigate to the Apps page
2. Click create an app
   - name: Set a name for your app
   - type: Script
   - description: Optional
   - about url: Optional
   - redirect uri: http://localhost:8080

Note the outputted client id and secret and add it your code's [local.settings.json](./CommentRedditPost/local.settings.json).

# Setup

1. Create an Azure function as mentioned [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=python).
2. Update the __init__.py code with the code from this repo's [__init__.py](./CommentRedditPost/__init__.py).
3. Add the required credentials to [local.settings.json](./CommentRedditPost/local.settings.json).
4. In VS code, press F5 to test the function locally.
5. Set the frequency you want your script to run in [function.json](./CommentRedditPost/function.json#:~:text=%22schedule%22%3A%20%220%20*%202%20*%20*%20*%22)
6. Deploy to azure as mentioned [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=python#publish-to-azure).

This repo was inspired from the following repo:
https://github.com/yashar1/reddit-comment-bot
