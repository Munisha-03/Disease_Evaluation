
from langchain_core.output_parsers import PydanticOutputParser
from datatypes import DiseaseVerify,DiseaseResponse

parser_verify = PydanticOutputParser(pydantic_object=DiseaseVerify)
parser_details = PydanticOutputParser(pydantic_object=DiseaseResponse)


