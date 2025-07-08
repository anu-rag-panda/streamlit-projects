import streamlit as st

#grade mapping
GRADE_POINTS = {
    "O": 10,
    "E": 9,
    "A": 8,
    "B": 7,
    "C": 6,
    "D": 5,
    "F": 2,
    "I": 2
}

#semester wise subject and default credits
SEMESTER_SUBJECTS = {
    "1st Semester": [
        ("Mathematics I A", 4),
        ("Physics I", 4),
        ("Basic Electrical Engineering", 4),
        ("Physics I Laboratory", 1.5),
        ("Basic Electrical Engineering Laboratory", 1.0),
        ("Workshop Practice", 3)
    ],
    
    "2nd Semester": [
        ("Chemistry I", 4),
        ("Mathematics II A", 4),
        ("Programming for Problem Solving", 3),
        ("English", 2),
        ("Chemistry I Laboratory", 1.5),
        ("Programming for Problem Solving Laboratory", 2),
        ("Engineering Graphics Laboratory", 3),
        ("Language Laboratory", 1)
    ]
}

#streamlit app

#title and Description
st.set_page_config(page_title="MAKAUT SGPA and Percentage Calculator", layout="centered")
st.title("MAKAUT SGPA and Percentage Calculator")
st.markdown("""
            select your semester, input subject wise grades and credits and instantly get your SGPA and percentage.""")

#dark mode toggle
dark_mode = st.toggle("🌙 Dark Mode", value=False)
if dark_mode:
    st.markdown("""
                <style>
                .stApp {
                    background-color: gray;
                    color: white;
                }
                </style>
                """, unsafe_allow_html=True)

#semester selection
semester = st.selectbox("📚 Select Semester ", list(SEMESTER_SUBJECTS.keys()))

with st.form("sgpa_form"):
    st.subheader(f"📝 Enter Grades & Credits for {semester}")
    total_credit = 0
    total_weighted_points = 0
    failed_subjects = False
    
    subject_inputs = []
    
    for subject, default_credit in SEMESTER_SUBJECTS[semester]:
        st.markdown(f"**{subject}**")
        col1, col2 = st.columns(2)
        
        with col1:
            credit = st.number_input(f"Credits for {subject}", min_value=0.0, value=float(default_credit), step=0.5, key=f"{subject}_credit")
            
        with col2:
            grade = st.selectbox(f"Grade for {subject}", list(GRADE_POINTS.keys()), key=f"{subject}_grades")
            
        subject_inputs.append((credit, GRADE_POINTS[grade]))
        
        if GRADE_POINTS[grade] == 0:
            failed_subjects = True
            
    submitted = st.form_submit_button("🔍 Calculate SGPA & Percentage")
    
    if submitted:
        for credit, grade_point in subject_inputs:
            total_credit += credit
            total_weighted_points += credit * grade_point
            
        if total_credit == 0:
            st.error("Total Credit cannot be zero.")
        else:
            sgpa = total_weighted_points / total_credit
            percentage = (sgpa - 0.5) * 10
            
            st.success(f"📊 **SGPA:** {sgpa:.2f}")
            st.success(f"📈 **Percentage:** {percentage:.2f}%")
            
            if failed_subjects:
                st.warning("⚠️ You have failed in one or more subjects.")
                
            # Show formula tooltip (optional)
            with st.expander("ℹ️ View Calculation Formula"):
                st.markdown("""
                **SGPA = (Σ Credit × Grade Point) / Σ Credit**

                **Percentage ≈ SGPA × 9.5**
                """)
                
if st.button("🔄 Reset"):
    st.experimental_rerun()
    
#grade scale INFO
with st.expander("ℹ️ Grade Scale"):
    st.table({"Grade": list(GRADE_POINTS.keys()), "Points": list(GRADE_POINTS.values())})


#footer
st.markdown("""
            <style>
            h2 {
                text-align: center;
                color: #888;
                font-size: 1.2rem;
            }
            </style>
            <h2>Made with ❤️ by Anurag Panda</h2>
            """, unsafe_allow_html=True)

