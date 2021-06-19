'''
Entry point for all the code for this web application

'''

import emoji
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash
from io import BytesIO
import base64
import nltk
from webapp_layout import *
from webapp_functions import load_model,check_review,open_browser,get_freq_words,plot_cloud,get_etsy_labels



nltk.download('stopwords')
external_stylesheets=[dbc.themes.BOOTSTRAP,'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)





     


@app.callback(
    Output( 'result'   , 'children'),
    Input( 'button_review'    ,  'n_clicks'    ),
    State( 'textarea_review'  ,   'value'  )
    )
def update_app_ui_2(n_clicks,value):

    print("Data Type = ", str(type(n_clicks)))
    print("Value = ", str(n_clicks))


    print("Data Type = ", str(type(value)))
    print("Value = ", str(value))


    if (n_clicks > 0):
        
        res_acc=(check_review(value)[0][0])*100
        res_acc=f'{res_acc:.2f}%.'
        
        response =check_review(value)
        print(response)
        
        if (response[0]<0.8):
            result = 'NEGATIVE'
            feel=emoji.emojize(':thumbsdown:',use_aliases=True)
            result=f'This is a {result} sentence with a sentiment score of {res_acc} {feel}'
        elif (response[0]>=0.8 ):
            result = 'POSITIVE'
            feel=emoji.emojize(':thumbsup:',use_aliases=True)
            result=f'This is a {result} sentence with a sentiment score of {res_acc} {feel}'
        else:
            result = 'Unknown'
            
        
        return result
        
    else:
        return ""
    
    
    
    
    
word_list=get_freq_words()    
    
@app.callback(Output('image_wc', 'src'),Input('image_wc', 'id'))
def make_image(b):
    img = BytesIO()
    plot_cloud(word_list).save(img, format='PNG')
    
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())
    



@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open




def main():
    print("Start of project")
    load_model()
    open_browser()
    
    
    global scrappedReviews
    global project_name
    global app
    
    project_name = "Sentiment Analysis with Insights"
    
    
    
    app.title = project_name
    app.layout = layout
    
    app.run_server(debug=False)
    
    
    
    print("End of my project")
    project_name = None
    scrappedReviews = None
    app = None
    
        

if __name__ == '__main__':
    main()
    
