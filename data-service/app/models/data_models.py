from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, Float

# from ..db import Base
from ..db_config.config import Base

class Company(Base):
    __tablename__ = "company"
    __table_args__ = {"schema": "silas"}
    id = Column(Integer, primary_key=True)
    named_insured = Column(String)
    inception_date = Column(Date)
    expiration_date = Column(Date)
    occupancy = Column(String)
    broker = Column(String)
    domiciled = Column(String) 

class Metrics(Base):
    __tablename__ = "metrics"
    __table_args__ = {"schema": "silas"}
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('company.id'))
    year = Column(Integer)
    tiv = Column(Numeric(precision=8, scale=2))
    property_damage = Column(Numeric(precision=12, scale=2))
    policy_limit = Column(Numeric(precision=12, scale=2))
    base_rate = Column(Numeric(precision=8, scale=2))
    brokerage = Column(Numeric(precision=8, scale=2))
    fees_and_commissions = Column(Numeric(precision=8, scale=2))
    gct_cpy = Column(Numeric(precision=12, scale=2))
    number_of_claims = Column(Numeric(precision=12, scale=2))
    gct_cat = Column(Numeric(precision=12, scale=2))
    aop_deductible = Column(Numeric(precision=12, scale=2))
    bi_deductible = Column(Numeric(precision=12, scale=2))
    tech_price = Column(Numeric(precision=12, scale=2))
    aal = Column(Numeric(precision=12, scale=2))

class CalculatedMetrics(Base):
    __tablename__ = "company_metrics"
    __table_args__ = {"schema": "silas"}
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    company_id = Column(Integer, ForeignKey('company.id'))
    gwp = Column(Numeric(precision=8, scale=2))
    business_interruption = Column(Numeric(precision=12, scale=2))
    tech_price_adequacy = Column(Numeric(precision=12, scale=2))
    gct_not_cat = Column(Numeric(precision=8, scale=2))
    nwp = Column(Numeric(precision=8, scale=2))
    aal_perc_gwp = Column(Numeric(precision=8, scale=2))
    gct_perc_gwp = Column(Numeric(precision=8, scale=2))
    gct_perc_nwp = Column(Numeric(precision=8, scale=2))


class CalculatedFiveYSummaryMetrics(Base):
    __tablename__ = "five_y_company_summary"
    __table_args__ = {"schema": "silas"}
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('company.id'))
    gwp = Column(Numeric(precision=8, scale=2))
    business_interruption = Column(Numeric(precision=12, scale=2))
    tech_price_adequacy = Column(Numeric(precision=12, scale=2))
    gct_not_cat = Column(Numeric(precision=8, scale=2))
    nwp = Column(Numeric(precision=8, scale=2))

class FiveYearSummaryMetrics(Base):
    __tablename__ = "company_metrics_summary"
    __table_args__ = {"schema": "silas"}
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('company.id'))
    tiv = Column(Numeric(precision=8, scale=2))
    property_damage = Column(Numeric(precision=12, scale=2))
    gct_cpy = Column(Numeric(precision=12, scale=2))
    number_of_claims = Column(Numeric(precision=12, scale=2))
    gct_cat = Column(Numeric(precision=12, scale=2))
    aop_deductible = Column(Numeric(precision=12, scale=2))
    bi_deductible = Column(Numeric(precision=12, scale=2))
    tech_price = Column(Numeric(precision=12, scale=2))
    aal = Column(Numeric(precision=12, scale=2))    

class AccountOverview(Base):
    # __tablename__ = 'acct_overview'
    __tablename__ = 'temp_metrics'
    __table_args__ = {"schema": "silas"}
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('company.id'))
    named_insured = Column(String(50), nullable=True)
    year = Column(Integer)
    tiv = Column(Integer)
    property_damage = Column(Integer)
    business_interruption = Column(Integer)
    policy_limit = Column(Integer)
    gwp = Column(Integer)
    base_rate = Column(Float)
    claims_total = Column(Integer)
    loss_ratio = Column(Float)
    technical_adequacy = Column(Integer)
    modelled_results_aal = Column(Integer)

