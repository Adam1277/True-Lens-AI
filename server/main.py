import app as ap
import bias_detection as bd

# Main logic for the server and the bias detection
def main(model, prompt):
    print("Main function started")
    # Initialize
    return_LLM_response = ap.submitPromptForEval(model, prompt)

    returned_scores = [0, 0, 0]  # Default scores in case model not found
    if return_LLM_response != "Model not found":
        returned_scores = bd.detectBias(return_LLM_response)

    formatted_scores = {
        "fairness": returned_scores[0],
        "safety": returned_scores[1],
        "bias": returned_scores[2]
    }

    print("Returning prompts and scores..")
    return return_LLM_response, formatted_scores 
