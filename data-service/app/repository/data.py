from sqlalchemy.orm import Session
from ..models.data_models import *

class DataRepository: 
    def __init__(self, sess:Session):
        self.sess:Session = sess

    def get_all_accounts(self):
        return self.sess.query(Account).all() 
    
    def get_all_accounts_yoy(self):
        return self.sess.query(AccountYoY).all() 
    
    def get_global_metrics(self, company_id:int):
        print('Company id')
        print(company_id)
        return self.sess.query(NewMetrics).filter(NewMetrics.company_id == company_id).all()
    
    def get_global_metrics_per_year(self, company_id:int, year_value: int):
        return self.sess.query(NewMetrics).filter(NewMetrics.company_id == company_id, NewMetrics.year == year_value).all()

    def get_account_overview(self, company_id:int):
        return self.sess.query(AccountOverview).filter(AccountOverview.company_id == company_id).all()
    
    def get_department_occupancy(self):
        return self.sess.query(DepartmentOccupancy).all()

    def get_department_overview(self):
        return self.sess.query(DepartmentOverview).all()

    def get_all_companies(self):
        return self.sess.query(Company).all()

    def get_company_details(self):
        return self.sess.query(Company, Metrics, CalculatedMetrics).filter(Company.id == Metrics.company_id).filter(Company.id == CalculatedMetrics.company_id).filter(Metrics.year == 2023).filter(CalculatedMetrics.year == 2023).all()


    def get_accounts_metrics_one_year(self, company_id: int):
        return self.sess.query(Company, Metrics, CalculatedMetrics).filter(Company.id == company_id).filter(Company.id == Metrics.company_id).filter(Company.id == CalculatedMetrics.company_id).first()
        
    def get_accounts_metrics_five_years(self, company_id: int):
        return self.sess.query(Company, FiveYearSummaryMetrics, CalculatedFiveYSummaryMetrics).filter(Company.id == company_id).filter(Company.id == FiveYearSummaryMetrics.company_id).filter(Company.id == CalculatedFiveYSummaryMetrics.company_id).first()