import streamlit as st

st.header("**Atipan+ Health Map: A GIS-Based Health Facility Navigation and Accessibility Platform for Western Visayas**")
st.divider(width="stretch")

st.subheader("Background and Motivation")
st.write("""The UHC Act prioritizes the delivery of health services to underserved and geographically isolated populations to ensure equitable healthcare distribution across the country. However, fragmented health facility data and limited navigational tools pose significant challenges for patients in locating appropriate and timely care.
         
Mapping health facilities serves as a foundational step toward establishing a reliable referral and access system using existing infrastructure, enabling informed health-seeking behavior and improved system efficiency""")
st.image("assets/healthmap/Slide 16_9 - 5.png")
st.divider(width="stretch")

st.subheader("Methodology")
st.image("assets/healthmap/Slide 16_9 - 7.png")

st.subheader("Key Features")
st.image("assets/healthmap/Slide 16_9 - 17.png")
st.image("assets/healthmap/Slide 16_9 - 9.png")
st.image("assets/healthmap/Slide 16_9 - 10.png")
st.image("assets/healthmap/Slide 16_9 - 11.png")
st.image("assets/healthmap/Slide 16_9 - 12.png")
st.image("assets/healthmap/Slide 16_9 - 13.png")

st.divider(width="stretch")
st.subheader("Results and Key Contributions")
st.write("""- Centralized and visualized health facility data for the Western Visayas region""")
st.write("""- Improved spatial awareness of healthcare accessibility""")
st.write("""- Enabled route optimization and informed facility selection""")
st.write("""- Provided a foundational tool for GIS-driven public health planning and referral systems""")

st.divider(width="stretch")
st.subheader("Impact and Applications")
st.write("""Atipan+ Health Map empowers communities—particularly those in GIDAs—by giving users autonomy over their healthcare journeys through informed navigation and service discovery. From a systems perspective, the platform supports evidence-based decision-making in public health planning, resource allocation, and service optimization.
         The tool also lays the groundwork for evaluating changes in health-seeking behavior, knowledge, attitudes, and practices among communities, contributing to improved population health outcomes""")

st.divider(width="stretch")
with st.container():
    with st.container(horizontal=True, border=True, horizontal_alignment="left", vertical_alignment="center"):
        st.write("Deployment")
        st.link_button("Go to the live application",  url="https://atipan-healthmap.netlify.app/", icon=":material/arrow_forward:")
    with st.container(horizontal=True, border=True, horizontal_alignment="left", vertical_alignment="center"):
        st.write("Preliminary Data Visualization")
        st.link_button("Go to Tableau Public",  url="https://public.tableau.com/views/CommunityHealthMap/ReliableReferralNetwork?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link", icon=":material/arrow_forward:")
st.caption("Upon transitioning, last access/maintenance on my end was on September 2024 and any updates beyond that is out of my control. The autonomy is fully transfered within the organization.")
