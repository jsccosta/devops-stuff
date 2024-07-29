INSERT INTO silas.company (named_insured,inception_date,expiration_date,occupancy,broker,domiciled) VALUES
	 ('Maariyaah Ltd','2023-01-01',NULL,'Pharmaceuticals','AON','USA'),
	 ('Rhonda Ltd','2023-03-01',NULL,'Hotels','Marsh','Portugal'),
	 ('Joel Ltd','2023-07-15',NULL,'Food',NULL,'England'),
	 ('Nikhil Ltd','2023-10-01',NULL,'Manufacturing',NULL,'Taiwan'),
	 ('Hassan Ltd','2023-12-01',NULL,'Retail',NULL,'Jordan');

INSERT INTO silas.company_metrics (company_id,gwp,business_interruption,tech_price_adequacy,gct_not_cat,nwp,aal_perc_gwp,gct_perc_gwp,gct_perc_nwp,"year") VALUES
	 (1,2509936.00,351094374.00,91.27,130462.00,21334,26.93,64.96,76.43,2023),
	 (1,3859917.63,638293294.00,148.86,200462.00,32230,17.45,45.35,54.31,2022),
	 (1,2192520.20,350134374.00,84.39,890462.00,18198,29.94,90.78,109.38,2021),
	 (1,2275825.20,331320374.00,176.56,-119538.00,18411,30.75,49.67,61.40,2020),
	 (1,2413843.20,82494274.00,110.37,385462.00,20566,25.77,82.05,96.30,2019),
	 (2,1288355.23,291125587.00,134.29,12937.00,10307,9.70,29.11,36.38,2023),
	 (2,1895442.54,581224587.00,216.28,51937.00,14747,8.18,19.20,24.68,2022),
	 (2,1281084.60,438108587.00,139.27,22037.00,9864,10.54,28.42,36.91,2021),
	 (2,1836936.87,629625018.00,199.45,-7563.00,14567,7.89,20.01,25.23,2020),
	 (2,2022780.19,282120024.00,231.70,75937.00,15798,5.69,22.94,29.37,2019);
INSERT INTO silas.company_metrics (company_id,gwp,business_interruption,tech_price_adequacy,gct_not_cat,nwp,aal_perc_gwp,gct_perc_gwp,gct_perc_nwp,"year") VALUES
	 (3,2358775.26,184346174.00,102.56,0.00,22172,40.06,37.03,39.40,2023),
	 (3,2001552.90,470846134.00,91.03,111700.00,18795,47.71,48.62,51.78,2022),
	 (3,2238156.35,453838464.00,93.33,102000.00,20871,43.56,40.82,43.77,2021),
	 (3,2221551.42,210346273.00,105.30,119710.00,20594,43.44,44.72,48.24,2020),
	 (3,2473017.17,484923524.00,125.15,17000.00,22999,40.03,35.73,38.42,2019),
	 (4,8556631.23,510010664.00,122.24,0.00,68453,38.49,0.00,0.00,2023),
	 (4,7976741.01,1105775664.00,115.10,0.00,62617,40.74,0.00,0.00,2022),
	 (4,8740041.77,63960659.00,126.81,0.00,67517,26.24,0.00,0.00,2021),
	 (4,10130209.83,1535480579.00,129.44,0.00,79320,39.43,0.00,0.00,2020),
	 (4,8756699.20,-244021384.00,123.06,0.00,69616,45.46,0.00,0.00,2019);
INSERT INTO silas.company_metrics (company_id,gwp,business_interruption,tech_price_adequacy,gct_not_cat,nwp,aal_perc_gwp,gct_perc_gwp,gct_perc_nwp,"year") VALUES
	 (5,739980.48,32528791.00,77.89,0.00,6660,16.72,0.00,0.00,2023),
	 (5,855526.74,96662791.00,97.77,0.00,7550,18.21,0.00,0.00,2022),
	 (5,940903.98,85384778.00,95.44,0.00,8195,18.68,0.00,0.00,2021),
	 (5,655923.93,60992778.00,65.68,0.00,5470,28.93,0.00,0.00,2020),
	 (5,978923.01,127923796.00,109.07,0.00,8429,22.86,0.00,0.00,2019);


