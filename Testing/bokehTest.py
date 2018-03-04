from bokeh.plotting import figure, output_file, show
import holoviews as hv 
hv.extension('bokeh')

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("lines.html")

data = [('one',8),('two', 10), ('three', 16), ('four', 8), ('five', 4), ('six', 1)]
bars = hv.Bars(data, hv.Dimension('Car occupants'), 'Count')


"""
# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y', toolbar_location=None)

# add a line renderer with legend and line thickness
p.line(x, y, legend="Temp.", line_width=2)
"""


# show the results
show(bars)