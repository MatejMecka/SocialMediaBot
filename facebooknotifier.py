from fbchat import log, Client
from slackclient import SlackClient
import json
from config import *

sc = SlackClient(SlackToken)

class Notifier(Client):
    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
    
        log.info("Message from {} in {} ({}): {}".format(author_id, thread_id, thread_type.name, message))
        author = client.fetchUserInfo(author_id)[author_id]
        user = author.name
        msg = message
        jsondata =  [
            {
                "fallback": "Facebook.",
                "color": "#536dfe",
                "pretext": "You've got a new message!",
                "author_name": "Facebook",
                "author_link": "http://facebook.com",
                "author_icon": "URLHere",
                "title": "New Facebook Message!",
                "text": "This is all information I know about:",
                "fields": [
                    {
                        "title": "Author: ",
                        "value": str(user),
                        "short": "true"
                    },
                    {
                        "title": "Message",
                        "value": str(msg),
                        "short": "false"
                    }
                ],

                "footer": "Facebook",
                "footer_icon": ""

            }
        ]
        if author_id != self.uid:
             sc.api_call("chat.postMessage", channel=UserID, text=" ", as_user="True", attachments=json.dumps(jsondata)) 

client = Notifier(FacebookUsername, FacebookPassword)
client.listen()
