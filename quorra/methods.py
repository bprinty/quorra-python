# -*- coding: utf-8 -*-
#
# Methods for interacting with quorra plots.
# 
# @author <bprinty@gmail.com>
# ------------------------------------------------


# imports
# -------
import os
import uuid


# config
# ------
_phantom = None
_app = None


# methods
# -------
def export(plot, filename):
    """
    Export plot to file.

    Args:
        plot (quorra.Plot): Quorra plot object to export.
        filename (str): Filename to export to.
    """
    global _phantom
    if _phantom is None:
        from selenium.webdriver import PhantomJS
        _phantom = PhantomJS();
    cwd = os.path.dirname(os.path.realpath(__file__))
    tmpl = os.path.join(cwd, 'tmpl', 'export.html')
    exp = '/tmp/' + str(uuid.uuid1()) + '.html'
    with open(tmpl, 'r') as fi, open(exp, 'w') as fo:
        fo.write(fi.read().replace('var plot = undefined;', 'var plot = {};'.format(str(plot))))
    _phantom.get('file://' + exp)
    _phantom.save_screenshot(filename.replace('.png', '') + '.png')
    # os.remove(exp)
    return


def render(plot, append=False, port=5000):
    """
    Update current view with new plot.

    Args:
        plot (quorra.Plot): Quorra plot object to render.
        append (bool): Whether or not to append the plot
            to the current view.
        port (int): The application to send the plot to.
    """
    if _app is None:
        from .app.app import create_app
        from .app.settings import DevConfig
        _app = create_app(DevConfig)
        # run in separate process
        # _app.run()
    return
