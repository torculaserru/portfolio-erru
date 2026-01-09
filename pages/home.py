import streamlit as st

#st.logo(sidebar_logo, icon_image=main_body_logo)

with st.container():
    col1, col2 = st.columns(2, vertical_alignment="bottom")
    
    with col1:
        with st.container(width=300):
            st.image("assets/sablay.jpg")
    with col2:
        st.title("Erru Torculas")
        st.text("I am a university researcher of the Marine Science Institute at the University of the Philippines Diliman. I work at the intersection of data science, geospatial intelligence, and marine/climate science. I am driven by building forecasting, intelligent systems that integrate AI or machine learning and coastal observations to address environmental issues that are simulated through models over time.", text_alignment="justify")
        with st.container(horizontal=True, horizontal_alignment="distribute"):
            st.link_button("Email", type="secondary",  url="mailto:torculas.erru@gmail.com", icon=":material/mail:")
            st.link_button("Github", type="secondary", url="https://github.com/errutorculas", icon=":material/merge:")
            st.link_button("LinkedIn", type="secondary", url="https://www.linkedin.com/in/errutorculas/", icon=":material/network_node:")
            # st.link_button("Google Scholar", url="https://scholar.google.com/citations?user=YvBpN3oAAAAJ&hl=en", icon=":material/mail:")
            # st.link_button("OCRID", url="https://orcid.org/0009-0004-5351-087X", icon=":material/mail:")

st.divider(width="stretch")

st.subheader("Research Interests")

col1, col2, col3 = st.columns(3)
col1.metric("Research Experience", "2+ years", "1+ year as Software Developer", border=True)
col2.metric("Research Domains", "3", "Marine • Health • AI", border=True)
col3.metric("Citations", "3", "+1 in 2025", border=True)
st.caption("Source: Google Scholar • Updated Jan 2026")


st.markdown(
    '''
    My research interests include (1) :green-badge[:material/modeling: Ecosystem Modeling and Complex Systems] specifically biogeochemical and fuzzy models; (2) :orange-badge[:material/neurology: Machine Learning and Artificial Intelligence (ML/AI)], especially intelligent systems and explainable AI; and (3) :violet-badge[:material/modeling: Geo-information Science and Earth Observation] particularly in energy, marine, and climate sciences.
    '''
)

st.divider(width="stretch")

#st.space("medium")
