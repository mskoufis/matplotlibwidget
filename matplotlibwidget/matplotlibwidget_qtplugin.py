from pydm.widgets.qtplugin_base import qtplugin_factory, WidgetCategory
from pydm.widgets.qtplugin_extensions import RulesExtension
from qtpy.QtGui import QIcon, QPixmap
from os import path
from matplotlibwidget import MatplotlibWidget


# PyDM Matplotlib Widget plugin
print("Loading MatplotlibWidgetPlugin!")
dirname = path.dirname(__file__)
icon_file = path.join(dirname, 'images/Matplotlib_icon.png')
MatplotlibWidgetPlugin = qtplugin_factory(MatplotlibWidget, 
                                       group=WidgetCategory.PLOT, 
                                       is_container=False, 
                                       extensions=[RulesExtension],
                                       icon=QIcon(QPixmap(icon_file)))
