import typing
import modules.script_callbacks as script_callbacks

def on_infotext_pasted(infotext: str, result: dict[str, typing.Any]):
    if "Color Enhance" in result.keys():
        return

    result["Color Enhance"] = 0

script_callbacks.on_infotext_pasted(on_infotext_pasted)
