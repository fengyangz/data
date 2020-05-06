#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

                         


# In[ ]:


external_stylesheets = ['https://usfmumaanalyticsteam.github.io/learn.css']


# In[ ]:


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# In[ ]:


df = pd.read_csv('https://github.com/fengyangz/data/blob/master/AC-items.csv')
df2 = pd.read_csv('https://github.com/fengyangz/data/blob/master/AC-critic.csv')


# In[ ]:


def generate_table(dataframe, max_rows=16):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


# In[ ]:


app.layout=html.Div([ html.H1('Data Visualization for Story Telling'),
    html.Div([
    html.P('About the New version of Animal Crossing'),]),
    html.Div([html.Table(style={'width':'100%'},children= html.Tr(children=[html.Th(style={'width':'30%'},children=[html.H3('Grades of Animal Crossing')]),
    
    


# In[ ]:


html.Th(style={'width':'70%'},children=[html.H3('Categories in Animal Crossing')])]),
        
html.Tr(children=[html.Td(children=[dcc.Graph(id='example-graph',figure={'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'grade'},{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'date'},],
'layout': {'title': 'Grades from Game Critics'}})]),

html.Td(children=[dcc.Graph(id='ac-cate',
                                figure={
                                    'data': [
                                        dict(
                                            x=df[df['continent'] == i]['gdp per capita'],
                                            y=df[df['continent'] == i]['life expectancy'],
                                            text=df[df['continent'] == i]['country'],
                                            mode='markers',
                                            opacity=0.7,
                                            marker={
                                                'size': 15,
                                                'line': {'width': 0.5, 'color': 'white'}
                                            },
                                            name=i
                                        ) for i in df.continent.unique()
                                    ],
                                    'layout': dict(
                                        xaxis={'type': 'log', 'title': 'category'},
                                        yaxis={'title': 'num_id'},
                                        margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                                        legend={'x': 0, 'y': 1},
                                        hovermode='closest'
                                    ), 'layout': {
                                            'title': 'Animal Crossing Categories'}
                                   
                                    })
                           
                                
                             ]
                         
                         )
                     
                     ]
                 
                 )     
              



if __name__ == '__main__':

    app.run_server(debug=False)


# In[ ]:





# In[ ]:




