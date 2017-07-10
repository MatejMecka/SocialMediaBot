import praw
from praw.models import Comment
from slackclient import SlackClient
import json
import time
from config import *

sc = SlackClient(SlackToken)

checked = [""]

print("Booting up...")


def main():
    print("Searching for messages...")
    reddit = praw.Reddit(user_agent='RedditNotifierForSlack by /u/MatejMecka',client_id=RedditClientID,client_secret=RedditClientSecret,username=RedditUsername,password=RedditPassword)
    for item in reddit.inbox.unread(limit=None):
        if item in checked:
            pass
        else:
            print("Message from: " + str(item.author) + " with subject: " + str(item.subject) + " Here it is: " + str(item.body))
            jsondata = [{"author_link": "https://reddit.com", "color": "#448aff", "text": "This is what I know about it.", "author_name": "Reddit", "footer_icon": "ImageURL", "pretext": "You've got a new Message!", "footer": "Reddit API", "fields": [{"short": "true", "value": str(item.author), "title": "Author:"}, {"short": "true", "value": str(item.subject), "title": "Subject: "}, {"short": "false", "value": str(item.body), "title": "Message:"}], "title": "Reddit Message", "title_link": "https://reddit.com/message/inbox", "fallback": "Reddit Message", "author_icon": "ImageURL"}]

            sc.api_call("chat.postMessage", channel=UserID, text=" ", as_user="True", attachments=json.dumps(jsondata))
            checked.append(item)

while True:
    main()
    time.sleep(5)
