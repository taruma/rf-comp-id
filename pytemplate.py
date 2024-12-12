"""
PLOTLY TEMPLATE BASED ON THEME
version: v1.2.0 (modified from taruma/anfrek)
"""

from plotly import colors
from dash_bootstrap_templates import load_figure_template
import plotly.io as pio

load_figure_template("journal")
mytemplate = pio.templates[pio.templates.default]

# VARS
_FONT_FAMILY = mytemplate.layout.font.family
FONT_COLOR_TUPLE = colors.hex_to_rgb(mytemplate.layout.font.color)
_red, _green, _blue = FONT_COLOR_TUPLE
FONT_COLOR_RGB_ALPHA = f"rgba({_red},{_green},{_blue},0.2)"

# GENERAL

mytemplate.layout.hovermode = "x"
mytemplate.layout.margin.t = 0
mytemplate.layout.margin.b = 0
mytemplate.layout.margin.l = 0  
mytemplate.layout.margin.r = 0
mytemplate.layout.margin.pad = 0
mytemplate.layout.paper_bgcolor = mytemplate.layout.plot_bgcolor

# LEGEND
LEGEND_FONT_SIZE = 12
mytemplate.layout.showlegend = False
mytemplate.layout.legend.font.size = LEGEND_FONT_SIZE
mytemplate.layout.legend.font.family = _FONT_FAMILY
mytemplate.layout.legend.bgcolor = 'rgba(255,255,255,0.6)'
mytemplate.layout.legend.groupclick = "toggleitem"


# MODEBAR
mytemplate.layout.modebar.activecolor = "blue"
mytemplate.layout.modebar.add = (
    "hoverclosest hovercompare v1hovermode togglehover drawrect eraseshape".split()
)
mytemplate.layout.modebar.bgcolor = "rgba(0,0,0,0)"
mytemplate.layout.modebar.color = "rgba(0,0,0,0.6)"

# NEWSHAPE
mytemplate.layout.newshape.line.color = "red"
mytemplate.layout.newshape.line.width = 3

# HOVERLABEL
mytemplate.layout.hoverlabel.font.family = _FONT_FAMILY

# TITLE
mytemplate.layout.title.pad = dict(b=10, l=0, r=0, t=0)
mytemplate.layout.title.x = 0
mytemplate.layout.title.xref = "paper"
mytemplate.layout.title.y = 1
mytemplate.layout.title.yref = "paper"
mytemplate.layout.title.yanchor = "bottom"
mytemplate.layout.title.font.size = 35

# XAXIS
_XAXIS_GRIDCOLOR = "black" # .layout.xaxis.gridcolor
_XAXIS_LINEWIDTH = 1
_XAXIS_TITLE_FONT_SIZE = 20
_XAXIS_TITLE_STANDOFF = 20
mytemplate.layout.xaxis.mirror = True
mytemplate.layout.xaxis.showline = True
mytemplate.layout.xaxis.linewidth = _XAXIS_LINEWIDTH
mytemplate.layout.xaxis.linecolor = _XAXIS_GRIDCOLOR
mytemplate.layout.xaxis.spikecolor = _XAXIS_GRIDCOLOR
mytemplate.layout.xaxis.gridcolor = FONT_COLOR_RGB_ALPHA
mytemplate.layout.xaxis.gridwidth = _XAXIS_LINEWIDTH
mytemplate.layout.xaxis.title.text = "<b>PLACEHOLDER XAXIS</b>"
mytemplate.layout.xaxis.title.font.size = _XAXIS_TITLE_FONT_SIZE
mytemplate.layout.xaxis.title.standoff = _XAXIS_TITLE_STANDOFF
mytemplate.layout.xaxis.spikethickness = 1
mytemplate.layout.xaxis.spikemode = "across"
mytemplate.layout.xaxis.spikedash = "solid"


# YAXIS
_YAXIS_GRIDCOLOR = "black"  # .layout.yaxis.gridcolor
_YAXIS_LINEWIDTH = 1
_YAXIS_TITLE_FONT_SIZE = 20
_YAXIS_TITLE_STANDOFF = 15
mytemplate.layout.yaxis.mirror = True
mytemplate.layout.yaxis.showline = True
mytemplate.layout.yaxis.linewidth = _YAXIS_LINEWIDTH
mytemplate.layout.yaxis.linecolor = _YAXIS_GRIDCOLOR
mytemplate.layout.yaxis.spikecolor = _YAXIS_GRIDCOLOR
mytemplate.layout.yaxis.rangemode = "tozero"
mytemplate.layout.yaxis.gridcolor = FONT_COLOR_RGB_ALPHA
mytemplate.layout.yaxis.gridwidth = _YAXIS_LINEWIDTH
mytemplate.layout.yaxis.title.text = "<b>PLACEHOLDER XAXIS</b>"
mytemplate.layout.yaxis.title.font.size = _YAXIS_TITLE_FONT_SIZE
mytemplate.layout.yaxis.title.standoff = _YAXIS_TITLE_STANDOFF

# SUBPLOTS
# ANNOTATION
mytemplate.layout.annotationdefaults.font.color = mytemplate.layout.font.color
mytemplate.layout.annotationdefaults.font.size = 15

# LAYOUT BAR
mytemplate.layout.barmode = "stack"
mytemplate.layout.bargap = 0

# =============
# PLOT SPECIFIC
# =============

# MAP
mytemplate.layout.map.style = "open-street-map"
mytemplate.layout.map.zoom = 9
mytemplate.layout.map.center.lon = 107.66088653834305
mytemplate.layout.map.center.lat = -7.017416613305268