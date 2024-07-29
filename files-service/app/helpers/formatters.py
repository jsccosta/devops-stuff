def formatYearMetrics(results):
    return {
        "id": results.Company.id,
        "named_insured": results.Company.named_insured,
        "tiv": results.Metrics.tiv,
        "property_damage": results.Metrics.property_damage,
        "policy_limit": results.Metrics.policy_limit if results.Metrics.policy_limit is not None else '--',
        "base_rate": results.Metrics.base_rate if results.Metrics.base_rate is not None else '--',
        "brokerage": results.Metrics.brokerage if results.Metrics.brokerage is not None else '--',
        "fees_and_commissions": results.Metrics.fees_and_commissions if results.Metrics.fees_and_commissions is not None else '--',
        "gct_cpy": results.Metrics.gct_cpy,
        "number_of_claims": results.Metrics.number_of_claims,
        "gct_cat": results.Metrics.gct_cat,
        "aop_deductible": results.Metrics.aop_deductible,
        "bi_deductible": results.Metrics.bi_deductible,
        "tech_price": results.Metrics.tech_price,
        "aal": results.Metrics.aal,
        "gwp": results.CalculatedMetrics.gwp,
        "business_interruption": results.CalculatedMetrics.business_interruption,
        "tech_price_adequacy": results.CalculatedMetrics.tech_price_adequacy if results.CalculatedMetrics.tech_price_adequacy is not None else '--',
        "gct_not_cat": results.CalculatedMetrics.gct_not_cat,
        "nwp": results.CalculatedMetrics.nwp,
        "aal_perc_gwp": results.CalculatedMetrics.aal_perc_gwp if results.CalculatedMetrics.aal_perc_gwp is not None else '--',
        "gct_perc_gwp": results.CalculatedMetrics.gct_perc_gwp if results.CalculatedMetrics.gct_perc_gwp is not None else '--',
        "gct_perc_nwp": results.CalculatedMetrics.gct_perc_nwp if results.CalculatedMetrics.gct_perc_nwp is not None else '--',
        "overviewMetricsData": [
            {"title": "Gross Written Premium", "value": results.CalculatedMetrics.gwp, "formatter": "dollar"},
            {"title": "Policy Limit", "value": results.Metrics.policy_limit, "formatter": "dollar"},
            {"title": "Base Rate", "value": "0.12%"},
            {"title": "Rate Change", "value": "5.11%"},
            {"title": "Brokerage", "value": results.Metrics.brokerage if results.Metrics.brokerage is not None else '--'
             },
            {
                "title": "Fees and Commissions",
                "value": results.Metrics.fees_and_commissions if results.Metrics.fees_and_commissions is not None else '--'
                ,
            },
            {"title": "Net Written Premium", "value": results.CalculatedMetrics.nwp, "formatter": "dollar"},
            {"title": "Number of Claims", "value": "1"},
            {"title": "Claims to Date (USD)", "value": "$ 51,937"},
            {
                "title": "Gross Claims as % of GWP",
                "value": results.CalculatedMetrics.gct_perc_gwp if results.CalculatedMetrics.gct_perc_gwp is not None else '--',
                "formatter": "percentage"
            },
            {
                "title": "Gross Claims as a % of NWP",
                "value": results.CalculatedMetrics.gct_perc_nwp if results.CalculatedMetrics.gct_perc_nwp is not None else '--',
                "formatter": "percentage"
            },
            {"title": "Property Damage", "value": results.Metrics.property_damage, "formatter": "dollar"},
        ],

        "businessMetricsData": [
            {"title": "Business Interruption", "value": "$291,125,587"},
            {"title": "AOP Deductible", "value": "$250,000"},
            {"title": "BI Deductible (Days)", "value": "$782,503,773"},
            {"title": "Property Damage", "value": "1"},
        ],
        "technicalMetricsData": [
            {"title": "AAl", "value": results.Metrics.aal, "formatter": "dollar"},
            {
                "title": "AAL as % of GWP",
                "value": results.CalculatedMetrics.aal_perc_gwp if results.CalculatedMetrics.aal_perc_gwp is not None else '--',
                "formatter": "percentage"
            },
            {"title": "Rate Change ", "value": "5.11%"},
            {"title": "Technical Premium", "value": "$959,399"},
            {
                "title": "Technical Price Adequacy",
                "value": results.CalculatedMetrics.tech_price_adequacy if results.CalculatedMetrics.tech_price_adequacy is not None else '--',
                "formatter": "percentage"
            },
            {"title": "Average Rate Change", "value": "12.5%"},
            {"title": "Incidental Rate", "value": "?"},
            {"title": "Rate on Line", "value": "0.37%"},
            {"title": "Rate on TIV", "value": "0.12%"},
        ],
    }


