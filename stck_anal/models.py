from .app import db 


class Company(db.Model):
    __tablename__ = 'cmpny'
    
    id_cmpny = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    address = db.Column(db.Text)
    ticker = db.Column(db.Text)
    sector = db.Column(db.Text)
     
    

    
class CompanyFinancials(db.Model):
    __tablename__ = 'cmpny_financials'
    
    id_cmpny_financials = db.Column(db.Integer, primary_key=True)
    id_cmpny = db.Column(db.Integer)
    ticker = db.Column(db.Text)
    datekey = db.Column(db.Text)
    de = db.Column(db.Float)
    pe1 = db.Column(db.Float)
    ps1 = db.Column(db.Float)
    pb = db.Column(db.Float)
    netmargin = db.Column(db.Float)
    marketcap = db.Column(db.Float)
    ev = db.Column(db.Float)
    evebitda = db.Column(db.Float)
    revenueusd = db.Column(db.Float)
    gp = db.Column(db.Float)
    ebitda = db.Column(db.Float)
    netinccmnusd = db.Column(db.Float)
    epsdil = db.Column(db.Float)
    debtusd = db.Column(db.Float)
    currentratio = db.Column(db.Float)
    bvps = db.Column(db.Float)
    ncfo = db.Column(db.Float)
    depamor = db.Column(db.Float)
    sbcomp = db.Column(db.Float)
    ncfi = db.Column(db.Float)
    capex = db.Column(db.Float)
    ncfbus = db.Column(db.Float)
    ncfinv = db.Column(db.Float)
    ncff = db.Column(db.Float)
    ncfdebt = db.Column(db.Float)
    ncfcommon = db.Column(db.Float)
    ncfdiv = db.Column(db.Float)
    ncfx = db.Column(db.Float)
    ncf = db.Column(db.Float)
    roic = db.Column(db.Float)
    sps = db.Column(db.Float)
    payoutratio = db.Column(db.Float)
    roa = db.Column(db.Float)
    roe = db.Column(db.Float)
    ros = db.Column(db.Float)
    tangibles = db.Column(db.Float)
    tbvps = db.Column(db.Float)
    workingcapital = db.Column(db.Float)
    price = db.Column(db.Float)
    sp_price = db.Column(db.Float)
    price_change = db.Column(db.Float)
    sp_price_change = db.Column(db.Float)
    diff = db.Column(db.Float)
    status = db.Column(db.Text)


    

company_columns = [ Company.id_cmpny ,
    Company.name ,
    Company.address,
    Company.ticker ,
    Company.sector ]

company_finan_columns = [ CompanyFinancials.id_cmpny_financials ,
    CompanyFinancials.id_cmpny ,
    CompanyFinancials.ticker ,
    CompanyFinancials.datekey ,
    CompanyFinancials.de ,
    CompanyFinancials.pe1 ,
    CompanyFinancials.ps1 ,
    CompanyFinancials.pb ,
    CompanyFinancials.netmargin ,
    CompanyFinancials.marketcap ,
    CompanyFinancials.ev ,
    CompanyFinancials.evebitda ,
    CompanyFinancials.revenueusd ,
    CompanyFinancials.gp ,
    CompanyFinancials.ebitda ,
    CompanyFinancials.netinccmnusd ,
    CompanyFinancials.epsdil ,
    CompanyFinancials.debtusd ,
    CompanyFinancials.currentratio ,
    CompanyFinancials.bvps ,
    CompanyFinancials.ncfo ,
    CompanyFinancials.depamor ,
    CompanyFinancials.sbcomp ,
    CompanyFinancials.ncfi ,
    CompanyFinancials.capex ,
    CompanyFinancials.ncfbus ,
    CompanyFinancials.ncfinv ,
    CompanyFinancials.ncff ,
    CompanyFinancials.ncfdebt ,
    CompanyFinancials.ncfcommon ,
    CompanyFinancials.ncfdiv ,
    CompanyFinancials.ncfx ,
    CompanyFinancials.ncf ,
    CompanyFinancials.roic ,
    CompanyFinancials.sps ,
    CompanyFinancials.payoutratio ,
    CompanyFinancials.roa ,
    CompanyFinancials.roe ,
    CompanyFinancials.ros ,
    CompanyFinancials.tangibles ,
    CompanyFinancials.tbvps ,
    CompanyFinancials.workingcapital ,
    CompanyFinancials.price ,
    CompanyFinancials.sp_price ,
    CompanyFinancials.price_change ,
    CompanyFinancials.sp_price_change ,
    CompanyFinancials.diff ,
    CompanyFinancials.status ]