class Account(Base):
    __tablename__ = 'accounts'
    __table_args__ = {"schema": "silas"}
    id = Column(Integer, primary_key=True)
    named_insured = Column(String(50), nullable=True)
    underwriter = Column(String(50), nullable=True)
    broker = Column(String(50), nullable=True)
    inception_date = Column(String(50), nullable=True)
    tiv = Column(Integer, nullable=True)
    occupancy = Column(String(50), nullable=True)
    gwp = Column(Integer, nullable=True)
    base_rate = Column(Float, nullable=True)
    loss_ratio = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)

class AccountYoY(Base):
    __tablename__ = 'accounts_yoy'
    __table_args__ = {"schema": "silas"}
    id = Column(Integer, primary_key=True)
    date = Column(String(50), nullable=True)
    accts_written_by_month = Column(Integer, nullable=True)
    gwp_by_month = Column(Integer, nullable=True)
    nwp_by_month = Column(Integer, nullable=True)

class DepartmentOverview(Base):
    __tablename__ = 'department_overview'
    __table_args__ = {"schema": "silas"}
    id = Column(Integer, primary_key=True)
    department = Column(Integer)
    year = Column(Integer)
    brokerage = Column(Float)
    fees_and_commissions = Column(Float)
    nwp = Column(Integer)
    gwp = Column(Integer)
    loss_ratio = Column(Float)
    gross_claims_total = Column(Integer)
    number_of_claims = Column(Integer)
    total_cat = Column(Integer)
    total_non_cat = Column(Integer)
    total_cat_perc_gwp = Column(Float)
    total_cat_perc_nwp = Column(Float)

class DepartmentOccupancy(Base):
    __tablename__ = 'department_occupancy'
    __table_args__ = {"schema": "silas"}
    id = Column(Integer, primary_key=True)
    department = Column(Integer)
    occupancy = Column(String(50))
    iso = Column(Integer)
    gwp = Column(Integer)
    tiv = Column(Integer)
    base_rate = Column(Float)
    claims_total = Column(Integer)
    loss_ratio = Column(Integer)


class NewMetrics(Base):
    __tablename__ = 'new_metrics'
    __table_args__ = {"schema": "silas"}
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer)
    named_insured = Column(String)
    year = Column(Integer)
    gwp = Column(Integer)
    nwp = Column(Integer)
    base_rate = Column(Numeric(precision=8, scale=2))
    rate_change = Column(Numeric(precision=8, scale=2))
    policy_limit = Column(Numeric(precision=12, scale=2))
    brokerage = Column(Numeric(precision=8, scale=2))
    fees_and_commissions = Column(Numeric(precision=8, scale=2))
    number_of_claims = Column(Numeric(precision=12, scale=2))
    property_damage = Column(Numeric(precision=12, scale=2))
    bi_deductible = Column(Numeric(precision=12, scale=2))
    tech_price = Column(Numeric(precision=12, scale=2))
    aal = Column(Numeric(precision=12, scale=2))
    gct_cpy = Column(Numeric(precision=12, scale=2))
    gct_cat = Column(Numeric(precision=12, scale=2))
    gct_perc_gwp = Column(Numeric(precision=8, scale=2))
    gct_perc_nwp = Column(Numeric(precision=8, scale=2))
    business_interruption = Column(Numeric(precision=12, scale=2))
    aop_deductible = Column(Numeric(precision=12, scale=2))
    aal_perc_gwp = Column(Numeric(precision=8, scale=2))
    avg_rate_change = Column(Numeric(precision=8, scale=2))
    rate_on_tiv = Column(Numeric(precision=8, scale=2))
    rate_on_line = Column(Numeric(precision=8, scale=2))
    tiv = Column(Numeric(precision=8, scale=2))
    gct_not_cat = Column(Numeric(precision=12, scale=2))
    claims_total = Column(Integer)
    loss_ratio = Column(Integer)
    technical_adequacy = Column(Integer)