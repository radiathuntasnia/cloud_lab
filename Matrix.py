import dash
from dash import dcc, html
import pandas as pd

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    dcc.Markdown('''
    # Matrix Multiplication Result
    '''),
    dcc.Graph(id='matrix-result'),
])


# Callback to calculate the matrix multiplication result
@app.callback(
    dash.dependencies.Output('matrix-result', 'figure'),
    dash.dependencies.Input('matrix-result', 'figure')
)
def calculate_matrix_result(_):
    # Program to multiply two matrices using nested loops
    # 2x3 matrix
    P = [[20, 40, 10],
         [30, 90, 30]]
    # 3x2 matrix
    Q = [[10, 30],
         [20, 40],
         [60, 80]]
    # result is 2x2
    value = [[0, 0],
              [0, 0]]

    # iterate through rows of X
    for i in range(len(P)):
        # iterate through columns of Y
        for j in range(len(Q[0])):
            # iterate through rows of Y
            for k in range(len(Q)):
                value[i][j] += P[i][k] * Q[k][j]

    # Convert the result matrix to a DataFrame for visualization
    df = pd.DataFrame(value, columns=['Column 1', 'Column 2'])

    # Create a bar chart for the matrix result
    fig = {
        'data': [
            {'x': df.columns, 'y': df.iloc[0], 'type': 'bar', 'name': 'Row 1'},
            {'x': df.columns, 'y': df.iloc[1], 'type': 'bar', 'name': 'Row 2'},
        ],
        'layout': {
            'title': 'Matrix Multiplication Result',
            'barmode': 'group',
        }
    }

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
