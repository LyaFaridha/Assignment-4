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

# Define app layout
app.layout = html.Div([
    html.H1("MCM7003 Data Visualization Interactive Demo", style={'textAlign': 'center'}),
    
    # Radio buttons for selecting the chart
    dcc.RadioItems(
        id='chart-selector',
        options=[
            {'label': 'Country Counts', 'value': 'country_counts'},
            {'label': 'Scatter Plot', 'value': 'scatter_plot'},
            {'label': 'Box Plot', 'value': 'box_plot'},
        ],
        value='country_counts',
        labelStyle={'display': 'block'}
    ),

    # Graph component to display selected chart
    dcc.Graph(id='graph-output'),

    # Checkboxes for customization options
    html.Label("Customization Options:", style={'font-weight': 'bold'}),
    dcc.Checklist(
        id='custom-options',
        options=[
            {'label': 'Show Grid Lines', 'value': 'show-grid'},
            {'label': 'Show Markers', 'value': 'show-markers'},
        ],
        value=['show-grid']
    ),
    
    # Tabs for additional information
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Tab 1', value='tab-1'),
        dcc.Tab(label='Tab 2', value='tab-2'),
    ]),
    
    # Placeholder for tab content
    html.Div(id='tab-content')
])

# Callback to update

