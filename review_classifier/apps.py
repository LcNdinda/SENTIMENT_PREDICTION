from django.apps import AppConfig
from keras.models import load_model
import pickle


class ReviewClassifierConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "review_classifier"
    model = None

    def ready(self):
        # Adjust the path as needed
        ReviewClassifierConfig.model = load_model(
            '../final_model_2.h5',
            compile=False)

        # Load the tokenizer
        with open(
                '../tokenizer_2.pickle',
                'rb') as handle:
            ReviewClassifierConfig.tokenizer = pickle.load(handle)
