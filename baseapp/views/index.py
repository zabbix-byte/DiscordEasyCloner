import json
import asyncio
import threading


from pypulse.View import view
from pypulse.Template import RenderTemplate
from pypulse import Aplication
from baseapp.cloner.service import main


@view(name="index", path_trigger="/")
def index(request):
    config = open(f"{Aplication.Vars.APLICATION_PATH}\\baseapp\\cloner\\data.json", "r")
    data = json.loads(config.read())

    error = ""
    token_val = data["token"]
    target_value = data["target"]
    destination_value = data["destination"]

    if request.get("method") == "POST":

        data["token"] = request["body"].get("token").strip()
        token_val = data["token"]
        data["target"] = request["body"].get("target").strip()
        target_value = data["target"]
        data["destination"] = request["body"].get("destination").strip()
        destination_value = data["destination"]
        data["route"] = f"{Aplication.Vars.APLICATION_PATH}\\static\\info.log"

        open(
            f"{Aplication.Vars.APLICATION_PATH}\\baseapp\\cloner\\data.json", "w"
        ).write(json.dumps(data))

        try:
            #asyncio.run(main())
            t1 = threading.Thread(target=asyncio.run, args=(main(), ))
            t1.start()
        except Exception as e:
            error = str(e)

    if "token" in error:
        token_error = True
    else:
        token_error = False

    return RenderTemplate(
        "index.html",
        {
            "token_error": token_error,
            "token_val": token_val,
            "target_value": target_value,
            "destination_value": destination_value,
        },
    )
