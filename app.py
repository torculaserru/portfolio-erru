import streamlit as st


#.venv\Scripts\activate.bat


iconLogo = "assets/erru-logo-black.png"
st.logo(iconLogo)

st.set_page_config(
    page_title="Erru Torculas",
    page_icon="assets/erru.png",
    layout="centered",
)


pages = {
    "": [
        st.Page("pages/home.py", title="Erru Torculas", default=True),
        st.Page("pages/papers.py", title="Papers", icon=":material/stacks:"),
        st.Page("pages/talks.py", title="Talks", icon=":material/comic_bubble:"),
        st.Page("pages/projects.py", title="All Projects", icon=":material/tactic:"),
    ],
    "Projects": [
        st.Page("pages/projects/frai.py", title="frAI", icon=":material/eye_tracking:"),
        st.Page("pages/projects/healthmap.py", title="ATIPAN Health Map", icon=":material/health_metrics:"),
        st.Page("pages/projects/habits.py", title="HABiTS", icon=":material/microbiology:"),
        st.Page("pages/projects/idk.py", title="ATIPAN Health Map", icon=":material/health_metrics:"),
        # st.Page("pages/projects/frai.py", title="frAI", icon=":material/eye_tracking:"),
        # st.Page("pages/projects/frai.py", title="frAI", icon=":material/eye_tracking:"),
        #st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages, position="top")
pg.run()