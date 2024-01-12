import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime
ecom_data = pd.read_csv('ecom_sales.csv')
ecom_data = ecom_data.drop('Description', axis=1)
total_sales_by_Country = ecom_data.groupby('Country')['OrderValue'].agg('sum').reset_index()
total_sales_by_Country = total_sales_by_Country.sort_values(by='OrderValue', ascending=False)
top_country = total_sales_by_Country.loc[0]['Country']
fig = px.bar(data_frame=total_sales_by_Country,
                 x='OrderValue',
                 y='Country',
                 title='Sales by Country', color='Country')
fig.update_layout({'bargap':0.5})

app = dash.Dash(__name__)
app.layout = html.Div(
    [
    html.H1('Sales by Country 1. dash app'),
    html.Span
        (children=[f'Prepared:{datetime.now().date()}',' by ', html.B('Nikita')]),
    dcc.Graph(figure=fig),
    html.Span
        (children=[f'The most sales came from: ', html.B(top_country)]),
    html.Div
        (children=[html.I('***Created by FAS finance a.s.')])
    ],
    style={'text-align':'center', 'font-size':22}
)
if __name__ == '__main__':
    app.run_server(debug=True)