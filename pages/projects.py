import streamlit as st

st.title("Projects")

with st.container():
    with st.container():
        col1, col2 = st.columns(2, border=True)
        
        with col1:
            st.badge("Applied Research", icon=":material/co_present:", color="green")
            st.markdown("**frAI: Automated Milkfish (***Chanos chanos***) Fry Detector and Counter Using Machine Learning Classifiers and Computer Vision**")
            #st.markdown("*John Markton M. Olarte, Erru G. Torculas, Francis D. Dimzon*")
            st.caption("frAI is an automated milkfish (*Chanos chanos*) fry detection and counting system designed to address the inefficiencies of traditional fry-counting practices in Philippine aquaculture. Manual head-counting methods are labor-intensive, time-consuming, and prone to significant inaccuracies, particularly in large-scale operations involving thousands of fry. The project introduces a cost-effective, AI-driven solution that leverages computer vision and machine learning classifiers to improve accuracy, efficiency, and scalability in fry counting")
            
            with st.container(horizontal_alignment="right"):
                st.page_link(label="View", icon=":material/visibility:", page="pages/projects/frai.py")
            
        
        with col2:
            st.badge("Applied Research", icon=":material/co_present:", color="green")
            st.markdown("**Atipan+ Health Map: A GIS-Based Health Facility Navigation and Accessibility Platform for Western Visayas**")
            st.caption("Atipan+ Health Map is a web-based geographic information system (GIS) developed to support equitable access to healthcare services in Western Visayas, Philippines. Anchored on the mandates of the Universal Health Care (UHC) Act, the platform consolidates geocoded health facility data and provides location-aware navigation, accessibility analysis, and service discovery—particularly for geographically isolated and disadvantaged areas (GIDAs)")
            st.space(3)
            with st.container(horizontal_alignment="right"):
                st.page_link(label="View", icon=":material/visibility:", page="pages/projects/healthmap.py")
    
        col1, col2 = st.columns(2, border=True)
    
    with st.container():
        with col1:
            st.badge("Applied Research", icon=":material/co_present:", color="green")
            st.markdown("**HABItS: A Harmful Algal Bloom Intelligent System for Early Warning and Community-Centered Coastal Risk Management**")
            st.caption("The Harmful Algal Bloom Intelligent System (HABItS) is an AI-powered early warning platform designed to detect, classify, and forecast harmful algal blooms (HABs) in Philippine coastal waters. The system integrates remote sensing, machine learning-based plankton classification, and local ecological knowledge to transform satellite data and community observations into actionable risk alerts for small-scale fishers and coastal stakeholders")
            
            with st.container(horizontal_alignment="right"):
                st.page_link(label="View", icon=":material/visibility:", page="pages/projects/habits.py")
            
        
        with col2:
            st.badge("Applied Research", icon=":material/co_present:", color="green")
            st.markdown("**Atipan+ Health Map: A GIS-Based Health Facility Navigation and Accessibility Platform for Western Visayas**")
            st.caption("Atipan+ Health Map is a web-based geographic information system (GIS) developed to support equitable access to healthcare services in Western Visayas, Philippines. Anchored on the mandates of the Universal Health Care (UHC) Act, the platform consolidates geocoded health facility data and provides location-aware navigation, accessibility analysis, and service discovery—particularly for geographically isolated and disadvantaged areas (GIDAs)")
            with st.container(horizontal_alignment="right"):
                st.page_link(label="View", icon=":material/visibility:", page="pages/projects/idk.py")
    
