import streamlit as st

st.header("**HABItS: A Harmful Algal Bloom Intelligent System for Early Warning and Community-Centered Coastal Risk Management**")
st.divider(width="stretch")

st.subheader("Background and Motivation")
st.write("""Harmful algal blooms pose severe ecological, public health, and economic risks to coastal communities. In the Philippines, sudden HAB events—commonly known as red tide—have caused widespread fish kills, shellfish bans, and income losses affecting nearly 40,000 fisherfolk across 22 coastal villages. Existing monitoring systems rely heavily on laboratory testing and centralized advisories, resulting in delayed warnings that are often inaccessible to small-scale fishers.
         
HABItS addresses this gap by providing a **localized**, **timely**, and **intelligible early warning system**, empowering communities to act before HABs escalate into crises.""")

st.divider(width="stretch")
st.subheader("System Concept and Architecture")
st.write("HABItS combines three complementary information streams:")
st.write("""- **Satellite Remote Sensing**: Detection of spatial patterns and temporal trends associated with algal blooms""")
with st.container():
    st.write("**Google Earth Engine - Sentinel 3**")
    st.write("Analyzed using Normalized Difference Chlorophyll Index to isolate pigmented waters through various band")
    st.latex(r'''NDCI= \frac{B5-B4}{B5+B4}''')
    st.caption("B5 is red band wavelength and B4 is the Red-edge band wavelength")
    col1, col2 = st.columns(2, vertical_alignment="center")
    
    with col1:
        st.image("assets/habits/15.png")
        st.image("assets/habits/17.png")
    with col2:
        st.image("assets/habits/16.png")
        st.image("assets/habits/18.png")
    st.caption("Satellite imaging of HABs occurence in Boliano, Pangasinan and verified through a local government shellfish bullettin from the Bureau of Fisheries and Aquatic REsource (BFAR) advising the public of possible Red Tide event in the coastal waters")
st.write("""- **Machine Learning-Based Image Classification**: Identification of toxic and non-toxic phytoplankton species""")
st.image("assets/habits/13.png")
st.write("""- **Community Knowledge & Field Inputs**: Fisherfolk observations and low-cost algal bloom test kits""")


st.divider(width="stretch")
st.subheader("Key Innovations and Key Contributions")
st.write("""- Early species-level identification of HABs to reduce ecological and public health risks""")
st.write("""- Community-centered design that positions fisherfolk as active contributors, not passive recipients""")
st.write("""- Fusion of local knowledge with AI-driven forecasting""")
st.write("""- Scalable framework adaptable to other coastal regions vulnerable to HABs""")

st.divider(width="stretch")
st.subheader("Inteligent System Platform")
st.image("assets/habits/19.png")
st.image("assets/habits/20.png")
st.image("assets/habits/21.png")

st.divider(width="stretch")
st.subheader("Impact and Applications")
st.write("HABItS enhances coastal resilience by enabling:")
st.write("""- Timely decision-making for aquaculture operators and fisherfolk""")
st.write("""- Proactive management of shellfish harvesting and fish cage operations""")
st.write("""- Improved coordination between communities and regulatory agencies""")
st.write("""- Reduction of economic losses and health risks associated with delayed HAB detection""")