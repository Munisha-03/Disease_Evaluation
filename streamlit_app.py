import streamlit as st
import asyncio
from main import disease_verify, TextInput

# Page configuration
st.set_page_config(
    page_title="Disease Evaluation App",
    page_icon="🏥",
    layout="wide"
)

# Custom CSS for a more premium look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    .header-text {
        color: #1e3d59;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏥 Disease Evaluation & Information System")
st.markdown("<h4 class='header-text'>Get comprehensive details about various diseases, their symptoms, causes, and treatments.</h4>", unsafe_allow_html=True)
st.divider()

# Sidebar for additional info or settings
with st.sidebar:
    st.info("### About\nThis app uses AI to provide detailed information about diseases. Please consult a professional medical advisor for any health concerns.")
    st.image("https://img.icons8.com/clouds/200/000000/medical-doctor.png")

# Main Input Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    disease_input = st.text_input("Enter the name of the disease:", placeholder="e.g., Diabetes, Hypertension, etc.")
    analyze_button = st.button("Analyze Disease")

if analyze_button or disease_input:
    if not disease_input.strip():
        st.warning("Please enter a disease name.")
    else:
        with st.spinner(f"Analyzing {disease_input}..."):
            try:
                # Wrap the async call
                input_data = TextInput(disease=disease_input)
                result = asyncio.run(disease_verify(input_data))

                if isinstance(result, dict) and "error" in result:
                    st.error(f"Error: {result['error']}. Please enter a valid disease name.")
                else:
                    details = result.disease_details
                    
                    st.success(f"Analysis complete for **{details.disease_name}**")
                    
                    # Layout for results
                    tab1, tab2, tab3, tab4 = st.tabs(["Overview & Symptoms", "Causes & Risks", "Diagnosis & Treatment", "Prevention"])
                    
                    with tab1:
                        st.subheader("Description")
                        st.write(details.description)
                        st.subheader("Common Symptoms")
                        for symptom in details.symptoms:
                            st.write(f"- {symptom}")
                    
                    with tab2:
                        st.subheader("Main Causes")
                        for cause in details.causes:
                            st.write(f"- {cause}")
                        st.subheader("Risk Factors")
                        for factor in details.risk_factors:
                            st.write(f"- {factor}")
                    
                    with tab3:
                        st.subheader("Diagnosis")
                        st.write(details.diagnosis)
                        st.subheader("Treatment Options")
                        st.write(details.treatment)
                    
                    with tab4:
                        st.subheader("Prevention Methods")
                        st.write(details.prevention)
                        st.info("💡 Always follow medical advice for prevention.")

            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")

st.divider()
st.markdown("<p style='text-align: center; color: #6c757d;'>© 2026 Disease Evaluation App. Powered by Gemini AI.</p>", unsafe_allow_html=True)
