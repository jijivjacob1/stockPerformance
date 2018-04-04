# import necessary libraries
import numpy as np
import pandas as pd
import os
import datetime

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







