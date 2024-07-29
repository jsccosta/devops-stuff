-- company data info
INSERT INTO public.company
    (id, named_insured, inception_date, occupancy)
VALUES
    (nextval('company_id_seq'::regclass), 'Maariyaah Ltd', '01/01/2023', 'Pharmaceuticals'),
    (nextval('company_id_seq'::regclass), 'Rhonda Ltd', '03/01/2023', 'Hotels'),
    (nextval('company_id_seq'::regclass), 'Joel Ltd', '07/15/2023','Food'),
    (nextval('company_id_seq'::regclass), 'Nikhil Ltd', '10/01/2023', 'Manufacturing'),
    (nextval('company_id_seq'::regclass), 'Hassan Ltd', '12/01/2023', 'Retail'); 


INSERT INTO public.metrics
(id, company_id, tiv, property_damage, policy_limit, base_rate, brokerage, fees_and_commissions, gct_cpy, number_of_claims, gct_cat, aop_deductible, bi_deductible, tech_price, aal)
VALUES
    (nextval('metrics_id_seq'::regclass),1,1254968000,903873626,500000000,0.20,15.00,0.00,1630462,2,1500000,1000000,3,2750000,675839),
    (nextval('metrics_id_seq'::regclass),2,1073629360,782503773,350000000,0.12,20.00,0.00,364000,3,312063,100000,1,959399,125000),
    (nextval('metrics_id_seq'::regclass),3,873620468,689274294,150000000,0.27,3.50,2.50,873520,1,873520,500000,3,2300000,945000),
    (nextval('metrics_id_seq'::regclass),4,2673947260,2163936596,250000000,0.32,20.00,0.00,0,0,0,1250000,5,7000000,3293473),
    (nextval('metrics_id_seq'::regclass),5,435282634,402753843,100000000,0.17,10.00,0.00,0,0,0,200000,0,950000,123754);
