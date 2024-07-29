---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
CREATE TABLE company_metrics (
    id SERIAL PRIMARY KEY,
    year
    company_id INTEGER,
    gwp NUMERIC(18, 2),
    business_interruption NUMERIC(18, 2),
    tech_price_adequacy NUMERIC(18, 2),
    gct_not_cat NUMERIC(18, 2),
    nwp INTEGER,
    aal_perc_gwp NUMERIC(18, 2),
    gct_perc_gwp NUMERIC(18, 2),
    gct_perc_nwp NUMERIC(18, 2)
);

INSERT INTO company_metrics (company_id, year, gwp, business_interruption, tech_price_adequacy, gct_not_cat, nwp, aal_perc_gwp, gct_perc_gwp, gct_perc_nwp)
SELECT
    c.id AS company_id,
    m.year as year,
    m.base_rate/100 * m.tiv AS gwp,
    m.tiv - m.property_damage AS business_interruption,
    m.base_rate * m.tiv / m.tech_price AS tech_price_adequacy,
    m.gct_cpy - m.gct_cat AS gct_not_cat,
    CAST(ROUND((m.base_rate/100 * m.tiv) * (1 - (m.brokerage / 100 + m.fees_and_commissions / 100)) / 100) AS INTEGER) AS nwp,
    ROUND(((m.aal / ((m.base_rate / 100) * m.tiv)) * 100)::NUMERIC, 2) AS aal_perc_gwp,
    ROUND(((m.gct_cpy / ((m.base_rate / 100) * m.tiv)) * 100)::NUMERIC, 2) AS gct_perc_gwp,
    ((m.gct_cpy / CAST(ROUND(((m.base_rate * m.tiv) * (1 - (m.brokerage / 100 + m.fees_and_commissions / 100)) / 10000)::NUMERIC, 2) AS INTEGER))) AS gct_perc_nwp
FROM
    public.company c 
JOIN
    public.metrics m ON c.id = m.company_id
GROUP BY
    c.id,
    m.year,
    gwp,
    tiv,
    business_interruption,
    tech_price_adequacy,
    gct_not_cat,
    nwp,
    aal_perc_gwp,
    gct_perc_gwp,
    gct_perc_nwp
order by
	c.id, year desc

CREATE OR REPLACE FUNCTION update_company_metrics()
RETURNS TRIGGER AS $$
BEGIN
    -- Update the calculated values in company_metrics based on the changes in metrics table
    UPDATE company_metrics AS cm
    SET 
		gwp = m.base_rate/100 * m.tiv,
		business_interruption =    m.tiv - m.property_damage,
		tech_price_adequacy=    m.base_rate * m.tiv / m.tech_price,
		gct_not_cat=     m.gct_cpy - m.gct_cat,
		nwp = CAST(ROUND((m.base_rate/100 * m.tiv) * (1 - (m.brokerage / 100 + m.fees_and_commissions / 100)) / 100) AS INTEGER),
		aal_perc_gwp = ROUND(((m.aal / ((m.base_rate / 100) * m.tiv)) * 100)::NUMERIC, 2),
		gct_perc_gwp = ROUND(((m.gct_cpy / ((m.base_rate / 100) * m.tiv)) * 100)::NUMERIC, 2),
		gct_perc_nwp =    ((m.gct_cpy / CAST(ROUND(((m.base_rate * m.tiv) * (1 - (m.brokerage / 100 + m.fees_and_commissions / 100)) / 10000)::NUMERIC, 2) AS INTEGER)))
    FROM 
        metrics AS m
    WHERE 
        cm.company_id = m.company_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create a trigger to invoke the function when metrics table is updated
CREATE TRIGGER update_company_metrics_trigger
AFTER INSERT OR UPDATE OR DELETE
ON public.metrics
FOR EACH ROW
EXECUTE FUNCTION update_company_metrics();
