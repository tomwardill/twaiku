import sys

from pyhaiku import haiku_checker
import tweepy


def get_users_timeline(username_to_check, auth = None, username = None, password = None):

    if auth == None and username == None:
        return None
    elif auth == None and username and password:
        auth = tweepy.BasicAuthHandler(username, password)

    api = tweepy.API(auth)
    status = api.user_timeline(username_to_check)
    return [s.text for s in status]

def check_for_haiku(status):
    haiku = []
    for s in status:
        haiku.append(haiku_checker.find_haiku(s))
    return haiku

if __name__ == '__main__':
    if len(sys.argv) == 3:
        status = get_users_timeline('tomwardill', username = sys.argv[1], password = sys.argv[2])
        haiku = check_for_haiku(status)
        print haiku
    else:
        print "Argument error"
