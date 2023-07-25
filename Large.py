import dash
from dash import dcc, html

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    dcc.Markdown('''
    # Find the 6th Largest Number
    '''),
    html.Div(id='result')
])

# Callback to calculate the 6th largest number
@app.callback(
    dash.dependencies.Output('result', 'children'),
    dash.dependencies.Input('result', 'children')
)
def find_6th_largest_number(_):
    # List of Integers
    values = [20, 50, 60, 80, 30, 40, 52, 62, 78, 10, 42]

    # Sorting list of Integers
    values.sort()
    return "6th largest number from the given list is " + str(values[len(values) - 6])

if __name__ == '__main__':
    app.run_server(debug=True)
