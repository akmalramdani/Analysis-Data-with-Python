import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
from babel.numbers import format_currency
sns.set(style='white')
import streamlit as st
from scipy.stats import linregress
 
with st.sidebar:
    
    st.text('Berikan Nilai Terhadap Project Ini')
    
    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=10, value=(0,10)
    )
    st.write('Values:', values)
#Load Data
day_df = pd.read_csv("Dashboard/day.csv")
hour_df= pd.read_csv("Dashboard/hour.csv")

#Grafik 1

# Print columns to check names
st.write("Columns in day_df:", day_df.columns.tolist())

# Data Preparation
# Ensure the 'cnt' column is used if 'count' is not found
count_column = 'count' if 'count' in day_df.columns else 'cnt'
season_rental = day_df[[count_column, 'season']].groupby(by='season').sum().reset_index()
season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
season_rental['season'] = season_rental['season'].map(season_map)
season_rental.sort_values(by=count_column, ascending=False, inplace=True)

# Plotting
st.write("### Total Rentals by Season")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=season_rental, y='season', x=count_column, palette='coolwarm', ax=ax)
ax.set_title("Total Rentals by Season", fontsize=20)
ax.set_xlabel("Number of Rentals", fontsize=14)
ax.set_ylabel("Season", fontsize=14)

# Add data labels
for index, value in enumerate(season_rental[count_column]):
    ax.text(value, index, str(value), va='center', ha='left', fontsize=12)

st.pyplot(fig)

#Grafik 2
# Data Preparation
season_rental = pd.DataFrame({
    'season': ['Spring', 'Summer', 'Autumn', 'Winter'],
    'count': [100, 200, 150, 180]
})

# Function to add labels
def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center', va='bottom')

# Plotting
st.write("### Number of Rentals per Season")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='count', data=season_rental, palette='coolwarm', ax=ax)

# Adding labels
addlabels(season_rental['season'], season_rental['count'])

# Title and labels
ax.set_title("Number of Rentals per Season", fontsize=20)
ax.set_xlabel("Season", fontsize=14)
ax.set_ylabel("Number of Rentals", fontsize=14)

# Show plot in Streamlit
st.pyplot(fig)

#Grafik 3

# Data
season_rental = {
    'season': ['Spring', 'Summer', 'Autumn', 'Winter'],
    'normal_count': [80, 150, 100, 120],
    'premium_count': [20, 50, 50, 60]
}

# Convert dictionary to DataFrame
season_rental_df = pd.DataFrame(season_rental)

# Reshape data for clustering
season_rental_long = season_rental_df.melt(id_vars='season', var_name='type', value_name='count')

# Function to add labels
def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center', va='bottom')

# Plotting
st.write("### Number of Rentals per Season by Type")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='count', hue='type', data=season_rental_long, palette='coolwarm', ax=ax)

# Title and labels
ax.set_title("Number of Rentals per Season by Type", fontsize=20)
ax.set_xlabel("Season", fontsize=14)
ax.set_ylabel("Number of Rentals", fontsize=14)

# Add legend
ax.legend(title='Type')

# Show plot in Streamlit
st.pyplot(fig)

#Grafik 4

# Data Preparation
monthly_2011_df = day_df[day_df['yr'] == 0][['mnth', 'cnt']].groupby('mnth').sum()
monthly_2011_df = monthly_2011_df.reset_index()

# Plotting
st.write("### Number of Rentals per Month in 2011")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=monthly_2011_df, x="mnth", y="cnt", color='blue', ci=None, ax=ax)

# Title and labels
ax.set_title("Number of Rentals per Month", fontsize=20, pad=20)
ax.set_xlabel("Month", fontsize=14, labelpad=15)
ax.set_ylabel("Number of Rentals", fontsize=14, labelpad=15)
ax.set_xticks(range(12))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax.grid(True, linestyle='--', alpha=0.7)

# Tambahkan label pada setiap batang
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                xytext=(0, 10),
                textcoords='offset points',
                fontsize=10)

plt.tight_layout()
st.pyplot(fig)

#Grafik 5

# Data Preparation
monthly_2012_df = day_df[day_df['yr'] == 1][['mnth', 'cnt']].groupby('mnth').sum()
monthly_2012_df = monthly_2012_df.reset_index()

# Plotting
st.write("### Number of Rentals per Month in 2012")
fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(monthly_2012_df["mnth"], monthly_2012_df["cnt"], color='red')

# Title and labels
ax.set_title("Number of Rentals per Month (2012)", loc="center", fontsize=20)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Number of Rentals", fontsize=14)
ax.set_xticks(range(12))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax.grid(True, color='gray', linestyle='--', linewidth=0.5)  # Set grid color

# Add Label BarChart
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), va='bottom', fontsize=10, ha='center')

plt.tight_layout()
st.pyplot(fig)

#Grafik 6

# Data Preparation
workingday_rental = day_df[['workingday', 'casual', 'registered', 'cnt']].groupby(by='workingday').sum().reset_index()

# Plotting
st.write("### Number of Rentals on Working Days vs Holidays")
fig, ax = plt.subplots(figsize=(10, 6))
workingday_rental.plot(kind='bar', x='workingday', y=['casual', 'registered', 'cnt'], color=['blue', 'red', 'green'], ax=ax)

# Annotate bars
for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Labels and title
ax.set_xlabel('Holiday')
ax.set_ylabel('Total')
ax.set_title('Number of Rentals on Working Days vs Holidays')
ax.set_xticks([0, 1])
ax.set_xticklabels(['Hari Libur', 'Hari Kerja'], rotation=0)
ax.legend(['Casual', 'Registered', 'Total'])

plt.tight_layout()
st.pyplot(fig)

#grafik 7

# Data Preparation
holiday_rental = day_df[['holiday', 'casual', 'registered', 'cnt']].groupby(by='holiday').sum().reset_index()

# Plotting
st.write("### Number of Rentals on Holidays")
fig, ax = plt.subplots(figsize=(10, 6))
holiday_rental.plot(kind='bar', x='holiday', y=['casual', 'registered', 'cnt'],
                    color=['green', 'yellow', 'red'], ax=ax)

# Annotate bars
for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Labels and title
ax.set_xlabel('Holiday', fontsize=14)
ax.set_ylabel('Total', fontsize=14)
ax.set_title('Number of Rentals on Holidays', fontsize=18)
ax.set_xticks([0, 1])
ax.set_xticklabels(['Tidak Libur', 'Libur'], rotation=0)
ax.legend(['Casual', 'Registered', 'Total'], fontsize=12)
ax.set_ylim(0, holiday_rental[['casual', 'registered', 'cnt']].values.max() * 1.2)  # Adjust y-axis range

plt.tight_layout()
st.pyplot(fig)

#Grafik 8 (Analisis Lanjutan)

# Calculate regression parameters
slope, intercept, r_value, p_value, std_err = linregress(day_df['cnt'], day_df['registered'])

# Calculate R^2 value
r_squared = r_value**2

# Plot scatter plot and regression line
st.write("### Scatter Plot with Regression Line")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='cnt', y='registered', data=day_df, ax=ax, color='blue')
sns.regplot(x='cnt', y='registered', data=day_df, scatter=False, color='red', ax=ax)

# Set labels
ax.set_xlabel('Count')
ax.set_ylabel('Registered')

# Add R^2 text to the plot
ax.text(0.05, 0.95, f'$R^2 = {r_squared:.3f}$', transform=ax.transAxes, fontsize=14,
        verticalalignment='top')

plt.tight_layout()
st.pyplot(fig)

