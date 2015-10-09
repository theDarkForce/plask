# __init__
# create at 2015/10/4
# autor: qianqians

import os
path = os.path.split(os.path.realpath(__file__))[0] + '\plask'
import sys
print path
sys.path.append(path)
import pysession
from pyaudio import pyaudio
from pyvideo import pyvideo
from pytext import pytext
from pytext import pydynamictext
from pyimg import pyimg
from pylink import pylink
from pybutton import pybutton
from pyedit import pyedit
from pycanvas import pycanvas
from pycontainer import pycontainer
from pyhtmlstyle import pyhtmlstyle
from pyelement import pyelement
from pyparagraph import pyparagraph
from pyfile import pyfile
from tools import *
from pypage import pypage
from pypopup import *
from pyborder import pyborder
from plaskapp import plaskapp
from pymsgbox import *