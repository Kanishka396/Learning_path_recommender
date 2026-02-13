import streamlit as st
from agents.explainer_agent import explain_skill
from agents.planner_agent import learning_planner_agent
from agents.progress_coach_agent import progress_coach_agent
import sys
import os
import base64

def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


st.set_page_config(layout="wide")
bg_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "assets",
    "bg.jpg"
)

set_bg(bg_path)



# -------------------- CSS Loader --------------------
def load_css():
    css_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "styles",
        "style.css"
    )
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# -------------------- Fix Import Path --------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data.paths import LEARNING_PATHS

# -------------------- Auth Check --------------------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()

# -------------------- Session State Init --------------------
if "completed_skills" not in st.session_state:
    st.session_state.completed_skills = []

# -------------------- Header --------------------
st.markdown("## 🧭 PathFinder Dashboard")
st.caption("Your AI-powered learning companion")

# -------------------- Layout --------------------
col1, col2 = st.columns([2, 1])

# -------------------- Inputs --------------------
with col1:
    goal = st.selectbox(
        "🎓 Career Goal",
        list(LEARNING_PATHS.keys())
    )

    all_skills = LEARNING_PATHS[goal]["skills"]

    completed = st.multiselect(
        "✅ Skills you already know",
        all_skills,
        default=st.session_state.completed_skills
    )

    st.session_state.completed_skills = completed

# -------------------- Progress --------------------
progress = int((len(completed) / len(all_skills)) * 100)

with col2:
    st.metric("📊 Progress", f"{progress}%")
    st.progress(progress)

# -------------------- AI Learning Plan --------------------
st.divider()
st.markdown("## 🤖 PathFinder AI Plan")

agent_result = learning_planner_agent(
    goal=goal,
    all_skills=all_skills,
    completed_skills=completed
)

st.caption(f"Planner source: {agent_result.get('source', 'AI')}")

if agent_result["status"] == "complete":
    st.success("🎉 All skills completed!")

elif agent_result["status"] == "error":
    st.error(agent_result["message"])

else:
    for step in agent_result["plan"]:
        explain = explain_skill(step["skill"], goal)

        st.markdown(f"### 🔹 Priority {step['priority']}: {step['skill']}")
        st.write(f"**Why?** {step['reason']}")

        with st.expander("🤖 AI Insight"):
            st.write(explain["explanation"])

        courses = LEARNING_PATHS[goal]["courses"].get(step["skill"], [])
        if courses:
            st.write("🎓 **Recommended Courses:**")
            for course, link in courses:
                st.markdown(f"- [{course}]({link})")

        st.markdown("---")

# -------------------- PROGRESS COACH --------------------
st.divider()
st.markdown("## 🧠 PathFinder Progress Coach")

coach_result = progress_coach_agent(
    goal=goal,
    completed_skills=completed,
    all_skills=all_skills
)

if coach_result["source"] == "AI":
    st.success("AI Coach Feedback")
else:
    st.info("Coach Feedback (Fallback Mode)")

st.write(coach_result["message"])
pwd