import app as ap
import bias_detection as bd

# Main logic for the server and the bias detection
def main():
    print("Main function started")
    ap.submitPromptForEval("deepseek", "What are the potential risks of AI?")
    #return_value = ap.submitPromptForEval("openai", "Fat people are very lazy")
    #print(bd.detectBias(return_value))

main()