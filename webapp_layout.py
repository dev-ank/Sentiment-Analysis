'''

UI designing for the web application

'''


import emoji
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash
import plotly.express as px
from app import get_etsy_labels



PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

count_list=get_etsy_labels()



tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div(html.H1("A Pie-Chart showing the pictorial representation of number of Positive and Negative reviews", className="display-5"),style={'padding': '85px'}),
            dcc.Graph(id="pie-chart",figure=px.pie(values=count_list,names=['Positive Reviews','Negative Reviews'])),
            html.P(f'This Pie-Chart is generated from the reviews scraped from www.etsy.com . This Pie-Chart depicts the percentage of Positive and Negative Reviews. This gives an overall idea whether people are liking the products on the website or not. Hover over the Pie-Chart to get exact numbers.',style={'padding': '78px','font-family': 'courier'}),
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div(html.H1("WordCloud showing the most frequent words on the website", className="display-5"),style={'padding': '85px'}),
            html.Div(html.Img(id="image_wc"),style={'padding-left':'30%'}),
            html.P(f'This wordcloud is generated from the reviews scraped from www.etsy.com . This wordcloud contains 500 most frequent words in those reviews. This gives an overall idea whether people are liking the products on the website or not. All the words present are mostly adjectives. Stopwords have been removed before generating the wordcloud.',style={'padding': '78px','font-family': 'courier'}),
        ]
    ),
    className="mt-3",
)

tab3_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div([
                html.Div(html.H1("Check the sentiment of any sentence with the exact sentiment score", className="display-5"),style={'padding': '30px'}),
                
                dcc.Textarea(
                    id = 'textarea_review',
                    placeholder = 'Enter the review here.....',
                    style = {'width':'100%', 'height':100,'float':'30px'}
                    ),
                
                html.P('Note: The lower the score, more negative the sentence will be and vice-versa.'),
    
                dbc.Button(
                    children = 'Get Result',
                    id = 'button_review',
                    color = 'success',
                    className="mr-1"
                    
                    ),
                dbc.Popover(
                    children=None,
                    id="result",
                    target="button_review",
                    trigger="legacy",
                    ),
                
    
                    ])
        ]
    ),
    className="mt-3",
)







layout = html.Div([
    
    dbc.Navbar(
       
    [
        html.A(
            
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("MySentimentAnalysis", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
                                
                
            ),
            href="http://127.0.0.1:8050/",
        ),
        
    ],
    color="dark",
    dark=True,
    
    
),
    
    
    
    dbc.Row(
            [
                dbc.Col(
                dbc.Button("About", color="info", className="ml-2",id="collapse-button"),
                width="auto",
                        ),
        
                dbc.Collapse(
                dbc.Card("This Web Application currently has 3 sections. The First SECTION depicts a Pie-Chart of the reviews scraped from an ecommerce website called etsy.com. These reviews has been classified by as POSITIVE or NEGATIVE based on previosly trained Neural Network. The SECOND SECTION shows the Wordclould generated from the same reviews. It shows the top 500 most used words in those reviews. LAST SECTION has a Sentiment Analysis part which classifies any sentence into POSITIVE or NEGATIVE one alongwith the sentiment score."),
                id="collapse")
            ],
            
            
            no_gutters=True,
            style={'padding-top':'2%'}
            ),
    
   

    dbc.Container(
            [
                
                html.Div(html.H1("Analyse the sentiment and get Insights!", className="display-3"),style={'padding': '30px'}),
                
                html.Div([html.P(
                    f"This is a real time application which classifies any sentence into positive{emoji.emojize(':thumbsup:',use_aliases=True)} or negative{emoji.emojize(':thumbsdown:',use_aliases=True)}.",
                    className="lead",
                    style={'padding-left':'3%'}
                ),
                html.P(
                    f"This application can also generate some insights{emoji.emojize(':chart_with_upwards_trend:',use_aliases=True)} on the reviews of an ecommerce website.",
                    className="lead",
                    style={'padding-left':'3%'}
                ),
                html.P(
                    f"Those insights could be useful to conclude the nature{emoji.emojize(':smiley:',use_aliases=True)} of reviews and words present on the website.",
                    className="lead",
                    style={'padding-left':'3%'}
                )])
                
            ],
            style={'float': 'top','margin': '50px'},
            fluid=True,
            
            
        ),
    
    dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Pie Chart"),
        dbc.Tab(tab2_content, label="Word Cloud"),
        dbc.Tab(tab3_content, label="Sentiment Analysis"),
        
    ],
    style={'float': 'top','margin': '10px'}
),
    
    
    html.Footer( 
                 [dbc.NavbarBrand("Connect with me-", className="ml-2",style={'color':'white','padding-left':'3.5%'}),
                 dbc.Row(dcc.Link(children='Github',href='https://github.com/dev-ank',style={'padding-left':'5%'})),
                 dbc.Row(dcc.Link(children='LinkedIn',href='https://www.linkedin.com/in/ankit-upadhyay-140697/',style={'padding-left':'5%'})),
                 dbc.Row([dcc.Link(children='Kaggle',href='https://www.kaggle.com/ankitupadhyay14',style={'padding-left':'5%'}),html.P('This website is for educational purpose only.',style={'color':'white','padding-left':'30%'})]),
                 
                 ],style={'background-color':'#333'}
                 )
    
])