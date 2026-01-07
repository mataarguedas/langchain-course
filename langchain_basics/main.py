from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama


load_dotenv()

def main():
    print("Hello from langchain-course!")
    information = """
        Costa Rica,[a] officially the Republic of Costa Rica,[b] is a country in Central America. It borders Nicaragua to the north, the Caribbean Sea to the northeast, Panama to the southeast, and the Pacific Ocean to the southwest, sharing a maritime border with Ecuador to the south of Cocos Island. It has a population of around five million[10][11] in a land area of nearly 51,180 km2 (19,760 sq mi);[12] the capital and largest city is San José, home to around 350,000 residents and two million people in the surrounding metropolitan area.[13]

        Humans have been present in Costa Rica since between 7,000 and 10,000 BC. Various indigenous peoples lived in the territory before it was colonized by Spain in the 16th century. Costa Rica was a peripheral colony of the Spanish Empire until independence in 1821 as part of the First Mexican Empire, followed by membership in the Federal Republic of Central America in 1823, from which it formally declared independence in 1847. The country underwent gradual modernization under relatively stable authoritarian rule until the late 19th century, when it promulgated a liberal constitution and held the first free and fair national election in Central America.[14]

        Following a brief civil war in 1948, Costa Rica adopted its current constitution in 1949, which granted universal suffrage, provided various social, economic, and educational guarantees for all citizens, and permanently abolished the army, becoming one of the few sovereign nations without a standing military.[15][16][17] Costa Rica is a presidential republic with a robust and stable democracy.[18] About one-fourth of the national budget is spent on education—which has been free and compulsory since 1886—equal to about 6.2% of the country's GDP, compared to a global average of 3.8%;[19] The economy, once heavily dependent on agriculture, has diversified to include finance, corporate services for foreign companies, pharmaceuticals, and ecotourism.[20][21]

        Costa Rica has consistently performed favorably in the Human Development Index (HDI), placing 62nd globally, and fifth in Latin America, in 2023. Costa Rica is classified by the World Bank as a high-income country[22] and it is the only OECD country in Central America and the Caribbean.[23] It has also been cited by the United Nations Development Programme (UNDP) as having attained much higher human development than other countries at the same income levels, with a better record on human development and inequality than the regional median.[24] Costa Rica performs well in metrics of democratic governance, press freedom, subjective happiness and sustainable wellbeing;[25] it has one of the highest literacy rates in the Americas,[26] and is considered a regional leader in human rights and environmentalism.[26]     """


    summary_template = """
    given the information {information} about a country I want you to create:
    1. A short summary
    2. two interesting facts about it.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-4o")
    # llm = ChatOllama(temperature=0, model="gemma3:270m")


    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})

    print(response.content)


if __name__ == "__main__":
    main()
