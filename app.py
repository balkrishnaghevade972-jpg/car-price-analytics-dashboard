# ============================================================
# CAR PRICE ANALYTICS DASHBOARD
# Midnight Garage Theme
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
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    .stApp {
        background: linear-gradient(
            135deg,
            #050b18 0%,
            #0a1428 50%,
            #07101f 100%
        );
        color: white;
    }

    .main-title {
        font-size: 45px;
        font-weight: 800;
        text-align: center;
        color: #00e5ff;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #a9c6d9;
        margin-bottom: 30px;
    }

    .section-title {
        color: #00e5ff;
        font-size: 28px;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 20px;
    }

    .kpi-card {
        background: linear-gradient(
            145deg,
            #101f38,
            #0b172b
        );
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #1f4564;
        text-align: center;
        box-shadow: 0 5px 20px rgba(0, 229, 255, 0.08);
    }

    .kpi-title {
        color: #9bb5c7;
        font-size: 15px;
    }

    .kpi-value {
        color: #00e5ff;
        font-size: 28px;
        font-weight: 700;
    }

    .insight-card {
        background: #0d1b30;
        border-left: 4px solid #00e5ff;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 12px;
    }

    .prediction-card {
        background: linear-gradient(
            135deg,
            #09243a,
            #102b48
        );
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #00e5ff;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 10px 35px rgba(0, 229, 255, 0.15);
    }

    .prediction-price {
        color: #00e5ff;
        font-size: 42px;
        font-weight: 800;
    }

    .footer {
        text-align: center;
        color: #78909c;
        padding: 30px;
        margin-top: 40px;
    }
    .stDownloadButton button {
    background-color: #ff4b4b !important;
    color: white !important;
    border: none !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
}

