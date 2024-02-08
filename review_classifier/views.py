from django.shortcuts import render
from .apps import ReviewClassifierConfig  # Ensure this correctly imports your AppConfig subclass
import numpy as np
from keras.preprocessing.sequence import pad_sequences
def predict_review(request):
    sentiment = 'Please submit a review to analyze.'  # Default message
    review_text = ''

    if request.method == 'POST':
        review_text = request.POST.get('review_text', "").strip()

        # Ensure there's actual text to process
        if review_text:
            # Tokenize the input text
            sequence = ReviewClassifierConfig.tokenizer.texts_to_sequences([review_text])

            # Debugging: Print the tokenized sequence
            print("Tokenized sequence:", sequence)

            # Pad the sequences
            padded_sequence = pad_sequences(sequence, maxlen=200)  # Adjust as per your model

            # Debugging: Print the padded sequence
            print("Padded sequence:", padded_sequence)

            # Predict sentiment
            sentiment_scores = ReviewClassifierConfig.model.predict(padded_sequence)[0]
            print(f"Raw model output: {sentiment_scores}")  # For debugging

            # Interpret the prediction
            sentiment_idx = np.argmax(sentiment_scores)
            sentiments = ['Negative', 'Positive', 'Neutral']  # Adjust based on your model
            sentiment = sentiments[sentiment_idx]
            print(sentiment)
        else:
            sentiment = "No review text provided."

    # Render the same template for form input and displaying results
    return render(request, 'review_classifier/predict_review.html', {'sentiment': sentiment, 'review_text': review_text})
