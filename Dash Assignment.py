#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# Uses an External Stylesheet
# Use a css file from your GitHub Pages site 
external_stylesheets = ['https://github.com/fengyangz/data/blob/master/data']

# Creates the app to instantiate the content for the Dashboard and use the external_stylesheets
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Use a csv dataset from a repository in your GitHub account. Use the Raw URL to expose the data to the Python dataframe
df = pd.read_csv('https://github.com/fengyangz/data/blob/master/AC-critic.csv')
df2 = pd.read_csv('https://github.com/fengyangz/data/blob/master/AC-user_reviews.csv')


# Custom function used to generate a data table from a dataframe
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


# Add content to the app layout
# Begin all content DIV
app.layout=html.Div([
   # Add your HTML tags to the content - notice a comma is added between HTML elements
   html.H1('Data Visualization for Story Telling'),
   html.Div([
       html.P('The rate of Animal crossing'),
   ]),
   # Begin of DIV surrounding both Tables
   html.Div([
   # Begin of First Table
   html.Table(style={'width':'100%'},
              # Begin of Table children
              children=[
                  #######################################################################
                  # Begin of First Tr
                html.Tr(
                    #Begin Tr children
                    children=[
                        # Begin Th
                        
                        html.Th(style={'width':'30%'},
                            # Begin Th children
                            children=[
                                html.H3('Review from Game Critics')
                            # End of Th children   
                            ]
                        
                        # End of Th - Notice a comma is placed here to separate the next Th
                        ),
                        # Begin of Th
                        html.Th(style={'width':'70%'},
                            # Begin of Th children
                            children=[
                                html.H3('Critics review')
                            # End of Th children    
                            ]
                        
                        # End of Th
                        )
                        
                    # End of Tr children    
                    ]
                # End of First Tr - Notice a comma is placed here to separate the next Tr
                ),
                   # Begin First Tr
                html.Tr(
                    #Begin Tr children
                    children=[
                        # Begin Th
                        html.Th(style={'width':'30%'},
                            # Begin Th children
                            children=[
                                html.H3('Review from users')
                            # End of Th children   
                            ]
                        
                        # End of Th - Notice a comma is placed here to separate the next Th
                        ),
                        #Begin of Th
                        html.Th(style={'width':'10%'},
                            # Begin of Th children
                                children=[
                                # Nothing to display here, just a place holder in the column
                                html.H2('')
                                # End of Th children    
                                ]
                            # End of Th - Notice a comma is placed here to separate the next Th
                        ),
                        # Begin of Th
                        html.Th(style={'width':'70%'},
                            # Begin of Th children
                            children=[        
                                   html.H3('User reviews')
                                                              
                            # End of Th children    
                            ]
                        # End of Th
                        )
                    # End of Tr children    
                    ]
                # End of First Tr
                ),
               #########################################################################                   
              #End of Table Children    
              ]
             # End of First Table - Notice a comma is placed here to separate the next Table
             )
       # End of DIV surrounding both Tables
   ]),
              
# End of all content DIV
])
   # Run the app on the web server
if __name__ == '__main__':
   # Set debug to False. Some configurations are not setup for Debug
   app.run_server(debug=False)


# In[ ]:




