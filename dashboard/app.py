from pathlib import Path

import pandas as pd
from dash import Dash, Input, Output, dcc, html
import plotly.express as px

# Load the launch data relative to this file so the app works from any directory.
DATA_PATH = Path(__file__).with_name("spacex_launch_dash.csv")
spacex_df = pd.read_csv(DATA_PATH)
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    # TASK 1: Dropdown list to enable Launch Site selection
    dcc.Dropdown(id='site-dropdown',
                 options=[
                     {'label': 'All Sites', 'value': 'ALL'},
                     {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                     {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                     {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                     {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
                 ],
                 value='ALL',
                 placeholder="Select a site",
                 searchable=True
                 ),
    html.Br(),

    # TASK 2: Pie chart to show the total successful launches count for all sites
    dcc.Graph(id='success-pie-chart'),
    html.Br(),

    html.P("Payload range (Kg):"),
    
    # TASK 3: Slider to select payload range
    dcc.RangeSlider(id="payload-slider",
                    min=0, max=10000, step=1000,
                    marks={0: '0', 10000: '10000'},
                    value=[min_payload, max_payload]),

    # TASK 4: Scatter chart to show the correlation between payload and launch success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# TASK 2:
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # Compute the total success launches for all sites
        fig = px.pie(spacex_df, values='class', 
                     names='Launch Site', 
                     title='Total Success Launches by Site')
    else:
        # Filter the data based on the selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        success_counts = filtered_df['class'].value_counts().reset_index(name='count')
        success_counts.columns = ['class', 'count']
        fig = px.pie(success_counts, values='count', names='class', 
                     title=f'Total Success Launches for Site {entered_site}')
    
    return fig

# TASK 4:
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id="payload-slider", component_property="value")]
)
def update_scatter_chart(selected_site, payload_range):
    if selected_site == 'ALL':
        filtered_df = spacex_df.copy()  # Use the entire dataset
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
    
    # Filter by payload range
    filtered_df = filtered_df[(filtered_df['Payload Mass (kg)'] >= payload_range[0]) &
                              (filtered_df['Payload Mass (kg)'] <= payload_range[1])]
    
    # Create scatter plot
    fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                     title='Payload vs. Success Outcome', 
                     labels={'Payload Mass (kg)': 'Payload Mass (kg)', 'class': 'Success Outcome'})
    
    # Update layout
    fig.update_layout(
        xaxis_title='Payload Mass (kg)',
        yaxis_title='Success Outcome',
        legend_title='Booster Version Category'
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8050)
