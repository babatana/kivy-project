"""
This document contains the various data classes necessary for mapping the sources and their IDs

    The most important Indicators for the project here

    Economic Indicators
    1. GDP per capita (current USD)
    2. GDP Annual Growth (annual %)
    3. Inflation, GDP Deflator (annual %)
    4. Inflation Consumer Prices (annual %)
    5. Central Government Debt (% of GDP)

    Energy and Mining
    1. Access to Electricity (% of population)
    2. Electric power consumption (kWh per capita)

"""

from dataclasses import dataclass


@dataclass
class Source:
    doing_business = 1
    # world_development_indicators = 2
    worldwide_governance_indicators = 3
    subnational_malnutrition_database = 5
    international_debt_statistics = 6
    # africa_development_indicators = 11
    education_statistics = 12
    global_economic_monitor = 15
    health_nutrition_population_statistics = 16
    millennium_development_goals = 19
    poverty_and_equity = 24
    jobs = 25
    global_economic_prospects = 27
    global_financial_inclusion = 28
    country_policy_and_institutional_assessment = 31
    universal_health_coverage = 58
    economic_fitness = 60
    human_capital_index = 63
    health_equity_and_financial_protection_indicators = 65
    logistics_performance_index = 66
    international_debt_statistics_ddsi = 81


@dataclass
class World_development_indicators:
    id = 2
    total_population = "SP.POP.TOTL"
    female_population = "SP.POP.TOTL.FE.IN"
    female_population_percentage = "SP.POP.TOTL.FE.ZS"
    male_population = "SP.POP.TOTL.MA.IN"
    male_population_percentage = "SP.POP.TOTL.MA.ZS"
    population_growth = "SP.POP.GROW "
    rural_population = "SP.RUR.TOTL"
    rural_population_percentage = "SP.RUR.TOTL.ZS"
    rural_population_growth = "SP.RUR.TOTL.ZG"
    urban_population = "SP.URB.TOTL"
    urban_population_percentage = "SP.URB.TOTL.IN.ZS "
    urban_population_growth = "SP.URB.GROW"


@dataclass
class Africa_development_indicators:
    # more to be added
    id = 11
    current_account_balance_GDP_percentage = "BN.CAB.XOKA.GD.ZS"
    current_account_balance = "BN.CAB.XOKA.CD"
    net_income_GDP_percentage = "BN.GSR.FCTY.CD.ZS"
    foreign_direct_investment_gdp_percentage = "BN.KLT.DINV.CD.ZS"
    migrant_remittance_inflow_gdp_percentage = "BM.TRF.MGR.CD"
    electricity_production_kwh = "EG.ELC.PROD.KH"
    energy_imports_net = "EG.IMP.CONS.ZS "
    gross_savings_gdp_percentage = "NY.GNS.ICTR.ZS"
    number_of_people_employed = "SL.EMP.TOTL"
    total_employed_female = "SL.EMP.TOTL.FE"
    total_employed_male = "SL.EMP.TOTL.MA"
    tax_revenue_gdp_percentage = "GC.TAX.TOTL.GD.ZS"
    gdp_per_capita_current = "NY.GDP.PCAP.CD "
    gdp_per_capita_const_2010 = "NY.GDP.PCAP.KD"
    gdp_per_capita_annual_growth = "NY.GDP.PCAP.KD.ZG"
    literacy_rate_adult_total = "SE.ADT.LITR.ZS"
    hiv_prevalence_rate_high = "SH.DYN.AIDS.HG.ZS"
    hiv_prevalence_rate_low = "SH.DYN.AIDS.LW.ZS"
    fertility_rate = "SP.DYN.TFRT.IN"
    total_population = "SP.POP.TOTL"
    total_population_female = "SP.POP.TOTL.FE.IN"
    total_population_female_percentage = "SP.POP.TOTL.FE.ZS"
    total_population_male = "SP.POP.TOTL.MA.IN"
    total_population_male_percentage = "SP.POP.TOTL.MA.ZS"
    rural_population_total = "SP.RUR.TOTL"
    rural_population_growth = "SP.RUR.TOTL.ZG"
    rural_population_percentage = "SP.RUR.TOTL.Zs"
    urban_population_total = "SP.URB.TOTL"
    urban_population_growth = "SP.URB.GROW"
    urban_population_percentage = "SP.RUR.TOTL.ZS"



@dataclass
class Country:
    id = 123456789
    angola = "AGO"
    benin = "BEN"
    botswana = "BWA"
    burkina_Faso = "BFA"
    burundi = "BDI"
    cameroon = "CMR"
    cape_verde = "Cape Verde"
    central_african_republic = "CAF"
    chad = "TCD"
    Comoros = "COM"
    congo_brazzaville = "COD"
    congo = "COG"
    democratic_depublic = "COG"
    côte_d_ivoire = "cote"
    djibouti = "DJI"
    equatorial_guinea = "GNQ"
    eritrea = "ERI"
    ethiopia = "ETH"
    gabon = "GAB"
    the_gambia = "the gambia"
    ghana = "GHA"
    guinea = "GIN"
    guinea_bissau = "GNB"
    kenya = "KEN"
    lesotho = "LSO"
    liberia = "LBR"
    madagascar = "MDG"
    malawi = "MWI"
    mali = "MLI"
    mauritania = "MRT"
    mauritius = "MUS"
    mozambique = "MOZ"
    namibia = "NAM"
    niger = "NER"
    nigeria = "NGA"
    réunion = "reunion"
    rwanda = "RWA"
    sao_tome_and_principe = "STP"
    senegal = "SEN"
    seychelles = "SYC"
    sierra_leone = "SLE"
    somalia = "SOM"
    south_africa = "ZA"
    south_sudan = "SSD"
    sudan = "SDN"
    swaziland = "SZ"
    tanzania = "Tanzania"
    togo = "TGO"
    uganda = "UGA"
    western_sahara = "Western Sahara"
    zambia = "ZMB"
    zimbabwe = "ZWE"


country_list = [
    "angola",
    "benin",
    "botswana",
    "burkina Faso",
    "burundi",
    "cameroon",
    "cape verde",
    "central african republic",
    "chad",
    "comoros",
    "congo brazzaville",
    "congo",
    "democratic republic",
    "côte d'ivoire",
    "djibouti",
    "equatorial guinea",
    "eritrea",
    "ethiopia",
    "gabon",
    "the_gambia",
    "ghana",
    "guinea",
    "guinea bissau",
    "kenya",
    "lesotho",
    "liberia",
    "madagascar",
    "malawi",
    "mali",
    "mauritania",
    "mauritius",
    "mozambique",
    "namibia",
    "niger",
    "nigeria",
    "réunion",
    "rwanda",
    "sao tome and principe",
    "senegal",
    "seychelles",
    "sierra leone",
    "somalia",
    "south africa",
    "sudan",
    "swaziland",
    "tanzania",
    "togo",
    "uganda",
    "western sahara",
    "zambia",
    "zimbabwe"
]


""" Egypt, Ghana material *** 
Credit growth 
Infation 
"""









