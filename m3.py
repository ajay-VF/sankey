from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Energy Production'),
    dcc.Graph(id="graph"),
    html.P("Opacity"),
    dcc.Slider(id='slider', min=0, max=1, 
               value=0.5, step=0.1),
    html.Script('''
        document.addEventListener('DOMContentLoaded', function() {
            var updateLabels = function() {
                var labels = document.querySelectorAll('.node-label');
                labels.forEach(function(label) {
                    var nodeX = parseFloat(label.getAttribute('x'));
                    if (nodeX < 50) {  // Adjust as necessary
                        label.setAttribute('text-anchor', 'start');
                        label.setAttribute('x', '-100');  // Align to left
                    }
                });
            };

            updateLabels();
            // Re-run updateLabels after a delay to account for any re-renders
            setTimeout(updateLabels, 500);
        });
    ''')
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
    ("Domestic Coal", "Coal"): '#77bdc9',    # Red
    ("Imported Coal", "Coal"): '#77bdc9',    # Green
    ("Coal Stock Exchange", "Coal"): '#77bdc9',
    ("Coal","Electricity Plant"): '#77bdc9',
    ("Coal","Coal Cons."):'#77bdc9',
    ("Coal","Coal Statistical Diff."):'#77bdc9',
    ("Coal","Coal Export"): '#77bdc9',
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
    
    # Create Sankey diagram
    fig = go.Figure(go.Sankey(link=links, node=nodes))
    
    # Adjust node positions
    # Start nodes (nodes with incoming links but no outgoing links) will be aligned to the left
    start_nodes = [i for i, label in enumerate(nodes['label']) if all(target != i for target in links['source'])]
    fig.update_traces(node=dict(
        x=[0.1 if i in start_nodes else None for i in range(len(nodes['label']))]  # Adjust position for start nodes
    ))
    
    fig.update_layout(font_size=15, height=1000)  # Adjust height as needed
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
















