import streamlit as st
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize



nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)



# --- Caching Resources for Speed ---
@st.cache_data
def load_resources():
    """Loads and preprocesses all necessary data and models."""
    DATA_DRIVEN_SKILL_DB = {
        'Hard Skills': [
            'account management', 'budget management', 'cash flow management', 'change management',
            'client relationship management', 'compensation management', 'crm', 'crm software',
            'crm systems', 'customer relationship management', 'data analysis', 'data analytics',
            'data entry', 'data management', 'erp systems', 'excel', 'financial analysis',
            'financial management', 'hr management', 'human resources management', 'inventory management',
            'it management', 'market analysis', 'marketing', 'microsoft excel', 'ms excel',
            'network security', 'payroll management', 'performance management', 'pipeline management',
            'power bi', 'project management', 'relationship management', 'risk management', 'saas',
            'sales management', 'salesforce', 'sap', 'sql', 'stakeholder management', 'talent management',
            'team management', 'territory management', 'time management', 'vendor management'
        ],
        'Soft Skills': [
            'accountability', 'accounting', 'accounting principles', 'accounts payable', 'active directory',
            'adaptability', 'analytical skills', 'analytical thinking', 'attention to detail', 'auditing',
            'b2b sales', 'background checks', 'benefits administration', 'budgeting', 'business acumen',
            'business development', 'cash handling', 'coaching', 'cold calling', 'collaboration',
            'communication', 'communication skills', 'compliance', 'computer skills', 'confidentiality',
            'conflict resolution', 'consultative selling', 'continuous improvement', 'continuous learning',
            'contract negotiation', 'cpa', 'creativity', 'critical thinking', 'cultural awareness',
            'curiosity', 'customer engagement', 'customer focus', 'customer service',
            'customer service orientation', 'cybersecurity', 'decision making', 'decision-making',
            'detail-oriented', 'discretion', 'documentation', 'empathy', 'employee engagement',
            'employee onboarding', 'employee relations', 'employment law', 'employment laws', 'engagement',
            'enthusiasm', 'entrepreneurial mindset', 'finance', 'financial forecasting', 'financial modeling',
            'financial planning', 'financial reporting', 'flexibility', 'forecasting', 'gaap',
            'goal-oriented', 'hris', 'hris systems', 'human resources', 'independence',
            'independent work', 'influence', 'influencing', 'influencing skills', 'information technology',
            'initiative', 'innovation', 'integrity', 'internal controls', 'interpersonal skills', 'jira',
            'judgment', 'lead generation', 'leadership', 'listening skills', 'market research', 'mentoring',
            'mentorship', 'merchandising', 'microsoft office', 'microsoft office suite',
            'microsoft powerpoint', 'microsoft word', 'motivation', 'ms office', 'ms office suite',
            'multi-tasking', 'multitasking', 'negotiation', 'networking', 'office 365', 'onboarding',
            'organization', 'organizational design', 'organizational development', 'organizational skills',
            'payroll administration', 'payroll processing', 'persuasion', 'pmp certification',
            'policy development', 'positive attitude', 'powerpoint', 'presentation skills', 'prioritization',
            'proactivity', 'problem solving', 'problem-solving', 'process improvement', 'product knowledge',
            'professionalism', 'prospecting', 'recruiting', 'recruitment', 'regulatory compliance',
            'relationship building', 'reporting', 'results-oriented', 'risk assessment', 'sales',
            'sales experience', 'sales forecasting', 'sales strategies', 'sales strategy',
            'sales strategy development', 'sales techniques', 'self-motivated', 'self-motivation',
            'self-starter', 'sharepoint', 'stakeholder engagement', 'strategic planning',
            'strategic thinking', 'succession planning', 'talent acquisition', 'team building',
            'team collaboration', 'team leadership', 'teamwork', 'technical support', 'training',
            'training and development', 'troubleshooting', 'valid driver\'s license', 'visual merchandising',
            'work ethic', 'workday', 'workforce planning'
        ]
    }
    hard_skills = set(DATA_DRIVEN_SKILL_DB['Hard Skills'])
    soft_skills = set(DATA_DRIVEN_SKILL_DB['Soft Skills'])
    all_skills = hard_skills.union(soft_skills)

    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    return all_skills, hard_skills, soft_skills, lemmatizer, stop_words

# Load all resources once at the start using the cached function
ALL_SKILLS, HARD_SKILLS, SOFT_SKILLS, lemmatizer, stop_words = load_resources()

# --- Core Skill Extraction Logic ---
def extract_skills_from_text(text):
    """Cleans the input text and searches for skills from the dictionary."""
    text = text.lower()
    tokens = word_tokenize(re.sub(r'[^\w\s]', ' ', text))
    lemmatized_text = ' '.join([lemmatizer.lemmatize(word) for word in tokens if word not in stop_words])

    found_skills = set()
    for skill in ALL_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, lemmatized_text):
            found_skills.add(skill)
    return found_skills

# --- Streamlit User Interface ---
st.set_page_config(layout="wide", page_title="Skill Extractor", page_icon="🚀")
st.title("🚀 Interactive Skill Extractor")
st.write("Paste a job description below to identify the key skills required. This tool uses a data-driven dictionary of over 200 common skills.")

job_description = st.text_area(
    "Paste the Job Description Here:",
    height=250,
    placeholder="e.g., 'We are looking for a software engineer with strong Python and SQL skills...'"
)

if st.button("Extract Skills", type="primary"):
    if job_description:
        with st.spinner("Analyzing..."):
            extracted_skills = extract_skills_from_text(job_description)
            found_hard_skills = sorted([skill for skill in extracted_skills if skill in HARD_SKILLS])
            found_soft_skills = sorted([skill for skill in extracted_skills if skill in SOFT_SKILLS])

            st.success(f"**Analysis Complete! Found {len(extracted_skills)} unique skills.**")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("🛠️ Hard Skills")
                if found_hard_skills:
                    for skill in found_hard_skills:
                        st.markdown(f"- {skill.capitalize()}")
                else:
                    st.markdown("_No hard skills were found._")
            with col2:
                st.subheader("🤝 Soft Skills")
                if found_soft_skills:
                    for skill in found_soft_skills:
                        st.markdown(f"- {skill.capitalize()}")
                else:
                    st.markdown("_No soft skills were found._")
    else:
        st.warning("Please paste a job description.")
