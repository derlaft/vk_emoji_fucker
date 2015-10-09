# -*- coding: utf-8 -*-

import vk
import re
import time

ACCESS_TOKEN = "put_token_here"

FUCK_LIST = [
        "\u2764",
        "\u263A",
        "\u261D",
        "\u270C",
        "\u270B",
        "\u2744",
        "\u26BD",
        "\u26C5",
        "\U0001F60A",
        "\U0001F603",
        "\U0001F609",
        "\U0001F606",
        "\U0001F61C",
        "\U0001F60B",
        "\U0001F60D",
        "\U0001F60E",
        "\U0001F612",
        "\U0001F60F",
        "\U0001F614",
        "\U0001F622",
        "\U0001F62D",
        "\U0001F629",
        "\U0001F628",
        "\U0001F610",
        "\U0001F60C",
        "\U0001F604",
        "\U0001F607",
        "\U0001F630",
        "\U0001F632",
        "\U0001F633",
        "\U0001F637",
        "\U0001F602",
        "\U0001F61A",
        "\U0001F615",
        "\U0001F62F",
        "\U0001F626",
        "\U0001F635",
        "\U0001F620",
        "\U0001F621",
        "\U0001F61D",
        "\U0001F634",
        "\U0001F618",
        "\U0001F61F",
        "\U0001F62C",
        "\U0001F636",
        "\U0001F62A",
        "\U0001F62B",
        "\U0001F600",
        "\U0001F625",
        "\U0001F61B",
        "\U0001F616",
        "\U0001F624",
        "\U0001F623",
        "\U0001F627",
        "\U0001F611",
        "\U0001F605",
        "\U0001F62E",
        "\U0001F61E",
        "\U0001F619",
        "\U0001F613",
        "\U0001F601",
        "\U0001F631",
        "\U0001F608",
        "\U0001F47F",
        "\U0001F47D",
        "\U0001F44D",
        "\U0001F44E",
        "\U0001F44C",
        "\U0001F44F",
        "\U0001F44A",
        "\U0001F64F",
        "\U0001F443",
        "\U0001F446",
        "\U0001F447",
        "\U0001F448",
        "\U0001F4AA",
        "\U0001F442",
        "\U0001F48B",
        "\U0001F4A9",
        "\U0001F34A",
        "\U0001F377",
        "\U0001F378",
        "\U0001F385",
        "\U0001F4A6",
        "\U0001F47A",
        "\U0001F428",
        "\U0001F51E",
        "\U0001F479",
        "\U0001F31F",
        "\U0001F34C",
        "\U0001F37A",
        "\U0001F37B",
        "\U0001F339",
        "\U0001F345",
        "\U0001F352",
        "\U0001F381",
        "\U0001F382",
        "\U0001F384",
        "\U0001F3C1",
        "\U0001F3C6",
        "\U0001F40E",
]

WALL_ID = -104215438

last_fucked = dict()

session = vk.Session(ACCESS_TOKEN)
api = vk.API(session, 10)

posts = [i["id"] for i in api.wall.get(owner_id=WALL_ID, count=20)[1:]]


def fuck(a):
    time.sleep(0.1)
    return api.wall.deleteComment(owner_id=WALL_ID, comment_id=a)

for post in posts:
    repeat = True
    while repeat:
        repeat = False
        comments = [ (i["id"], i["text"]) for i in api.wall.getComments(owner_id=WALL_ID, post_id=post, v="5.37", start_comment_id=last_fucked.get(post, 0))["items"] ]
        to_fuck = [c[0] for c in comments if any(s in l for l in c[1] for s in FUCK_LIST)]
        deleted = [fuck(i) for i in to_fuck]
        repeat = any(deleted)
        print(repeat)
        if (len(comments) > 0):
            last_fucked[post] = comments[-1][0]
        time.sleep(1)
