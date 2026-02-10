from langchain_core.prompts import PromptTemplate
from parser import parser_verify,parser_details

prompt1_verify= PromptTemplate(
    template="""
You are a medical AI assistant.
Verify whether given disease is an valid disease or not.

if the given string is an disease return : Disease Name
else return : Not_a_disease

Disease Name: {disease}

{format_instructions}
""",
    input_variables=["disease"],
    partial_variables={
        "format_instructions": parser_verify.get_format_instructions()
    }
)

prompt_details = PromptTemplate(
    template="""
You are a medical AI assistant.
Provide accurate, general medical information (not diagnosis).

Disease Name: {disease}

{format_instructions}
""",
    input_variables=["disease"],
    partial_variables={
        "format_instructions": parser_details.get_format_instructions()
    }
)