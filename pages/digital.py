import streamlit as st

# st.title("")


col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader(":material/code_blocks: Programming Languages")
        st.write("**Scientific Computing**")
        st.write("Python · R · Fortran · SQL · MATLAB · Wolfram · C/C++")
        st.write("**Web and Mobile Development**")
        st.write("JavaScript · TypeScript · Swift · Kotlin · Dart")
        st.write("**Others**")
        st.write("SQL · Bash · HPCs")
    with st.container(border=True):
        st.subheader(":material/desktop_mac: Operating Systems")
        st.write(" Microsoft Windows, UNIX systems (macOS, Linux - Ubuntu)")

with col2:
    with st.container(border=True):
        st.subheader(":material/analytics: Modeling and Analysis")
        st.write("Tensorflow · SciPy · JupyterLab · Anaconda · NetCDF · Dask · Scikit-learn")
    with st.container(border=True):
        st.subheader(":material/stacked_bar_chart: Data Management and Visualization")
        st.write("Seaborn · Plotly · Matplotlib · Tableau · D3.js · REDCap · Knack")
    
    with st.container(border=True):
        st.subheader(":material/globe_location_pin: Geospatial Tools")
        st.write("QGIS · Google Earth Engine · SentinelHub · Leaflet · Mapbox · Copernicus Data Space Ecosystem")
    


# with st.container():
#     with st.container(horizontal=True, border=True, horizontal_alignment="left", vertical_alignment="center"):
#         st.write("**Operating Systems**")
#         st.write(" Microsoft Windows, UNIX systems (macOS, Linux - Ubuntu) macOS")