INSERT INTO silas.company_metrics_summary (company_id,tiv,number_of_claims,property_damage,bi_deductible,tech_price,aop_deductible,aal,gct_cpy,gct_cat) VALUES
	 (1,5993127050,18.00,4239790360.00,22.00,11417000.00,6000000.00,3327595.00,8482310.00,6995000.00),
	 (3,4571693339,23.00,2767392770.00,17.00,10982700.00,2798000.00,4830000.00,4637300.00,4286890.00),
	 (5,2358293149,13.00,1954800215.00,14.00,4707110.00,1070000.00,868770.00,0.00,0.00),
	 (2,5979529590,19.00,3757325787.00,20.00,4549665.00,620000.00,675000.00,1934600.00,1779315.00),
	 (4,13627929162,13.00,10656722980.00,21.00,35764000.00,7680000.00,16811265.00,0.00,0.00);


INSERT INTO silas.five_y_company_summary (company_id,gwp,business_interruption,tech_price_adequacy,gct_not_cat,nwp) VALUES
	 (1,13252042.23,1753336690.00,611.45,1487310.00,110740),
	 (2,8324599.42,2222203803.00,920.99,155285.00,65283),
	 (3,11293053.10,1804300569.00,517.36,350410.00,105431),
	 (4,44160323.03,2971206182.00,616.66,0.00,347523),
	 (5,4171258.14,403492934.00,445.85,0.00,36304);


INSERT INTO silas.metrics (company_id,tiv,base_rate,brokerage,fees_and_commissions,number_of_claims,property_damage,bi_deductible,tech_price,aop_deductible,aal,policy_limit,gct_cpy,gct_cat,"year") VALUES
	 (3,873620468,0.27,3.50,2.50,1.00,689274294.00,3.00,2300000.00,500000.00,945000.00,150000000.00,873520.00,873520.00,2023),
	 (4,2673947260,0.32,20.00,0.00,0.00,2163936596.00,5.00,7000000.00,1250000.00,3293473.00,250000000.00,0.00,0.00,2023),
	 (5,435282634,0.17,10.00,0.00,0.00,402753843.00,0.00,950000.00,200000.00,123754.00,100000000.00,0.00,0.00,2023),
	 (1,1254968000,0.20,15.00,0.00,2.00,903873626.00,3.00,2750000.00,1000000.00,675839.00,500000000.00,1630462.00,1500000.00,2023),
	 (5,515222639,0.19,12.00,1.90,3.00,387298843.00,1.00,897500.00,215000.00,223754.00,120000000.00,0.00,0.00,2019),
	 (2,1263628360,0.15,21.50,0.70,6.00,682403773.00,3.00,876399.00,150000.00,155000.00,370000000.00,364000.00,312063.00,2022),
	 (4,2573142260,0.31,21.00,0.50,1.00,1467366596.00,4.00,6930000.00,1350000.00,3249373.00,270000000.00,0.00,0.00,2022),
	 (4,2913347255,0.30,22.00,0.75,5.00,2849386596.00,3.00,6892000.00,1570000.00,2293473.00,285000000.00,0.00,0.00,2021),
	 (4,2813947175,0.36,20.50,1.20,4.00,1278466596.00,7.00,7826000.00,1550000.00,3994473.00,245000000.00,0.00,0.00,2020),
	 (4,2653545212,0.33,19.00,1.50,3.00,2897566596.00,2.00,7116000.00,1960000.00,3980473.00,266000000.00,0.00,0.00,2019);
INSERT INTO silas.metrics (company_id,tiv,base_rate,brokerage,fees_and_commissions,number_of_claims,property_damage,bi_deductible,tech_price,aop_deductible,aal,policy_limit,gct_cpy,gct_cat,"year") VALUES
	 (5,475292634,0.18,11.00,0.75,4.00,378629843.00,4.00,875000.00,210000.00,155754.00,110000000.00,0.00,0.00,2022),
	 (5,495212621,0.19,11.50,1.40,1.00,409827843.00,7.00,985900.00,220000.00,175754.00,175000000.00,0.00,0.00,2021),
	 (5,437282621,0.15,14.50,2.10,5.00,376289843.00,2.00,998710.00,225000.00,189754.00,115000000.00,0.00,0.00,2020),
	 (1,1543967050,0.25,16.00,0.50,5.00,905673756.00,4.00,2593000.00,1500000.00,673439.00,550000000.00,1750462.00,1550000.00,2022),
	 (1,1153958000,0.19,16.50,0.50,3.00,803823626.00,6.00,2598000.00,1200000.00,656339.00,510000000.00,1990462.00,1100000.00,2021),
	 (1,1034466000,0.22,18.40,0.70,1.00,703145626.00,8.00,1289000.00,1100000.00,699839.00,540000000.00,1130462.00,1250000.00,2020),
	 (1,1005768000,0.24,14.00,0.80,7.00,923273726.00,1.00,2187000.00,1200000.00,622139.00,490000000.00,1980462.00,1595000.00,2019),
	 (2,1073629360,0.12,20.00,0.00,3.00,782503773.00,1.00,959399.00,100000.00,125000.00,350000000.00,375000.00,362063.00,2023),
	 (2,1413028360,0.13,19.50,1.20,2.00,783403342.00,8.00,920989.00,120000.00,145000.00,390000000.00,367500.00,375063.00,2020),
	 (2,1064621150,0.19,21.00,0.90,6.00,782501126.00,3.00,872999.00,110000.00,115000.00,400000000.00,464000.00,388063.00,2019);
INSERT INTO silas.metrics (company_id,tiv,base_rate,brokerage,fees_and_commissions,number_of_claims,property_damage,bi_deductible,tech_price,aop_deductible,aal,policy_limit,gct_cpy,gct_cat,"year") VALUES
	 (3,953120428,0.21,3.90,2.20,4.00,482274294.00,5.00,2198700.00,550000.00,955000.00,170000000.00,973220.00,861520.00,2022),
	 (3,973111458,0.23,4.00,2.75,2.00,519272994.00,3.00,2398200.00,575000.00,975000.00,180000000.00,913520.00,811520.00,2021),
	 (3,888620567,0.25,4.10,3.20,7.00,678274294.00,5.00,2109800.00,598000.00,965000.00,190000000.00,993520.00,873810.00,2020),
	 (3,883220418,0.28,3.60,3.40,9.00,398296894.00,1.00,1976000.00,575000.00,990000.00,195000000.00,883520.00,866520.00,2019),
	 (2,1164622360,0.11,22.00,1.00,2.00,726513773.00,5.00,919879.00,140000.00,135000.00,375000000.00,364100.00,342063.00,2021);


INSERT INTO silas.temp_metrics (named_insured,company_id,"year",tiv,property_damage,business_interruption,policy_limit,gwp,base_rate,claims_total,loss_ratio,technical_adequacy,modelled_results_aal,id) VALUES
	 ('Maariyaah Ltd',1,2019,4000000,4000000,4000000,4000000,4000000,0.024,4000000,35,74,4000000,5),
	 ('Maariyaah Ltd',1,2020,4000000,4000000,4000000,4000000,4000000,0.04,4000000,50,52,4000000,4),
	 ('Maariyaah Ltd',1,2021,4000000,4000000,4000000,4000000,4000000,0.4,4000000,40,40,4000000,3),
	 ('Maariyaah Ltd',1,2022,4000000,9000000,20000000,14000000,8000000,0.08,8000000,80,80,8000000,2),
	 ('Maariyaah Ltd',1,2023,180000000,18000000,30000000,13000000,15000000,0.15,15000000,15,15,15000000,1),
	 ('Rhonda Ltd',2,2019,4150000,4050000,4050000,4050000,4050000,0.034,4050000,37,36,4080000,10),
	 ('Rhonda Ltd',2,2020,4050000,4050000,4050000,4050000,4050000,0.05,4050000,53,54,4080000,9),
	 ('Rhonda Ltd',2,2021,3950000,4050000,4050000,4050000,4050000,0.39,4050000,42,38,4080000,8),
	 ('Rhonda Ltd',2,2022,3900000,9100000,21000000,14500000,8100000,0.09,8100000,82,81,8100000,7),
	 ('Rhonda Ltd',2,2023,175000000,18500000,31000000,13500000,15500000,0.16,15500000,14,16,15200000,6);
INSERT INTO silas.temp_metrics (named_insured,company_id,"year",tiv,property_damage,business_interruption,policy_limit,gwp,base_rate,claims_total,loss_ratio,technical_adequacy,modelled_results_aal,id) VALUES
	 ('Joel Ltd',3,2019,3850000,3950000,3950000,3950000,3950000,0.028,3950000,31,34,3980000,15),
	 ('Joel Ltd',3,2020,3950000,3950000,3950000,3950000,3950000,0.04,3950000,48,47,3980000,14),
	 ('Joel Ltd',3,2021,3800000,4100000,4100000,4100000,4100000,0.42,4100000,40,41,4080000,13),
	 ('Joel Ltd',3,2022,4100000,8900000,19000000,13000000,7900000,0.09,7900000,79,78,7900000,12),
	 ('Joel Ltd',3,2023,178000000,18000000,30000000,13000000,15000000,0.14,15000000,17,17,15100000,11),
	 ('Nikhil Ltd',4,2019,4200000,4150000,4150000,4150000,4150000,0.031,4150000,39,39,4180000,20),
	 ('Nikhil Ltd',4,2020,4150000,4150000,4150000,4150000,4150000,0.045,4150000,56,57,4180000,19),
	 ('Nikhil Ltd',4,2021,3850000,3950000,3950000,3950000,3950000,0.35,3950000,45,43,3980000,18),
	 ('Nikhil Ltd',4,2022,3950000,9200000,22000000,15000000,8200000,0.08,8200000,83,80,8200000,17),
	 ('Nikhil Ltd',4,2023,185000000,19000000,32000000,14000000,16000000,0.17,16000000,15,18,15800000,16);
INSERT INTO silas.temp_metrics (named_insured,company_id,"year",tiv,property_damage,business_interruption,policy_limit,gwp,base_rate,claims_total,loss_ratio,technical_adequacy,modelled_results_aal,id) VALUES
	 ('Hassan Ltd',5,2019,4250000,4200000,4200000,4200000,4200000,0.03,4200000,38,37,4180000,25),
	 ('Hassan Ltd',5,2020,4200000,4200000,4200000,4200000,4200000,0.04,4200000,55,56,4180000,24),
	 ('Hassan Ltd',5,2021,3900000,4100000,4100000,4100000,4100000,0.38,4100000,44,45,4080000,23),
	 ('Hassan Ltd',5,2022,4000000,9200000,22000000,15000000,8200000,0.08,8200000,80,81,8200000,22),
	 ('Hassan Ltd',5,2023,180000000,19000000,32000000,14000000,16000000,0.16,16000000,16,17,15800000,21);
INSERT INTO silas.department_occupancy (department,occupancy,iso,gwp,tiv,base_rate,claims_total,loss_ratio) VALUES
	 (1,'Hotels',10,10000,1800000,0.49,34000,34),
	 (1,'Manufacturing',40,3000000,1800000,0.39,55000,67),
	 (1,'Pharmaceuticals',30,1000,3000000,0.2,34000,53),
	 (1,'Food',60,6500,13000000,0.14,89000,38),
	 (1,'Retail',90,3490,15000000,0.18,34000,27);

INSERT INTO silas.department_overview (department,"year",brokerage,fees_and_commissions,nwp,gwp,loss_ratio,gross_claims_total,number_of_claims,total_cat,total_non_cat,total_cat_perc_gwp,total_cat_perc_nwp) VALUES
	 (1,2023,13.7,0.5,12892666,15453678,18.56,2867982,6,2685583,182399,18.56,22.25);


