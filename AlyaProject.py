from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server = app.server

app.title = "MCM7003 Data Visualization Interactive Demo"

# Load data from the provided URL
data_url = "https://raw.githubusercontent.com/LyaFaridha/Assignment3/main/df_arabica_clean.csv"
df = pd.read_csv(data_url)

# Create a bar chart for the 'Country of Origin' counts
country_counts = df['Country of Origin'].value_counts()
fig_country_counts = px.bar(country_counts, x=country_counts.index, y=country_counts.values)

fig_country_counts.update_layout(
    xaxis_title='Country of Origin',
    yaxis_title='Count',
    title={'text': 'Distribution of Country of Origins', 'x': 0.5}
)

# Define the app layout
app.layout = html.Div([
    html.H1("Data Visualization"),

    dcc.RadioItems(
        id='radio-graph',
        options=[
            {'label': 'Country of Origin', 'value': 'country-counts'},
            {'label': 'Aroma vs. Flavor', 'value': 'aroma-flavor'},
            {'label': 'Processing Method', 'value': 'processing-method'},
        ],
        value='country-counts',
        labelStyle={'display': 'block'}
    ),

    dcc.Graph(id='graph-output'),

])

# Define callback to update the graph based on radio button selection
@app.callback(
    Output('graph-output', 'figure'),
    Input('radio-graph', 'value')
)
def update_graph(radio_value):
    if radio_value == 'country-counts':
        return fig_country_counts
    elif radio_value == 'aroma-flavor':
        # Replace with the appropriate scatter plot for aroma vs. flavor
        # You can reuse your existing fig1
        return fig1
    elif radio_value == 'processing-method':
        # Replace with the appropriate box plot for processing methods
        # You can reuse your existing fig2
        return fig2



# Create the first scatter plot
fig1 = px.scatter(df, x='Aroma', y='Flavor', color='Country of Origin',
                 labels={'Aroma': 'Aroma', 'Flavor': 'Flavor', 'Country of Origin': 'Country of Origin'},
                 title='Relationship between Aroma and Flavor Attributes by Country of Origin')
fig1.update_traces(
    marker=dict(size=10),
    selector=dict(mode='markers')
)

# Create the second box plot
fig2 = px.box(df, x='Processing Method', y=['Aroma', 'Flavor'],
             labels={'variable': 'Attribute', 'value': 'Rating', 'Processing Method': 'Processing Method'},
             title='Comparison of Aroma and Flavor Attributes across Processing Methods')

# Define the app layout
app.layout = html.Div([
    html.H1("Data Visualization"),

    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Bar Chart', value='tab-1'),
        dcc.Tab(label='Scatter Plot', value='tab-2'),
        dcc.Tab(label='Box Plot', value='tab-3'),
    ]),

    html.Div(id='tabs-content'),

    html.Br(),

    dcc.RadioItems(
        id='radio-graph',
        options=[
            {'label': 'Country of Origin', 'value': 'country-counts'},
            {'label': 'Aroma vs. Flavor', 'value': 'aroma-flavor'},
            {'label': 'Processing Method', 'value': 'processing-method'},
        ],
        value='country-counts',
        labelStyle={'display': 'block'}
    ),

    html.Br(),

    dcc.Checklist(
        id='checklist',
        options=[
            {'label': 'Show Grid', 'value': 'grid'},
            {'label': 'Show Lines', 'value': 'lines'},
        ],
        value=['grid', 'lines']
    )
])

# Define callback to update graphs and beautify them
@app.callback(
    Output('tabs-content', 'children'),
    Output('graph-output', 'figure'),
    Output('graph1-output', 'figure'),
    Output('graph2-output', 'figure'),
    Input('tabs', 'value'),
    Input('radio-graph', 'value'),
    Input('checklist', 'value')
)
def update_graph(tab, radio_value, checklist_value):
    fig = None
    if tab == 'tab-1':
        fig = fig_country_counts
    elif tab == 'tab-2':
        fig = fig1
    elif tab == 'tab-3':
        fig = fig2

    # Customize the appearance based on checklist values
    for value in checklist_value:
        if value == 'grid':
            fig.update_xaxes(showgrid=True)
            fig.update_yaxes(showgrid=True)
        elif value == 'lines':
            fig.update_xaxes(showline=True, linewidth=1, linecolor='black')
            fig.update_yaxes(showline=True, linewidth=1, linecolor='black')

    return html.Div([
        dcc.Graph(id='graph-output', figure=fig),
        dcc.Graph(id='graph1-output', figure=fig1),
        dcc.Graph(id='graph2-output', figure=fig2)
    ]), fig_country_counts, fig1, fig2

if __name__ == '__main__':
    app.run_server(debug=True)
This code adds tabs for different graphs, radio buttons to switch between them, and checkboxes to customize their appearance (show/hide grid and lines). You can further customize the appearance and functionality according to your requirements.








