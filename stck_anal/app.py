# import necessary libraries
import numpy as np
import pandas as pd
import os
import datetime
import dateutil.relativedelta
import quandl
import sys
from sklearn.externals import joblib

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///stck_anal.sqlite"
app.config['GOOGLE_API_KEY'] = os.environ.get('GOOGLE_API_KEY', '') or ''
app.config['QUANDL_API_KEY'] = os.environ.get('QUANDL_API_KEY', '') or ''


db = SQLAlchemy(app)
from .models import Company,company_columns,CompanyFinancials,company_finan_columns


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/companies')
def companies():
    results = db.session.query(*company_columns).all()

    df = pd.DataFrame(results, columns=['id_cmpny','name','address','ticker','sector'])
   

    return jsonify(df.to_dict(orient="records"))

@app.route('/companyFinancials/<ticker>')
def companyFinancials(ticker):
    
    ticker = ticker.upper()

    results = db.session.query(*company_finan_columns).filter(CompanyFinancials.ticker == ticker).all()

    df = pd.DataFrame(results, columns=['id_cmpny_financials',
    'id_cmpny' ,
    'ticker' ,
    'datekey' ,
    'de' ,
    'pe1' ,
    'ps1' ,
    'pb' ,
    'netmargin' ,
    'marketcap' ,
    'ev' ,
    'evebitda' ,
    'revenueusd' ,
    'gp' ,
    'ebitda' ,
    'netinccmnusd' ,
    'epsdil' ,
    'debtusd' ,
    'currentratio' ,
    'bvps' ,
    'ncfo' ,
    'depamor' ,
    'sbcomp' ,
    'ncfi' ,
    'capex' ,
    'ncfbus' ,
    'ncfinv' ,
    'ncff' ,
    'ncfdebt' ,
    'ncfcommon' ,
    'ncfdiv' ,
    'ncfx' ,
    'ncf' ,
    'roic' ,
    'sps' ,
    'payoutratio' ,
    'roa' ,
    'roe' ,
    'ros' ,
    'tangibles' ,
    'tbvps' ,
    'workingcapital' ,
    'price' ,
    'sp_price' ,
    'price_change' ,
    'sp_price_change' ,
    'diff' ,
    'status'])
   

    return jsonify(df.to_dict(orient="records"))


@app.route('/predictStock/<ticker>')
def predicStock(ticker):

    company_ticker = ticker.upper()

    quandl.ApiConfig.api_key = "bkLgy-fmbYDf_AuKMJeV"
    sp_test = pd.read_csv("GSPC.csv")
    column_not_needed = ["Open","High","Low","Adj Close","Volume"]
    sp_test.drop(column_not_needed,axis=1,inplace=True)
    sp_test.columns = ['datekey','sp_price']
    sp_test['datekey'] = pd.to_datetime(sp_test['datekey'])
    stck_fund_attr = ['datekey','DE','PE1','PS1','PB','NETMARGIN',
                                        'MARKETCAP',
                                        'EV',
                                        'EVEBITDA',
                                        'REVENUEUSD',
                                        'GP',
                                        'EBITDA',
                                        'NETINCCMNUSD',
                                        'EPSDIL',
                                        'DEBTUSD',
                                        'CURRENTRATIO',
                                        'BVPS',
                                        'NCFO',
                                        'DEPAMOR',
                                        'SBCOMP',
                                        'NCFI',
                                        'CAPEX',
                                        'NCFBUS',
                                        'NCFINV',
                                        'NCFF',
                                        'NCFDEBT',
                                        'NCFCOMMON',
                                        'NCFDIV',
                                        'NCFX',
                                        'NCF',
                                        'SPS',
                                        'PAYOUTRATIO',
                                        'TANGIBLES',
                                        'TBVPS',
                                        'WORKINGCAPITAL',
                                        'price']
    cmpny_financials_attr  = stck_fund_attr.copy()

    cmpny_financials_attr.extend(['sp_price' ,'price_change' ,'sp_price_change' ,'diff' ,'status'])                                     
                  
    cmpny_financials_attr = [x.lower() for x in cmpny_financials_attr]                                                                                   

    df_company_fundmntls = pd.DataFrame(columns=stck_fund_attr)

    try:
        
        print("starting " + company_ticker)

        df_company_fundmntls = quandl.get_table('SHARADAR/SF1', qopts={"columns":stck_fund_attr}, ticker=[company_ticker],dimension = 'ARQ')
        
        df_company_fundmntls.fillna(0.0)
    
        df_company_fundmntls = df_company_fundmntls.sort_values(by=['datekey'])
        df_company_fundmntls["sp_price"] = 0.0
        df_company_fundmntls["price_change"] = 0.0
        df_company_fundmntls["sp_price_change"] = 0.0
        df_company_fundmntls["diff"] = 0.0
        df_company_fundmntls["status"] = "underperform"
            

    
        stock_start_value = 0.0
        sp_start_value = 0.0
        diff = 0
        

         
          
        for index,row in df_company_fundmntls.iterrows():
             
              

              try:
                   check_sp_date_exists = sp_test[(sp_test.datekey == row["datekey"])]
                   df_company_fundmntls.set_value(index,"sp_price",check_sp_date_exists["sp_price"])

              except ValueError:
                   rpt_dt = row["datekey"]
                   print(rpt_dt)
                   rpt_dt = rpt_dt - dateutil.relativedelta.relativedelta(days=4)
                   print(rpt_dt)
                   check_sp_date_exists = sp_test[(sp_test.datekey == rpt_dt)]
                   df_company_fundmntls.set_value(index,"sp_price",check_sp_date_exists["sp_price"])
                  

    
            
                    
              if (index != 0):

                  if (stock_start_value > 0):
                      df_company_fundmntls.set_value(index,"price_change",(((row["price"] - stock_start_value) / stock_start_value)*100))

                  if (sp_start_value > 0.0):

                      df_company_fundmntls.set_value(index,"sp_price_change" ,(((check_sp_date_exists["sp_price"] - sp_start_value) / sp_start_value)*100))
                  diff = (df_company_fundmntls.get_value(index,"price_change") - df_company_fundmntls.get_value(index,"sp_price_change"))
                  df_company_fundmntls.set_value(index,"diff", diff)
              else:
                  stock_start_value = row["price"]
                  sp_start_value = df_company_fundmntls.get_value(index,"sp_price")


              if diff > 0:
                    status = "outperform"
              else:
                    status = "underperform"  
            
              df_company_fundmntls.set_value(index,"status", status)   
#               stock_start_value = row["price"]

              

              
              
            
        print("ending" + company_ticker)

    except quandl.NotFoundError as e:

        print(company_ticker + " not found ")
        pass
        
    except Exception as e :
        print("Unexpected error:", sys.exc_info()[0])
        pass

    
    X_test = df_company_fundmntls[(df_company_fundmntls.datekey == df_company_fundmntls["datekey"].max())]
    X_test = X_test.reset_index()
    column_not_needed = ["None","datekey","price","sp_price","price_change",'sp_price_change','diff','status']
    X_test.drop(column_not_needed,axis=1,inplace=True)

    saved_rf = joblib.load('rand_frst.pkl')


    df_pred_val = df_company_fundmntls[['datekey','pe1','tangibles','sps','ps1','debtusd','evebitda',
                      'depamor','de','epsdil','price','sp_price','price_change','sp_price_change','status']]

    df_pred_val["status"] = saved_rf.predict(X_test)[0]

    df_pred_val = df_pred_val.reset_index()

    df_pred_val.drop('None',axis=1,inplace=True)

    return jsonify(df_pred_val.to_dict(orient="records"))









