import streamlit as st
import pandas as pd
import plotly.express as px

# ---- Set Page Config ----
st.set_page_config(page_title="Routelligent Dashboard", layout="wide")

# ---- Mock Data ----
vehicle_data = {
    "Fuel Remaining (L)": [20, 18, 15, 13, 10],
    "Distance Covered (km)": [50, 120, 190, 260, 330],
    "Fuel Used (L)": [5, 7, 8, 6, 7],
    "Trip Time (hrs)": [1, 2, 3, 4, 5],
    "Date": ["2024-12-23", "2024-12-24", "2024-12-25", "2024-12-26", "2024-12-27"]
}

# Create DataFrame
df = pd.DataFrame(vehicle_data)

# ---- Inject Custom CSS for Styling ----
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #e0f7fa, #80deea); /* Soft blue gradient */
        color: #000000; /* Black text */
    }
    h1, h2, h3 {
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        color: #004d40; /* Teal shade for titles */
        text-align: center; /* Center title */
    }
    .stMetric-label {
        font-size: 1.2em;
        color: #004d40;
    }
    .stMetric-value {
        font-size: 2em;
        color: #004d40;
    }
    .stDataFrame table {
        font-family: 'Arial', sans-serif;
        color: #000000; /* Black text */
        background-color: #ffffff; /* White background */
    }
    .travel-info {
        font-size: 1.5em;
        font-weight: bold;
        color: #004d40; /* Teal for travel message */
        background-color: #e0f2f1; /* Light teal background */
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    footer {
        font-size: 0.9em;
        text-align: center;
        margin-top: 20px;
        color: #004d40;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Layout ----
st.markdown("# Routelligent Dashboard 🚗🗺️", unsafe_allow_html=True)

# ---- Key Performance Indicators (KPIs) ----
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Current Fuel Remaining", value=f"{df['Fuel Remaining (L)'].iloc[-1]} L")
with col2:
    st.metric(label="Total Distance Covered", value=f"{sum(df['Distance Covered (km)'])} km")
with col3:
    st.metric(label="Fuel Used Today", value=f"{df['Fuel Used (L)'].iloc[-1]} L")

# ---- Performance Metrics Grid ----
st.markdown("### Performance Metrics Over Time")
col1, col2 = st.columns(2)

# Line Chart - Distance Covered
fig_distance = px.line(
    df,
    x="Date",
    y="Distance Covered (km)",
    title="Distance Covered Over Time",
    markers=True,
    template="simple_white",
    color_discrete_sequence=["#1f77b4"]  # Soft blue line
)
fig_distance.update_layout(font=dict(family="Arial", size=14), title_font=dict(size=18))
col1.plotly_chart(fig_distance, use_container_width=True)

# Bar Chart - Fuel Used
fig_fuel = px.bar(
    df,
    x="Date",
    y="Fuel Used (L)",
    title="Fuel Usage Over Time",
    color="Fuel Used (L)",
    template="simple_white",
    color_continuous_scale=px.colors.sequential.Viridis  # Visible gradient
)
fig_fuel.update_layout(font=dict(family="Arial", size=14), title_font=dict(size=18))
col2.plotly_chart(fig_fuel, use_container_width=True)

# ---- Pie Chart ----
st.markdown("### Fuel Distribution")
fuel_data = {"Fuel Remaining": df["Fuel Remaining (L)"].iloc[-1], "Fuel Used": sum(df["Fuel Used (L)"])}

fig_pie = px.pie(
    names=list(fuel_data.keys()),
    values=list(fuel_data.values()),
    title="Fuel Remaining vs. Used",
    template="simple_white",
    color_discrete_sequence=px.colors.qualitative.Pastel  # Bright pastel colors
)
fig_pie.update_traces(textinfo="percent+label", hole=0.4)
fig_pie.update_layout(font=dict(family="Arial", size=14), title_font=dict(size=18))
st.plotly_chart(fig_pie, use_container_width=True)

# ---- Detailed Trip Data ----
st.markdown("### Detailed Trip Data")
st.dataframe(df)

# ---- Travel Info ----
distance_left = 500 - sum(vehicle_data["Distance Covered (km)"])
st.markdown(
    f"<div class='travel-info'>The vehicle needs to travel {distance_left} km to complete the journey.</div>",
    unsafe_allow_html=True
)

# ---- Footer ----
st.markdown("<footer>Designed by Aditya. Powered by Streamlit.</footer>", unsafe_allow_html=True)
