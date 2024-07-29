CREATE OR REPLACE FUNCTION update_company_metrics()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE silas.company_metrics AS cm
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
        silas.metrics AS m
    WHERE 
        cm.company_id = m.company_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create a trigger to invoke the function when metrics table is updated
CREATE TRIGGER update_company_metrics_trigger
AFTER INSERT OR UPDATE OR DELETE
ON silas.metrics
FOR EACH ROW
EXECUTE FUNCTION update_company_metrics();


CREATE OR REPLACE FUNCTION update_company_metrics_summary()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE silas.company_metrics_summary AS cms
    SET
        total_tiv = (
            SELECT SUM(tiv) FROM silas.metrics WHERE company_id = NEW.company_id
        ),
        total_base_rate = (
            SELECT SUM(base_rate) FROM silas.metrics WHERE company_id = NEW.company_id
        )
    WHERE cms.company_id = NEW.company_id;
    
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER metrics_5y_summary_update_trigger
AFTER UPDATE OF tiv, number_of_claims, property_damage, bi_deductible, tech_price,
	aop_deductible, aal, gct_cpy, gct_cat
ON silas.metrics
FOR EACH ROW
EXECUTE FUNCTION update_company_metrics_summary();


 
   -- Create or replace the trigger function
CREATE OR REPLACE FUNCTION update_five_y_company_summary()
RETURNS TRIGGER AS
$$
BEGIN
    -- Update the company_summary table based on the changes in the metrics
    UPDATE silas.five_y_company_summary AS cs
    SET 
        gwp = subquery.gwp,
        business_interruption = subquery.business_interruption,
        tech_price_adequacy = subquery.tech_price_adequacy,
        gct_not_cat = subquery.gct_not_cat,
        nwp = subquery.nwp
    FROM (
        SELECT
            c.id AS company_id,
            SUM(m.base_rate/100 * m.tiv) AS gwp,
            SUM(m.tiv - m.property_damage) AS business_interruption,
            SUM(m.base_rate * m.tiv / m.tech_price) AS tech_price_adequacy,
            SUM(m.gct_cpy - m.gct_cat) AS gct_not_cat,
            CAST(ROUND(SUM((m.base_rate/100 * m.tiv) * (1 - (m.brokerage / 100 + m.fees_and_commissions / 100)) / 100)) AS INTEGER) AS nwp
        FROM
            silas.company c 
        JOIN
            silas.metrics m ON c.id = m.company_id
        WHERE
            c.id = NEW.company_id  -- Filter based on the changed company_id
        GROUP BY
            c.id
    ) AS subquery
    WHERE
        cs.company_id = subquery.company_id;

    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

-- Create the trigger
CREATE TRIGGER metrics_update_trigger
AFTER INSERT OR UPDATE ON silas.metrics
FOR EACH ROW
EXECUTE FUNCTION update_five_y_company_summary();