import streamlit as st

st.title("Engagements")

sections = [
    "Talks & Workshops",
    "Service & Leadership",
    "Awards & Recognition",
]

selected = st.multiselect(
    "***Contents*** *(Select sections to display)*",
    sections,
    default=sections
)

st.divider()

if "Talks & Workshops" in selected:
    st.header("Talks and Workshops")
    st.write("Working... Under Construction...")

    # with st.container(border=True):
    #     st.badge("Talk", icon=":material/co_present:", color="blue")
    #     st.subheader("Top 10 Finalist - Digital Inclusion Challenge")
    #     st.markdown("Team Hiraya - Philippines")
    #     st.caption("Developed EduBuddy, an SMS-based education platform for the international innovation hackathon. Collaborated with 5 people in Team Hiraya - Philippines. Developed the frontend and backend of the Android mobile application.")
    #     with st.container(horizontal=True, horizontal_alignment="right"):
    #             st.link_button(label="Pitch Video", icon=":material/visibility:", url="https://www.youtube.com/watch?v=zLPdY5lROac")
    #             st.link_button(label="Demo Video", icon=":material/live_tv:", url="https://www.youtube.com/watch?v=zVfpAy1fi4g")

if "Service & Leadership" in selected:
    st.header(":material/person_raised_hand: Service & Leadership")
    with st.container(border=True):
        st.badge("Leadership", icon=":material/school:", color="green")
        st.subheader("Founder - TechForward")
        st.markdown(":yellow-background[TechForward] · :gray[ Regional]")
        st.caption("TechForward is a digital inclusion advocacy that aims to address the 'digital divide, specifically, the issues of digital illiteracy, inaccessibility to and use of technology, and inequitable economic opportunity for out of school youth and children in conflict with the law by creating a digital literacy seminar and ICT skills program and workshop.")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="Link", icon=":material/visibility:", url="https://web.facebook.com/techforward.ph")

    with st.container(border=True):
        st.badge("Leadership", icon=":material/school:", color="green")
        st.subheader("Young Southeast Asian Leaders Initiative - Leader")
        st.markdown(":yellow-background[U.S. Mission to ASEAN & Philippines] · :gray[ International]")
        st.caption("The Young Southeast Asian Leaders Initiative (YSEALI) builds the leadership capabilities of youth in the region and promotes cross-border cooperation to solve regional and global challenges. The YSEALI community consists of bright young leaders, 18–35 years old, from Brunei, Burma, Cambodia, Indonesia, Malaysia, Philippines, Laos, Singapore, Thailand, Timor-Leste and Vietnam who are making a difference in their communities, countries, and the region.")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="Link", icon=":material/visibility:", url="https://asean.usmission.gov/young-southeast-asian-leaders-initiative/")

    with st.container(border=True):
        st.badge("Leadership", icon=":material/school:", color="green")
        st.subheader("Councilor - University Student Council")
        st.markdown(":yellow-background[University of the Philippines Visayas] · :gray[ University]")
        st.caption("Led and supported student communications, public information campaigns, and media initiatives to strengthen student engagement and representation.")
        # with st.container(horizontal=True, horizontal_alignment="right"):
        #         st.link_button(label="Link", icon=":material/visibility:", url="https://asean.usmission.gov/young-southeast-asian-leaders-initiative/")

    with st.container(border=True):
        st.badge("Leadership", icon=":material/school:", color="green")
        st.subheader("Executive Core Committee - Google Developers Student Clubs")
        st.markdown(":yellow-background[University of the Philippines Visayas] · :gray[ University]")
        st.caption("DSC is a community of developers and aspiring developers with a passion to solve real-life problems through technology.")
        # with st.container(horizontal=True, horizontal_alignment="right"):
        #         st.link_button(label="Link", icon=":material/visibility:", url="https://asean.usmission.gov/young-southeast-asian-leaders-initiative/")

    with st.container(border=True):
        st.badge("Leadership", icon=":material/school:", color="green")
        st.subheader("Public Information Officer - UPV Komsai.org")
        st.markdown(":yellow-background[University of the Philippines Visayas] · :gray[ University]")
        st.caption("UPV Komsai.Org is a university-wide organization for anyone who are BS Computer Science students, faculty, and alumni of the University of the Philippines Visayas.")
        # with st.container(horizontal=True, horizontal_alignment="right"):
        #         st.link_button(label="Link", icon=":material/visibility:", url="https://asean.usmission.gov/young-southeast-asian-leaders-initiative/")

