import streamlit as st
from streamlit_extras.buy_me_a_coffee import button

version: str = "0.0.1"
logo_gif: str = (
    "https://media1.tenor.com/m/d54XfQ2BGwcAAAAd/raccoon-circle-dance-round.gif"
)
coffee_username: str = "astrayn"

if "current_question_idx" not in st.session_state:
    st.session_state.current_question_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "attempted_questions" not in st.session_state:
    st.session_state.attempted_questions = set()
if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 1

# Page setup
HomePage = st.Page(page="pages/Main.py", icon="🏠", title="Main", default=True)

AboutPage = st.Page(page="pages/About.py", icon="👤", title="About")

# Navigation Bar
pg = st.navigation([HomePage, AboutPage])

total_questions = st.session_state.total_questions
st.logo(logo_gif, size="large")
with st.sidebar:
    st.header("Progress")
    st.progress(len(st.session_state.attempted_questions) / total_questions)
    st.write(
        f"Questions attempted: {len(st.session_state.attempted_questions)}/{total_questions}"
    )
    st.markdown(9 * "<br>", unsafe_allow_html=True)
    st.caption("Support me by clicking on this button 👇")
    button(username=coffee_username, floating=False, width=221)
    st.caption(version)
pg.run()
