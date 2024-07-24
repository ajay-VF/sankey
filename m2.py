from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Energy Production'),
    dcc.Graph(id="graph"),
    html.P("Opacity"),
    dcc.Slider(id='slider', min=0, max=1, 
               value=0.5, step=0.1)
])

data = [
    {"from": "Domestic Coal", "to": "Coal", "weight": 369.8},
    {"from": "Imported Coal", "to": "Coal", "weight": 126.3},
    {"from": "Coal Stock Exchange", "to": "Coal", "weight": 6.1},
    {"from": "Coal", "to": "Coal Statistical Diff.", "weight": 7.0},
    {"from": "Coal", "to": "Coal Export", "weight": 0.8},
    {"from": "Coal", "to": "Coal Cons.", "weight": 168.5},
    {"from": "Coal", "to": "Electricity Plant", "weight": 326.0},
    {"from": "Coal Cons.", "to": "Industry", "weight": 168.5},
    {"from": "Industry", "to": "Iron & steel", "weight": 39.9},
    {"from": "Industry", "to": "Chemical & petrochemical", "weight": 0.5},
    {"from": "Industry", "to": "Pulp & Paper", "weight": 0.8},
    {"from": "Industry", "to": "Construction", "weight": 4.5},
    {"from": "Industry", "to": "Textile & leather", "weight": 0.6},
    {"from": "Industry", "to": "Non-specified (industry)", "weight": 122.2},
    {"from": "Domestic Crude", "to": "Crude Oil", "weight": 29.8},
    {"from": "Imported Crude", "to": "Crude Oil", "weight": 237.9},
    {"from": "Crude Statistical Diff.", "to": "Crude Oil", "weight": 19.7},
    {"from": "Crude Oil", "to": "Oil Refinery", "weight": 260.8},
    {"from": "Crude Oil", "to": "Oil Refinery Losses", "weight": 26.5},
    {"from": "PP Imports", "to": "Petroleum Products", "weight": 44.6},
    {"from": "Oil Refinery", "to": "Petroleum Products", "weight": 272.0},
    {"from": "Petroleum Products", "to": "Exports", "weight": 63.7},
    {"from": "Petroleum Products", "to": "PP Statistical Diff.", "weight": 24.9},
    {"from": "Petroleum Products", "to": "Electricity Plant", "weight": 0.9},
    {"from": "Petroleum Products", "to": "Oil Cons.", "weight": 227.1},
    {"from": "Oil Cons.", "to": "Industry", "weight": 49.5},
    {"from": "Oil Cons.", "to": "Transport", "weight": 49.6},
    {"from": "Oil Cons.", "to": "Residential", "weight": 29.0},
    {"from": "Oil Cons.", "to": "Agriculture", "weight": 0.4},
    {"from": "Oil Cons.", "to": "Commercial & Public Services", "weight": 0.1},
    {"from": "Oil Cons.", "to": "Others", "weight": 98.5},
    {"from": "Industry", "to": "Iron & steel", "weight": 1.0},
    {"from": "Industry", "to": "Chemical & petrochemical", "weight": 11.8},
    {"from": "Industry", "to": "Construction", "weight": 0.4},
    {"from": "Industry", "to": "Textile & leather", "weight": 0.2},
    {"from": "Industry", "to": "Non-ferrous metals", "weight": 0.4},
    {"from": "Industry", "to": "Non-specified (industry)", "weight": 34.5},
    {"from": "Industry", "to": "Machinery", "weight": 0.1},
    {"from": "Industry", "to": "Mining and quarrying", "weight": 1.2},
    {"from": "Transport", "to": "Road", "weight": 37.9},
    {"from": "Transport", "to": "Rail", "weight": 1.8},
    {"from": "Transport", "to": "Domestic aviation", "weight": 7.8},
    {"from": "Transport", "to": "Domestic navigation", "weight": 2.1},
    {"from": "Domestic NG", "to": "Natural Gas", "weight": 31.9},
    {"from": "Imported NG", "to": "Natural Gas", "weight": 24.3},
    {"from": "NG Statistical Diff.", "to": "Natural Gas", "weight": 3.3},
    {"from": "Natural Gas", "to": "Electricity Plant", "weight": 7.5},
    {"from": "Natural Gas", "to": "NG Cons.", "weight": 35.2},
    {"from": "Natural Gas", "to": "Own Use", "weight": 16.6},
    {"from": "Natural Gas", "to": "NG Losses", "weight": 0.1},
    {"from": "NG Cons.", "to": "Industry", "weight": 0.8},
    {"from": "NG Cons.", "to": "Transport", "weight": 12.8},
    {"from": "NG Cons.", "to": "Agriculture", "weight": 0.1},
    {"from": "NG Cons.", "to": "Others", "weight": 0.9},
    {"from": "NG Cons.", "to": "Non-Energy Use", "weight": 20.6},
    {"from": "Industry", "to": "Non-specified (industry)", "weight": 0.8},
    {"from": "Transport", "to": "Road", "weight": 11.1},
    {"from": "Transport", "to": "Pipeline Trans.", "weight": 1.6},
    {"from": "Nuclear Prod.", "to": "Nuclear", "weight": 12.0},
    {"from": "Nuclear", "to": "Electricity Plant", "weight": 12.0},
    {"from": "Hydro Prod.", "to": "Hydro", "weight": 14.0},
    {"from": "Hydro", "to": "Electricity Plant", "weight": 13.9},
    {"from": "Hydro", "to": "Captive", "weight": 0.0},
    {"from": "Renewable Prod.", "to": "Renewable", "weight": 18.3},
    {"from": "Renewable", "to": "Electricity Plant", "weight": 17.5},
    {"from": "Renewable", "to": "Captive", "weight": 0.8},
    {"from": "Electricity Plant", "to": "Thermal Losses in Power Plants", "weight": 238.7},
    {"from": "Electricity Imports", "to": "Electricity", "weight": 0.7},
    {"from": "Electricity Plant", "to": "Electricity", "weight": 139.1},
    {"from": "Auto Producer", "to": "Electricity", "weight": 19.4},
    {"from": "Electricity", "to": "Elec. Statistical Diff.", "weight": 4.8},
    {"from": "Electricity", "to": "Electricity Final Cons.", "weight": 120.7},
    {"from": "Electricity", "to": "T&D Loss", "weight": 24.0},
    {"from": "Electricity", "to": "Electricity Export", "weight": 0.9},
    {"from": "Electricity", "to": "Auxiliary Cons.", "weight": 8.9},
    {"from": "Electricity Final Cons.", "to": "Industry", "weight": 51.2},
    {"from": "Electricity Final Cons.", "to": "Transport", "weight": 2.2},
    {"from": "Electricity Final Cons.", "to": "Residential", "weight": 31.1},
    {"from": "Electricity Final Cons.", "to": "Commercial & Public Services", "weight": 9.0},
    {"from": "Electricity Final Cons.", "to": "Agriculture", "weight": 20.7},
    {"from": "Electricity Final Cons.", "to": "Others", "weight": 6.5},
    {"from": "Industry", "to": "Non-specified (industry)", "weight": 51.2},
    {"from": "Transport", "to": "Rail", "weight": 2.2}
]

