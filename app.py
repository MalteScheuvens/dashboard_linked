from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output


app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.DataFrame({
    "Fruit":
        ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount":
        [4, 1, 2, 2, 4, 5],
    "City":
        ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
'''
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
'''
app.layout = html.Div(style={'backgroundColor': colors['background']},
                      children=[
                          html.H1(
                              children='Hello Dash',
                              style={
                                  'textAlign': 'center',
                                  'color': colors['text']
                              }
                          ),

                          html.Div(children='Dash: A web application framework for your data.', style={
                              'textAlign': 'center',
                              'color': colors['text']
                          }),

                          html.Br(),
                          html.Label('Dropdown'),
                          dcc.Dropdown(
                              df['Fruit'].unique(),
                              id='dropdown',
                              ),
                          html.Br(),

                          dcc.Graph(
                              id='example-graph'
                          )
                      ])


@app.callback(Output(component_id='example-graph', component_property='figure'),
              Input(component_id='dropdown', component_property='value'))
def plot_bar(fruit):
    df_temp = df[df.Fruit == fruit]
    fig = px.bar(df_temp, x="Fruit", y="Amount", color="City", barmode="group")

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=False)