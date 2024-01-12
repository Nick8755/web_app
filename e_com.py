import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime

e_com = pd.read_csv('e_com.csv', encoding='latin1')
ecom_data = e_com.drop('Description', axis=1)
ecom_data['InvoiceDate'] = pd.to_datetime(ecom_data['InvoiceDate'])
ecom_data['Total'] = ecom_data['Quantity']*ecom_data['UnitPrice']
ecom_data.to_csv('ecom_data.csv', index=False)
sales_by_date = ecom_data.groupby(ecom_data['InvoiceDate'].dt.date)['Total'].sum().reset_index()
fig = px.line(data_frame=sales_by_date, x='InvoiceDate', y='Total', title='Total $ per day')
fig.update_xaxes(title_text='Date')
fig.update_yaxes(title_text='Total sales ($)')
fig.show()