if "Awards & Recognition" in selected:
    st.header(":material/social_leaderboard: Awards & Recognition")

    with st.container(border=True):
        st.badge("Scholarship", icon=":material/school:", color="yellow")
        st.subheader("NUS Enterprise Summer Programme in Entrepreneurship")
        st.markdown(":yellow-background[National University of Singapore - TEMASEK Foundation] · :gray[ International]")
        st.caption("Awarded SGD 4,650 for full programme ride in summer school in entrepreneurship in NUS. Among the 5 delegates in the Philippines selected to be part of the programme.")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="NUSSP", icon=":material/visibility:", url="https://enterprise.nus.edu.sg/education-programmes/summer-programme/")

    with st.container(border=True):
        st.badge("Hackathon", icon=":material/smart_toy:", color="blue")
        st.subheader("Champion, Product Category (Collegiate Level) -  AIA LIFEHACKERS 2022: HACKVENTURE")
        st.markdown(":yellow-background[AIA Philippines] · :gray[ National]")
        st.caption("Spearheaded the module policy system architecture ideation in the product and technology category. Ideated the UX and UI design of the web application and supported the team on the data analysis of the insurance landscape.")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="INQUIRER.net", icon=":material/news:", url="https://technology.inquirer.net/123623/aia-philippines-lifehackers-2022-presents-more-innovative-insurance-solutions")
                st.link_button(label="Manila Bulletin", icon=":material/news:", url="https://mb.com.ph/2023/5/10/to-ingenuity-and-beyond-meet-the-winners-of-aia-lifehackers-2023")
                st.link_button(label="UPV News", icon=":material/news:", url="https://www.upv.edu.ph/index.php/news/up-students-emerge-as-winners-of-aia-lifehackers-2022-hackventure-competition")

    with st.container(border=True):
        st.badge("Hackathon", icon=":material/smart_toy:", color="blue")
        st.subheader("Champion - Orange Open Hack: Digital Solutions for VAW-Free Communities")
        st.markdown(":yellow-background[University of the Philippines Visayas] · :gray[ University]")
        st.caption("Developed the user interface and front-end development of the web application that would assist companies in setting up their own VAW reporting desk for VAW-affected employee. Supported the database design and user experience of the solution for streamlining the system’s data and human interaction on the proposed solution.")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="News", icon=":material/news:", url="https://www.upv.edu.ph/index.php/news/upv-joins-18-day-evaw-campaign?fbclid=IwAR272zXriN-zCQ9_9R_ALc7BAqi95LK-GefDblMIKUH0sds-5gOgQIX_SkA")

    with st.container(border=True):
        st.badge("Hackathon", icon=":material/smart_toy:", color="blue")
        st.subheader("Regional Finalist - ASEAN Data Science Explorers")
        st.markdown(":yellow-background[ASEAN Foundation] · :gray[ International]")
        st.caption("Presented the data-driven solution for Municipal Solid Waste (MSW) management in the Philippines, UPTrack, a cloud innovation to mitigate waste generation across ASEAN region on an international scale.")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="ASEAN DSE", icon=":material/visibility:", url="https://aseandse.org/")
                st.link_button(label="Pitch Deck", icon=":material/download:", url="https://aseandse.org/?smd_process_download=1&download_id=9651")

    with st.container(border=True):
        st.badge("Hackathon", icon=":material/smart_toy:", color="blue")
        st.subheader("National Winners (Philippines) - ASEAN Data Science Explorers")
        st.markdown(":yellow-background[ASEAN Foundation] · :gray[ National]")
        st.caption("Ideated and pitched the data-driven solution for waste management in the Philippines incorporating various Sustainable Development Goals (SDG). Created UPTrack, a cloud innovation to mitigate waste generation across ASEAN region. Used critical thinking skills to breakdown waste management problems on Municipal Solid Waste (MSW) in the country, evaluated solutions, and made data-driven decisions to formulate cohesive solutions using SAP Analytics.")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="Department of Foreign Affairs Philippines", icon=":material/account_balance:", url="https://jakartapm.dfa.gov.ph/79-about-asean/697-university-of-the-philippines-visayas-wins-the-asean-data-science-explorers-philippine-national-finals")
                st.link_button(label="News", icon=":material/news:", url="https://goodnewspilipinas.com/up-visayas-team-amplifys-waste-tracker-reps-ph-in-asean-data-science-finals/")

    with st.container(border=True):
        st.badge("Hackathon", icon=":material/smart_toy:", color="blue")
        st.subheader("Second Winner - Youth Social Innovation Lab")
        st.markdown(":yellow-background[Youth Co:Lab, United Nations Development Programme (UNDP)] · :gray[ National]")
        st.caption("Defined clear targets and objectives to communicate to other team members (Team Eunoia). Established EduBuddy for long-range plans. Pitched the project on a nation-wide scale to reach far-flung communities for prototyping.")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="News", icon=":material/news:", url="https://www.rappler.com/hustle/purpose/youth-hackathon-winners-undp-philippines-2021/")

    with st.container(border=True):
        st.badge("Hackathon", icon=":material/smart_toy:", color="blue")
        st.subheader("Top 10 Finalist - Digital Inclusion Challenge")
        st.markdown(":yellow-background[Convergence.tech] · :gray[ International]")
        st.caption("Developed EduBuddy, an SMS-based education platform for the international innovation hackathon. Collaborated with 5 people in Team Hiraya - Philippines. Developed the frontend and backend of the Android mobile application.")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="Pitch Video", icon=":material/visibility:", url="https://www.youtube.com/watch?v=zLPdY5lROac")
                st.link_button(label="Demo Video", icon=":material/live_tv:", url="https://www.youtube.com/watch?v=zVfpAy1fi4g")

    


# · Team Enui