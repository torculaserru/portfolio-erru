import streamlit as st

st.title("Projects")

with st.container():
    with st.container():
        col1, col2 = st.columns(2, border=True)
        
        with col1:
            with st.container(horizontal=True):
                st.badge("Applied Research", icon=":material/co_present:", color="green")
                st.badge("Conference Paper", icon=":material/podium:", color="violet")
            st.markdown("**frAI: Automated Milkfish (***Chanos chanos***) Fry Detector and Counter Using Machine Learning Classifiers and Computer Vision**")
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
        
    with st.container():
        col1, col2 = st.columns(2, border=True)

        with col1:
            with st.container(horizontal=True):
                st.badge("Applied Research", icon=":material/co_present:", color="green")
                st.badge("Conference Paper", icon=":material/podium:", color="violet")
            st.markdown("**HABITS: An Early-Warning Intelligent System Integrating Remote Sensing and Deep Learning for Harmful Algal Bloom Detection and Species Identification**")
            st.caption("The Harmful Algal Bloom Intelligent System (HABItS) is an AI-powered early warning platform designed to detect, classify, and forecast harmful algal blooms (HABs) in Philippine coastal waters. The system integrates remote sensing, machine learning-based plankton classification, and local ecological knowledge to transform satellite data and community observations into actionable risk alerts for small-scale fishers and coastal stakeholders")
            
            with st.container(horizontal_alignment="right"):
                st.page_link(label="View", icon=":material/visibility:", page="pages/projects/habits.py")
            
        
        with col2:
            with st.container(horizontal=True):
                st.badge("Applied Research", icon=":material/co_present:", color="green")
                st.badge("Peer-reviewed Paper", icon=":material/grading:", color="violet")
            st.markdown("**Forecasting Energy Consumption in the Philippines Using Machine Learning Algorithms**")
            st.caption("This research investigates the use of machine learning algorithms to forecast national energy consumption in the Philippines, with particular emphasis on structural changes introduced by the COVID-19 pandemic. By modeling both pre-pandemic and pandemic periods, the study evaluates how different machine learning approaches respond to abrupt socio-economic disruptions in time-series energy data.")
            with st.container(horizontal=True, horizontal_alignment="right", vertical_alignment="center"):
                st.link_button("Paper", type="tertiary", url="https://doi.org/10.1007/978-3-031-42430-4_35", icon=":material/attach_file:")
                st.page_link(label="View", icon=":material/visibility:", page="pages/projects/aciids.py")

        
    with st.container():
        col1, col2 = st.columns(2, border=True)
        
        with col1:
            with st.container(horizontal=True):
                st.badge("Applied Research", icon=":material/co_present:", color="green")
                st.badge("Special Problem/Undergraduate Thesis", icon=":material/podium:", color="violet")
            st.markdown("**HanApp: A Missing Persons Reporting and Alerting Application Suite in the Philippines**")
            st.caption("Missing persons cases remain a major issue in the Philippines, occurring not only after catastrophes but also in everyday situations. Existing attempts of the Philippine National Police (PNP) make scant use of modern technologies and lack community-driven processes. To fill these deficiencies, the researchers created HanApp, a mobile application that simplifies missing person reporting, case management, and verification while allowing for community-based search operations. The system was built using the Flutter Framework for cross-platform deployment and includes Google Location Services, Google Maps APIs, and Firebase for serverless backend, database, and storage.")
            
            with st.container(horizontal_alignment="right"):
                st.link_button("Paper", type="tertiary", url="https://github.com/HanApp-MissingPersons/HanApp_SP/blob/main/Written%20Outputs/SP_FinalPaper/HanApp_SP_FinalPaper_FinalRev_SIGNED.pdf", icon=":material/attach_file:")
            
        
        with col2:
            st.badge("Concept Research", icon=":material/co_present:", color="yellow")
            st.markdown("**A Hybrid BFM–ANFIS Modeling Framework for Predicting Phytoplankton Assemblage Composition and Productivity in Philippine Coastal Waters**")
            st.caption("This project proposes a hybrid ecosystem modeling framework that integrates the mechanistic strengths of the Biogeochemical Flux Model coupled with NEMO (BFM-NEMO) and the adaptive learning capabilities of an Adaptive Neuro-Fuzzy Inference System (ANFIS) to improve predictions of phytoplankton assemblage composition and productivity. The framework is designed to enhance ecosystem-based management (EBM) by providing interpretable, data-driven, and process-aware forecasts of lower-trophic dynamics under climate variability and anthropogenic pressure in Philippine coastal systems")
            st.space(3)
            with st.container(horizontal_alignment="right"):
                st.page_link(label="View", icon=":material/visibility:", page="pages/projects/healthmap.py", disabled=True)
    