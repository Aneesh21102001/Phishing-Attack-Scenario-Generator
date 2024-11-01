import requests

# Define the list of test prompts
test_prompts = [
    "Suspicious Login Attempt",
    "Account Verification Needed",
    "Your Account Will Be Suspended",
    "You’ve Won a Lottery!"
]

# Base URL for the Flask app
base_url = "http://127.0.0.1:5000/generate_scenario"

# Function to test prompts
def run_tests():
    for prompt in test_prompts:
        try:
            response = requests.get(base_url, params={"prompt": prompt})
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            print(f"Prompt: {data['prompt']}")
            print(f"Scenario: {data['scenario']}\n")
        except requests.exceptions.RequestException as e:
            print(f"Failed to generate scenario for prompt: {prompt}, Error: {e}")

# Run the tests
if __name__ == "__main__":
    run_tests()
