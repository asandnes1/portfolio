# go.Figure layout template

# Imports
from utils.third_party import go


def fig_layout_template():
    """
    Template for a Plotly figure layout.

    This template includes a title, axis labels, and some basic formatting
    options. The layout is set up to be used with a dark background, but you
    can easily change this by modifying the `paper_bgcolor` and `plot_bgcolor`
    options.

    Parameters
    ----------
    None

    Returns
    -------
    fig_layout_template : go.Figure
        A Plotly figure layout template.
    """

    fig_layout_template = go.Figure(
        layout=go.Layout(
            # Titles
            title='Title',
            xaxis_title='X-axis Title',
            yaxis_title='Y-axis Title',
            
            # Axes
            xaxis=go.layout.XAxis(
                # type='category',
                showgrid=False,
            ),
            yaxis=go.layout.YAxis(
                # type='category',
                showgrid=False,
            ),

            # # Legend
            # legend=go.layout.Legend(
            #     orientation="h",
            #     x=0,
            #     y=1,
            #     xanchor="left",
            #     yanchor="top"
            # ),

            # Margin and padding
            margin=go.layout.Margin(
                l=50,
                r=50,
                b=50,
                t=50,
                pad=4
            ),

            # Colors
            # paper_bgcolor='rgba(0,0,0,0)',
            # plot_bgcolor='rgba(0,0,0,0)',
            
            # Font
            # font=dict(
            #     color='white'
            # ),

            # template='plotly_dark',
            hovermode='closest',
            hoverlabel=dict(
                # bgcolor='rgba(0,0,0,0)',
                font=dict(
                    family='Arial',
                    size=12,
                    # color='white',
                    weight='bold'
                ),
            ),
            annotations=[
                dict(
                    x=0.0,
                    y=-0.1,
                    xref='paper',
                    yref='paper',
                    text='Source: Data source (if known)',
                    showarrow=False,
                    font=dict(
                        size=10,
                        # color='white'
                    ),
                    # bgcolor='rgba(0,0,0,0)'
                )
            ],
            showlegend=True,
            width=800,
            height=600
        )
    )

    return fig_layout_template

