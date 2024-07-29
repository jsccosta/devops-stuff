CREATE TABLE public.company_metrics_summary as
SELECT
    company_id,
    SUM(tiv) AS tiv,
    SUM(number_of_claims) AS number_of_claims,
    SUM(property_damage) AS property_damage,
    SUM(bi_deductible) AS bi_deductible,
    SUM(tech_price) AS tech_price,
    SUM(aop_deductible) AS aop_deductible,
    SUM(aal) AS aal,
    SUM(gct_cpy) AS gct_cpy,
    SUM(gct_cat) AS gct_cat
FROM
    public.metrics
GROUP BY
    company_id;
   
   

ALTER TABLE public.company_metrics_summary
ADD COLUMN id SERIAL PRIMARY KEY;



CREATE OR REPLACE FUNCTION update_company_metrics_summary()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE public.company_metrics_summary AS cms
    SET
        total_tiv = (
            SELECT SUM(tiv) FROM public.metrics WHERE company_id = NEW.company_id
        ),
        total_base_rate = (
            SELECT SUM(base_rate) FROM public.metrics WHERE company_id = NEW.company_id
        )
    WHERE cms.company_id = NEW.company_id;
    
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER metrics_5y_summary_update_trigger
AFTER UPDATE OF tiv, number_of_claims, property_damage, bi_deductible, tech_price,
	aop_deductible, aal, gct_cpy, gct_cat
ON public.metrics
FOR EACH ROW
EXECUTE FUNCTION update_company_metrics_summary();

