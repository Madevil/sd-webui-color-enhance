import gradio

import modules.scripts as scripts
import modules.infotext_utils as infotext_utils

import mmaker_color_enhance_core as core

class Script(scripts.Script):
    def __init__(self):
        super().__init__()

    def title(self):
        return "Color Enhance"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gradio.Row(elem_id = "_gr_row_color_enhance"):
            slider_strength = gradio.Slider(label = "Color Enhance strength", minimum = 0, maximum = 1, step = 0.01, value = 0)
            self.infotext_fields = [ infotext_utils.PasteField(slider_strength, "Color Enhance", api = "color_enhance") ]
        return [slider_strength]

    def postprocess_image_after_composite(self, p, pp: scripts.PostprocessImageArgs, *args):
        strength = args[0]
        if strength == 0:
            return

        pp.image = core.color_enhance(pp.image, strength)
        p.extra_generation_params["Color Enhance"] = strength
