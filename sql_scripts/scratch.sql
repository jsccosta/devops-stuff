--------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------
-- -- NOT BEING USED - FOR REFERENCE ONLY
-- CREATE MATERIALIZED VIEW company_metrics_view AS
-- SELECT
--     c.id AS company_id,
--     m.base_rate * m.tiv AS gwp,
--     m.tiv-m.property_damage as business_interruption,
--     m.base_rate * m.tiv/m.tech_price as tech_price_adequacy,
--     m.gct_cpy-m.gct_cat as gct_not_cat,
-- 	CAST(ROUND((m.base_rate * m.tiv)*(1-(m.brokerage/100+m.fees_and_commissions/100))/100) AS integer) as nwp,
-- 	ROUND(((m.aal/((m.base_rate/100) * m.tiv))*100)::numeric,2) as aal_perc_gwp,
-- 	ROUND(((m.gct_cpy /((m.base_rate/100) * m.tiv))*100)::numeric,2) as gct_perc_gwp,
-- 	((m.gct_cpy /cast(ROUND(((m.base_rate * m.tiv)*(1-(m.brokerage/100+m.fees_and_commissions/100))/10000)::numeric,2) as integer))) as gct_perc_nwp
-- FROM
--     public.company c 
-- JOIN
--     public.metrics m ON c.id = m.company_id;

-- CREATE UNIQUE INDEX idx_company_metrics_view ON public.company_metrics_view (company_id);

   
-- CREATE OR REPLACE FUNCTION tg_refresh_my_mv()
-- RETURNS trigger LANGUAGE plpgsql AS $$
-- BEGIN
--     REFRESH MATERIALIZED VIEW CONCURRENTLY company_metrics_view;
--     RETURN NULL;
-- END;
-- $$;


-- CREATE TRIGGER tg_refresh_my_mv AFTER INSERT OR UPDATE OR DELETE
-- ON public.metrics 
-- FOR EACH STATEMENT EXECUTE PROCEDURE tg_refresh_my_mv();
----------------------------------------------------------------------
----------------------------------------------------------------------
----------------------------------------------------------------------
----------------------------------------------------------------------