# Extract unique labels and calculate values
labels = list(set([item['from'] for item in data] + [item['to'] for item in data]))

# Create a mapping from label to index
label_indices = {label: i for i, label in enumerate(labels)}

# Calculate sums of values for each node
node_values = {label: 0 for label in labels}
inner_nodes = {item['to'] for item in data}

for item in data:
    if item['from'] not in inner_nodes:
        node_values[item['from']] += item['weight']
    node_values[item['to']] += item['weight']

# Create nodes with labels including values
nodes = {
    'label': [f"{label} ({node_values[label]:.1f})" for label in labels],
    'color': ['rgba(31, 119, 180, 0.8)' for _ in labels]  # Default color
}

# Define node colors
node_colors = {
    "Domestic Coal": '#77bdc9',
    "Imported Coal": '#77bdc9',
    "Coal Stock Exchange": '#77bdc9',
    "Coal": '#77bdc9',
    "Coal Statistical Diff.": '#77bdc9',
    "Coal Export": '#77bdc9',
    "Coal Cons.": '#7db2d4',
    "Electricity Plant": '#a4adb0',
    "Industry": '#c9adc9',
    "Iron & steel": '#dea985',
    "Chemical & petrochemical": '#9fa789',
    "Pulp & Paper": '#77bdc9',
    "Construction": '#77bdc9',
    "Textile & leather": '#77bdc9',
    "Non-specified (industry)": '#f2c2e4',
    "Domestic Crude": '#77bdc9',
    "Imported Crude": '#77bdc9',
    "Crude Statistical Diff.": '#77bdc9',
    "Crude Oil": '#77bdc9',
    "Oil Refinery": '#b88e74',
    "Oil Refinery Losses": '#77bdc9',
    "PP Imports": '#b88e74',
    "Petroleum Products": '#b88e74',
    "Exports": '#ffc593',
    "PP Statistical Diff.": '#ffc593',
    "Oil Cons.": '#b88e74',
    "Transport": '#706f8f',
    "Residential": '#D52627',
    "Agriculture": '#c5c5c5',
    "Commercial & Public Services": '#77bdc9',
    "Others": '#7f8487',
    "Non-ferrous metals": '#77bdc9',
    "Machinery": '#77bdc9',
    "Mining and quarrying": '#77bdc9',
    "Road": '#827879',
    "Rail": '#827879',
    "Domestic aviation": '#827879',
    "Domestic navigation": '#827879',
    "Domestic NG": '#77bdc9',
    "Imported NG": '#77bdc9',
    "NG Statistical Diff.": '#77bdc9',
    "Natural Gas": '#999367',
    "NG Cons.": '#77bdc9',
    "Own Use": '#77bdc9',
    "NG Losses": '#77bdc9',
    "Non-Energy Use": '#876580',
    "Pipeline Trans.": '#77bdc9',
    "Nuclear Prod.": '#77bdc9',
    "Nuclear": '#77bdc9',
    "Hydro Prod.": '#77bdc9',
    "Hydro": '#77bdc9',
    "Captive": '#77bdc9',
    "Renewable Prod.": '#77bdc9',
    "Renewable": '#77bdc9',
    "Thermal Losses in Power Plants": '#7F8487',
    "Electricity Imports": '#77bdc9',
    "Electricity": '#7f8487',
    "Auto Producer": '#77bdc9',
    "Elec. Statistical Diff.": '#77bdc9',
    "Electricity Final Cons.": '#7f8487',
    "T&D Loss": '#f2c2e4',
    "Electricity Export": '#77bdc9',
    "Auxiliary Cons.": '#77bdc9'
}


