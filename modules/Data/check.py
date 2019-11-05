import json
import os


def CheckPermission(message):
    if os.path.exists("modules/Data/%s.json" % message.chat.id):
        f = open("modules/Data/%s.json" % message.chat.id, "r")
        data = json.load(f)
        f.close()
        if data["Permission"] == "User":
            return "User"
        elif data["Permission"] == "Admin":
            return "Admin"
    else:
        return False
