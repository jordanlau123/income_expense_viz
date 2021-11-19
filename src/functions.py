import pandas as pd
import numpy as np
import plotly.graph_objects as go


def pie_chart(type, label_df, value_df):
    """
    pie chart to visualize distribution of income or expenses
    """
    
    layout = go.Layout(
        margin=go.layout.Margin(
        l=50, #left margin
        r=50, #right margin
        b=50, #bottom margin
        t=50,  #top margin
        pad=0
        )
    )
    if type == 'income':
        color = ['#40B5BC', '#87CEEB', '#8FD0CA', '#7FFFD4', '#3CB371']
        
        labels = label_df[1:6]
        values = value_df[:6]
        
    else: 
        color = ['#fde0e0',
                 '#f4c1c1',
                 '#fdaaaa',
                 '#E0BBE4',
                 '#D291BC',
                 '#FEC8D8',
                 '#D6F1DF']
        
        labels = label_df[7:]
        values = value_df[5:]
        
    fig = go.Figure(data=[go.Pie(labels=labels, 
                                 values=values, 
                                 hole=.3, marker_colors= color
                               )], layout = layout)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(showlegend=False, autosize=True)
        
    return fig

def high_low(input, inverse=False):
    """
    return 'higher' or 'lower' based on the amount. Used for metric comparison boxes
    """
    if input > 0 and inverse == False:
        return 'higher'
    if input > 0 and inverse == True:
        return "lower"
    if input < 0 and inverse == True:
        return "higher"
    else:
        return 'lower'
    
    
def update_input(job,
            business,
            catpial_gains,
            rental_income,
            other_income,
            housing_expense,
            transportation_expense,
            utility_expense,
            grocery_expense,
            debt_repayment_expense,
            leisure_expense,
            savings_left):
    """
    updates values when user changes their inputs 
    """
    value = [0] * 12

    value[0] = job
    value[1] = business
    value[2] = catpial_gains
    value[3] = rental_income
    value[4] = other_income
    value[5] =  housing_expense
    value[6] = transportation_expense
    value[7] = utility_expense
    value[8] = grocery_expense
    value[9] = debt_repayment_expense
    value[10] = leisure_expense
    value[11] = savings_left
    
    return value