# A2 - Car Price Prediction

### Description:

Car price prediction tool provides the means for users to input the car specifications such as car max power (BHP), manufacture year, fuel type and brand in order to find the best selling price of the car. Our tool uses Random Forest Regressor model with $R^2$ score of 93% and linear regression model using gradient descent method with $R^2$ score of 73% for the predictions.

 ### How to use:

 1. Install the following extensions on your Visual Studio Code; Docker and Remote Explorer.
 2. Simply open the main directory of 'Car-Price-Prediction' in Visual Studio Code then locates the 'docker-compose.yaml' file inside the 'app' folder. Right click on the file and select 'Compose Up' then wait until everything is set up.
 3. Switch to Docker view in yor VS Code and right click on 'parunng/car_price_prediction:a2' image inside the 'app' container then select 'Attach Visual Studio Code'. A new window of VS Code will pop up.
 4. Finally, run the script 'main.py' inside the '/root/code' folder, the application of car price prediction tool will run on http://127.0.0.1:8001/

Alternatively, you can visit our website at a2.st124026.ml2023.cs.ait.ac.th in order to access our prediction tool directly from the internet.