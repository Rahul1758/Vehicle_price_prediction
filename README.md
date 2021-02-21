# Vehicle Price predictor

1. DESCRIPTION
--------------
There are many sites which provide approximate selling price of your car based on its features (e.g Carwale). This application mimics the same task using Machine learning algorithms based on the car data avaiable. 

2. DATA
--------------
The dataset for this project is placed in the repository with name 'car data.csv'. The data collected includes buying year, car features and selling transaction details of the cars sold over the years. 

3. MODEL TRAINING
--------------
The libraries used in this project are scikit-learn, pandas & numpy.
Two algorithms were trained in this task, RandomForest & XGBoostRegressor and both performed equally well on the dataset with around 96% r2 score.
I have added the feature in which the user can chose one of the model mentioned above and get the predicted Selling price of the car. Please head to Webapp to try it out.

4. DEPLOYMENT
--------------
The app uses Streamlit framework to create a front-end API and is deployed on Heroku.
Streamlit is framework using which you can create aesthetic front-end Webapp without the need of HTML and CSS. You can check their website here. https://www.streamlit.io/
Please feel free to try out the app by hitting this link!! https://vehicle-price-predictor-1.herokuapp.com/

5. INSIGHTS
--------------
Though both the models perform well, the dataset is small and I think I could use more data to make predictions more accurate.