.stDownloadButton button:hover {
    background-color: #ff6666 !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)


<style>
/* ============================================================
   MODERN AUTOMOTIVE UI — GLASS / PREMIUM GARAGE
   ============================================================ */

:root {
    --bg-1: #070b14;
    --bg-2: #0d1322;
    --card: rgba(18, 25, 40, 0.72);
    --card-strong: rgba(23, 32, 51, 0.92);
    --line: rgba(255,255,255,0.09);
    --text: #f4f7fb;
    --muted: #94a3b8;
    --accent: #38bdf8;
    --accent-2: #818cf8;
}

/* Main background */
.stApp {
    background:
        radial-gradient(circle at 10% 0%, rgba(56,189,248,.10), transparent 28%),
        radial-gradient(circle at 90% 10%, rgba(129,140,248,.10), transparent 30%),
        linear-gradient(135deg, var(--bg-1), var(--bg-2) 55%, #080d18);
    color: var(--text);
}

.main .block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Hide Streamlit chrome */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {background: transparent !important;}

/* Premium hero */
.hero {
    position: relative;
    overflow: hidden;
    padding: 34px 38px;
    margin-bottom: 24px;
    border: 1px solid var(--line);
    border-radius: 26px;
    background:
        linear-gradient(120deg, rgba(15,23,42,.94), rgba(15,23,42,.68)),
        radial-gradient(circle at 90% 20%, rgba(56,189,248,.16), transparent 35%);
    box-shadow: 0 20px 60px rgba(0,0,0,.28);
}

.hero::after {
    content: "01";
    position: absolute;
    right: 35px;
    bottom: -35px;
    font-size: 150px;
    font-weight: 900;
    color: rgba(255,255,255,.025);
}

.hero-kicker {
    color: var(--accent);
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.hero-title {
    color: #fff;
    font-size: clamp(34px, 4vw, 58px);
    line-height: 1;
    font-weight: 900;
    letter-spacing: -2px;
    margin: 0;
}

.hero-title span {
    color: var(--accent);
}

.hero-subtitle {
    color: #a8b4c7;
    font-size: 16px;
    margin-top: 13px;
    max-width: 680px;
}

.hero-pill {
    display: inline-block;
    margin-top: 20px;
    padding: 7px 13px;
    border-radius: 999px;
    background: rgba(56,189,248,.09);
    border: 1px solid rgba(56,189,248,.22);
    color: #bae6fd;
    font-size: 12px;
    font-weight: 700;
}

/* KPI cards */
.kpi-card {
    min-height: 118px;
    padding: 21px 22px;
    border-radius: 20px;
    border: 1px solid var(--line);
    background: linear-gradient(145deg, rgba(24,34,54,.90), rgba(12,18,31,.82));
    box-shadow: 0 12px 35px rgba(0,0,0,.20);
    transition: transform .2s ease, border-color .2s ease;
}

.kpi-card:hover {
    transform: translateY(-3px);
    border-color: rgba(56,189,248,.35);
}

.kpi-title {
    color: var(--muted);
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .8px;
}

.kpi-value {
    color: #fff;
    font-size: 30px;
    font-weight: 850;
    margin-top: 9px;
}

/* Section headings */
.section-title {
    color: #fff;
    font-size: 28px;
    font-weight: 850;
    letter-spacing: -.6px;
    margin: 8px 0 20px;
}

/* Tabs */
button[data-baseweb="tab"] {
    color: #91a0b5 !important;
    font-weight: 700 !important;
    border-radius: 12px !important;
    padding: 10px 14px !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #e0f2fe !important;
    background: rgba(56,189,248,.10) !important;
}

div[data-baseweb="tab-highlight"] {
    background-color: var(--accent) !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, rgba(8,13,24,.98), rgba(12,18,31,.98));
    border-right: 1px solid rgba(255,255,255,.06);
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 1.5rem;
}

section[data-testid="stSidebar"] h2 {
    color: #fff;
    font-weight: 850;
}

/* Inputs */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div,
.stTextInput > div > div,
.stNumberInput > div > div {
    background: rgba(15,23,42,.75) !important;
    border: 1px solid rgba(255,255,255,.09) !important;
    border-radius: 12px !important;
}

div[data-baseweb="select"] > div:focus-within,
.stTextInput > div > div:focus-within,
.stNumberInput > div > div:focus-within {
    border-color: rgba(56,189,248,.55) !important;
    box-shadow: 0 0 0 2px rgba(56,189,248,.08) !important;
}

/* Sliders */
div[data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] {
    background: var(--accent) !important;
}

/* Streamlit metrics */
div[data-testid="stMetric"] {
    background: rgba(17,24,39,.72);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 15px;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button {
    border: 1px solid rgba(56,189,248,.28) !important;
    border-radius: 13px !important;
    min-height: 45px !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #0ea5e9, #6366f1) !important;
    color: white !important;
    box-shadow: 0 8px 25px rgba(14,165,233,.16);
    transition: transform .18s ease, box-shadow .18s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(56,189,248,.24);
}

/* Cards generated by our app */
.insight-card {
    background: rgba(15,23,42,.76);
    border: 1px solid var(--line);
    border-left: 3px solid var(--accent);
    padding: 16px 18px;
    border-radius: 14px;
    margin: 10px 0;
}

.prediction-card {
    background:
        radial-gradient(circle at 50% 0%, rgba(56,189,248,.15), transparent 50%),
        rgba(15,23,42,.85);
    padding: 34px;
    border-radius: 24px;
    border: 1px solid rgba(56,189,248,.25);
    text-align: center;
    box-shadow: 0 18px 50px rgba(0,0,0,.28);
}

.prediction-price {
    color: #7dd3fc;
    font-size: 48px;
    font-weight: 900;
    letter-spacing: -1.5px;
}

/* Dataframes */
div[data-testid="stDataFrame"] {
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid var(--line);
}

/* Alerts */
div[data-testid="stAlert"] {
    border-radius: 14px;
}

/* Dividers */
hr {
    border-color: rgba(255,255,255,.07) !important;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    padding: 38px 10px 10px;
    margin-top: 45px;
    font-size: 13px;
}
</style>


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
    "## 🏎️ Midnight Garage"
)
st.sidebar.caption("CAR PRICE ANALYTICS • v2.0")
st.sidebar.markdown("### Filters & Discovery")

st.sidebar.markdown("---")


# ============================================================
# SEARCH CAR
# ============================================================

search_car = st.sidebar.text_input(
    "🔎 Search Car",
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
    "🏢 Manufacturer",
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
    "⛽ Fuel Type",
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
    "💰 Price Range",
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
    "🐎 HorsePower",
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
    "🚀 Top Speed",
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
    """
    <div class="hero">
        <div class="hero-kicker">Automotive Intelligence • Data Analytics</div>
        <div class="hero-title">CAR PRICE <span>ANALYTICS</span></div>
        <div class="hero-subtitle">
            Explore market patterns, compare vehicle performance and
            estimate car prices using machine learning.
        </div>
        <div class="hero-pill">● LIVE DATA EXPLORATION &nbsp; • &nbsp; ML PRICE PREDICTION</div>
    </div>
    """,
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
            <div class="kpi-title">🚘 Cars</div>
            <div class="kpi-value">{total_cars}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">💰 Average Price</div>
            <div class="kpi-value">${average_price:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">🐎 Average HorsePower</div>
            <div class="kpi-value">{average_hp:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">🚀 Average Speed</div>
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
        "📋 Summary",
        "📊 Overview",
        "🏁 Performance",
        "💰 Pricing",
        "⚖️ Compare",
        "🏢 Brands",
        "🔎 Explorer",
        "🤖 Predict Price"
    ]
)


# ============================================================
# PROJECT SUMMARY
# ============================================================

with summary:

    st.markdown(
        '<div class="section-title">📋 Project Summary</div>',
        unsafe_allow_html=True
    )

    st.markdown("### 🎯 Problem Statement")

    st.write(
        """
        The objective of this project is to analyze car specifications,
        understand factors affecting car prices, and develop a machine
        learning model capable of predicting car prices.
        """
    )


    st.markdown("### 🎯 Project Objectives")

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
            "✔️ " + objective
        )


    st.markdown("### 📊 Dataset Information")


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


    st.markdown("### 🧹 Data Cleaning")


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
            "✔️ " + point
        )


    st.markdown("### 🔬 Exploratory Data Analysis")


    st.write(
        """
        The project analyzes fuel types, manufacturers, prices,
        horsepower, top speed, acceleration performance and
        correlations between numerical variables.
        """
    )


    st.markdown("### 🤖 Machine Learning")


    st.write(
        """
        Two regression approaches were explored:

        • Linear Regression

        • Random Forest Regression

        The Random Forest model is used in the dashboard for
        price prediction.
        """
    )


    st.markdown("### 🛠️ Technologies Used")


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
            "🔹 " + technology
        )


    st.markdown("### 🔄 Project Workflow")


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
        '<div class="section-title">🌌 Market Overview</div>',
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
            "### 💡 Live Insights"
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
            💰 Highest priced car in the current selection:
            <b>{highest_price_car['Cars Names']}</b>
            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            f"""
            <div class="insight-card">
            🐎 Highest horsepower car:
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
        '<div class="section-title">🏎️ Performance Analysis</div>',
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
            "### 📊 Correlation with Price"
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
        '<div class="section-title">💰 Pricing Analysis</div>',
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
        # FIXED PRICE SEGMENTS
        # ----------------------------------------------------

        st.markdown(
            "### 📊 Price Segments"
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


        # IMPORTANT FIX:
        # Convert Pandas Interval objects to strings

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
            "### 🏆 Highest-Priced Cars"
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
        '<div class="section-title">⚖️ Compare Cars</div>',
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
        '<div class="section-title">🏢 Manufacturer Analysis</div>',
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
            "### 📊 Manufacturer Summary"
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
        '<div class="section-title">🔎 Car Explorer</div>',
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
        f"### 🏎️ {explorer_car}"
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
        "### 📋 Technical Specifications"
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
        '<div class="section-title">💰 Car Price Prediction</div>',
        unsafe_allow_html=True
    )


    st.write(
        """
        Enter the specifications of a car and the trained
        Random Forest model will estimate its price.
        """
    )


    st.info(
        "🤖 Prediction is generated using the Random Forest model trained in Google Colab."
    )


    col1, col2 = st.columns(2)


    # --------------------------------------------------------
    # LEFT SIDE
    # --------------------------------------------------------

    with col1:

        manufacturer = st.selectbox(
            "🏢 Manufacturer",
            sorted(
                df["Company Names"]
                .dropna()
                .unique()
            ),
            key="prediction_manufacturer"
        )


        fuel_type = st.selectbox(
            "⛽ Fuel Type",
            sorted(
                df["Fuel Types"]
                .dropna()
                .unique()
            ),
            key="prediction_fuel"
        )


        horsepower = st.number_input(
            "🐎 HorsePower",
            min_value=0.0,
            value=150.0,
            step=1.0,
            key="prediction_hp"
        )


        top_speed = st.number_input(
            "🚀 Top Speed (km/h)",
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
            "⚡ 0–100 km/h Performance (seconds)",
            min_value=0.0,
            value=8.0,
            step=0.1,
            key="prediction_performance"
        )


        cc_battery = st.number_input(
            "🔋 CC / Battery Capacity",
            min_value=0.0,
            value=1500.0,
            step=50.0,
            key="prediction_cc"
        )


        seats = st.number_input(
            "💺 Seats",
            min_value=1.0,
            value=5.0,
            step=1.0,
            key="prediction_seats"
        )


        torque = st.number_input(
            "🔧 Torque (Nm)",
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
        "🚀 Predict Car Price",
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
    f"""<div style="text-align:center;">
    <div style="color:#a9c6d9; font-size:18px;">
    Estimated Car Price
    </div>
    <div class="prediction-price">
    ${prediction_value:,.2f}
    </div>
    <div style="color:#9bb5c7; margin-top:10px;">
    Based on the specifications provided
    </div>
    </div>""",
    unsafe_allow_html=True
)


            st.markdown(
                "### 📋 Prediction Input"
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
                "❌ Prediction could not be generated."
            )

            st.code(
                str(e)
            )


# ============================================================
# DOWNLOAD FILTERED DATA
# ============================================================

st.markdown("---")


st.markdown(
    "### 📥 Download Current Dataset"
)


csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Current Dataset",
    data=csv_data,
    file_name="current_car_dataset.csv",
    mime="text/csv",
    use_container_width=True
)


# ============================================================
# FOOTER
# ============================================================

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer">  <b>Car Price Analytics Dashboard</b><br>'
    'Built with Python • Pandas • Plotly • Scikit-learn • Streamlit</div>',
    unsafe_allow_html=True
)
