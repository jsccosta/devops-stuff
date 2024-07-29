SET search_path TO silas;

CREATE TABLE silas.company (
	id serial4 NOT NULL,
	named_insured varchar NULL,
	inception_date date NULL,
	expiration_date date NULL,
	occupancy varchar NULL,
	broker varchar NULL,
	domiciled varchar NULL,
	CONSTRAINT company_pkey PRIMARY KEY (id)
);

CREATE TABLE silas.company_metrics (
	id serial4 NOT NULL,
	company_id int4 NULL,
	gwp numeric(18, 2) NULL,
	business_interruption numeric(18, 2) NULL,
	tech_price_adequacy numeric(18, 2) NULL,
	gct_not_cat numeric(18, 2) NULL,
	nwp int4 NULL,
	aal_perc_gwp numeric(18, 2) NULL,
	gct_perc_gwp numeric(18, 2) NULL,
	gct_perc_nwp numeric(18, 2) NULL,
	"year" int4 NULL,
	CONSTRAINT company_metrics_pkey PRIMARY KEY (id)
);

CREATE TABLE silas.company_metrics_summary (
	company_id int4 NULL,
	tiv numeric NULL,
	number_of_claims numeric NULL,
	property_damage numeric NULL,
	bi_deductible numeric NULL,
	tech_price numeric NULL,
	aop_deductible numeric NULL,
	aal numeric NULL,
	gct_cpy numeric NULL,
	gct_cat numeric NULL,
	id serial4 NOT NULL,
	CONSTRAINT company_metrics_summary_pkey PRIMARY KEY (id)
);

CREATE TABLE silas.five_y_company_summary (
	id serial4 NOT NULL,
	company_id int4 NULL,
	gwp numeric(18, 2) NULL,
	business_interruption numeric(18, 2) NULL,
	tech_price_adequacy numeric(18, 2) NULL,
	gct_not_cat numeric(18, 2) NULL,
	nwp int4 NULL,
	CONSTRAINT five_y_company_summary_pkey PRIMARY KEY (id)
);

CREATE TABLE silas.metrics (
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

CREATE TABLE silas.temp_metrics (
	named_insured varchar NULL,
	company_id int4 NULL,
	"year" int4 NULL,
	tiv int4 NULL,
	property_damage int4 NULL,
	business_interruption int4 NULL,
	policy_limit int4 NULL,
	gwp int4 NULL,
	base_rate float4 NULL,
	claims_total int4 NULL,
	loss_ratio int4 NULL,
	technical_adequacy int4 NULL,
	modelled_results_aal int4 NULL,
	id int4 NULL
);

CREATE TABLE silas.department_overview (
	department int4 NULL,
	"year" int4 NULL,
	brokerage float4 NULL,
	fees_and_commissions float4 NULL,
	nwp int4 NULL,
	gwp int4 NULL,
	loss_ratio float4 NULL,
	gross_claims_total int4 NULL,
	number_of_claims int4 NULL,
	total_cat int4 NULL,
	total_non_cat int4 NULL,
	total_cat_perc_gwp float4 NULL,
	total_cat_perc_nwp float4 NULL,
	id serial4 NOT NULL,
	CONSTRAINT department_overview_pkey PRIMARY KEY (id)
);

CREATE TABLE silas.department_occupancy (
	department int4 NULL,
	occupancy varchar(50) NULL,
	iso int4 NULL,
	gwp int4 NULL,
	tiv int4 NULL,
	base_rate float4 NULL,
	claims_total int4 NULL,
	loss_ratio int4 NULL,
	id serial4 NOT NULL,
	CONSTRAINT department_occupancy_pkey PRIMARY KEY (id)
);

CREATE TABLE silas.acct_overview (
	company_id int4 NULL,
	"year" int4 NULL,
	tiv int4 NULL,
	property_damage int4 NULL,
	business_interruption int4 NULL,
	policy_limit int4 NULL,
	gwp int4 NULL,
	base_rate float4 NULL,
	claims_total int4 NULL,
	loss_ratio int4 NULL,
	technical_adequacy int4 NULL,
	modelled_results_aal int4 NULL,
	id serial4 NOT NULL,
	CONSTRAINT acct_overview_pkey PRIMARY KEY (id)
);

CREATE TABLE silas.accounts_yoy (
	"date" varchar(50) NULL,
	accts_written_by_month int4 NULL,
	gwp_by_month int4 NULL,
	nwp_by_month int4 NULL,
	id serial4 NOT NULL,
	CONSTRAINT accounts_yoy_pkey PRIMARY KEY (id)
);

CREATE TABLE silas.accounts_written_month (
	account_id int4 NULL,
	"month" varchar(50) NULL,
	accounts_written int4 NULL
);

CREATE TABLE silas.accounts (
	named_insured varchar(50) NULL,
	underwriter varchar(50) NULL,
	broker varchar(50) NULL,
	inception_date varchar(50) NULL,
	tiv int4 NULL,
	occupancy varchar(50) NULL,
	gwp int4 NULL,
	base_rate float4 NULL,
	loss_ratio int4 NULL,
	company_id int4 NULL,
	id serial4 NOT NULL,
	CONSTRAINT accounts_pkey PRIMARY KEY (id)
);

CREATE TABLE silas.submissions (
	id serial4 NOT NULL,
	account_name varchar NULL,
	domicile varchar NULL,
	broker varchar NULL,
	filenames jsonb NULL,
	created_at timestamp NULL DEFAULT CURRENT_TIMESTAMP,
	underwriter varchar NULL,
	CONSTRAINT files_pkey PRIMARY KEY (id)
);
CREATE INDEX idx_account_name ON silas.submissions USING btree (account_name);

CREATE TABLE silas.new_metrics (
	id serial4 NOT NULL,
	company_id int4 NULL,
	named_insured varchar NULL,
	"year" int4 NULL,
	gwp int4 NULL,
	nwp int4 NULL,
	base_rate numeric(8, 2) NULL,
	brokerage numeric(8, 2) NULL,
	fees_and_commissions numeric(8, 2) NULL,
	number_of_claims numeric(12, 2) NULL,
	property_damage numeric(12, 2) NULL,
	bi_deductible numeric(12, 2) NULL,
	tech_price numeric(12, 2) NULL,
	aal numeric(12, 2) NULL,
	gct_cpy numeric(12, 2) NULL,
	gct_cat numeric(12, 2) NULL,
	claims_total int4 NULL,
	loss_ratio int4 NULL,
	technical_adequacy int4 NULL,
	rate_change numeric(8, 2) NULL,
	policy_limit numeric(12, 2) NULL,
	gct_perc_gwp numeric(18, 2) NULL,
	gct_perc_nwp numeric(18, 2) NULL,
	business_interruption numeric(18, 2) NULL,
	aop_deductible numeric(12, 2) NULL,
	aal_perc_gwp int4 NULL,
	avg_rate_change int4 NULL,
	rate_on_line int4 NULL,
	rate_on_tiv int4 NULL,
	tiv numeric NULL,
	gct_not_cat numeric(18, 2) NULL
);

CREATE TABLE silas.tenants (
	id serial4 NOT NULL,
	tenant varchar NOT NULL,
	bucket varchar NOT NULL,
	CONSTRAINT tenants_pkey PRIMARY KEY (id)
);