import re


def process_intent(body):
    nb_phrases = ["nb", "north", "n", "work"]
    sb_phrases = ["sb", "south", "s", "home"]

    if body is None:
        return "error"

    body = re.sub(r'\W+', ' ', body)
    body = body.lower().split()

    if len(body) == 1:
        if body[0] in nb_phrases:
            return "n"
        elif body[0] in sb_phrases:
            return "s"

    for word in body:
        for nb, sb in zip(nb_phrases, sb_phrases):
            if word == nb:
                return "n"
            elif word == sb:
                return "s"

    return "error"


def build_message(intent, time_saved, toll):
    if intent == "n":
        destination = "to work"
    elif intent == "s":
        destination = "back home"

    if(time_saved < 0):
        msg = "Because this toll road very poorly designed, taking MoPac will cost you " + \
            toll + " dollars and " + (str(abs(time_saved))) + " minutes of your life."
    elif(time_saved == 0):
        msg = "Don't take the toll, it won't save you any time and will cost you " + \
            toll + "."
    elif(time_saved == 1):
        msg = "Toll rate to get " + destination + " is " + toll + \
            " and will save you " + str(time_saved) + " minute."
    else:
        msg = "Toll rate to get " + destination + " is " + toll + \
            " and will save you " + str(time_saved) + " minutes."

    return msg
