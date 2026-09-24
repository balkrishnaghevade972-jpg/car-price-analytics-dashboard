# ============================================================
# CAR PRICE ANALYTICS DASHBOARD
# Professional Automotive Analytics Theme
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Car Price Analytics",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* ============================================================
   GLOBAL APPLICATION
   ============================================================ */

.stApp {
    background: #0b0f14;
    color: #e8edf2;
}

.main {
    background: #0b0f14;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1450px;
}


/* ============================================================
   HEADER
   ============================================================ */

.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    color: #f5f7fa;
    letter-spacing: 1px;
    margin-bottom: 4px;
}

.subtitle {
    text-align: center;
    font-size: 16px;
    color: #8f9aa6;
    margin-bottom: 30px;
}


/* ============================================================
   SECTION HEADINGS
   ============================================================ */

.section-title {
    color: #4da3ff;
    font-size: 26px;
    font-weight: 650;
    margin-top: 10px;
    margin-bottom: 22px;
    border-bottom: 1px solid #252d36;
    padding-bottom: 10px;
}


/* ============================================================
   KPI CARDS
   ============================================================ */

.kpi-card {
    background: #121820;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #252e38;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
}

.kpi-title {
    color: #8f9aa6;
    font-size: 14px;
    margin-bottom: 6px;
}

.kpi-value {
    color: #4da3ff;
    font-size: 27px;
    font-weight: 700;
}


/* ============================================================
   INSIGHT CARDS
   ============================================================ */

.insight-card {
    background: #121820;
    border-left: 3px solid #4da3ff;
    padding: 14px 16px;
    border-radius: 6px;
    margin-bottom: 12px;
    color: #d9e0e7;
}


/* ============================================================
   PREDICTION
   ============================================================ */

.prediction-card {
    background: #121820;
    padding: 30px;
    border-radius: 12px;
    border: 1px solid #4da3ff;
    text-align: center;
    margin-top: 20px;
}

.prediction-price {
    color: #4da3ff;
    font-size: 40px;
    font-weight: 750;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

[data-testid="stSidebar"] {
    background: #0f141a;
    border-right: 1px solid #252d36;
}

[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #f5f7fa;
}

[data-testid="stSidebar"] label {
    color: #b8c2cc !important;
}


/* ============================================================
   INPUTS
   ============================================================ */

.stSelectbox label,
.stTextInput label,
.stNumberInput label,
.stSlider label {
    color: #b8c2cc !important;
    font-weight: 500;
}

.stSelectbox div[data-baseweb="select"] > div {
    background-color: #151b22;
    border-color: #303944;
}

.stTextInput input,
.stNumberInput input {
    background-color: #151b22;
    color: #f5f7fa;
    border: 1px solid #303944;
}


/* ============================================================
   BUTTONS
   ============================================================ */

.stButton button {
    background: #2f80ed;
    color: white;
    border: none;
    border-radius: 7px;
    font-weight: 600;
    padding: 10px 20px;
}

.stButton button:hover {
    background: #4da3ff;
    color: white;
}


/* ============================================================
   DOWNLOAD BUTTON
   ============================================================ */

.stDownloadButton button {
    background: #2f80ed !important;
    color: white !important;
    border: none !important;
    font-weight: 600 !important;
    border-radius: 7px !important;
}

.stDownloadButton button:hover {
    background: #4da3ff !important;
    color: white !important;
}


/* ============================================================
   TABS
   ============================================================ */

.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: #0f141a;
    border-bottom: 1px solid #252d36;
}

.stTabs [data-baseweb="tab"] {
    color: #8f9aa6;
    font-weight: 500;
    padding: 12px 16px;
}

.stTabs [aria-selected="true"] {
    color: #4da3ff !important;
    border-bottom: 2px solid #4da3ff;
}


/* ============================================================
   DATAFRAME
   ============================================================ */

[data-testid="stDataFrame"] {
    border: 1px solid #252e38;
    border-radius: 8px;
}


/* ============================================================
   METRICS
   ============================================================ */

