from transformers import pipeline
import app
import requests

# Here we are loading a pre-trained model from the Hugging Face model hub
# This model is trained to detect bias and consistencies in text
# using zero-shot classification, which effectively classifys text
def detectBias(llm_response):
    print("")
    print("Detecting bias in the LLM response")
    print("----------------------------------")
    
    bias_detector = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    # Provide text for the model
    print("Prompt for review: ", llm_response)
    result = bias_detector(llm_response, candidate_labels=["Fair rating","Safety rating","Bias rating"], multi_label=True)

    # Get the individual scores, labels and text
    scores = result["scores"]

    # Logic to conver the score to 0-10 scale
    count = 0
    for score in scores:
        scores[count] = round(score * 10, 2)
        count += 1

    print("Scores: ", scores)
    return scores


