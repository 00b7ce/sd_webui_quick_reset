import os
import gradio as gr
from modules import script_callbacks
from modules import shared, scripts
import modules.scripts as scripts


script_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
flavors = ['Restart']
def on_ui_settings():
    section = ('manko', 'OMANKO')
    shared.opts.add_option("quick_restart", 
                            shared.OptionInfo(
                                default=[], 
                                label="Restart",  
                                component=gr.CheckboxGroup, 
                                component_args={"choices": flavors}, 
                                refresh=on_ui_settings_change, 
                                section=section))

def on_ui_settings_change():
    shared.state.interrupt()
    shared.state.need_restart = True

script_callbacks.on_ui_settings(on_ui_settings)