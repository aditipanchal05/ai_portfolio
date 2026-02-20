import streamlit as st
from PIL import Image
st.set_page_config(page_title="ai_portfolio", layout="wide")
st.markdown("""
<style>
@media (max-width: 768px) {
    .hero-name {
        font-size: 36px !important;
    }
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="ai_portfolio", layout="wide")

# -------------------- CUSTOM CSS --------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0f0f1a;
    color: white;
}

.section {
    padding-top: 60px;
    padding-bottom: 60px;
}

.hero-name {
    font-size: 55px;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(90deg, #c084fc, #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.tagline {
    text-align: center;
    font-size: 20px;
    color: #d8b4fe;
    margin-top: 10px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 20px;
    border-bottom: 2px solid #7c3aed;
    display: inline-block;
    padding-bottom: 5px;
}

.card {
    background-color: #1a1a2e;
    padding: 25px;
    border-radius: 12px;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.02);
    box-shadow: 0px 0px 25px #7c3aed;
}

img {
    border-radius: 12px;
    box-shadow: 0px 0px 25px #7c3aed;
}

</style>
""", unsafe_allow_html=True)

# -------------------- HERO SECTION --------------------

# -------------------- HERO SECTION --------------------

st.markdown('<div class="section">', unsafe_allow_html=True)

col1, col2 = st.columns([2,1])

with col1:
    st.markdown('<div class="hero-name" style="text-align:left;">ADITI PANCHAL</div>', unsafe_allow_html=True)
    st.markdown('<div class="tagline" style="text-align:left;">SOFTWARE DEVELOPER | CLOUD & AI ENTHUSIAST</div>', unsafe_allow_html=True)

with col2:
    image = Image.open("assets/profile.jpg")
    st.image(image, width=250)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------- ABOUT SECTION --------------------

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">ABOUT</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
I am a final-year Computer Science Engineering student with a strong foundation in software development and cloud technologies. 
I have hands-on experience in building scalable applications using Python, C++, and modern web technologies. 
Through internships and industry exposure, I have developed practical skills in cloud computing, DevOps, and AI-driven systems. 
I am particularly interested in Gen AI and Agentic AI solutions that bridge innovation with real-world impact. 
I am currently seeking opportunities to gain deeper industry experience and contribute to dynamic development teams. 
I am committed to continuous learning and building efficient, production-ready systems.
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------- KEY SKILLS SECTION --------------------

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">KEY SKILLS</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <b>Programming Languages</b><br><br>
    Python<br>
    C++<br>
    C
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <b>Databases</b><br><br>
    MongoDB<br>
    SQL<br>
    DBMS
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <b>Web Technologies</b><br><br>
    HTML<br>
    CSS<br>
    JavaScript<br>
    React.js<br>
    Node.js<br>
    Express.js
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <b>Cloud & Tools</b><br><br>
    AWS (EC2, S3, Console)<br>
    DevOps Fundamentals<br>
    VS Code
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
# -------------------- PROJECTS SECTION --------------------

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">PROJECTS</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<b>AI Real Estate Assessment Bot</b><br><br>
<b>Tech Stack:</b> Python, Streamlit, LLM Integration, Prompt Engineering<br><br>
Developed an AI-driven real estate assessment system that evaluates user responses based on property listings using Large Language Models. 
Implemented dynamic scoring logic and contextual evaluation to simulate intelligent domain-specific analysis. 
Designed an interactive interface for structured assessments and automated feedback generation.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<b>CineGram – Genre-Based Movie Recommendation System</b><br><br>
<b>Tech Stack:</b> Python, Pandas, Scikit-learn, Streamlit<br><br>
Built a genre-based movie recommendation system that suggests personalized movie options based on user-selected preferences. 
Implemented content-based filtering techniques using feature similarity and metadata processing. 
Designed an intuitive interface to deliver dynamic and responsive recommendations.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<b>AI Portfolio Website</b><br><br>
<b>Tech Stack:</b> Streamlit, Python, Custom CSS<br><br>
Designed and developed a responsive AI-themed personal portfolio using Streamlit with custom styling and structured one-page navigation. 
Integrated dynamic UI elements and modular sections to present technical experience, internships, certifications, and projects in a professional format.
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
# -------------------- EXPERIENCE SECTION --------------------

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">INTERNSHIPS & EXPERIENCE</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<b>DataGami – Gen AI & Agentic AI Intern (Ongoing)</b><br><br>
Currently working on developing intelligent automation workflows and AI-driven solutions focused on Gen AI and Agentic AI systems. 
Gaining hands-on experience in real-world AI deployment along with exposure to DevOps practices for scalable system management. 
Actively contributing to experimental AI architectures and optimization pipelines.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<b>AWS Industry Internship – Cloud Computing</b><br><br>
Completed a one-month in-house industry internship focused on AWS cloud services including EC2 instance management, S3 storage configuration, and AWS console operations. 
Developed foundational understanding of cloud architecture, deployment workflows, and infrastructure management in an enterprise-oriented environment.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<b>Capgemini – Letter of Intent (Software Role)</b><br><br>
Received a Letter of Intent from Capgemini for a software role, demonstrating readiness for industry-level development responsibilities and strong technical foundation.<br><br>
<a href="https://drive.google.com/file/d/1AekypRN8uFh69KJaC-oXeQaOFMbV4aGb/view?usp=drivesdk" target="_blank" style="color:#c084fc; text-decoration:none;"><b>View Letter of Intent →</b></a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
# -------------------- EDUCATION SECTION --------------------

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">EDUCATION</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<b>Medi-Caps University</b><br><br>
Bachelor of Technology – Computer Science Engineering<br>
Final Year (8th Semester)<br>
Current SGPA: 8.60
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# -------------------- CERTIFICATIONS SECTION --------------------


# -------------------- CERTIFICATIONS SECTION --------------------

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">CERTIFICATIONS</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<b>Cloud Architecting Certification</b><br><br>
Completed certification focused on scalable cloud infrastructure design, deployment strategies, and security best practices within AWS environments.<br><br>
<a href="https://drive.google.com/file/d/1fpMgn4RdhA-3Y5fi-Te10M9ZgnvUUBTg/view?usp=drivesdk" target="_blank" style="color:#c084fc; text-decoration:none;"><b>View Certificate →</b></a>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<b>Cloud Foundations Certification</b><br><br>
Gained foundational knowledge of cloud computing principles including virtualization, distributed systems, and core AWS services.<br><br>
<a href="https://drive.google.com/file/d/1trig5DbBjFUYwvkGdKTwq0sqDbAgZlzS/view?usp=drivesdk" target="_blank" style="color:#c084fc; text-decoration:none;"><b>View Certificate →</b></a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
# -------------------- CONTACT SECTION --------------------

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title" style="text-align:center;">CONTACT</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card" style="text-align:center;">

<b>Email:</b><br>
<a href="mailto:aditipanchal83@gmail.com" target="_blank" style="color:#c084fc; text-decoration:none;">
aditipanchal83@gmail.com
</a>

<br><br>

<b>LinkedIn:</b><br>
<a href="https://www.linkedin.com/in/aditi-panchal-59228629a" target="_blank" style="color:#c084fc; text-decoration:none;">
View LinkedIn Profile →
</a>

<br><br>

<b>Phone:</b><br>
7974192961

</div>
""", unsafe_allow_html=True)


st.markdown('</div>', unsafe_allow_html=True)
