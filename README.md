# Project Structure

This project aims to predict the outcome of an NBA game using a wide range of dataframes and ML models. We employed 5 different dataframes and 4 different models. Feel free to navigate through our project to see our process :)

## Part 1: Data Collection

- Navigate to the /data collection directory

Files:
1. data_collection.ipynb

## Part 2: Data Parsing

- Navigate to the /data parsing directory

Files:
1. data_parsing.ipynb

## Part 3: Data Preparation

- Navigate to the /data preparation directory
  
Files:
1. data_preparation.ipynb

## Part 4: Feature Engineering

- Navigate to the /feature engineering directory

Files:
1. feature_engineering_df.ipynb
2. export_cumulative_df.ipynb
3. export_prev_game_df.ipynb
4. export_rolling_average_df.ipynb

## Part 5: Data Exploration

- Navigate to the /data exploration directory
Files:
1. data_exploration-4-factors.ipynb
2. data_exploration.ipynb


## Part 6: Model Training, Validation and Testing

- Navigate to the /model training directory

Files:
1. model_training_cumulative_averages.ipynb
2. model_training_windowed_average_5_day.ipynb
3. model_training_windowed_average.ipynb
4. model_training_windowed_average_10_day.ipynb
5. model_training_prev_games.ipynb

## Part 7: View Results

- To view various metrics relating to how each dataframe performed under each model, navigate to the /csvs/model_results directory
- Here, you can find CSV files containing each dataframe's accuracy, recall, precision, F1 score and ROC_AUC.
- For the testing results, you can find them near the end of the model_training_cumulative_averages.ipynb notebook. The results are located here because we decided to use the features in the cumulative averages dataframe for testing, as it provided the best validation results. Therefore, after we compared all the different combinations of models and dataframes, we just continued off of that specific notebook.
