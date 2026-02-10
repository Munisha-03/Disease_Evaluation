from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from datatypes import DiseaseDetails, DiseaseVerify, TextInput
from prompt import prompt_details, prompt1_verify
from parser import parser_verify,parser_details

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)


# print(response)

async def disease_verify(disease: TextInput):
    chain = prompt1_verify | llm | parser_verify
    verify = await chain.ainvoke({"disease": disease.disease})
    # return verify

    if "Not_a_disease" in verify.disease:
        return {"error": "NOT A DISEASE"}

    return await get_disease_details(disease) 

async def get_disease_details(disease: TextInput):
    chain = prompt_details | llm | parser_details
    response = await chain.ainvoke({"disease": disease.disease})
    return response