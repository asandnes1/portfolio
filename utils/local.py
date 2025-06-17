# Local imports

from utils.third_party import go


fig = go.Figure(
    go.Scattermap(
        lat=['45.5017'],
        lon=['-73.5673'],
        mode='markers',
        marker=go.scattermap.Marker(
            size=14
        ),
        text=['Montreal'],
    ),
    layout=go.Layout(
        # plot_bgcolor='',
        paper_bgcolor='rgba(164, 216, 250, 0.2)',
    )
)

fig.update_layout(
    hovermode='closest',
    map=dict(
        bearing=0,
        center=go.layout.map.Center(
            lat=45,
            lon=-73
        ),
        pitch=0,
        zoom=5,
        style='light'
    )
)

