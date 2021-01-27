# Paulo Nuin Jan 2021


import altair as alt
import pandas as pd
import numpy as np

def plot_graph(json_file):
    """

    :return:
    """

    dataframe = pd.read_json(json_file)
    dataframe.index.name = 'x'
    dataframe = dataframe.reset_index().melt('x', var_name='category', value_name='y')

    nearest = alt.selection(type='single', nearest=True, on='mouseover', fields=['x'], empty='none')

    # The basic line
    line = alt.Chart(dataframe).mark_line(interpolate='basis').encode(
        x='x:Q',
        y='y:Q',
        color='category:N'
    )

    # Transparent selectors across the chart. This is what tells us
    # the x-value of the cursor
    selectors = alt.Chart(dataframe).mark_point().encode(x='x:Q',opacity=alt.value(0),).add_selection(nearest)

    # Draw points on the line, and highlight based on selection
    points = line.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))

    # Draw text labels near the points, and highlight based on selection
    text = line.mark_text(align='left', dx=5, dy=-5).encode(text=alt.condition(nearest, 'y:Q', alt.value(' ')))

    # Draw a rule at the location of the selection
    rules = alt.Chart(dataframe).mark_rule(color='gray').encode(x='x:Q',).transform_filter(nearest)

    # Put the five layers into a chart and bind the data
    chart = alt.layer(line, selectors, points, rules, text).properties(width=2000, height=800)

    chart.save('drift.html')





if __name__ == '__main__':

    plot_graph('drift.json')