[data-testid="stMetric"] {
    background: #121820;
    padding: 15px;
    border-radius: 8px;
    border: 1px solid #252e38;
}

[data-testid="stMetricLabel"] {
    color: #8f9aa6 !important;
}

[data-testid="stMetricValue"] {
    color: #f5f7fa !important;
}


/* ============================================================
   ALERTS
   ============================================================ */

.stAlert {
    background: #121820;
    border: 1px solid #303944;
}


/* ============================================================
   DIVIDERS
   ============================================================ */

hr {
    border-color: #252d36;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;
    color: #687582;
    padding: 30px;
    margin-top: 40px;
    border-top: 1px solid #252d36;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    data = pd.read_csv("final_car_dataset.csv")

    return data


# ============================================================
# LOAD MACHINE LEARNING MODEL
# ============================================================

@st.cache_resource
def load_model():

    model = joblib.load("car_price_model_v2.pkl")

    return model


df = load_data()
model = load_model()


# ============================================================
# DATA PREPARATION
# ============================================================

df.columns = df.columns.str.strip()


numeric_columns = [
    "HorsePower",
    "Total Speed",
    "Performance(0 - 100 )KM/H",
    "CC_Battery",
    "Seats_Clean",
    "Torque_Nm",
    "Price"
]


for column in numeric_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


df = df.dropna(
    subset=["Price"]
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    "## CAR ANALYTICS"
)

st.sidebar.markdown(
    "### Dashboard"
)

st.sidebar.markdown("---")


# ============================================================
# SEARCH CAR
# ============================================================

search_car = st.sidebar.text_input(
    "Search Car",
    ""
)


# ============================================================
# MANUFACTURER FILTER
# ============================================================

companies = sorted(
    df["Company Names"]
    .dropna()
    .unique()
)


selected_company = st.sidebar.selectbox(
    "Manufacturer",
    ["All"] + companies
)


# ============================================================
# FUEL FILTER
# ============================================================

fuel_types = sorted(
    df["Fuel Types"]
    .dropna()
    .unique()
)


selected_fuel = st.sidebar.selectbox(
    "Fuel Type",
    ["All"] + fuel_types
)


# ============================================================
# PRICE FILTER
# ============================================================

min_price = float(
    df["Price"].min()
)

max_price = float(
    df["Price"].max()
)


price_range = st.sidebar.slider(
    "Price Range",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price)
)


# ============================================================
# HORSEPOWER FILTER
# ============================================================

min_hp = float(
    df["HorsePower"].min()
)

max_hp = float(
    df["HorsePower"].max()
)


hp_range = st.sidebar.slider(
    "HorsePower",
    min_value=min_hp,
    max_value=max_hp,
    value=(min_hp, max_hp)
)


# ============================================================
# TOP SPEED FILTER
# ============================================================

min_speed = float(
    df["Total Speed"].min()
)

max_speed = float(
    df["Total Speed"].max()
)


speed_range = st.sidebar.slider(
    "Top Speed",
    min_value=min_speed,
    max_value=max_speed,
    value=(min_speed, max_speed)
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if search_car:

    filtered_df = filtered_df[
        filtered_df["Cars Names"]
        .astype(str)
        .str.contains(
            search_car,
            case=False,
            na=False
        )
    ]


if selected_company != "All":

    filtered_df = filtered_df[
        filtered_df["Company Names"] == selected_company
    ]


if selected_fuel != "All":

    filtered_df = filtered_df[
        filtered_df["Fuel Types"] == selected_fuel
    ]


filtered_df = filtered_df[
    (filtered_df["Price"] >= price_range[0])
    &
    (filtered_df["Price"] <= price_range[1])
]


filtered_df = filtered_df[
    (filtered_df["HorsePower"] >= hp_range[0])
    &
    (filtered_df["HorsePower"] <= hp_range[1])
]


filtered_df = filtered_df[
    (filtered_df["Total Speed"] >= speed_range[0])
    &
    (filtered_df["Total Speed"] <= speed_range[1])
]


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">CAR PRICE ANALYTICS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Automotive Data Analytics • Explore • Compare • Predict</div>',
    unsafe_allow_html=True
)


