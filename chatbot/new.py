import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyAPTKofQo51ucu4LswGwvtYrGT0R2vLq4g")

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Expanded prompt with detailed info request
prompt = (
    "Please provide a detailed life history of MS Dhoni, one of the greatest Indian cricketers and captains. "
    "Start with his early life and childhood in Ranchi, including his family background and how he developed an interest in cricket. "
    "Describe his journey from playing local cricket to making his debut in international cricket, and highlight his rise as a wicketkeeper-batsman.\n\n"

    "Explain his leadership style and how he became the captain of the Indian cricket team, including his achievements such as leading India to win the ICC T20 World Cup in 2007, the ICC ODI World Cup in 2011, and the ICC Champions Trophy in 2013. "
    "Mention key moments like his finishing abilities in matches, calmness under pressure, and innovations on the field.\n\n"

    "Also include details about his personal life, such as his marriage, hobbies, and interests outside cricket. "
    "Discuss his impact on Indian cricket and young players, and what makes him a respected figure both on and off the field.\n\n"

    "Finally, talk about his retirement from international cricket, his role in the Indian Premier League (IPL) with Chennai Super Kings, and his ventures outside cricket including business and philanthropy."
)

# Generate the response
response = model.generate_content(prompt)

# Print the detailed life history
print("Detailed MS Dhoni Life History:\n", response.text)
