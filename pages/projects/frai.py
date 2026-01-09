import streamlit as st
import pandas as pd

st.header("**frAI: Automated Milkfish (***Chanos chanos***) Fry Detector and Counter Using Machine Learning Classifiers and Computer Vision**")
#st.write("**John Markton M. Olarte, Erru G. Torculas, Francis D. Dimzon**")
#st.caption("Department of Computer Science, University of the Philippines Visayas")
st.divider(width="stretch")


st.image("assets/frai/1.png")
st.subheader("Background and Motivation")
st.write("""Aquaculture accounts for more than half of the Philippines’ total fisheries production, with milkfish (“bangus”) serving as the backbone of the industry. In 2022 alone, aquaculture contributed 54.1% of total fisheries output, while milkfish production reached over 442 thousand metric tons, showing a steady increase over recent years.
         
Despite this growth, fry acquisition and counting remain critical bottlenecks in seed production and pond stocking. Existing methods fail to scale efficiently and lack technological support tailored for high-volume fry handling, motivating the development of an automated, image-based solution.""")
st.divider(width="stretch")

st.image("assets/frai/7.png")

with st.container():
    st.subheader("Image Processing")
    col1, col2 = st.columns(2, vertical_alignment="center")
    
    with col1:
        st.image("assets/frai/8.png")
        st.image("assets/frai/9.png")
        st.image("assets/frai/10.png")
    with col2:
        st.image("assets/frai/11.png")
        st.image("assets/frai/12.png")
        st.image("assets/frai/13.png")
    
    st.image("assets/frai/14.png")

st.divider(width="stretch")
st.subheader("Results and Key Contributions")
results = pd.DataFrame(
    {   
        #"Fry Count": [100, 200, 300, 400],
        "Mean": [99.98, 199.96, 300.14, 400.26],
        "Standard Deviation": [5.046, 16.803, 22.944, 32.104],
        "Minimum": [90, 156, 251, 346],
        "Maximum": [116, 270, 371, 473],
    },
    index=["100", "200", "300", "400"],
)
st.table(results)
st.caption("A table of Descriptive statistics of each fry counts")
st.write("""- Demonstrated accurate detection and counting of milkfish fry at varying densities""")
st.write("""- Improved robustness of contour detection through morphological grid search: accuracy of *100* and *200* fry counts - **99.98%**, *300* - **99.95%**, *400* - **99.94%**""")
st.write("""- Validated the feasibility of low-cost AI solutions for aquaculture operations""")
st.write("""- Showed strong potential for reducing labor costs and human error in fry counting""")
models = pd.DataFrame(
    {   
        "Accuracy (in %)": ["100", "100", "98.39"],
    },
    index=["k-Nearest Neighbors", "Random Forest", "XGBoost"],
)


st.table(models)
st.caption("A table of accuracy of machine learning classifiers")

st.divider(width="stretch")
st.image("assets/frai/18.png")
st.subheader("Impact and Applications")
st.write("""The frAI system enables fish farmers to determine optimal stocking densities, leading to better pond management, increased production efficiency, and improved profitability. Beyond operational gains, the project highlights how AI adoption in fisheries can contribute to sustainable aquaculture practices and data-driven decision-making in developing economies""")