# ============================================================
# KPI SECTION
# ============================================================

if len(filtered_df) > 0:

    total_cars = len(filtered_df)

    average_price = filtered_df["Price"].mean()

    average_hp = filtered_df["HorsePower"].mean()

    average_speed = filtered_df["Total Speed"].mean()

else:

    total_cars = 0
    average_price = 0
    average_hp = 0
    average_speed = 0


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Cars</div>
            <div class="kpi-value">{total_cars}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Average Price</div>
            <div class="kpi-value">${average_price:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Average HorsePower</div>
            <div class="kpi-value">{average_hp:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Average Speed</div>
            <div class="kpi-value">{average_speed:,.0f} km/h</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("---")


# ============================================================
# TABS
# ============================================================

summary, overview, performance, pricing, comparison, companies_tab, explorer, prediction = st.tabs(
    [
        "Project Summary",
        "Overview",
        "Performance",
        "Pricing",
        "Compare Cars",
        "Manufacturers",
        "Car Explorer",
        "Price Prediction"
    ]
)


# ============================================================
# PROJECT SUMMARY
# ============================================================

with summary:

    st.markdown(
        '<div class="section-title">Project Summary</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Problem Statement")

    st.write(
        """
        The objective of this project is to analyze car specifications,
        understand factors affecting car prices, and develop a machine
        learning model capable of predicting car prices.
        """
    )


    st.markdown("### Project Objectives")

    objectives = [
        "Clean and preprocess the car dataset.",
        "Perform Exploratory Data Analysis (EDA).",
        "Identify relationships between car specifications and price.",
        "Create useful visualizations.",
        "Build machine learning models.",
        "Evaluate model performance.",
        "Develop an interactive dashboard.",
        "Provide car price prediction."
    ]


    for objective in objectives:

        st.write(
            objective
        )


    st.markdown("### Dataset Information")


    info_col1, info_col2, info_col3 = st.columns(3)


    with info_col1:

        st.metric(
            "Total Records",
            len(df)
        )


    with info_col2:

        st.metric(
            "Total Columns",
            len(df.columns)
        )


    with info_col3:

        st.metric(
            "Average Price",
            f"${df['Price'].mean():,.0f}"
        )


    st.markdown("### Data Cleaning")


    cleaning_points = [
        "Removed unnecessary spaces.",
        "Converted numerical values into numeric format.",
        "Handled missing values.",
        "Converted ranges into representative numerical values.",
        "Created cleaned columns such as CC_Battery, Seats_Clean and Torque_Nm.",
        "Removed duplicate records during preprocessing."
    ]


    for point in cleaning_points:

        st.write(
            point
        )


    st.markdown("### Exploratory Data Analysis")


    st.write(
        """
        The project analyzes fuel types, manufacturers, prices,
        horsepower, top speed, acceleration performance and
        correlations between numerical variables.
        """
    )


    st.markdown("### Machine Learning")


    st.write(
        """
        Two regression approaches were explored:

        • Linear Regression

        • Random Forest Regression

        The Random Forest model is used in the dashboard for
        price prediction.
        """
    )


    st.markdown("### Technologies Used")


    technologies = [
        "Python",
        "Google Colab",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Seaborn",
        "Plotly",
        "Scikit-learn",
        "Joblib",
        "Streamlit"
    ]


    for technology in technologies:

        st.write(
            technology
        )


    st.markdown("### Project Workflow")


    st.write(
        """
        Dataset → Data Cleaning → EDA → Feature Engineering →
        Machine Learning → Model Evaluation → Dashboard →
        Price Prediction
        """
    )


# ============================================================
# OVERVIEW
# ============================================================

with overview:

    st.markdown(
        '<div class="section-title">Market Overview</div>',
        unsafe_allow_html=True
    )


    if len(filtered_df) == 0:

        st.warning(
            "No cars match the selected filters."
        )

    else:

        col1, col2 = st.columns(2)


        # ----------------------------------------------------
        # FUEL MARKET SHARE
        # ----------------------------------------------------

        with col1:

            fuel_counts = (
                filtered_df["Fuel Types"]
                .value_counts()
                .reset_index()
            )


            fuel_counts.columns = [
                "Fuel Type",
                "Count"
            ]


            fig = px.pie(
                fuel_counts,
                names="Fuel Type",
                values="Count",
                hole=0.55,
                title="Fuel Type Distribution"
            )


            fig.update_layout(
                template="plotly_dark"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


        # ----------------------------------------------------
        # AVERAGE PRICE BY FUEL
        # ----------------------------------------------------

        with col2:

            avg_fuel_price = (
                filtered_df
                .groupby("Fuel Types")["Price"]
                .mean()
                .reset_index()
                .sort_values(
                    "Price",
                    ascending=False
                )
            )


            fig = px.bar(
                avg_fuel_price,
                x="Fuel Types",
                y="Price",
                title="Average Price by Fuel Type"
            )


            fig.update_layout(
                template="plotly_dark"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


        # ----------------------------------------------------
        # PRICE DISTRIBUTION
        # ----------------------------------------------------

        fig = px.histogram(
            filtered_df,
            x="Price",
            nbins=40,
            title="Car Price Distribution"
        )


        fig.update_layout(
            template="plotly_dark"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


        # ----------------------------------------------------
        # LIVE INSIGHTS
        # ----------------------------------------------------

        st.markdown(
            "### Live Insights"
        )


        highest_price_car = filtered_df.loc[
            filtered_df["Price"].idxmax()
        ]


        highest_hp_car = filtered_df.loc[
            filtered_df["HorsePower"].idxmax()
        ]


        st.markdown(
            f"""
            <div class="insight-card">
            Highest priced car in the current selection:
            <b>{highest_price_car['Cars Names']}</b>
            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            f"""
            <div class="insight-card">
            Highest horsepower car:
            <b>{highest_hp_car['Cars Names']}</b>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# PERFORMANCE
# ============================================================

with performance:

    st.markdown(
        '<div class="section-title">Performance Analysis</div>',
        unsafe_allow_html=True
    )


    if len(filtered_df) == 0:

        st.warning(
            "No data available for the selected filters."
        )

    else:

        col1, col2 = st.columns(2)


        with col1:

            fig = px.scatter(
                filtered_df,
                x="HorsePower",
                y="Price",
                hover_name="Cars Names",
                title="HorsePower vs Price"
            )


            fig.update_layout(
                template="plotly_dark"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


        with col2:

            fig = px.scatter(
                filtered_df,
                x="Total Speed",
                y="Price",
                hover_name="Cars Names",
                title="Top Speed vs Price"
            )


            fig.update_layout(
                template="plotly_dark"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


        fig = px.scatter(
            filtered_df,
            x="Performance(0 - 100 )KM/H",
            y="Price",
            hover_name="Cars Names",
            title="0–100 km/h Performance vs Price"
        )


        fig.update_layout(
            template="plotly_dark"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


        st.markdown(
            "### Correlation with Price"
        )


        correlation_columns = [
            "HorsePower",
            "Total Speed",
            "Performance(0 - 100 )KM/H",
            "CC_Battery",
            "Seats_Clean",
            "Torque_Nm",
            "Price"
        ]


        correlation_data = (
            filtered_df[
                correlation_columns
            ]
            .corr()["Price"]
            .drop("Price")
            .sort_values(
                ascending=False
            )
            .reset_index()
        )


        correlation_data.columns = [
            "Feature",
            "Correlation"
        ]


        fig = px.bar(
            correlation_data,
            x="Feature",
            y="Correlation",
            title="Feature Correlation with Price"
        )


        fig.update_layout(
            template="plotly_dark"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ============================================================
# PRICING
# ============================================================

with pricing:

    st.markdown(
        '<div class="section-title">Pricing Analysis</div>',
        unsafe_allow_html=True
    )


    if len(filtered_df) == 0:

        st.warning(
            "No data available."
        )

    else:

        p1, p2, p3, p4 = st.columns(4)


        with p1:

            st.metric(
                "Minimum Price",
                f"${filtered_df['Price'].min():,.0f}"
            )


        with p2:

            st.metric(
                "Median Price",
                f"${filtered_df['Price'].median():,.0f}"
            )


        with p3:

            st.metric(
                "Average Price",
                f"${filtered_df['Price'].mean():,.0f}"
            )


        with p4:

            st.metric(
                "Maximum Price",
                f"${filtered_df['Price'].max():,.0f}"
            )


        # ----------------------------------------------------
        # PRICE SEGMENTS
        # ----------------------------------------------------

        st.markdown(
            "### Price Segments"
        )


        price_segments = pd.cut(
            filtered_df["Price"],
            bins=5
        )


        segment_df = (
            price_segments
            .value_counts()
            .sort_index()
            .reset_index()
        )


        segment_df.columns = [
            "Price Range",
            "Cars"
        ]


        segment_df["Price Range"] = (
            segment_df["Price Range"]
            .astype(str)
        )


        fig = px.bar(
            segment_df,
            x="Price Range",
            y="Cars",
            title="Cars by Price Segment"
        )


        fig.update_layout(
            template="plotly_dark",
            xaxis_title="Price Range",
            yaxis_title="Number of Cars"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


        # ----------------------------------------------------
        # HIGHEST PRICED CARS
        # ----------------------------------------------------

        st.markdown(
            "### Highest-Priced Cars"
        )


        expensive_cars = (
            filtered_df[
                [
                    "Cars Names",
                    "Company Names",
                    "Fuel Types",
                    "Price"
                ]
            ]
            .sort_values(
                "Price",
                ascending=False
            )
            .head(10)
        )


        st.dataframe(
            expensive_cars,
            use_container_width=True
        )


# ============================================================
# COMPARE CARS
# ============================================================

with comparison:

    st.markdown(
        '<div class="section-title">Compare Cars</div>',
        unsafe_allow_html=True
    )


    car_list = sorted(
        df["Cars Names"]
        .dropna()
        .unique()
    )


    if len(car_list) >= 2:

        col1, col2 = st.columns(2)


        with col1:

            car1 = st.selectbox(
                "Select Car 1",
                car_list,
                key="comparison_car_1"
            )


        with col2:

            car2 = st.selectbox(
                "Select Car 2",
                car_list,
                index=1,
                key="comparison_car_2"
            )


        car1_data = df[
            df["Cars Names"] == car1
        ].iloc[0]


        car2_data = df[
            df["Cars Names"] == car2
        ].iloc[0]


        comparison_data = pd.DataFrame({

            "Metric": [
                "Price",
                "HorsePower",
                "Top Speed",
                "0–100 km/h",
                "CC / Battery",
                "Seats",
                "Torque"
            ],

            car1: [
                car1_data["Price"],
                car1_data["HorsePower"],
                car1_data["Total Speed"],
                car1_data["Performance(0 - 100 )KM/H"],
                car1_data["CC_Battery"],
                car1_data["Seats_Clean"],
                car1_data["Torque_Nm"]
            ],

            car2: [
                car2_data["Price"],
                car2_data["HorsePower"],
                car2_data["Total Speed"],
                car2_data["Performance(0 - 100 )KM/H"],
                car2_data["CC_Battery"],
                car2_data["Seats_Clean"],
                car2_data["Torque_Nm"]
            ]

        })


        st.dataframe(
            comparison_data,
            use_container_width=True,
            hide_index=True
        )


        # ----------------------------------------------------
        # RADAR CHART
        # ----------------------------------------------------

        categories = [
            "Price",
            "HorsePower",
            "Top Speed",
            "Performance",
            "CC/Battery",
            "Seats",
            "Torque"
        ]


        values1 = [
            car1_data["Price"],
            car1_data["HorsePower"],
            car1_data["Total Speed"],
            car1_data["Performance(0 - 100 )KM/H"],
            car1_data["CC_Battery"],
            car1_data["Seats_Clean"],
            car1_data["Torque_Nm"]
        ]


        values2 = [
            car2_data["Price"],
            car2_data["HorsePower"],
            car2_data["Total Speed"],
            car2_data["Performance(0 - 100 )KM/H"],
            car2_data["CC_Battery"],
            car2_data["Seats_Clean"],
            car2_data["Torque_Nm"]
        ]


        radar_df = pd.DataFrame({

            "Metric": categories,

            car1: values1,

            car2: values2

        })


        for column in [car1, car2]:

            maximum = radar_df[column].max()

            if maximum != 0:

                radar_df[column] = (
                    radar_df[column] / maximum
                )


        fig = go.Figure()


        fig.add_trace(
            go.Scatterpolar(
                r=radar_df[car1],
                theta=categories,
                fill="toself",
                name=car1
            )
        )


        fig.add_trace(
            go.Scatterpolar(
                r=radar_df[car2],
                theta=categories,
                fill="toself",
                name=car2
            )
        )


        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )
            ),
            template="plotly_dark",
            title="Normalized Car Comparison"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ============================================================
# MANUFACTURERS
# ============================================================

with companies_tab:

    st.markdown(
        '<div class="section-title">Manufacturer Analysis</div>',
        unsafe_allow_html=True
    )


    company_summary = (
        filtered_df
        .groupby("Company Names")
        .agg(
            Cars=("Cars Names", "count"),
            Average_Price=("Price", "mean"),
            Average_HorsePower=("HorsePower", "mean")
        )
        .reset_index()
        .sort_values(
            "Cars",
            ascending=False
        )
    )


    if len(company_summary) > 0:

        fig = px.bar(
            company_summary.head(15),
            x="Company Names",
            y="Cars",
            title="Top Manufacturers by Number of Cars"
        )


        fig.update_layout(
            template="plotly_dark"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


        st.markdown(
            "### Manufacturer Summary"
        )


        st.dataframe(
            company_summary,
            use_container_width=True
        )


# ============================================================
# CAR EXPLORER
# ============================================================

with explorer:

    st.markdown(
        '<div class="section-title">Car Explorer</div>',
        unsafe_allow_html=True
    )


    explorer_car = st.selectbox(
        "Select a car",
        sorted(
            df["Cars Names"]
            .dropna()
            .unique()
        ),
        key="explorer_car"
    )


    selected_car = df[
        df["Cars Names"] == explorer_car
    ].iloc[0]


    st.markdown(
        f"### {explorer_car}"
    )


    e1, e2, e3, e4 = st.columns(4)


    with e1:

        st.metric(
            "Price",
            f"${selected_car['Price']:,.0f}"
        )


    with e2:

        st.metric(
            "HorsePower",
            f"{selected_car['HorsePower']:,.0f}"
        )


    with e3:

        st.metric(
            "Top Speed",
            f"{selected_car['Total Speed']:,.0f} km/h"
        )


    with e4:

        st.metric(
            "Torque",
            f"{selected_car['Torque_Nm']:,.0f} Nm"
        )


    st.markdown(
        "### Technical Specifications"
    )


    specs = pd.DataFrame({

        "Specification": [
            "Manufacturer",
            "Fuel Type",
            "Engine",
            "HorsePower",
            "Top Speed",
            "0–100 km/h",
            "CC / Battery",
            "Seats",
            "Torque"
        ],

        "Value": [
            selected_car["Company Names"],
            selected_car["Fuel Types"],
            selected_car["Engines"],
            selected_car["HorsePower"],
            selected_car["Total Speed"],
            selected_car["Performance(0 - 100 )KM/H"],
            selected_car["CC_Battery"],
            selected_car["Seats_Clean"],
            selected_car["Torque_Nm"]
        ]

    })


    st.dataframe(
        specs,
        use_container_width=True
    )


# ============================================================
# PRICE PREDICTION
# ============================================================

with prediction:

    st.markdown(
        '<div class="section-title">Car Price Prediction</div>',
        unsafe_allow_html=True
    )


    st.write(
        """
        Enter the specifications of a car and the trained
        Random Forest model will estimate its price.
        """
    )


    st.info(
        "Prediction is generated using the Random Forest model trained in Google Colab."
    )


    col1, col2 = st.columns(2)


    # --------------------------------------------------------
    # LEFT SIDE
    # --------------------------------------------------------

    with col1:

        manufacturer = st.selectbox(
            "Manufacturer",
            sorted(
                df["Company Names"]
                .dropna()
                .unique()
            ),
            key="prediction_manufacturer"
        )


        fuel_type = st.selectbox(
            "Fuel Type",
            sorted(
                df["Fuel Types"]
                .dropna()
                .unique()
            ),
            key="prediction_fuel"
        )


        horsepower = st.number_input(
            "HorsePower",
            min_value=0.0,
            value=150.0,
            step=1.0,
            key="prediction_hp"
        )


        top_speed = st.number_input(
            "Top Speed (km/h)",
            min_value=0.0,
            value=200.0,
            step=1.0,
            key="prediction_speed"
        )


    # --------------------------------------------------------
    # RIGHT SIDE
    # --------------------------------------------------------

    with col2:

        performance = st.number_input(
            "0–100 km/h Performance (seconds)",
            min_value=0.0,
            value=8.0,
            step=0.1,
            key="prediction_performance"
        )


        cc_battery = st.number_input(
            "CC / Battery Capacity",
            min_value=0.0,
            value=1500.0,
            step=50.0,
            key="prediction_cc"
        )


        seats = st.number_input(
            "Seats",
            min_value=1.0,
            value=5.0,
            step=1.0,
            key="prediction_seats"
        )


        torque = st.number_input(
            "Torque (Nm)",
            min_value=0.0,
            value=200.0,
            step=10.0,
            key="prediction_torque"
        )


    st.markdown("---")


    # --------------------------------------------------------
    # PREDICTION BUTTON
    # --------------------------------------------------------

    predict_button = st.button(
        "Predict Car Price",
        use_container_width=True,
        type="primary"
    )


    if predict_button:

        try:

            input_data = pd.DataFrame({

                "Company Names": [
                    manufacturer
                ],

                "Fuel Types": [
                    fuel_type
                ],

                "HorsePower": [
                    horsepower
                ],

                "Total Speed": [
                    top_speed
                ],

                "Performance(0 - 100 )KM/H": [
                    performance
                ],

                "CC_Battery": [
                    cc_battery
                ],

                "Seats_Clean": [
                    seats
                ],

                "Torque_Nm": [
                    torque
                ]

            })


            prediction_value = model.predict(
                input_data
            )[0]


            st.markdown(
                f"""
                <div class="prediction-card">

                    <div style="
                        color:#8f9aa6;
                        font-size:16px;
                        margin-bottom:10px;
                    ">
                        Estimated Car Price
                    </div>

                    <div class="prediction-price">
                        ${prediction_value:,.2f}
                    </div>

                    <div style="
                        color:#8f9aa6;
                        margin-top:10px;
                    ">
                        Based on the specifications provided
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


            st.markdown(
                "### Prediction Input"
            )


            prediction_summary = pd.DataFrame({

                "Specification": [
                    "Manufacturer",
                    "Fuel Type",
                    "HorsePower",
                    "Top Speed",
                    "0–100 km/h",
                    "CC / Battery",
                    "Seats",
                    "Torque"
                ],

                "Value": [
                    manufacturer,
                    fuel_type,
                    horsepower,
                    f"{top_speed} km/h",
                    f"{performance} sec",
                    cc_battery,
                    seats,
                    f"{torque} Nm"
                ]

            })


            st.dataframe(
                prediction_summary,
                use_container_width=True
            )


        except Exception as e:

            st.error(
                "Prediction could not be generated."
            )

            st.code(
                str(e)
            )


# ============================================================
# DOWNLOAD FILTERED DATA
# ============================================================

st.markdown("---")


st.markdown(
    "### Download Current Dataset"
)


csv_data = filtered_df.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    label="Download Current Dataset",
    data=csv_data,
    file_name="current_car_dataset.csv",
    mime="text/csv",
    use_container_width=True
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        <b>Car Price Analytics Dashboard</b><br>
        Built with Python • Pandas • Plotly • Scikit-learn • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
