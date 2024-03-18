import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
st.title("Sales Outlook Dashboard")

# Load the sales data
sales_data = pd.read_csv("merged_sales.csv")
sales_data['city'] = sales_data['address'].str.split(',').str[-2].str.strip()

st.write("Time Series")
# convert date to datetime
sales_data['date'] = pd.to_datetime(sales_data['date'],format='%d-%m-%Y')
print(type(sales_data['date'].min()))

sales_data['date'] = sales_data['date'].dt.strftime('%m-%d-%Y')
sales_data['date'] = pd.to_datetime(sales_data['date'],format='%m-%d-%Y')
sales_data['date'] = sales_data['date'].dt.date
# Create a slider for selecting the date range
#date_range = st.slider("Select Date Range", min_value=sales_data['date'].min(), max_value=sales_data['date'].max())
start_date, end_date = st.date_input("Select Date Range", [sales_data['date'].min(), sales_data['date'].max()])
date_range = [start_date, end_date]
# Filter the sales data based on the selected date range
filtered_data = sales_data[(sales_data['date'] >= date_range[0]) & (sales_data['date'] <= date_range[1])]

# want checkbox for category
# Create a checkbox for selecting the category
categories = st.multiselect("Select Categories", options=sales_data['category'].unique())

# Filter the sales data based on the selected category
filtered_data = filtered_data[filtered_data['category'].isin(categories)]

# Group the filtered data by category and date, and calculate the sum of sales_amount
grouped_data = filtered_data.groupby(['category', 'date']).sum().reset_index()

# Create an interactive line plot using streamlit

st.line_chart(grouped_data, x='date', y='sales_amount', color='category')

# Create a scatter plot using streamlit
st.write("Scatter Plot")

# Create a scatter plot between different numeric variables
# selct x and y from dropdown menu
x_col = st.selectbox("Select X", options=filtered_data.columns)
y_col = st.selectbox("Select Y", options=filtered_data.columns)

scatter_plot = alt.Chart(sales_data).mark_circle(size=60).encode(
    x=x_col,
    y=y_col,
    tooltip=[x_col, y_col,'category']
)
# Display the chart in Streamlit
st.altair_chart(scatter_plot, use_container_width=True)

# Create a barchart using streamlit
st.write("Bar Chart")

# dropdown to select category or region
group_by = st.selectbox("Group By", options=['category', 'region_name'])

# Group the sales data by category or region and calculate the sum of sales_amount
grouped_data = sales_data.groupby(group_by).agg( "sales_amount").sum().reset_index()

# Create an interactive bar chart using streamlit
st.bar_chart(grouped_data, x=group_by, y='sales_amount')

# Create a pie chart of total sales_amount over different categories or city
st.write("Pie Chart")
chart_type = st.selectbox("Select Chart Type", options=['Categories', 'City'])
if chart_type == 'Categories':
    pie_chart_data = sales_data.groupby('category')['sales_amount'].sum().reset_index()
    st.plotly_chart(px.pie(pie_chart_data, values='sales_amount', names='category', title='Sales Amount by Category'))
elif chart_type == 'City':
    pie_chart_data = sales_data.groupby('city')['sales_amount'].sum().reset_index()
    st.plotly_chart(px.pie(pie_chart_data, values='sales_amount', names='city', title='Sales Amount by City'))

# create heatmap based on sales amount and region
# Create a heatmap based on sales amount and region
st.write("Heatmap")
group_by_type = st.selectbox("Select Chart Type", options=['region_name', 'city'])

heatmap_data = sales_data.groupby([group_by_type, 'category']).agg('sales_amount').sum().reset_index()

heatmap = alt.Chart(heatmap_data).mark_rect().encode(
    x=group_by_type,
    y='category',
    color='sales_amount'
)
st.altair_chart(heatmap, use_container_width=True)