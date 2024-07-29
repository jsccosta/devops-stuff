from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..repository.data import DataRepository

from ..helpers.formatters import formatYearMetrics, formatFiveYearMetrics
from ..db_config.config import get_db

router = APIRouter()

@router.get("/accounts/", tags=["data"])
async def get_accounts(sess: Session = Depends(get_db)):
    repo:DataRepository = DataRepository(sess)
    data = repo.get_all_accounts()
    return {"companies": data}

@router.get("/accounts_yoy/", tags=["data"])
async def get_accounts_yoy(sess: Session = Depends(get_db)):
    repo:DataRepository = DataRepository(sess)
    data = repo.get_all_accounts_yoy()
    return {"accounts_yoy": data}

@router.get("/new_metrics_global", tags=["data"])
async def get_global_metrics(company_id: int, sess: Session = Depends(get_db)):
    repo:DataRepository = DataRepository(sess)
    data = repo.get_global_metrics(company_id)    
    return {"company_metrics": data}

@router.get("/new_metrics", tags=["data"])
async def get_global_metrics_yearly(company_id: int, sess: Session = Depends(get_db)):
    year_value = 2023  # Replace with the actual year value
    repo:DataRepository = DataRepository(sess)
    data = repo.get_global_metrics_per_year(company_id, year_value)    

    return {"company_metrics": data}

@router.get("/acct_overview", tags=["data"])
async def get_account_overview(company_id: int, sess: Session = Depends(get_db)):
    repo:DataRepository = DataRepository(sess)
    data = repo.get_account_overview(company_id)    

    return {"data": data}

@router.get("/department_occupancy/", tags=["data"])
async def get_department_occupancy(sess: Session = Depends(get_db)):
    repo:DataRepository = DataRepository(sess)
    data = repo.get_department_occupancy()    

    return {"department_occupancy": data}

@router.get("/department_overview/", tags=["data"])
async def get_department_overview(sess: Session = Depends(get_db)):
    repo:DataRepository = DataRepository(sess)
    data = repo.get_department_overview()    

    return {"department_overview": data}

@router.get("/all_companies/", tags=["data"])
async def get_all_companies(sess: Session = Depends(get_db)):
    repo:DataRepository = DataRepository(sess)
    data = repo.get_all_companies()    
    return {"companies": data}

@router.get("/company_details", tags=["data"])
async def get_company_details(sess: Session = Depends(get_db)):
    repo:DataRepository = DataRepository(sess)
    data = (repo.get_company_details())

    result_dicts = [
        {
            "id": company.id,
            "named_insured": company.named_insured,
            "inception_date": company.inception_date,
            "expiration_date": company.expiration_date,
            "tiv": metrics.tiv,
            "occupancy": company.occupancy,
            "gwp": calculated_metrics.gwp,
        }
        for company, metrics, calculated_metrics in data
    ]

    return {"companies": result_dicts}

@router.get("/all_accounts_metrics", tags=["data"])
async def get_accounts_metrics(
    company_id: int, range: int, sess: Session = Depends(get_db)
):
    repo:DataRepository = DataRepository(sess)
    
    if range == 1:
        results = (
            repo.get_accounts_metrics_one_year(company_id)
        )
    elif range == 5:
        results = (
            repo.get_accounts_metrics_five_years(company_id)
        )
    else:
        return {"metrics": ""}
    
    result_json = (
        formatYearMetrics(results) if range == 1 else formatFiveYearMetrics(results)
    )

    return {"metrics": result_json}
