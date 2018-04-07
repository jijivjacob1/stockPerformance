# The Oracles of Wall Street
### Stock Performance Predictions using Machine Learning
____________________________________________________________________________________________________________
Emotions can drive short-term market fluctuations causing disconnect between the price and true value of a company’s shares.  Over long periods of time, a company’s fundamentals ultimately cause the value and market price of its shares to converge. This projects uses forty stock features to attempt to predict stock performance compared to the S&P 500 Index using two machine learning algorithms: 

    * Support Vector Machine Classifier
    * Random Forest Classifier

The final application allows dynamic exploration of S&P 500 stocks as well as the abiilty to query QUANDL for up-to-date stock information to provide a performance prediction of a chosen stock. We hope to be better than a coin flip!

____________________________________________________________________________________________________________

### Languages and Tools:
* Pandas
* SQlite DB
* Scikit Learn
* Flask
* Java Script
* D3
* HTML
* Tableau


### Process: 

*  Quandl was used to gather data from 2008-2018. 
*  Data manipulation and engineering completed using pandas. 
*  Tableau used to create interactive visualizations for data exploration. Tableau Public used to obtain 
   tag to embed into webpage. 
*  FlaskAPI used to generate dynamic app pulling current stock data from quandl and running to ML algorithm.

### ML Outcomes:

Model   |   Kernels   |   Accuracy
--- | --- | ---
Support Vector Machine Classifier     | RBF ( C=50, gamma = 0.005) | 73%
Support Vector Machine Classifier     | Linear ( C=5, gamma = 0.0001) | 67%
Random Forest Classifier  | N_estimators = 700, max_features = sqrt | 87%






### Team Members:
Jiji Jacob, Bopanna Malachira, Adam Darnell, Wendy Walsh