INSERT INTO silas.accounts_yoy ("date",accts_written_by_month,gwp_by_month,nwp_by_month) VALUES
	 ('01/01/2023',123,1357,1237),
	 ('02/01/2023',4,2456,2445),
	 ('03/01/2023',93,9876,9187),
	 ('04/01/2023',24,3456,3156),
	 ('05/01/2023',66,12345,11234),
	 ('06/01/2023',12,1356,1135),
	 ('07/01/2023',84,2456,1245),
	 ('08/01/2023',33,2311,2131),
	 ('09/01/2023',9,2345,2134),
	 ('10/01/2023',16,1234,1123);
INSERT INTO silas.accounts_yoy ("date",accts_written_by_month,gwp_by_month,nwp_by_month) VALUES
	 ('11/01/2023',77,1245,2124),
	 ('12/01/2023',33,4325,2432);

INSERT INTO silas.accounts (named_insured,underwriter,broker,inception_date,tiv,occupancy,gwp,base_rate,loss_ratio,company_id) VALUES
	 ('Maariyaah Ltd','Taciana','Aon','12/01/1994',4000000,'Hotels',10000,0.17,37,1),
	 ('Rhonda Ltd','Lorena','Marsh','29/12/2023',9000000,'Manufacturing',50000,0.23,65,2),
	 ('Joel Ltd','Beatriz','Howden','01/10/2020',20000000,'Food',78000,0.11,45,3),
	 ('Hassan Ltd','Kristina','Aon','17/07/2021',14000000,'Hotels',1000000,0.09,67,4),
	 ('Nikhil Ltd','Sara','Marsh','30/11/2001',8000000,'Pharmaceuticals',23000000,0.05,47,5);

INSERT INTO silas.submissions (account_name,domicile,broker,filenames,created_at,underwriter) VALUES
	 ('Joe Gibbs','uk','AON','{"filenames": ["v1-doc.pdf", "v2-doc.pdf", "v1-doc.pdf"]}','2024-03-12 16:08:21.385817','Mark Steeves'),
	 ('Mark','usa','AON','{"filenames": ["v1-doc.pdf", "v1-doc.pdf", "v2-doc.pdf"]}','2024-03-12 16:16:22.55762','Joe'),
	 ('Mega','canada','AON','{"filenames": ["v1-doc.pdf", "v2-doc.pdf", "v1-doc.pdf"]}','2024-03-12 17:17:16.648289','Joe Schmoe'),
	 ('One Test','uk','AON','{"filenames": ["v1-doc.pdf", "v2-doc.pdf", "v2-doc.pdf"]}','2024-03-12 17:17:55.531189','Maggie May');


