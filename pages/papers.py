import streamlit as st


with st.container(gap="medium", horizontal_alignment="right"):
    
    with st.popover("Filters", icon=":material/filter_alt:"):
        selectedYears = st.pills(
            "Year",
            options=["2025", "2024", "2023"],
            selection_mode="multi",
            default=["2025", "2024", "2023"],
        )
        selectedTypes = st.pills(
            "Type",
            options=["Conference", "Chapter", "Preprint", "Workshop", "Technical Report"],
            selection_mode="multi",
            default=["Conference", "Chapter", "Preprint", "Workshop", "Technical Report"],
    )

papers = [
    {
        "year": "2025",
        "type": "Conference",
        "badge_icon": ":material/co_present:",
        "badge_color": "green",
        "title": "HABITS: An Early-Warning Intelligent System Integrating Remote Sensing and Deep Learning for Harmful Algal Bloom Detection and Species Identification",
        "authors": "Erru Torculas and Sherlon Salupas",
        "caption": "8th International Conference for Fisheries and Aquatic Sciences (ICFAS), Iloilo City, Philippines, November 2025",
    },
    {
        "year": "2025",
        "type": "Preprint",
        "badge_icon": ":material/draft:",
        "badge_color": "grey",
        "title": "Toward Sustainable Computing in Hyperscale Data Centers: Evaluating Memory Management and Scheduling Mechanisms for Carbon-Aware Resource Management Optimization in Large-Scale Distributed Systems",
        "authors": "Erru Torculas",
        "caption": "Preprint – Abstract Submission",
    },
    {
        "year": "2025",
        "type": "Technical Report",
        "badge_icon": ":material/assignment:",
        "badge_color": "violet",
        "title": "Water Quality Monitoring through Forecasting Chlorophyll-a",
        "authors": "Erru Torculas",
        "caption": "XAI for Public Policy Bootcamp: Data Science for Public Policy, UP Center for Integrative and Development Studies (UP CIDS), University of the Philippines Diliman, Quezon City, Philippines, July 2025",
    },
    {
        "year": "2024",
        "type": "Preprint",
        "badge_icon": ":material/draft:",
        "badge_color": "grey",
        "title": "Atipan Telehealth Project: Modelling the cost of healthcare for Indigenous communities in the Philippines",
        "authors": "Alanna Panes, Alfie Gonzaga, Jimuel Celeste, Jr., Crist John Quema, Jeff Tolentino, Erru Torculas, John Paul Petrola, Romulo de Castro, Arto Ohinmaa",
        "caption": "Preprint – Abstract Submission",
    },
    {
        "year": "2024",
        "type": "Workshop",
        "badge_icon": ":material/podium:",
        "badge_color": "yellow",
        "title": "Community Health Mapping: Reliable Referral Network",
        "authors": "Erru Torculas and Alanna Marie Panes",
        "caption": "University of San Agustin Iloilo, Iloilo City, Philippines, March 2024",
    },
    {
        "year": "2023",
        "type": "Conference",
        "badge_icon": ":material/co_present:",
        "badge_color": "green",
        "title": "frAI: Automated Milkfish (***Chanos chanos***) Fry Detector and Counter Using Machine Learning Classifiers and Computer Vision",
        "authors": "John Markton M. Olarte, Erru G. Torculas, and Francis D. Dimzon",
        "caption": "7th International Conference for Fisheries and Aquatic Sciences (ICFAS 2023), Iloilo City, Philippines, October 2023",
    },
    {
        "year": "2023",
        "type": "Chapter",
        "badge_icon": ":material/book_5:",
        "badge_color": "blue",
        "title": "Forecasting of Energy Consumption in the Philippines Using Machine Learning Algorithms",
        "authors": "Erru G. Torculas, Earl James Rentillo, and Ara Abigail Ambita",
        "caption": "E. Torculas, E. J. Rentillo, and A. A. Ambita, “Forecasting of energy consumption in the Philippines using machine learning algorithms,” in Recent Challenges in Intelligent Information and Database Systems (ACIIDS 2023), N. T. Nguyen et al., Eds. Cham, Switzerland: Springer, 2023, vol. 1863, Communications in Computer and Information Science, pp. 424–435, doi: 10.1007/978-3-031-42430-4_35",
    },
    {
        "year": "2023",
        "type": "Conference",
        "badge_icon": ":material/co_present:",
        "badge_color": "green",
        "title": "Forecasting of Energy Consumption in the Philippines Using Machine Learning Algorithms",
        "authors": "Erru G. Torculas, Earl James Rentillo, and Ara Abigail Ambita",
        "caption": "15th Asian Conference on Intelligent Information and Database Systems (ACIIDS 2023), Phuket, Thailand, July 2023",
    },
    {
        "year": "2023",
        "type": "Conference",
        "badge_icon": ":material/co_present:",
        "badge_color": "green",
        "title": "Comparative Analysis of Machine Learning Models for Energy Consumption Using Time Series Forecasting in the Philippines",
        "authors": "Erru G. Torculas, Earl James Rentillo, and Ara Abigail Ambita",
        "caption": "De La Salle University Research Congress 2023, Manila, Philippines, July 2023",
    },
]

def renderEntry(item):
    with st.container(border=True):
        st.badge(item["type"], icon=item["badge_icon"], color=item["badge_color"])
        st.subheader(f"**{item['title']}**")
        st.markdown(item["authors"])
        st.caption(item["caption"])

filtered = [
    item for item in papers
    if item["year"] in selectedYears
    and item["type"] in selectedTypes
]

# Order by year (latest first)
yearsView = sorted({item["year"] for item in filtered}, reverse=True)

for idx, year in enumerate(yearsView):
    st.subheader(year)

    with st.container(gap="medium"):
        for item in filtered:
            if item["year"] == year:
                renderEntry(item)

    # Divider only between years
    if idx < len(yearsView) - 1:
        st.divider()