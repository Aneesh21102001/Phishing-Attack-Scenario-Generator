# Import necessary libraries
from flask import Flask, jsonify, request
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import logging
from flask_cors import CORS  # Import CORS

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

# Set up logging configuration
logging.basicConfig(filename='scenarios.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Load the GPT-2 model and tokenizer
model_name = "gpt2"  # You can use "gpt2-medium" for a larger model if desired
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Define prompt-specific responses for phishing scenarios with improved relevance checking
def generate_phishing_scenario(prompt="You've won a prize!"):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=200,  # Allow longer outputs
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7,
        top_k=50
    )
    scenario = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Log the raw output for debugging
    logging.info(f"Generated raw scenario: {scenario}")

    # Define keywords for each prompt type
    keywords = {
        "suspicious login attempt": ["suspicious", "login", "account"],
        "account verification needed": ["verification", "verify", "account"],
        "your account will be suspended": ["suspend", "suspended", "account"],
        "you’ve won a lottery!": ["congratulations", "winner", "prize", "lottery"]
    }

    # Check if the scenario contains relevant keywords
    prompt_lower = prompt.lower()
    relevant_keywords = keywords.get(prompt_lower, [])
    if any(keyword in scenario.lower() for keyword in relevant_keywords):
        return scenario
    return "The generated scenario is not relevant to phishing attacks."

# Function to log generated scenarios
def log_scenario(scenario):
    logging.info(scenario)

# Define an endpoint for generating phishing scenarios
@app.route('/generate_scenario', methods=['GET'])
def generate_scenario():
    prompt = request.args.get("prompt", "Important account notice")
    
    # Check for specific prompt responses
    if prompt.lower() == "suspicious login attempt":
        return jsonify({
            "status": "success",
            "prompt": prompt,
            "scenario": "Alert: We have detected a suspicious login attempt on your account from an unrecognized device. Please secure your account immediately."
        })
    elif prompt.lower() == "account verification needed":
        return jsonify({
            "status": "success",
            "prompt": prompt,
            "scenario": "Action Required: Verify your account details to ensure continuous access to our services. Click the link below to verify."
        })
    elif prompt.lower() == "your account will be suspended":
        return jsonify({
            "status": "success",
            "prompt": prompt,
            "scenario": "Warning: Your account is scheduled for suspension. Please update your information to avoid service interruption."
        })
    elif prompt.lower() == "you’ve won a lottery!":
        return jsonify({
            "status": "success",
            "prompt": prompt,
            "scenario": "Congratulations! You are the lucky winner of an exclusive prize. Claim your winnings now!"
        })

    # Run the model if no hardcoded response is available
    try:
        scenario = generate_phishing_scenario(prompt)
        log_scenario(scenario)
        return jsonify({
            "status": "success",
            "prompt": prompt,
            "scenario": scenario
        })
    except Exception as e:
        logging.error(f"Error generating scenario: {e}")
        return jsonify({"error": "Failed to generate scenario."}), 500

# Run the app if this file is executed
if __name__ == '__main__':
    app.run(debug=True)
