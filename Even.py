import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url'),  # Add the dcc.Location component
    html.H1('List of Even Numbers'),
    html.Div(id='even-numbers'),
])

@app.callback(
    dash.dependencies.Output('even-numbers', 'children'),
    dash.dependencies.Input('url', 'pathname')
)
def update_output(pathname):
    p = []
    for j in range(200, 300, 2):
        p.append(j)
    return str(p)

if __name__ == '__main__':
    app.run_server(debug=True)


