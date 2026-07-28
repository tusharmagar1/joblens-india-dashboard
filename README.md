<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=220&section=header&text=JobLens%20India&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Decode%20India's%20Job%20Market%20—%20City%20by%20City,%20Skill%20by%20Skill&descAlignY=58&descSize=18" width="100%"/>

<br/>

<a href="#-features">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=2800&pause=900&color=2EC4B6&center=true&vCenter=true&width=650&lines=Interactive+Job+Heatmap+across+India+%F0%9F%97%BA;Real-time+Salary+%26+Sector+Insights+%F0%9F%92%B0;Smart+Search+%2B+CSV+Export+%F0%9F%94%8D;Onboarding+Wizard+that+personalises+everything+%F0%9F%A7%99" alt="Typing SVG" />
</a>

<br/><br/>

<img src="https://img.shields.io/badge/Python-3.10%2B-2EC4B6?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-Data-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-Compute-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
<img src="https://img.shields.io/badge/Plotly-Viz-3F4F75?style=for-the-badge&logo=plotly&logoColor=white"/>

<br/>

<img src="https://img.shields.io/github/last-commit/TusharMagar/JobLens-India?style=flat-square&color=2EC4B6"/>
<img src="https://img.shields.io/github/repo-size/TusharMagar/JobLens-India?style=flat-square&color=2EC4B6"/>
<img src="https://img.shields.io/badge/status-actively%20maintained-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square"/>

<br/><br/>

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bar%20Chart.png" width="90"/>

**A data analytics dashboard that turns raw job-market data into a story — built for freshers, by a fresher.**

</div>

---

## 📌 Table of Contents

<details open>
<summary>Click to expand</summary>

- [✨ Features](#-features)
- [🎥 Live Preview](#-live-preview)
- [🛠 Tech Stack](#-tech-stack)
- [📂 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
- [🧠 How It Works](#-how-it-works)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [👨‍💻 Author](#-author)

</details>

---

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 🗺 Job Heatmap
Interactive density map of job openings across Indian cities — zoom, hover, and explore hiring hotspots in real time.

### 📊 Market Metrics
Total jobs, average, median & mode salary — the pulse of the market at a glance.

### 📈 Sector Demand
Bar chart of hiring activity by industry, ranked and colour-coded.

### 💰 Salary Distribution
Histogram of salary ranges across roles, so you know exactly where you stand.

### 🏙 Jobs by City
Cities ranked by hiring volume — find where the opportunities actually are.

### 🧠 Skill Analysis
Top 10 most in-demand skills, updated dynamically with your filters.

</td>
<td width="50%" valign="top">

### 🏆 City Leaderboard
Ranked table with market share % — a competitive view of India's job hubs.

### 🏢 Top Companies
Top 8 hiring companies with logos, pulled straight from the dataset.

### 🔍 Smart Search
Instantly filter listings by company or skill — no page reloads.

### 🌙 Dark / Light Mode
One-click theme toggle with smooth CSS transitions.

### 🧙 Onboarding Wizard
A 3-step profile setup that auto-personalises every filter on the dashboard.

### ⬇️ CSV Export
Download your filtered job listings for offline analysis.

</td>
</tr>
</table>

---

## 🎥 Live Preview

<div align="center">

```
┌─────────────────────────────────────────────┐
│   🔍  JobLens India  —  Dashboard Preview    │
├─────────────────────────────────────────────┤
│   [ Heatmap ]  [ Salary Chart ]  [ Sectors ] │
│                                               │
│   ▓▓▓▓▓▓▓▓░░░░  Bengaluru   ████████ 18.2%  │
│   ▓▓▓▓▓▓░░░░░░  Pune        ██████   12.4%  │
│   ▓▓▓▓▓░░░░░░░  Hyderabad   █████    10.1%  │
└─────────────────────────────────────────────┘
```

*Run the app locally to see the full interactive experience — heatmaps, live filters, and animated charts included.*

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/World%20Map.png" width="70"/>

</div>

> 💡 **Tip:** Add real screenshots or a screen-recorded GIF here once deployed —
> drop them in a `/assets` folder and reference them like:
> `![Dashboard Preview](assets/dashboard_demo.gif)`

---

## 🛠 Tech Stack

<div align="center">

| Layer | Tools |
|---|---|
| **Language** | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Framework** | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) |
| **Data Handling** | ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat-square&logo=numpy&logoColor=white) |
| **Visualization** | ![Plotly](https://img.shields.io/badge/-Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white) |

</div>

---

## 📂 Project Structure

```bash
JobLens-India/
│
├── joblens_app.py                 # Main Streamlit application
├── joblens_india_dataset.csv      # Core job listings dataset
├── joblens_company_logos_100.csv  # Company logo mappings
└── README.md                      # You are here 📍
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/TusharMagar/JobLens-India.git
cd JobLens-India
```

### 2️⃣ Install dependencies
```bash
pip install streamlit pandas numpy plotly
```

### 3️⃣ Run the app
```bash
streamlit run joblens_app.py
```

### 4️⃣ Open in browser
Streamlit will auto-launch at:
```
http://localhost:8501
```

<div align="center">
<img src="https://img.shields.io/badge/status-ready%20to%20run-2EC4B6?style=for-the-badge"/>
</div>

---

## 🧠 How It Works

```mermaid
flowchart LR
    A[📂 CSV Datasets] --> B[🐼 Pandas Processing]
    B --> C[🧮 NumPy Aggregation]
    C --> D[📊 Plotly Visualizations]
    D --> E[🖥 Streamlit Dashboard]
    E --> F[🧙 Onboarding Wizard]
    F --> G[🎯 Personalised View]
```

1. **Load** — Job listings & company data are read from CSV.
2. **Wizard** — A 3-step onboarding captures the user's role, city, and skill focus.
3. **Filter** — Inputs personalise the heatmap, charts, and leaderboard live.
4. **Visualize** — Plotly renders interactive charts; Streamlit ties it all together.
5. **Export** — Users can download their filtered view as CSV.

---

## 🗺 Roadmap

- [x] Job heatmap & market metrics
- [x] Onboarding wizard
- [x] Dark/Light mode
- [ ] User accounts & saved searches
- [ ] Live job-board API integration
- [ ] Deploy to Streamlit Community Cloud

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

```bash
# Fork it, then:
git checkout -b feature/your-feature
git commit -m "Add your feature"
git push origin feature/your-feature
```
Open a Pull Request and let's make JobLens even better. ⭐

---

## 👨‍💻 Author

<div align="center">

**Tushar Magar**
Bachelor of Computer Science · Aspiring Data Analyst / Data Scientist

<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
<img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
<img src="https://img.shields.io/badge/Portfolio-2EC4B6?style=for-the-badge&logo=todoist&logoColor=white"/>

<br/><br/>

⭐ **If JobLens India helped you, consider giving it a star!** ⭐

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2C5364,50:203A43,100:0F2027&height=120&section=footer" width="100%"/>

</div>
