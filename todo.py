import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Goutam Gulati | Student AI Dashboard",
    page_icon="🎓",
    layout="wide",
)

# Custom High-Tech Styling (Glassmorphism & Glowing Accents)
st.markdown(
    """
<style>
    /* Dark Futuristic Theme */
    .stApp {
        background: #0b0f19;
        color: #e2e8f0;
    }
    
    /* Header Card */
    .profile-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.7);
        margin-bottom: 25px;
    }
    
    .profile-name {
        font-size: 32px;
        font-weight: 900;
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    
    .badge-gold {
        background: linear-gradient(90deg, #f59e0b, #d97706);
        color: white;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 700;
        display: inline-block;
        margin-right: 8px;
    }
    
    .badge-blue {
        background: linear-gradient(90deg, #0284c7, #2563eb);
        color: white;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 700;
        display: inline-block;
    }
    
    /* Metric Cards */
    div[data-testid="stMetricValue"] {
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        color: #38bdf8 !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Top Profile Banner
st.markdown(
    """
    <div class="profile-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <span class="badge-gold">⭐ TOP 1% RANKER</span>
                <span class="badge-blue">⚡ AQUARIUS TECH LEAD</span>
                <h1 class="profile-name" style="margin-top: 10px;">🎓 GOUTAM GULATI</h1>
                <p style="color: #94a3b8; margin-top: 5px; font-size: 16px;">
                    <b>Course:</b> BCA (Bachelor of Computer Applications) | <b>Semester:</b> 3rd Sem | <b>College:</b> Hindu College
                </p>
            </div>
            <div style="text-align: right;">
                <h3 style="color: #38bdf8; margin: 0;">STATUS: ACTIVE</h3>
                <p style="color: #4ade80; margin: 0;">✔️ Verified Academic Profile</p>
            </div>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# Quick Overview KPIs
st.subheader("📊 Academic Overview & Live Metrics")
col1, col2, col3, col4 = st.columns(4)

col1.metric("📅 Attendance", "91%", delta="+4% Above Safe Zone")
col2.metric("🏆 Current CGPA", "9.4 / 10", delta="Top 5 in Class")
col3.metric("📚 Active Subjects", "6 Core Subjects")
col4.metric("📝 Pending Tasks", "2 Assignments", delta="-3 Completed")

st.divider()

# Main Grid: Subject Performance & Interactive Analytics
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.subheader("🎯 Subject Wise Mastery & Progress")

    subjects_data = {
        "Subject": [
            "Python Programming",
            "Web Development",
            "DBMS (Database)",
            "Operating Systems",
            "Computer Networks",
            "Mathematics",
        ],
        "Score": [95, 92, 90, 88, 85, 82],
        "Status": [
            "Outstanding",
            "Excellent",
            "Very Good",
            "Very Good",
            "Good",
            "Good",
        ],
    }
    df_sub = pd.DataFrame(subjects_data)

    for index, row in df_sub.iterrows():
        c1, c2 = st.columns([3, 1])
        c1.write(f"*{row['Subject']}* — {row['Score']}% ({row['Status']})")
        c1.progress(row["Score"] / 100)

with col_right:
    st.subheader("🤖 Smart Attendance Simulator")
    st.caption(
        "Unique Feature: Calculate how many future classes you need to attend!"
    )

    total_classes = st.slider(
        "Total Classes Conducted",
        min_value=50,
        max_value=150,
        value=100,
        step=5,
    )
    attended_classes = st.slider(
        "Classes Attended",
        min_value=30,
        max_value=total_classes,
        value=91,
        step=1,
    )

    current_att = (attended_classes / total_classes) * 100
    st.info(f"Current Calculated Attendance: *{current_att:.1f}%*")

    if current_att >= 75:
        st.success("✅ Safe Zone! You are eligible for Exams.")
    else:
        st.error("⚠️ Medical/Attendance Alert: Below 75% limit!")

st.divider()

# Technical Skills & Placement Readiness Index (Super Unique)
st.subheader("⚡ Skill & Placement Readiness Radar")
s_col1, s_col2, s_col3, s_col4 = st.columns(4)

s_col1.markdown(
    "*🐍 Python / Data Science*\n\n`PRO LEVEL` ⭐⭐⭐⭐⭐\n\nStreamlit & Pandas Mastery"
)
s_col2.markdown(
    "*💻 Web Technologies*\n\n`ADVANCED` ⭐⭐⭐⭐☆\n\nHTML, CSS, JavaScript"
)
s_col3.markdown(
    "*🗄️ SQL & Databases*\n\n`INTERMEDIATE` ⭐⭐⭐⭐☆\n\nQueries & Schema Design"
)
s_col4.markdown(
    "*🚀 Problem Solving*\n\n`ACTIVE` ⭐⭐⭐⭐⭐\n\nDSA & Logic Building"
)

st.divider()

# Upcoming Deadlines / Schedule Table
st.subheader("📅 Recent Submissions & Action Center")
action_data = [
    {
        "Subject": "Python Streamlit Project",
        "Deadline": "2026-08-20",
        "Status": "Completed ✅",
        "Priority": "High",
    },
    {
        "Subject": "DBMS SQL Assignment",
        "Deadline": "2026-08-22",
        "Status": "In Progress ⏳",
        "Priority": "Medium",
    },
    {
        "Subject": "Computer Networks Lab File",
        "Deadline": "2026-08-25",
        "Status": "Pending 🔴",
        "Priority": "High",
    },
]
st.dataframe(pd.DataFrame(action_data), use_container_width=True)

st.markdown(
    "<br><hr><center><small>Designed & Developed by <b>Goutam Gulati</b> | High-Tech Student Portal v2.0</small></center>",
    unsafe_allow_html=True,
)
