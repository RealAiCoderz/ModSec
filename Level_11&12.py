import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

# Load the provided dataframe
data = pd.read_csv("main_sales.csv")

# Convert 'Order Date' to datetime format
data['Order Date'] = pd.to_datetime(data['Order Date'])

st.title('Sales Visualization')

# Sidebar for selecting visualization type
visualization_type = st.sidebar.selectbox(
    'Select Visualization Type',
    ['Line Plot', 'Scatter Plot', 'Bar Chart', 'Pie Chart', 'Heatmap'],
    key='visualization_type'  # Add a unique key
)

# Helper function to filter data
def filter_data(data, category=None, time_period=None):
    filtered_data = data.copy()
    if category:
        filtered_data = filtered_data[filtered_data['Product Category'] == category]
    if time_period:
        filtered_data = filtered_data[(filtered_data['Order Date'] >= pd.to_datetime(time_period[0])) & (filtered_data['Order Date'] <= pd.to_datetime(time_period[1]))]
    return filtered_data

# Line Plot for Monthly Average Sales
if visualization_type == 'Line Plot':
    st.sidebar.subheader('Filter Options')
    selected_category = st.sidebar.selectbox('Select Product Category', data['Product Category'].unique(), key='lineplot_category')  # Add a unique key
    
    # Filter the data based on selected category
    filtered_data = filter_data(data, selected_category)
    
    # Resample the data to monthly frequency and calculate average sales for each month
    monthly_average_sales = filtered_data.resample('M', on='Order Date')['Sales'].mean().reset_index()
    
    # Generate line plot for monthly average sales
    fig = px.line(monthly_average_sales, x='Order Date', y='Sales', title=f'Monthly Average Sales Trends for {selected_category}')
    
    # Display the line plot
    st.plotly_chart(fig)

# Scatter Plot
if visualization_type == 'Scatter Plot':
    st.sidebar.subheader('Filter Options')
    selected_category1 = st.sidebar.selectbox('Select Product Category', data['Product Category'].unique(), key='scatterplot_category')  # Unique key
    
    # Filter the data based on selected category
    filtered_data1 = filter_data(data, selected_category1)
    
    # Generate scatter plot
    fig1 = px.scatter(filtered_data1, x='Sales', y='Profit', color='Customer Segment', size='Discount', hover_name='Product Name', title=f'Sales vs Profit for {selected_category1}',
                     labels={'Sales': 'Sales', 'Profit': 'Profit', 'Customer Segment': 'Customer Segment', 'Discount': 'Discount'})
    
    # Add hover functionality and interactive legends
    fig1.update_traces(mode='markers', marker=dict(line=dict(width=1, color='DarkSlateGrey')), selector=dict(type='scatter', mode='markers'))
    fig1.update_layout(legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
                      hovermode='closest', hoverlabel=dict(bgcolor='white', font_size=12), showlegend=True)
    
    # Display the scatter plot
    st.plotly_chart(fig1)

# Bar Chart
if visualization_type == 'Bar Chart':
    st.sidebar.subheader('Filter Options')
    selected_category2 = st.sidebar.selectbox('Select Product Category', data['Product Category'].unique(), key='barchart_category')  # Unique key
    
    # Filter the data based on selected category
    filtered_data2 = filter_data(data, selected_category2)
    
    # Group by region and sum the sales
    sales_by_region = filtered_data2.groupby('Region')['Sales'].sum().reset_index()
    
    # Generate bar chart
    fig2 = px.bar(sales_by_region, x='Region', y='Sales', title=f'Sales Distribution by Region for {selected_category2}',
                 labels={'Sales': 'Total Sales', 'Region': 'Region'})
    
    # Display the bar chart
    st.plotly_chart(fig2)
# Pie Chart
if visualization_type == 'Pie Chart':
    # Group by product category and calculate total sales
    sales_by_category = data.groupby('Product Category')['Sales'].sum().reset_index()
    
    # Generate pie chart
    fig = px.pie(sales_by_category, values='Sales', names='Product Category', title='Sales Distribution by Product Category')
    
    # Display the pie chart
    st.plotly_chart(fig)

# Heatmap
if visualization_type == 'Heatmap':
    # Group by region and resample to monthly frequency
    sales_heatmap_data = data.groupby([pd.Grouper(key='Order Date', freq='M'), 'Region'])['Sales'].sum().reset_index()
    
    # Pivot the data to have regions as rows and months as columns
    sales_heatmap_pivot = sales_heatmap_data.pivot_table(index='Region', columns='Order Date', values='Sales', aggfunc='sum')
    
    # Generate heatmap
    fig = px.imshow(sales_heatmap_pivot, labels=dict(x='Date', y='Region', color='Sales'), x=sales_heatmap_pivot.columns, y=sales_heatmap_pivot.index)
    
    # Add title
    fig.update_layout(title='Sales Heatmap by Region')
    
    # Add zoom and pan functionality
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)
    
    # Allow users to adjust color maps
    color_map = st.sidebar.select_slider('Select Color Map', options=['Viridis', 'Plasma', 'Inferno', 'Magma'], key='heatmap_color_map') 
    
    # Update color scale based on user selection
    fig.update_layout(coloraxis_colorscale=color_map)
    
    # Allow users to adjust heatmap resolution
    heatmap_resolution = st.sidebar.slider('Select Heatmap Resolution', min_value=4, max_value=20, value=10, key='heatmap_resolution')
    
    # Update heatmap resolution
    fig.update_layout(xaxis=dict(nticks=heatmap_resolution), yaxis=dict(nticks=heatmap_resolution))
    
    # Display the heatmap
    st.plotly_chart(fig)