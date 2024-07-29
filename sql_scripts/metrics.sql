-- public.metrics definition

-- Drop table

-- DROP TABLE public.metrics;

CREATE TABLE public.metrics (
	id serial4 NOT NULL,
	company_id int4 NULL,
	tiv numeric NULL,
	base_rate numeric(8, 2) NULL,
	brokerage numeric(8, 2) NULL,
	fees_and_commissions numeric(8, 2) NULL,
	number_of_claims numeric(12, 2) NULL,
	property_damage numeric(12, 2) NULL,
	bi_deductible numeric(12, 2) NULL,
	tech_price numeric(12, 2) NULL,
	aop_deductible numeric(12, 2) NULL,
	aal numeric(12, 2) NULL,
	policy_limit numeric(12, 2) NULL,
	gct_cpy numeric(12, 2) NULL,
	gct_cat numeric(12, 2) NULL,
	"year" int4 NULL,
	CONSTRAINT metrics_pkey PRIMARY KEY (id)
);

-- Table Triggers

create trigger update_company_metrics_trigger after
insert
    or
delete
    or
update
    on
    public.metrics for each row execute function update_company_metrics();
create trigger metrics_update_trigger after
insert
    or
update
    on
    public.metrics for each row execute function update_five_y_company_summary();


-- public.metrics foreign keys

ALTER TABLE public.metrics ADD CONSTRAINT metrics_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.company(id);