import pandas as pd
import openpyxl
import plotly.graph_objects as go
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime

# Convert .xlsx to .csv
pd.read_excel('clients.xlsx', engine='openpyxl').to_csv('clients.csv', index = False)
pd.read_excel('requests.xlsx', engine='openpyxl').to_csv('requests.csv', index = False)
clients = pd.read_csv('clients.csv')
requests = pd.read_csv('requests.csv')

# Create graphs that shows rate of Individual vs Legal clients
group_by_type = clients.groupby(['Risk group','Type']).size().unstack(fill_value=0).reset_index()
group_by_type = group_by_type.sort_values(by='Risk group', ascending=False)

#print(group_by_type)
graph_by_type = px.bar(group_by_type, x='Risk group', y=['Individual Entity', 'Legal Entity'],
                       color_discrete_map={'Individual Entity':'tomato', 'Legal Entity':'sienna'},
                       labels={'value':'Number of Clients', 'Risk group': 'Type of risk group'},
                       title='Count of Legal vs Individual')
graph_by_type.show()