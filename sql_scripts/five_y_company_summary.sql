CREATE TABLE five_y_company_summary (
    id SERIAL PRIMARY KEY,
    company_id INTEGER,
    gwp NUMERIC(18, 2),
    business_interruption NUMERIC(18, 2),
    tech_price_adequacy NUMERIC(18, 2),
    gct_not_cat NUMERIC(18, 2),
    nwp INTEGER,
);

INSERT INTO five_y_company_summary (company_id, gwp, business_interruption, tech_price_adequacy, gct_not_cat, nwp)
SELECT
    c.id AS company_id,
    SUM(m.base_rate/100 * m.tiv) AS gwp,
    SUM(m.tiv - m.property_damage) AS business_interruption,
    SUM(m.base_rate * m.tiv / m.tech_price) AS tech_price_adequacy,
    SUM(m.gct_cpy - m.gct_cat) AS gct_not_cat,
    CAST(ROUND(SUM((m.base_rate/100 * m.tiv) * (1 - (m.brokerage / 100 + m.fees_and_commissions / 100)) / 100)) AS INTEGER) AS nwp
FROM
    public.company c 
JOIN
    public.metrics m ON c.id = m.company_id
GROUP BY
    c.id
ORDER BY
    c.id;
   
  
   -- Create or replace the trigger function
CREATE OR REPLACE FUNCTION update_five_y_company_summary()
RETURNS TRIGGER AS
$$
BEGIN
    -- Update the company_summary table based on the changes in the metrics
    UPDATE company_summary AS cs
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
            public.company c 
        JOIN
            public.metrics m ON c.id = m.company_id
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
AFTER INSERT OR UPDATE ON public.metrics
FOR EACH ROW
EXECUTE FUNCTION update_five_y_company_summary();