INSERT INTO silas.new_metrics (company_id,named_insured,"year",gwp,nwp,base_rate,brokerage,fees_and_commissions,number_of_claims,property_damage,bi_deductible,tech_price,aal,gct_cpy,gct_cat,claims_total,loss_ratio,technical_adequacy,rate_change,policy_limit,gct_perc_gwp,gct_perc_nwp,business_interruption,aop_deductible,aal_perc_gwp,avg_rate_change,rate_on_line,rate_on_tiv,tiv,gct_not_cat) VALUES
	 (1,'Maariyaah Ltd',2019,4000000,20566,0.24,14.00,0.80,7.00,923273726.00,1.00,2187000.00,622139.00,1980462.00,1595000.00,4000000,35,74,4.24,490000000.00,64.96,76.43,351094374.00,1200000.00,21,28,2,2,1005768000,385462.00),
	 (1,'Maariyaah Ltd',2021,4000000,18198,0.19,16.50,0.50,3.00,803823626.00,6.00,2598000.00,656339.00,1990462.00,1100000.00,4000000,40,40,1.44,490000000.00,64.96,76.43,351094374.00,1200000.00,19,21,2,2,1153958000,890462.00),
	 (1,'Maariyaah Ltd',2022,8000000,32230,0.25,16.00,0.50,5.00,905673756.00,4.00,2593000.00,673439.00,1750462.00,1550000.00,8000000,80,80,4.14,490000000.00,64.96,76.43,351094374.00,1200000.00,10,21,0,2,1543967050,200462.00),
	 (1,'Maariyaah Ltd',2023,15000000,21334,0.20,15.00,0.00,2.00,903873626.00,3.00,2750000.00,675839.00,1630462.00,1500000.00,15000000,15,15,4.00,490000000.00,64.96,76.43,351094374.00,1200000.00,9,18,2,0,1254968000,130462.00),
	 (2,'Rhonda Ltd',2022,8100000,14747,0.15,21.50,0.70,6.00,682403773.00,3.00,876399.00,155000.00,364000.00,312063.00,8100000,82,81,5.51,375000000.00,29.11,36.38,291125587.00,140000.00,30,12,1,2,1263628360,51937.00),
	 (2,'Rhonda Ltd',2023,15500000,10307,0.12,20.00,0.00,3.00,782503773.00,1.00,959399.00,125000.00,375000.00,362063.00,15500000,14,16,5.45,375000000.00,29.11,36.38,291125587.00,140000.00,11,16,3,3,1073629360,12937.00),
	 (1,'Maariyaah Ltd',2020,4000000,18411,0.22,18.40,0.70,1.00,703145626.00,8.00,1289000.00,699839.00,1130462.00,1250000.00,4000000,50,52,2.18,490000000.00,64.96,76.43,351094374.00,1200000.00,25,31,1,2,1034466000,119538.00),
	 (4,'Nikhil Ltd',2023,16000000,68453,0.32,20.00,0.00,0.00,2163936596.00,5.00,7000000.00,3293473.00,0.00,0.00,16000000,15,18,0.48,266000000.00,0.00,0.00,510010664.00,1960000.00,12,13,1,0,2673947260,0.00),
	 (3,'Joel Ltd',2021,4100000,20871,0.23,4.00,2.75,2.00,519272994.00,3.00,2398200.00,975000.00,913520.00,811520.00,4100000,40,41,0.24,195000000.00,37.03,39.40,184346174.00,575000.00,34,32,3,2,973111458,102000.00),
	 (3,'Joel Ltd',2022,7900000,18795,0.21,3.90,2.20,4.00,482274294.00,5.00,2198700.00,955000.00,973220.00,861520.00,7900000,79,78,2.92,195000000.00,37.03,39.40,184346174.00,575000.00,30,32,2,3,953120428,111700.00);
INSERT INTO silas.new_metrics (company_id,named_insured,"year",gwp,nwp,base_rate,brokerage,fees_and_commissions,number_of_claims,property_damage,bi_deductible,tech_price,aal,gct_cpy,gct_cat,claims_total,loss_ratio,technical_adequacy,rate_change,policy_limit,gct_perc_gwp,gct_perc_nwp,business_interruption,aop_deductible,aal_perc_gwp,avg_rate_change,rate_on_line,rate_on_tiv,tiv,gct_not_cat) VALUES
	 (3,'Joel Ltd',2023,15000000,22172,0.27,3.50,2.50,1.00,689274294.00,3.00,2300000.00,945000.00,873520.00,873520.00,15000000,17,17,1.33,195000000.00,37.03,39.40,184346174.00,575000.00,23,30,2,3,873620468,0.00),
	 (4,'Nikhil Ltd',2019,4150000,69616,0.33,19.00,1.50,3.00,2897566596.00,2.00,7116000.00,3980473.00,0.00,0.00,4150000,39,39,3.95,266000000.00,0.00,0.00,510010664.00,1960000.00,18,24,2,0,2653545212,0.00),
	 (4,'Nikhil Ltd',2020,4150000,79320,0.36,20.50,1.20,4.00,1278466596.00,7.00,7826000.00,3994473.00,0.00,0.00,4150000,56,57,3.25,266000000.00,0.00,0.00,510010664.00,1960000.00,25,17,3,3,2813947175,0.00),
	 (4,'Nikhil Ltd',2022,8200000,62617,0.31,21.00,0.50,1.00,1467366596.00,4.00,6930000.00,3249373.00,0.00,0.00,8200000,83,80,4.22,266000000.00,0.00,0.00,510010664.00,1960000.00,18,33,2,2,2573142260,0.00),
	 (4,'Nikhil Ltd',2021,3950000,67517,0.30,22.00,0.75,5.00,2849386596.00,3.00,6892000.00,2293473.00,0.00,0.00,3950000,45,43,4.16,266000000.00,0.00,0.00,510010664.00,1960000.00,33,25,3,1,2913347255,0.00),
	 (5,'Hassan Ltd',2019,4200000,8429,0.19,12.00,1.90,3.00,387298843.00,1.00,897500.00,223754.00,0.00,0.00,4200000,38,37,3.52,115000000.00,0.00,0.00,32528791.00,225000.00,13,31,0,0,515222639,0.00),
	 (5,'Hassan Ltd',2020,4200000,5470,0.15,14.50,2.10,5.00,376289843.00,2.00,998710.00,189754.00,0.00,0.00,4200000,55,56,1.12,115000000.00,0.00,0.00,32528791.00,225000.00,26,17,1,3,437282621,0.00),
	 (5,'Hassan Ltd',2021,4100000,8195,0.19,11.50,1.40,1.00,409827843.00,7.00,985900.00,175754.00,0.00,0.00,4100000,44,45,4.78,115000000.00,0.00,0.00,32528791.00,225000.00,18,35,1,2,495212621,0.00),
	 (5,'Hassan Ltd',2022,8200000,7550,0.18,11.00,0.75,4.00,378629843.00,4.00,875000.00,155754.00,0.00,0.00,8200000,80,81,4.20,115000000.00,0.00,0.00,32528791.00,225000.00,24,16,3,3,475292634,0.00),
	 (5,'Hassan Ltd',2023,16000000,6660,0.17,10.00,0.00,0.00,402753843.00,0.00,950000.00,123754.00,0.00,0.00,16000000,16,17,4.32,115000000.00,0.00,0.00,32528791.00,225000.00,32,25,2,3,435282634,0.00);
