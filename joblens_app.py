
# ===============================
# JobLens India - Streamlit App
# ===============================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go




st.set_page_config(page_title="JobLens India", layout="wide")
st.markdown("""
<style>

.stApp {
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

.glass {
background: rgba(255,255,255,0.08);
backdrop-filter: blur(10px);
padding:20px;
border-radius:15px;
border:1px solid rgba(255,255,255,0.2);
}

[data-testid="metric-container"]{
background: rgba(255,255,255,0.08);
border-radius:15px;
padding:20px;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("joblens_india_dataset.csv")
    return df

df = load_data()
logo_df = pd.read_csv("joblens_company_logos_100.csv")

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.title("Filters")

city_filter = st.sidebar.multiselect("City", df["city"].unique())
sector_filter = st.sidebar.multiselect("Sector", df["sector"].unique())
salary_filter = st.sidebar.slider("Salary Range (LPA)", int(df.salary_lpa.min()), int(df.salary_lpa.max()), (4,20))

filtered_df = df.copy()

if city_filter:
    filtered_df = filtered_df[filtered_df.city.isin(city_filter)]
if sector_filter:
    filtered_df = filtered_df[filtered_df.sector.isin(sector_filter)]
filtered_df = filtered_df[(filtered_df.salary_lpa >= salary_filter[0]) & (filtered_df.salary_lpa <= salary_filter[1])]

state_filter = st.sidebar.selectbox(
    "Select State",
    ["All India","Karnataka","Maharashtra","Delhi","Telangana","Tamil Nadu","West Bengal","Gujarat"]
)
filtered_df = filtered_df.merge(
    logo_df,
    on="company",
    how="left"
)

# -------------------------------
# Title Section
# -------------------------------
st.title("JobLens India")  # updated
st.markdown("### AI-Powered Career Insights Dashboard for Freshers")

# -------------------------------
# Section 1 - Job Heatmap
# -------------------------------

st.header("🗺 Job Heatmap Across Indian Cities")

city_coords = {
"Bangalore":[12.9716,77.5946],
"Hyderabad":[17.3850,78.4867],
"Pune":[18.5204,73.8567],
"Mumbai":[19.0760,72.8777],
"Delhi":[28.7041,77.1025],
"Chennai":[13.0827,80.2707],
"Gurgaon":[28.4595,77.0266],
"Noida":[28.5355,77.3910],
"Kolkata":[22.5726,88.3639],
"Ahmedabad":[23.0225,72.5714]
}

map_df = filtered_df.copy()

map_df["lat"] = map_df["city"].map(lambda x: city_coords.get(x,[None,None])[0])
map_df["lon"] = map_df["city"].map(lambda x: city_coords.get(x,[None,None])[1])

city_jobs = map_df.groupby("city").size().reset_index(name="job_count")

city_jobs["lat"] = city_jobs["city"].map(lambda x: city_coords.get(x,[None,None])[0])
city_jobs["lon"] = city_jobs["city"].map(lambda x: city_coords.get(x,[None,None])[1])

fig = px.density_mapbox(
    city_jobs,
    lat="lat",
    lon="lon",
    z="job_count",
    radius=45,
    center=dict(lat=22, lon=80),
    zoom=4,
    height=700,
    mapbox_style="carto-darkmatter",   # dark background
    color_continuous_scale="Turbo"
)

fig.add_scattermapbox(
    lat=city_jobs["lat"],
    lon=city_jobs["lon"],
    mode="markers+text",
    marker=dict(size=14,color="yellow"),
    text=city_jobs["city"],
    textposition="top center",
    hovertext=city_jobs["city"] + " | Jobs: " + city_jobs["job_count"].astype(str),
    hoverinfo="text"
)

fig.update_layout(
    margin=dict(l=0,r=0,t=0,b=0),
)

st.markdown("""
<style>
.block-container{
padding-top:2rem;
padding-left:2rem;
padding-right:2rem;
}
</style>
""", unsafe_allow_html=True)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# Section 2 - Metrics
# -------------------------------
st.header("📊 Market Insights")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Jobs", len(filtered_df))
col2.metric("Avg Salary", round(filtered_df.salary_lpa.mean(),2))
col3.metric("Median Salary", round(filtered_df.salary_lpa.median(),2))
col4.metric("Mode Salary", filtered_df.salary_lpa.mode()[0])

# -------------------------------
# Section 3 + 4
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Sector Job Demand")

    sector_counts = filtered_df["sector"].value_counts()

    fig_sector = px.bar(
        x=sector_counts.index,
        y=sector_counts.values,
        labels={"x":"Sector","y":"Jobs"},
        color=sector_counts.values
    )

    st.plotly_chart(fig_sector, use_container_width=True)


with col2:
    st.subheader("💰 Salary Distribution")

    fig_salary = px.histogram(
        filtered_df,
        x="salary_lpa",
        nbins=20,
        color_discrete_sequence=["#00c8ff"]
    )

    st.plotly_chart(fig_salary, use_container_width=True)
# -------------------------------
# Section 5 + 6
# -------------------------------
col3, col4 = st.columns(2)

with col3:
    st.subheader("🏙 Jobs by City")

    city_counts = filtered_df["city"].value_counts()

    fig_city = px.bar(
        x=city_counts.index,
        y=city_counts.values,
        color=city_counts.values
    )

    st.plotly_chart(fig_city, use_container_width=True)


with col4:
    st.subheader("🧠 Top Skills in Demand")

    skills_series = filtered_df["skills"].str.split(", ").explode()
    skills_counts = skills_series.value_counts().head(10)

    fig_skills = px.bar(
        x=skills_counts.index,
        y=skills_counts.values,
        color=skills_counts.values
    )

    st.plotly_chart(fig_skills, use_container_width=True)


    st.markdown("---")

st.markdown("## 🏆 City Leaderboard")

city_rank = filtered_df["city"].value_counts().reset_index()
city_rank.columns = ["City","Jobs"]

st.dataframe(
    city_rank,
    use_container_width=True
)

st.markdown("---")
st.markdown("## 🏢 Top Hiring Companies")

top_companies = filtered_df["company"].value_counts().head(8)

cols = st.columns(4)

for i, (company, count) in enumerate(top_companies.items()):

    logo_row = logo_df.loc[logo_df.company == company, "logo_url"]

    with cols[i % 4]:

        if not logo_row.empty:
            st.image(logo_row.values[0], width=60)
        else:
            st.write("🏢")   # fallback icon

        st.write(company)
        st.caption(f"{count} openings")

# -------------------------------
# Section 7 - Data Table
# -------------------------------
st.header("📋 Job Listings")

st.dataframe(
    filtered_df,
    height=400,
    use_container_width=True
)

# -------------------------------
# Section 8 - Data Exploration
# -------------------------------
st.header("📊 Dataset Statistics")

st.dataframe(
    filtered_df.describe(),
    use_container_width=True
)

st.markdown("---")
st.markdown("""
### Credits 

**Project:** JobLens India  
**Developer:** Tushar Magar  
 

**Tools Used**
- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Seaborn
- Matplotlib
""")

