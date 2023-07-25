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
    a = []
    for i in range(50, 151, 2):
        a.append(i)
    return str(a)

if __name__ == '__main__':
    app.run_server(debug=True)


