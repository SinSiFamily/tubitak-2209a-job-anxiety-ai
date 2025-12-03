import praw
import time
from using_pushhift import Data
import requests
data = Data(amount=10, start_time="2025-01-01", subreddit="ComputerEngineering")
all_ids, dicto = data.start_gathering()
reddit = praw.Reddit(
    client_id="o7sT31PL8hYRCKi-CsSTJw",
    client_secret="7ZFjTd6Zl2e999q-FoUB53qDZ1i4FA",
    user_agent="mybot by u/YOUR_REDDIT_USERNAME"
)
def to_base36(n):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        n, r = divmod(n, 36)
        result = chars[r] + result
    return result
for pid in all_ids:
    try:
        print(f"[+] Fetching post {pid}")
        post = reddit.submission(id=pid)
        post.comments.replace_more(limit=0)
        comments = [c.body for c in post.comments.list()]
        
        if post.title == "[deleted by user]":
            print("TITLE:", dicto[pid][1])
        else:
            print("TITLE:", post.title)
        if post.selftext == "[removed]":
            print("TEXT:", dicto[pid][0])
        else:
            print("TEXT:", post.selftext)
        print("Commments : ")
        for x in comments:
            print(x)
        print("COMMENTS:", len(comments))
        print("---")
        time.sleep(1)
    except Exception as e:
        print("[-] Error for", pid, ":", e)