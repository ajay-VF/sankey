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
