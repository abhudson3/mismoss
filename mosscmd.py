import re

def extract_http_substring(input_string):
    # Define the regex pattern to match a substring starting with "http" and continuing to the end
    pattern = r"http.*"

    # Search for the pattern in the input string
    match = re.search(pattern, input_string)

    # Check if a match was found
    if match:
        # Return the matched substring
        return match.group()
    else:
        # Return an empty string or appropriate message if no match is found
        return "No 'http' found in the string"

# Example usage
input_str = "Query submitted.  Waiting for the server's response. http://moss.stanford.edu/results/0/3564765107325"
result = extract_http_substring(input_str)
print(result)
