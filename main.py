"""
BIRDY bot by ser-gent
"""
import tweepy, requests
from datetime import date, timedelta
from keys import *

TAG = "[BIRDY]"


def convert_date(date):
    return date.strftime("%Y%m%d")


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
print(TAG + " : Twitter API connected OK")

today = date.today()
yesterday = today - timedelta(1)

data_json = requests.get(
    'https://api.sncf.com/v1/coverage/sncf/disruptions//?since=' + convert_date(
        yesterday) + 'T000000&until=' + convert_date(today) + 'T000000&',
    auth=(SNCF_TOKEN, '')).json()
print(TAG + " : Get disruptions from " + yesterday.strftime("%m/%d/%Y"))


