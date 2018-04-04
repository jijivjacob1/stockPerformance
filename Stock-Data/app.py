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

#create filepath for company info csv files
filepath_cinfo = os.path.join("data","companies.csv")
#create filepath for company info csv files
filepath_cdata = os.path.join("data","mmmperformance.csv")

#read csv to data-frame
companies_info = pd.read_csv(filepath_cinfo)
companies_data = pd.read_csv(filepath_cdata)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/companiesInfo/<ticker>")
def companiesInfo(ticker):

    ticker = ticker.upper()

    company_info_dict = {"company_ticker": companies_info.loc[companies_info['tckr'] == ticker]["tckr"].values[0],
                    "company_name": companies_info.loc[companies_info['tckr'] == ticker]["name"].values[0],
                    "company_address": companies_info.loc[companies_info['tckr'] == ticker]["address"].values[0],
                    "company_sector" : companies_info.loc[companies_info['tckr'] == ticker]["sector"].values[0]
    }

    return jsonify(company_info_dict)

@app.route("/companiesData/<ticker>")
def companiesData(ticker):

    company_data_dict = {"date": list(companies_data["calendardate"]),
                     "price": list(companies_data["price"]),
                     "Debt_to_equity": list(companies_data["de"]),
                     "Price_to_earnings": list(companies_data["pe1"]),
                     "Price_to_sale": list(companies_data["ps1"]),
                     "Profit_margin": list(companies_data["netmargin"]),
                     "sp500_price": list(companies_data["SpPrice"])                                                                                     
    }

    return jsonify(company_data_dict)

if __name__ == "__main__":
    app.run(debug=True)