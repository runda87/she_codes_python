import plotly.graph_objects as go

years = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
perth_population = [1.67, 1.83, 1.97, 2.02, 2.04, 2.14, 2.20, 2.28, 2.385, 2.47]
brisbane_population = [1.98, 2.10, 2.24, 2.27, 2.3, 2.38, 2.42, 2.48, 2.56, 2.62]
adelaide_population = [1.198, 1.251, 1.29, 1.3, 1.316, 1.34, 1.36, 1.38, 1.408, 1.429]


fig = go.Figure(data=[
    go.Bar(
        name="Perth",
        x=years,
        y=perth_population
    ),
    go.Bar(
        name="Brisbane",
        x= years,
        y= brisbane_population
    ),
    go.Scatter(
        name="Adelaide",
        x=years,1
        y=adelaide_population
    )
])
fig.update_layout(
    title="Population of Australian Cities 2011 - 2020",
    xaxis_title="Year",
    yaxis_title="Population (millions)",
)
fig.write_html("linegraph.html")