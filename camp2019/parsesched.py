#!/usr/bin/env python3
import json
import time
import sys

NUM_HOURS=1

def load_file():
    f = open("everything.schedule.json", "r")
    j = json.loads(f.read())
    conf = j["schedule"]["conference"]["days"]

    return conf

def get_day(conf, day):
    for confday in conf:
        if confday["index"] == day:
            return confday

def event_on_nowish(event, hour):
    eventtime = event["start"]
    eventhour = int(eventtime[:2])
    return (eventhour >= hour) and (eventhour <= hour + NUM_HOURS + 1)


def on_nowish():
    eventson = []
    conf = load_file()
    day = int(time.strftime("%d"))-20
    hour = int(time.strftime("%H"))
    confday = get_day(conf, day)
    for room, events in confday["rooms"].items():
        for event in events:
            if event_on_nowish(event, hour):
               eventson.append((
                    event["start"],
                    event["title"],
                    room))

    return sorted(eventson, key = lambda e : e[0])

def main():
    try:
        NUM_HOURS = int(sys.argv[1])
    except:
        pass
    eventson = on_nowish()
    print("Events on nowish:")
    for event in eventson:
        print("%s: %s (in %s)" % event)

if __name__ == "__main__": main()
