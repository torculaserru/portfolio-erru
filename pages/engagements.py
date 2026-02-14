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
    st.header(":material/comic_bubble: Talks and Workshops")

    with st.container(border=True):
        with st.container(horizontal=True):
            st.badge("Workshop", icon=":material/crowdsource:", color="orange")
            st.badge("Facilitator & Speaker", icon=":material/emoji_people:", color="violet")
        st.subheader("Ocean Data and BN-GIS Training as Support Tools for Marine Spatial Planning")
        st.markdown(":yellow-background[Bureau of Fisheries and Aquatic Resources (BFAR) - FMA9 [FishCORE]] · :gray[ National]")
        st.caption("Training to equip coastal and marine practitioners with the skills to obtain and process ocean data (model and observational), build simple Bayesian Network decision-support tool, and integrate with GIS for marine spatial planning and resource management. The event was held on November 11-14 in Cagayan de Oro, Philippines")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="Link", icon=":material/visibility:", url="https://www.canva.com/design/DAG3yt0CnVg/m3_-fhFdiTdg5KlVQ4zE6w/view?utm_content=DAG3yt0CnVg&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h30ac553f59")

    with st.container(border=True):
        with st.container(horizontal=True):
            st.badge("Workshop", icon=":material/crowdsource:", color="orange")
            st.badge("Participant", icon=":material/emoji_people:", color="violet")
        st.subheader("Cloud Native Ocean Data Analysis and Visualisation School")
        st.markdown(":yellow-background[CMCC, the University of Bologna, and EGI] · :gray[ International]")
        st.caption("Intensive, week-long training offers a unique opportunity for students and researchers to gain hands-on experience in coastal ocean modelling on the cloud, held on October 13-17, 2025 at the University of Bologna, Aula Biomedica, Department of Physics (Viale Berti Pichat 6/2)")
        # with st.container(horizontal=True, horizontal_alignment="right"):
        #         st.link_button(label="Link", icon=":material/visibility:", url="https://www.canva.com/design/DAG3yt0CnVg/m3_-fhFdiTdg5KlVQ4zE6w/view?utm_content=DAG3yt0CnVg&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h30ac553f59")

    with st.container(border=True):
        with st.container(horizontal=True):
            st.badge("Talk", icon=":material/record_voice_over:", color="yellow")
            #st.badge("Speaker", icon=":material/emoji_people:", color="violet")
        st.subheader("AI For Nature - Driving Sustainable Development Through AI and Greentech in the Philippines")
        st.markdown(":yellow-background[Kenan Foundation Asia & AI Futuremakers] · :gray[ National]")
        st.caption("Student-driven initiative supported by Kenan Foundation Asia through the 2025 YSEALI AI FutureMakers, dedicated to applying AI for marine conservation, empowering youth with tech and leadership for environmental protection.")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="Link", icon=":material/visibility:", url="https://www.facebook.com/ai4nature")
    
    with st.container(border=True):
        with st.container(horizontal=True):
            st.badge("Workshop", icon=":material/crowdsource:", color="orange")
            st.badge("Participant", icon=":material/emoji_people:", color="violet")
        st.subheader("AI Futuremakers - 2025 YSEALI Regional Workshop")
        st.markdown(":yellow-background[Young Southeast Asian Leaders Initiative (YSEALI) & Kenan Foundation Asia] · :gray[ International]")
        st.caption("The YSEALI AI FutureMakers Regional Workshop, held June 1-6 in Chonburi, Thailand, is an immersive, week-long program that brought together 56 youth leaders, social entrepreneurs, and tech enthusiasts from 11 countries across ASEAN and Timor-Leste. Fully funded by the U.S. Department of State and organized by the U.S. Embassy in Bangkok and Kenan Foundation Asia, the workshop focused on accelerating social impact through AI tools and innovation.")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="Link", icon=":material/visibility:", url="https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.kenan-asia.org%2Fmedias%2Fyseali-aifuturemaker%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHtXvqN4jozXYRYJSousNSXlowYRRicCrI9N67QkMOk6_P80GVti9FAVuAaYp_aem_2HpFJu0DCNYMlhdpznXWSg&h=AT0mCofXGMnLkWUnMPHIbee7LYFkIpNepqeL5gX_lfjPN9O5aWpgwXfevocAZ5mbujP6S7gmi7JE1f-XytdPzTnRGV0DL6GRKnutY08d-KOx62H6lQ8zr3gCTNmja2YfTfsepg-ZkSUmn_yA&__tn__=H-R&c[0]=AT0qaiB0MZylWSAXmj4zEVLUO9LSuLH_noeYy6C_OjRao_suuCCx3h99hj2AlMqXPz2mMLiNpn0TG2kKLFtc5gOH-HGe1lacG4QhmS_UGfpjWi6eUdg_-RhMr1eVL_z_LaIQs-zX2GzPT5woasfvvNFY8YanMFGkJBrTBSleQ6A7JT5j0VIeSiVtyXdPbZNIM5txSFImoVHXeXBI2tz4CMaG")

    with st.container(border=True):
        with st.container(horizontal=True):
            st.badge("Workshop", icon=":material/crowdsource:", color="orange")
            st.badge("Participant", icon=":material/emoji_people:", color="violet")
        st.subheader("Explainable Artificial Intelligence (XAI) for Public Policy: AI Informed Human Directed Public Policy Making")
        st.markdown(":yellow-background[The UP Center for Integrative and Development Studies Program on Data Science for Public Policy (UP CIDS-DSPPP)] · :gray[ Bootcamp]")
        st.caption("This bootcamp aims to empower the participants with the knowledge and practical skills needed to advance beyond the basics. Covering XAI in greater depth, fundamentals of Data Science and its Application to Artificial Intelligence using machine learning and traversing through the complexities of GIS alongside Governance Informatics (GI) and Big Data Analytics (BDA).")
        # with st.container(horizontal=True, horizontal_alignment="right"):
        #         st.link_button(label="Link", icon=":material/visibility:", url="https://drive.google.com/file/d/1y6F1M6s79SlUfY2HydflLF98f4FRMVuo/view?usp=sharing")

    with st.container(border=True):
        with st.container(horizontal=True):
            st.badge("Workshop", icon=":material/crowdsource:", color="orange")
            st.badge("Participant", icon=":material/emoji_people:", color="violet")
        st.subheader("Ocean Data Management")
        st.markdown(":yellow-background[OceanTeacher Global Academy - The International Oceanographic Data and Information Exchange (IODE) of the Intergovernmental Oceanographic Commission (IOC) of UNESCO] · :gray[ Training Course]")
        st.caption("Training course that is designed for marine data managers, data stewards and researchers, working in institutions responsible for the collection and good management of marine data. An introduction to several general aspects related to the management of marine data, including data formats, metadata, quality control, data policy, data sharing and publishing, data management plans and the research data life cycle.")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="Link", icon=":material/visibility:", url="https://drive.google.com/file/d/1y6F1M6s79SlUfY2HydflLF98f4FRMVuo/view?usp=sharing")
    
    with st.container(border=True):
        with st.container(horizontal=True):
            st.badge("Workshop", icon=":material/crowdsource:", color="orange")
            st.badge("Facilitator · Media", icon=":material/emoji_people:", color="violet")
        st.subheader("Local Stakeholders' Summit")
        st.markdown(":yellow-background[University of the Philippines Center for Research and Awareness of Diverse Living Environments (UP CRADLE)] · :gray[ National]")
        st.caption("The Local Stakeholders' Summit (LSS) was held last March 18-19, 2025, at the UP Center for Research and Awareness of Diverse Living Environments (CRADLE), Puerto Galera. The event brought together dedicated individuals and organizations to discuss the sustainable management of the 𝗣𝘂𝗲𝗿𝘁𝗼 𝗚𝗮𝗹𝗲𝗿𝗮 𝗕𝗶𝗼𝘀𝗽𝗵𝗲𝗿𝗲 𝗥𝗲𝘀𝗲𝗿𝘃𝗲 (𝗣𝗚𝗕𝗥). Through meaningful dialogue, collaboration, and community-driven solutions, we took a step forward in strengthening environmental resilience and local livelihoods.")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="Link", icon=":material/visibility:", url="https://www.facebook.com/share/p/1B46yyLvRR/")

    with st.container(border=True):
        with st.container(horizontal=True):
            st.badge("Workshop", icon=":material/crowdsource:", color="orange")
            st.badge("Participant & Facilitator", icon=":material/emoji_people:", color="violet")
        st.subheader("COMPASS Philippines - Coastal Observing and Modeling for Prediction and Assessment to Support Resilient Systems")
        st.markdown(":yellow-background[CoastPredict UN Ocean Decade GOOS Programme, SUSTAIN Program, CMCC Foundation] · :gray[ Training Course]")
        st.caption("The training focuses on advancing skills in coastal ocean, wave, and biogeochemical modeling, and introduces innovations in observation and remote sensing, that could be deployed to strengthen coastal resilience in the Philippines. A key feature of the course is hands-on training using the SURF ocean modeling platform, enabling participants to simulate real-world scenarios through detailed tutorials and case studies, centered on the Philippine coastal region. The program emphasizes integrating physical, biological, and chemical processes in marine systems to support the protection and sustainable management of natural resources")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="Link", icon=":material/visibility:", url="https://drive.google.com/file/d/1kRooNL0UzpctVkJWGD4Ha25fWDKr3fkK/view?usp=sharing")
    
    with st.container(border=True):
        with st.container(horizontal=True):
            st.badge("Talk", icon=":material/record_voice_over:", color="yellow")
            #st.badge("Speaker", icon=":material/emoji_people:", color="violet")
        st.subheader("Computer Science Society - Data Science in Action: Bridging Technological Research and Positive Change")
        st.markdown(":yellow-background[Universtity of the St. La Salle - Bacolod] · :gray[ Local]")
        st.caption("Delivered a talk for final year undergraduate students of Computer Science Society held on October 14, 2024. Discussed the valuable importance of data science and reseach for social good")
        with st.container(horizontal=True, horizontal_alignment="right"):
                st.link_button(label="Link", icon=":material/visibility:", url="https://drive.google.com/file/d/1oJOpWo0vGaliNAMidrZ9s1YUyWxM9oNW/view?usp=sharing")

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
                st.link_button(label="Transcript", icon=":material/article_shortcut:", url="https://drive.google.com/file/d/1kV91d1zGnnWxhIrCzcL0F2ReIv6Gh8RV/view?usp=sharing")

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