# Assign colors to nodes based on the defined node colors
for i, label in enumerate(labels):
    if label in node_colors:
        nodes['color'][i] = node_colors[label]
    else:
        nodes['color'][i] = 'rgba(31, 119, 180, 0.8)'  # Default color if node color is not defined
 
# Create links
links = {
    'source': [label_indices[item['from']] for item in data],
    'target': [label_indices[item['to']] for item in data],
    'value': [item['weight'] for item in data],
    'color': ['rgba(31, 119, 180, 0.8)' for _ in data]  # Default color
}

# Define path colors
path_colors = {
    ("Domestic Coal", "Coal"): '#97e2e9',    # Red
    ("Imported Coal", "Coal"): '#97e2e9',    # Green
    ("Coal Stock Exchange", "Coal"): '#97e2e9',
    ("Coal","Electricity Plant"): '#97e2e9',
    ("Coal","Coal Cons."):'#97e2e9',
    ("Coal","Coal Statistical Diff."):'#97e2e9',
    ("Coal","Coal Export"): '#97e2e9',

    ("Coal Cons.", "Industry") :'#7db2d4',
    ("Electricity Final Cons.", "Industry") :'#7db2d4',
    ("Oil Cons.", "Industry") :'#7db2d4',
    ("NG Cons.", "Industry") :'#7db2d4',

    ("Industry", "Iron & steel") :'#dea985',
    ("Industry", "Chemical & petrochemical") :'#62703e',
    ("Industry", "Pulp & Paper") :'#948d93',
    ("Industry", "Construction") :'#494d5c',
    ("Industry", "Textile & leather") :'#424242',
    ("Industry", "Non-specified (industry)") :'#f2c2e4',
    ("Industry", "Non-ferrous metals") :'#c9adc9',
    ("Industry", "Machinery") :'#c9adc9',
    ("Industry", "Mining and quarrying") :'#c9adc9',

    ("Imported NG", "Natural Gas") :'#999367',
    ("Domestic NG", "Natural Gas") :'#999367',
    ("NG Statistical Diff.", "Natural Gas") :'#999367',

    ("Naural Gas", "Electricity Plant") :'#c79879',
    ("Naural Gas", "NG Cons.") :'#c79879',
    ("Naural Gas", "Own Use") :'#c79879',
    ("Naural Gas", "NG Losses") :'#c79879',

    ("NG Cons.", "Non-Energy Use") :'#876580',
    #DOUBT
    #("NG Cons.", "Non-Energy Use") :'#876580',
    #("NG Cons.", "Non-Energy Use") :'#876580',
    #("NG Cons.", "Non-Energy Use") :'#876580',
    #("NG Cons.", "Non-Energy Use") :'#876580',

    ("Imported Crude", "Crude Oil") :'#9ac2dd',
    ("Domestic Crude", "Crude Oil") :'#9ac2dd',
    ("Crude Statistical Diff.", "Crude Oil") :'#9ac2dd',

    ("Crude Oil", "Oil Refinery") :'#9ac2dd',
    ("Crude Oil", "Oil Refinery Losses") :'#9ac2dd',

    ("Oil Refinery", "Petroleum Products") :'#ffc593',
    ("PP Imports", "Petroleum Products") :'#ffc593',

    ("Petroleum Products", "Oil Cons.") :'#ffc593',
    ("Petroleum Products", "Exports") :'#ffc593',
    ("Petroleum Products", "PP Statistical Diff.") :'#ffc593',
    ("Petroleum Products", "Electricity Plant") :'#ffc593',

    ("Oil Cons.", "Others") :'#c5c5c5',
    ("Oil Cons.", "Industry") :'#5b87a8',
    ("Oil Cons.", "Transport") :'#706f8f',
    ("Oil Cons.", "Agriculture") :'#8f8a68',
    ("Oil Cons.", "Residential") :'#ED9E9E',
    ("Oil Cons.", "Commercial & Public Services") :'#7d7e80',

    ("Transport", "Road") :'#827879',
    ("Transport", "Domestic aviation") :'#827879',
    ("Transport", "Rail") :'#827879',
    ("Transport", "Pipeline Trans.") :'#827879',
    ("Transport", "Domestic navigation") :'#827879',

    ("Nuclear Prod.", "Nuclear") :'#84cfd5',
    ("Nuclear", "Electricity Plant") :'#84cfd5',


    ("Hydro Prod.", "Hydro") :'#364e66',
    ("Hydro", "Electricity Plant") :'#364e66',

    ("Renewable Prod.", "Renewable") :'#3d5243',
    ("Renewable", "Electricity Plant") :'#364e66',

    ("Electricity Plant", "Thermal Losses in Power Plants") :'#c5c5c5',
    ("Electricity Plant", "Electricity") :'#c5c5c5',

    ("Auto Producer", "Electricity") :'#c5c5c5',
    ("Electricity Imports", "Electricity") :'#c5c5c5',

    ("Electricity", "Electricity Final Cons.") :'#c5c5c5',
    ("Electricity", "T&D Loss") :'#b09ab5',
    ("Electricity", "Auxiliary Cons.") :'#777c7d',
    ("Electricity", "Elec. Statistical Diff.") :'#767a4c',
    ("Electricity", "Electricity Export") :'#828687',

    ("Electricity Final Cons.", "Industry") :'#c5c5c5',
    ("Electricity Final Cons.", "Agriculture") :'#c5c5c5',
    ("Electricity Final Cons.", "Commercial & Public Services") :'#c5c5c5',
    ("Electricity Final Cons.", "Residential") :'#c5c5c5',
    ("Electricity Final Cons.", "Others") :'#c5c5c5',
    ("Electricity Final Cons.", "Transport") :'#c5c5c5',

    #("Nuclear Prod.", "Nuclear"): 'brown',
    #("Nuclear", "Electricity Plant"): 'brown',
    #("Hydro Prod.", "Hydro"): 'blue',
    #("Hydro", "Electricity Plant"): 'blue',
    #("Renewable Prod.", "Renewable"): 'green',
    #("Renewable", "Electricity Plant"): 'green',
    #("Auto Producer", "Electricity"): 'orange',
    #("Electricity Imports", "Electricity"):'purple',
    #("Imported NG", "Natural Gas"): 'olive',
    #("Domestic NG", "Natural Gas"): "olive",
    #("NG Statistical Diff.", "Natural Gas"): "olive",
    #("Imported Crude", "Crude Oil"): "lightgreen",
    #("Domestic Crude", "Crude Oil"): "lightyellow",
    #("Coal", "Electricity Plant"): "darkgrey",
    #("Petroleum Products", "Electricity Plant"): "darkgrey",
    #("Natural Gas", "Electricity Plant"): "darkgrey",
    #("Nuclear", "Electricity Plant"): "darkgrey",
    #("Hydro", "Electricity Plant"): "darkgrey",
    #("Renewable", "Electricity Plant"): "darkgrey",
    #("Electricity Imports", "Electricity"): "silver",
    #("Electricity Plant", "Electricity"): "silver",
    #("Auto Producer", "Electricity"): "silver",
    #("Electricity", "Electricity Final Cons."): "silver",
    #("Electricity", "Elec. Statistical Diff."): "silver",
    #("Electricity", "T&D Loss"): "silver",
    #("Electricity", "Electricity Export"): "silver",
    #("Electricity", "Auxiliary Cons."): "silver",
    #("Electricity Final Cons.", "Industry"): "peru",
    #("Electricity Final Cons.", "Transport"): "tan",
    #("Electricity Final Cons.", "Residential"): "lightcoral",
    #("Electricity Final Cons.", "Agriculture"): "olivedrab",
    #("Electricity Final Cons.", "Commercial & Public Services"): "chocolate",
    #("Electricity Final Cons.", ""): "peru",
    ("Domestic NG", "Domestic NG") :'black',


    






    #("Crude Statistical Diff.", "Crude Oil"): "lightbrown",





    # Add more path-specific colors as needed
}


# Assign colors to links based on the defined path colors
for i, item in enumerate(data):
    path = (item['from'], item['to'])
    if path in path_colors:
        links['color'][i] = path_colors[path]
    else:
        links['color'][i] = 'rgba(31, 119, 180, 0.8)'  # Default color if path is not defined

@app.callback(
    Output("graph", "figure"), 
    Input("slider", "value"))
def display_sankey(opacity):
    # Update link colors based on opacity
    links['color'] = [
        color.replace('0.8', str(opacity)) for color in links['color']
    ]

    fig = go.Figure(go.Sankey(link=links, node=nodes))
    fig.update_layout(font_size=15, height=1000)  # Adjust height as needed
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
