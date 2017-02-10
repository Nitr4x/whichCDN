import imp
import os

PluginFolder = "./plugins"
MainModule = "__init__"

def getPlugins():
    """List the plugins located in the plugins folder."""

    plugins = []
    pluginList = os.listdir(PluginFolder)
    for pluginName in pluginList:
        location = os.path.join(PluginFolder, pluginName)
        if not os.path.isdir(location) or not MainModule + ".py" in os.listdir(location):
            continue
        info = imp.find_module(MainModule, [location])
        plugins.append({"name": pluginName, "info": info})
    return plugins

def loadPlugin(plugin):
    """Loads the specified plugin.

    Parameters
    ----------
    plugin : Plugin
        Plugin to load

    Return
    ------
    The plugin loaded
    """

    return imp.load_module(MainModule, *plugin["info"])
