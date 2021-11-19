import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import functions as fn


#set wide page
st.set_page_config(layout="wide")

st.title('Visualizing Monthly Income and Expenses')
st.write('Welcome! This web app is created to help users gain a comprehensive picture of their financials through visualizations')
st.markdown('''
            1. Simply fill in the information in the boxes below. If some topics do not apply, just leave it at 0. (Don't worry, user data is not collected here)
            2. Plot and metrics are updated as the input response is changed
            3. The median and average metrics stated are based in Canada and in Canadian Dollars 
            
            ''')


# ----------- create boxes where user can input their reponses -----------------------------------
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader('Sources of income:')
    job = st.number_input('Job, net pay', min_value=0, max_value=100000000, value=50, step=1)
    business = st.number_input('Business', min_value=0, max_value=100000000, value=0, step=1)
    catpial_gains = st.number_input('Capital Gains or Dividends', min_value=0, max_value=100000000, value=0, step=1)
    rental_income = st.number_input('Rental Income', min_value=0, max_value=100000000, value=0, step=1)
    other_income = st.number_input('Other sources of income', min_value=0, max_value=100000000, value=0, step=1)
    
    st.subheader('Living Expenses:')
    mortgage = st.number_input('Rent / Mortgage', min_value=0, max_value=100000000, value=25, step=1)

with col2:
    st.subheader('Transportation:')
    car = st.number_input('Vehicle payment', min_value=0, max_value=100000000, value=0, step=1)
    gasoline = st.number_input('Gas / Electricity', min_value=0, max_value=100000000, value=0, step=1)
    bus = st.number_input('Bus Pass / Uber', min_value=0, max_value=100000000, value=0, step=1)
    
    st.subheader('Debt Repayment:')
    student_loans= st.number_input('Student Loans', min_value=0, max_value=100000000, value=0, step=1)
    credit_loans= st.number_input('Credit Card Loans', min_value=0, max_value=100000000, value=0, step=1)
    other_loans= st.number_input('Other Loans', min_value=0, max_value=100000000, value=0, step=1)
with col3:
    st.subheader("Grocery:")
    grocery = st.number_input('Grocery', min_value=0, max_value=100000000, value=0, step=1)
    
    st.subheader('Utility Bills:')
    internet = st.number_input('Internet', min_value=0, max_value=100000000, value=0, step=1)
    phone = st.number_input('Phone', min_value=0, max_value=100000000, value=0, step=1)
    electricity = st.number_input('Electricity', min_value=0, max_value=100000000, value=0, step=1)
    gas = st.number_input('Natural Gas', min_value=0, max_value=100000000, value=0, step=1)
    medical = st.number_input('Medical', min_value=0, max_value=100000000, value=0, step=1)
    utility_other = st.number_input('Others', min_value=0, max_value=100000000, value=0, step=1)
with col4:
    st.subheader('Leisure:')
    clothing = st.number_input('Clothing', min_value=0, max_value=100000000, value=0, step=1)
    dine_out = st.number_input('Dining Out', min_value=0, max_value=100000000, value=0, step=1)
    tv = st.number_input('TV Cable & Subscriptions', min_value=0, max_value=100000000, value=0, step=1)
    movie = st.number_input('Movies & Concerts', min_value=0, max_value=100000000, value=0, step=1)
    gym = st.number_input('Gym memberships', min_value=0, max_value=100000000, value=0, step=1)
    travel = st.number_input('Travelling', min_value=0, max_value=100000000, value=0, step=1)
    leisure_other = st.number_input('Other', min_value=0, max_value=100000000, value=0, step=1)

# ---------   Aggregating the income and expenses to larger topics ------------------------------

housing_expense = mortgage
transportation_expense = car + gasoline + bus
utility_expense = internet + phone + electricity + gas + medical + utility_other
grocery_expense = grocery
debt_repayment_expense = student_loans + credit_loans + other_loans
leisure_expense = clothing + dine_out + tv + movie + gym + travel + leisure_other

total_income = job + business + catpial_gains + rental_income + other_income 
total_expense = (housing_expense + transportation_expense + utility_expense + 
                 grocery_expense + debt_repayment_expense + leisure_expense)

savings_left = total_income -  total_expense



