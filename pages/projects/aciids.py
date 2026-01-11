import streamlit as st
import pandas as pd

st.header("**Forecasting of Energy Consumption in the Philippines Using Machine Learning Algorithms**")
st.divider(width="stretch")

st.subheader("Background and Motivation")
st.write("""The Philippines faces persistent challenges in energy sustainability, high electricity costs, and energy insecurity—issues that were further intensified by the COVID-19 pandemic. Accurate energy consumption forecasting is critical for informed policy-making, grid reliability, and sustainable energy planning. This project explores how machine learning models can improve national-level energy demand forecasting, particularly under disruptive conditions.
         
In the Philippines, the average energy consumption per person reached a peak of 5,205 kWh in 2019 and has been relatively increasing in each year prior. Some notable trends which follow this annual increase include country energy consumption (peaked at 563 TWh in 2019), country electricity generation (peaked at 108.27 TWh in 2021), and average electricity generation per person (peaked at 961 KWh in 2019). The work addresses a critical gap in developing-country contexts, where energy datasets are often limited, inconsistent, or aggregated, yet are essential for evidence-based energy planning and policy formulation.""")
st.image("assets/aciids/aciids-1.png")
st.divider(width="stretch")

st.subheader("Data and Methodology")

st.image("assets/aciids/aciids2.png")
st.image("assets/aciids/aciids3.png")

st.subheader("Evaluation Metrics ")

st.subheader("Evaluation Metrics ")
st.write("""**Root Mean Square Error**""")
st.latex(r'''RMSE = \sqrt{\frac{\sum_{i=1}^{n}(x_{1,i} - x_{2,i})^2}{n}}''')
st.write(""" > RMSE measures the di↵erences between the predicted and actual values and therefore a means to measure the quality of fit between the actual data and predicted model. It is preferred over the standard Mean Square Error (MSE) since it is a smaller value and can be compared more straightforwardly.""")

st.write("""**Mean Absolute Percentage Error**""")
st.latex(r'''MAPE = \frac{1}{n}\sum_{i=1}^{n}\left | \frac{x_{1,i} - x_{2,i}}{x_{1,i}} \right | \times 100''')
st.write(""" > MAPE is one of the metrics of evaluation used in this paper since it relatively measures how accurate the forecast system is. It measures forecast accuracy as the average percentage difference between forecasted and actual values, making it easy to interpret.""")

st.divider(width="stretch")
st.subheader("Results and Key Findings")
st.image("assets/aciids/aciids4.png")
st.caption("Performance of the models by period")
with st.container(horizontal=True, horizontal_alignment="distribute"):
    st.image("assets/aciids/aciids5.png")
    st.image("assets/aciids/aciids6.png")
st.caption("Machine learning models forecast in Pre-pandemic and Pandemic Period")

st.write("""- **XGBoost** achieved the highest accuracy during the pre-pandemic period, capturing stable long-term consumption trends.""")
st.write("""- **Random Forest** performed best during the pandemic period, demonstrating stronger adaptability to abrupt behavioral and economic shifts.""")
st.write("""- Tree-based models consistently outperformed linear approaches, highlighting their robustness to non-linear and disrupted time-series data.""")

with st.container(horizontal=True, horizontal_alignment="distribute"):
    st.image("assets/aciids/aciids7.png")
    st.image("assets/aciids/aciids8.png")
st.divider(width="stretch")

st.subheader("Impact and Relevance")
st.write("""This study demonstrates the **practical viability of machine learning for national energy forecasting in a developing-country context**, even with limited and aggregated data. The results support the use of data-driven forecasting tools by:""")
st.write("""- Energy planners and policymakers""")
st.write("""- Power market operators""")
st.write("""- Sustainability and energy efficiency initiatives""")
st.write("""The work provides a foundation for future high-resolution, seasonal, and climate-aware energy forecasting studies""")

st.divider(width="stretch")
with st.container():
    with st.container(horizontal=True, border=True, horizontal_alignment="left", vertical_alignment="center"):
        st.write("Paper link")
        st.link_button("See PDF file",  url="https://www.researchgate.net/publication/374284253_Forecasting_of_Energy_Consumption_in_the_Philippines_Using_Machine_Learning_Algorithms", icon=":material/picture_as_pdf:")
    # with st.container(horizontal=True, border=True, horizontal_alignment="left", vertical_alignment="center"):
    #     st.write("Preliminary Data Visualization")
    #     st.link_button("Go to Tableau Public",  url="https://public.tableau.com/views/CommunityHealthMap/ReliableReferralNetwork?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link", icon=":material/arrow_forward:")
# st.caption("Upon transitioning, last access/maintenance on my end was on September 2024 and any updates beyond that is out of my control. The autonomy is fully transfered within the organization.")