INSERT INTO silas.new_metrics (company_id,named_insured,"year",gwp,nwp,base_rate,brokerage,fees_and_commissions,number_of_claims,property_damage,bi_deductible,tech_price,aal,gct_cpy,gct_cat,claims_total,loss_ratio,technical_adequacy,rate_change,policy_limit,gct_perc_gwp,gct_perc_nwp,business_interruption,aop_deductible,aal_perc_gwp,avg_rate_change,rate_on_line,rate_on_tiv,tiv,gct_not_cat) VALUES
	 (2,'Rhonda Ltd',2019,4050000,15798,0.19,21.00,0.90,6.00,782501126.00,3.00,872999.00,115000.00,464000.00,388063.00,4050000,37,36,0.29,375000000.00,29.11,36.38,291125587.00,140000.00,18,21,1,2,1064621150,75937.00),
	 (2,'Rhonda Ltd',2020,4050000,14567,0.13,19.50,1.20,2.00,783403342.00,8.00,920989.00,145000.00,367500.00,375063.00,4050000,53,54,0.61,375000000.00,29.11,36.38,291125587.00,140000.00,17,16,3,2,1413028360,-7563.00),
	 (2,'Rhonda Ltd',2021,4050000,9864,0.11,22.00,1.00,2.00,726513773.00,5.00,919879.00,135000.00,364100.00,342063.00,4050000,42,38,0.11,375000000.00,29.11,36.38,291125587.00,140000.00,29,24,2,2,1164622360,22037.00),
	 (3,'Joel Ltd',2019,3950000,22999,0.28,3.60,3.40,9.00,398296894.00,1.00,1976000.00,990000.00,883520.00,866520.00,3950000,31,34,4.22,195000000.00,37.03,39.40,184346174.00,575000.00,18,25,1,3,883220418,17000.00),
	 (3,'Joel Ltd',2020,3950000,20594,0.25,4.10,3.20,7.00,678274294.00,5.00,2109800.00,965000.00,993520.00,873810.00,3950000,48,47,5.02,195000000.00,37.03,39.40,184346174.00,575000.00,27,30,2,3,888620567,119710.00);


INSERT INTO silas.tenants
(id, tenant, bucket)
VALUES(nextval('silas.tenants_id_seq'::regclass), 'alfa', 'alfa_bucket');