# warning message 
if savings_left < 0:
    st.warning('Note: Expenses are greater than total income')



source = [1,2,3,4,5, # incomes
          6,         # housing
          6,         # transportation
          6,         # utility_bills
          6,         # grocery
          6,         # debt_repayment
          6,         # leisure
          6]         # savings               


target = [6,6,6,6,6,
          7, 
          8,
          9,
          10,
          11, 
          12,
          13]

value = [3000,1000,500,100,200,  # 'Job', 'Business', 'Capital Gains + Dividenvds', 'Rental income', 'other'
          1500,                  #housing
          300,                   #transportation
          300,                   # utility bills
          500,                   # grocery
          300,                   #debt_repayment
          400,                   #leisure
          1500]                  #savings
   
label = ['placehold',
         'Job', 
         'Business', 
         'Capital Gains + Dividenvds', 
         'Rental income', 
         'Other income',
         'Budget',
         'Housing',
         'Transportation',
         'Utility bills',
         'Grocery',
         'Debt repayment',
         'Leisure',
         "Savings (what's left over)"]   


color_node = ['#40B5BC',
         '#40B5BC', 
         '#87CEEB', 
         '#8FD0CA', 
         '#7FFFD4', 
         '#3CB371',
         '#D3DACE',
         '#fde0e0', 
         '#f4c1c1',
         '#fdaaaa',
         '#E0BBE4',
         '#D291BC',
         '#FEC8D8',
         '#D6F1DF'] 

color_link = [
         '#5AC6C6', 
         '#87CEEB', 
         '#8FD0CA', 
         '#7FFFD4', 
         '#3CB371',
         '#fde0e0',
         '#f4c1c1',
         '#fdaaaa',
         '#E0BBE4',
         '#D291BC',
         '#FEC8D8',
         '#D6F1DF']

#update values from user input to plot
value = fn.update_input(job = job,
            business = business,
            catpial_gains = catpial_gains,
            rental_income = rental_income,
            other_income = other_income,
            housing_expense = housing_expense,
            transportation_expense = transportation_expense,
            utility_expense = utility_expense,
            grocery_expense = grocery_expense,
            debt_repayment_expense = debt_repayment_expense,
            leisure_expense = leisure_expense,
            savings_left = savings_left)


# Sankey plot
link = dict(source = source, target = target, value = value, color = color_link)
node = dict(label = label, pad=25, thickness= 15, color = color_node)
data = go.Sankey(link =link, node=node)
fig = go.Figure(data)

st.plotly_chart(fig, use_container_width = True)


# comparison metrics
average_income = 62900/12
average_housing = 1800
average_grocery = 214
average_savings_rate = 14.2

income_comparison = round(((total_income - average_income) / average_income)*100,2)
house_comparison = round(((housing_expense - average_housing) / average_housing)*100,2)
grocery_comparison = round(((grocery_expense - average_grocery) / average_grocery)*100,2)
saving_comparison = round((((savings_left / total_income)*100 - average_savings_rate) / average_savings_rate)*100, 2)
    

col1, col2, col3, col4 = st.columns(4)
col1.metric("Median Canadian monthly income is", 
            "$ 5241", 
            str(income_comparison) + "% " + str(fn.high_low(income_comparison)) + ' than the median')
col2.metric("Average Canadian home rent is", 
            '$ ' + str(average_housing), 
            str(house_comparison) + "% " + str(fn.high_low(income_comparison)) + ' than the average', delta_color= 'inverse')
col3.metric("Average Canadian monthly grocery cost is", 
            '$ ' + str(average_grocery), 
            str(grocery_comparison) + "% " + str(fn.high_low(grocery_comparison)) + ' than the average', delta_color= 'inverse')
col4.metric("Average percentage of income that goes to savings is", 
            str(average_savings_rate) + "%", 
            str(saving_comparison) + "% " + str(fn.high_low(saving_comparison)) + ' than the average')


# pie charts
col1, col2 = st.columns(2)
with col1:
    st.subheader("Distribution of Incomes")
    st.plotly_chart(fn.pie_chart('income', label, value), use_container_width = True)
with col2:
    st.subheader("Distribution of Expenses")
    st.plotly_chart(fn.pie_chart('expense', label, value), use_container_width = True)
    

