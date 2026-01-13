import streamlit as st

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader(":material/code_blocks: Programming Languages")
        st.write("**Scientific Computing**")
        with st.container(horizontal=True, horizontal_alignment="center", vertical_alignment="center"):
            st.image("assets/digital/Python.png", width=25)
            st.write("Python")

            st.image("assets/digital/rstudio.png", width=30)
            st.write("R")
            
            st.image("assets/digital/fortran.png", width=30)
            st.write("Fortran")

            st.image("assets/digital/matlab.png", width=30)
            st.write("MATLAB")

            st.image("assets/digital/wolfram.png", width=40)
            st.write("Wolfram")

            st.image("assets/digital/c++.png", width=30)
            st.write("C/C++")

            st.image("assets/digital/java.png", width=40)
            st.write("Java")

            st.image("assets/digital/sql.png", width=50)
            st.write("SQL")

        st.write("**Web and Mobile Development**")
        with st.container(horizontal=True, horizontal_alignment="center", vertical_alignment="center"):
            st.image("assets/digital/js.png", width=30)
            st.write("Javascript")

            st.image("assets/digital/ts.png", width=30)
            st.write("Typescript")

            st.image("assets/digital/swift.png", width=30)
            st.write("Swift")

            st.image("assets/digital/kotlin.png", width=30)
            st.write("Kotlin")

            st.image("assets/digital/dart.png", width=30)
            st.write("Dart")

        st.write("**Others**")
        with st.container(horizontal=True, horizontal_alignment="center", vertical_alignment="center"):
            st.image("assets/digital/bash.png", width=30)
            st.write("Bash")
    with st.container(border=True):
        st.subheader(":material/desktop_mac: Operating Systems")

        with st.container(horizontal=True, horizontal_alignment="center", vertical_alignment="center"):
            st.image("assets/digital/windows.png", width=50)
            st.write("Microsoft Windows")
            
            st.image("assets/digital/unix.png", width=80)
            st.image("assets/digital/macos.png", width=30)
            st.write("macOS")

            st.image("assets/digital/ubuntu.png", width=50)
            st.write("Ubuntu (Linux)")

with col2:
    with st.container(border=True):
        st.subheader(":material/analytics: Modeling and Analysis")
        with st.container(horizontal=True, horizontal_alignment="center", vertical_alignment="center"):
            st.image("assets/digital/tensorflow.png", width=30)
            st.write("Tensorflow")

            st.image("assets/digital/scipy.png", width=30)
            st.write("Scipy")

            st.image("assets/digital/jupyter.png", width=30)
            st.write("Jupyter")

            st.image("assets/digital/anaconda.png", width=30)
            st.write("Anaconda")

            st.image("assets/digital/netcdf.png", width=30)
            st.write("NetCDF")

            st.image("assets/digital/dask.png", width=30)
            st.write("Dask")

            st.image("assets/digital/scikit.png", width=40)
            st.write("Scikit-learn")

    with st.container(border=True):
        st.subheader(":material/stacked_bar_chart: Data Management and Visualization")
        with st.container(horizontal=True, horizontal_alignment="center", vertical_alignment="center"):
            st.image("assets/digital/seaborn.png", width=30)
            st.write("Seaborn")

            st.image("assets/digital/plotly.png", width=100)
            st.write("Plotly")

            st.image("assets/digital/matplotlib.png", width=30)
            st.write("Matplotlib")

            st.image("assets/digital/tableau.png", width=40)
            st.write("Tableau")

            st.image("assets/digital/d3.jpg", width=30)
            st.write("D3.js")

            st.image("assets/digital/redcap.png", width=30)
            st.write("REDCap")

            st.image("assets/digital/powerbi.png", width=30)
            st.write("Power BI")
    
    with st.container(border=True):
        st.subheader(":material/globe_location_pin: Geospatial Tools")
        with st.container(horizontal=True, horizontal_alignment="center", vertical_alignment="center"):
            st.image("assets/digital/qgis.png", width=30)
            st.write("QGIS")

            st.image("assets/digital/googleeart.png", width=30)
            st.write("Google Earth Engine")

            st.image("assets/digital/sentinelhub.png", width=30)
            st.write("SentinelHub")

            st.image("assets/digital/mapbox.png", width=80)
            st.write("Mapbox")