def formatFiveYearMetrics(results):
    return {
        "id": results.Company.id,
        "named_insured": results.Company.named_insured,
        "tiv": results.FiveYearSummaryMetrics.tiv,
        "property_damage": results.FiveYearSummaryMetrics.property_damage,
        "policy_limit": '--',
        "base_rate": '--',
        "brokerage": '--',
        "fees_and_commissions": '--',
        "gct_cpy": results.FiveYearSummaryMetrics.gct_cpy,
        "number_of_claims": results.FiveYearSummaryMetrics.number_of_claims,
        "gct_cat": results.FiveYearSummaryMetrics.gct_cat,
        "aop_deductible": results.FiveYearSummaryMetrics.aop_deductible,
        "bi_deductible": results.FiveYearSummaryMetrics.bi_deductible,
        "tech_price": results.FiveYearSummaryMetrics.tech_price,
        "aal": results.FiveYearSummaryMetrics.aal,
        "gwp": results.CalculatedFiveYSummaryMetrics.gwp,
        "business_interruption": results.CalculatedFiveYSummaryMetrics.business_interruption,
        "tech_price_adequacy": results.CalculatedFiveYSummaryMetrics.tech_price_adequacy if results.CalculatedFiveYSummaryMetrics.tech_price_adequacy is not None else '--',
        "gct_not_cat": results.CalculatedFiveYSummaryMetrics.gct_not_cat,
        "nwp": results.CalculatedFiveYSummaryMetrics.nwp,
        "aal_perc_gwp": '--',
        "gct_perc_gwp": '--',
        "gct_perc_nwp": '--',
        "overviewMetricsData": [
            {"title": "Gross Written Premium", "value": results.CalculatedFiveYSummaryMetrics.gwp, "formatter": "dollar"},
            {"title": "Policy Limit", "value": '0', "formatter": "dollar"},
            {"title": "Base Rate", "value": "0.12%"},
            {"title": "Rate Change", "value": "5.11%"},
            {"title": "Brokerage", "value": '--'
             },
            {
                "title": "Fees and Commissions",
                "value": '--'
                ,
            },
            {"title": "Net Written Premium", "value": results.CalculatedFiveYSummaryMetrics.nwp, "formatter": "dollar"},
            {"title": "Number of Claims", "value": "1"},
            {"title": "Claims to Date (USD)", "value": "$ 51,937"},
            {
                "title": "Gross Claims as % of GWP",
                "value": '--',
            },
            {
                "title": "Gross Claims as a % of NWP",
                "value": '--',
            },
            {"title": "Property Damage", "value": results.FiveYearSummaryMetrics.property_damage, "formatter": "dollar"},
        ],

        "businessMetricsData": [
            {"title": "Business Interruption", "value": "$291,125,587"},
            {"title": "AOP Deductible", "value": "$250,000"},
            {"title": "BI Deductible (Days)", "value": "$782,503,773"},
            {"title": "Property Damage", "value": "1"},
        ],
        "technicalMetricsData": [
            {"title": "AAl", "value": results.FiveYearSummaryMetrics.aal, "formatter": "dollar"},
            {
                "title": "AAL as % of GWP",
                "value": '--',
            },
            {"title": "Rate Change ", "value": "--"},
            {"title": "Technical Premium", "value": "$959,399"},
            {
                "title": "Technical Price Adequacy",
                "value": results.CalculatedFiveYSummaryMetrics.tech_price_adequacy if results.CalculatedFiveYSummaryMetrics.tech_price_adequacy is not None else '--',
                "formatter": "percentage"
            },
            {"title": "Average Rate Change", "value": "12.5%"},
            {"title": "Incidental Rate", "value": "?"},
            {"title": "Rate on Line", "value": "0.37%"},
            {"title": "Rate on TIV", "value": "0.12%"},
        ],
    }