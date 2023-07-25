import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import flask_mysqldb

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Configure MySQL
app.config['MYSQL_HOST'] = 'your_mysql_host'
app.config['MYSQL_USER'] = 'your_mysql_username'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_mysql_database'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = flask_mysqldb.MySQL(app)


def login_layout():
    return html.Div([
        html.H1("Login"),
        dbc.Input(id="username-input", type="text", placeholder="Username", style={'margin-bottom': '10px'}),
        dbc.Input(id="password-input", type="password", placeholder="Password", style={'margin-bottom': '10px'}),
        dbc.Button("Login", id="login-button", color="primary", n_clicks=0)
    ], style={'text-align': 'center', 'margin': '100px auto', 'width': '50%'})


@app.callback(
    Output('url', 'pathname'),
    Input('login-button', 'n_clicks'),
    State('username-input', 'value'),
    State('password-input', 'value')
)
def authenticate(n_clicks, username, password):
    if n_clicks > 0:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        if user and user['password'] == password:
            return "/success"
        else:
            return "/invalid"


@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/success':
        return html.H1("Login Successful!")
    elif pathname == '/invalid':
        return html.H1("Invalid Username or Password")
    else:
        return login_layout()


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

if __name__ == '__main__':
    app.run_server(debug=True)
