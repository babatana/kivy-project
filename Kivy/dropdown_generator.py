"""
    easier way to generate dropdown menus
"""

afro_dev_indicators = {
    'current_account_balance_GDP_percentage': 'BN.CAB.XOKA.GD.ZS',
    'current_account_balance': 'BN.CAB.XOKA.CD',
    'net_income_GDP_percentage': 'BN.GSR.FCTY.CD.ZS',
    'foreign_direct_investment_gdp_percentage': 'BN.KLT.DINV.CD.ZS',
    'migrant_remittance_inflow_gdp_percentage': 'BM.TRF.MGR.CD',
    'electricity_production_kwh': 'EG.ELC.PROD.KH',
    'energy_imports_net': 'EG.IMP.CONS.ZS',
    'gross_savings_gdp_percentage': 'NY.GNS.ICTR.ZS',
    'number_of_people_employed': 'SL.EMP.TOTL',
    'total_employed_female': 'SL.EMP.TOTL.FE',
    'total_employed_male': 'SL.EMP.TOTL.MA',
    'tax_revenue_gdp_percentage': 'GC.TAX.TOTL.GD.ZS',
    'gdp_per_capita_current': 'NY.GDP.PCAP.CD',
    'gdp_per_capita_const_2010': 'NY.GDP.PCAP.KD',
    'gdp_per_capita_annual_growth': 'NY.GDP.PCAP.KD.ZG',
    'literacy_rate_adult_total': 'SE.ADT.LITR.ZS',
    'hiv_prevalence_rate_high': 'SH.DYN.AIDS.HG.ZS',
    'hiv_prevalence_rate_low': 'SH.DYN.AIDS.LW.ZS',
    'fertility_rate': 'SP.DYN.TFRT.IN',
    'total_population': 'SP.POP.TOTL',
    'total_population_female': 'SP.POP.TOTL.FE.IN',
    'total_population_female_percentage': 'SP.POP.TOTL.FE.ZS',
    'total_population_male': 'SP.POP.TOTL.MA.IN',
    'total_population_male_percentage': 'SP.POP.TOTL.MA.ZS',
    'rural_population_total': 'SP.RUR.TOTL',
    'rural_population_growth': 'SP.RUR.TOTL.ZG',
    'rural_population_percentage': 'SP.RUR.TOTL.Zs',
    'urban_population_total': 'SP.URB.TOTL',
    'urban_population_growth': 'SP.URB.GROW',
    'urban_population_percentage': 'SP.RUR.TOTL.ZS',
}


def kpi_drop_down(kpi_dictionary):
    for key, value in kpi_dictionary.items():
        print("""Button:
                    text: """, key, """
                    size_hint_y: None
                    height: 35
                    on_press: gen_final_indicators(""", value, """)""")
