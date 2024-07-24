# from dash import Dash, dcc, html, Input, Output
# import plotly.graph_objects as go

# app = Dash(__name__)

# app.layout = html.Div([
#     html.H4('Energy Production'),
#     dcc.Graph(id="graph"),
#     html.P("Opacity"),
#     dcc.Slider(id='slider', min=0, max=1, 
#                value=0.5, step=0.1),
#     html.Script('''
#         document.addEventListener('DOMContentLoaded', function() {
#             var updateLabels = function() {
#                 var labels = document.querySelectorAll('.node-label');
#                 labels.forEach(function(label) {
#                     var nodeX = parseFloat(label.getAttribute('x'));
#                     if (nodeX < 50) {  // Adjust as necessary
#                         label.setAttribute('text-anchor', 'start');
#                         label.setAttribute('x', '-100');  // Align to left
#                     }
#                 });
#             };

#             updateLabels();
#             // Re-run updateLabels after a delay to account for any re-renders
#             setTimeout(updateLabels, 500);
#         });
#     ''')
# ])


# data = [
#     {"from": "Domestic Coal", "to": "Coal", "weight": 369.8},
#     {"from": "Imported Coal", "to": "Coal", "weight": 126.3},
#     {"from": "Coal Stock Exchange", "to": "Coal", "weight": 6.1},
#     {"from": "Coal", "to": "Coal Statistical Diff.", "weight": 7.0},
#     {"from": "Coal", "to": "Coal Export", "weight": 0.8},
#     {"from": "Coal", "to": "Coal Cons.", "weight": 168.5},
#     {"from": "Coal", "to": "Electricity Plant", "weight": 326.0},
#     {"from": "Coal Cons.", "to": "Industry", "weight": 168.5},
#     {"from": "Industry", "to": "Iron & steel", "weight": 39.9},
#     {"from": "Industry", "to": "Chemical & petrochemical", "weight": 0.5},
#     {"from": "Industry", "to": "Pulp & Paper", "weight": 0.8},
#     {"from": "Industry", "to": "Construction", "weight": 4.5},
#     {"from": "Industry", "to": "Textile & leather", "weight": 0.6},
#     {"from": "Industry", "to": "Non-specified (industry)", "weight": 122.2},
# ]

# # Extract unique labels and calculate values
# labels = list(set([item['from'] for item in data] + [item['to'] for item in data]))

# # Create a mapping from label to index
# label_indices = {label: i for i, label in enumerate(labels)}

# # Calculate sums of values for each node
# node_values = {label: 0 for label in labels}
# inner_nodes = {item['to'] for item in data}

# for item in data:
#     if item['from'] not in inner_nodes:
#         node_values[item['from']] += item['weight']
#     node_values[item['to']] += item['weight']

# # Create nodes with labels including values
# nodes = {
#     'label': [f"{label} ({node_values[label]:.1f})" for label in labels],
#     'color': ['rgba(31, 119, 180, 0.8)' for _ in labels]  # Default color
# }

# # Define node colors
# node_colors = {
#     "Domestic Coal": '#77bdc9',
#     "Imported Coal": '#77bdc9',
#     "Coal Stock Exchange": '#77bdc9',
#     "Coal": '#77bdc9',
#     "Coal Statistical Diff.": '#77bdc9',
#     "Coal Export": '#77bdc9',
# }


# # Assign colors to nodes based on the defined node colors
# for i, label in enumerate(labels):
#     if label in node_colors:
#         nodes['color'][i] = node_colors[label]
#     else:
#         nodes['color'][i] = 'rgba(31, 119, 180, 0.8)'  # Default color if node color is not defined

# # Create links
# links = {
#     'source': [label_indices[item['from']] for item in data],
#     'target': [label_indices[item['to']] for item in data],
#     'value': [item['weight'] for item in data],
#     'color': ['rgba(31, 119, 180, 0.8)' for _ in data]  # Default color
# }

# # Define path colors
# path_colors = {
#     ("Domestic Coal", "Coal"): '#77bdc9',    # Red
#     ("Imported Coal", "Coal"): '#77bdc9',    # Green
#     ("Coal Stock Exchange", "Coal"): '#77bdc9',
#     ("Coal","Electricity Plant"): '#77bdc9',
#     ("Coal","Coal Cons."):'#77bdc9',
#     ("Coal","Coal Statistical Diff."):'#77bdc9',
#     ("Coal","Coal Export"): '#77bdc9',
# }



# # Assign colors to links based on the defined path colors
# for i, item in enumerate(data):
#     path = (item['from'], item['to'])
#     if path in path_colors:
#         links['color'][i] = path_colors[path]
#     else:
#         links['color'][i] = 'rgba(31, 119, 180, 0.8)'  # Default color if path is not defined

# @app.callback(
#     Output("graph", "figure"), 
#     Input("slider", "value"))

# def display_sankey(opacity):
#     # Update link colors based on opacity
#     links['color'] = [
#         color.replace('0.8', str(opacity)) for color in links['color']
#     ]
    
#     # Create Sankey diagram
#     fig = go.Figure(go.Sankey(link=links, node=nodes))
    
#     # Adjust node positions
#     # Start nodes (nodes with incoming links but no outgoing links) will be aligned to the left
#     start_nodes = [i for i, label in enumerate(nodes['label']) if all(target != i for target in links['source'])]
#     fig.update_traces(node=dict(
#         x=[0.1 if i in start_nodes else None for i in range(len(nodes['label']))]  # Adjust position for start nodes
#     ))
    
#     fig.update_layout(font_size=15, height=1000)  # Adjust height as needed
#     return fig

# if __name__ == '__main__':
#     app.run_server(debug=True)
















from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import matplotlib.pyplot as plt

def get_color(weight, min_weight, max_weight):
    norm = plt.Normalize(vmin=min_weight, vmax=max_weight)
    cmap = plt.cm.ScalarMappable(norm=norm, cmap='viridis')  # Change 'viridis' to any preferred colormap
    return cmap.to_rgba(weight)

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

# Extract unique nodes and links
nodes = list(set([d['from'] for d in data] + [d['to'] for d in data]))
links = [{'source': nodes.index(d['from']), 'target': nodes.index(d['to']), 'value': d['weight']} for d in data]

# Get minimum and maximum weights for normalization
min_weight = min(d['weight'] for d in data)
max_weight = max(d['weight'] for d in data)

@app.callback(
    Output("graph", "figure"),
    Input("slider", "value")
)
def update_graph(opacity):
    link_colors = [get_color(d['weight'], min_weight, max_weight) for d in data]
    link_colors = [f'rgba({int(r*255)},{int(g*255)},{int(b*255)},{opacity})' for r, g, b, _ in link_colors]

    fig = go.Figure(go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=nodes
        ),
        link=dict(
            source=[link['source'] for link in links],
            target=[link['target'] for link in links],
            value=[link['value'] for link in links],
            color=link_colors
        )
    ))

    fig.update_layout(title_text="Energy Production", font_size=10)
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
