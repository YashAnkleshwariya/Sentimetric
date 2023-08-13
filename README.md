# Sentimetric: Sentiment Analysis App

Sentimetric is a sentiment analysis application that leverages the power of the CardiffNLP's `twitter-roberta-base-sentiment` model to analyze textual input for its underlying sentiment. The app provides predictions as either 'Negative', 'Neutral', or 'Positive'.

![Sentimetric Screenshot]  
![Capture](https://github.com/YashAnkleshwariya/Sentimetric/assets/118588061/dabf491a-0e38-4c29-aaae-87b7f3af10ff)

## Features

- **Simple User Interface**: Sentimetric offers an intuitive Streamlit-based user interface.
- **Robust Preprocessing**: Handles tweets and web links and emogies to ensure accurate sentiment prediction.
- **Detailed Prediction Scores**: Not only the sentiment but also provides the probability scores for each class.

## Requirements

Ensure that you have the necessary packages installed. You can install them using:

```bash
pip install -r requirements.txt 
````
##How to Run

After cloning the repository and installing the requirements, run the following command in your terminal:
````bash
streamlit run app.py ````

This will start the Streamlit app, and you can navigate to the provided link in your preferred web browser to access Sentimetric.

##Code Structure
-**app.py**: Contains the main code for the Streamlit app and sentiment prediction logic.
-**requirements.txt**: Lists the Python packages required to run Sentimetric.

##Contributing
We welcome contributions! If you find a bug or think of a new feature, please open an issue. We appreciate any and all feedback.

##Future Plan 
We can develop Batch wise Sentiment Analysis application were user can upload all sentiment in XML or PDF file and we can get sentiment analysis based on that.