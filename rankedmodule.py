from riotwatcher import LolWatcher, ApiError
import discord
import os
api_key = ''
watcher = LolWatcher(api_key)
my_region = 'eun1'
print("summoner name")
me = watcher.summoner.by_name(my_region, input())
ranked = watcher.league.by_summoner(my_region, me['id'])
if (ranked[1]['tier']) == "IRON" or (ranked[1]['tier']) == "BRONZE" or (ranked[1]['tier']) == "SILVER":
    print("you are low ELO trash")
    print("your rank is "+ranked[1]['tier'])
else:
    print("you are not low elo trash")
    print("your rank is " + ranked[1]['tier'])
if ranked[1]['veteran']:
    print("you're hardstuck")
else:
    print("you're not hardstuck")
