from google import genai

# Initialize the model correctly
model = genai.GenerativeModel(model_name="gemini-1.5-flash", api_key="AIzaSyAPTKofQo51ucu4LswGwvtYrGT0R2vLq4g")

# Two-paragraph Sona-style prompt
prompt = (
    "Hii, I'm Sona 🌸! I'm a little shy when it comes to tech stuff, but I’ve always been super curious about how things work — especially cool things like AI. "
    "I'm that girl who quietly sits in the corner, vibing to BTS 💜, probably daydreaming about Jungkook while secretly wondering how machines can 'think' like humans. "
    "I'm not a tech genius (yet 😅), but I do like learning new things in a soft and simple way. Please don’t make it too complex for my pookie brain 🐰✨."

    "\n\nSo, could you explain how AI works in just a few words? Like, what’s actually happening when an AI like you talks, learns, or gives answers? "
    "Imagine you're telling someone who's smart but also gets overwhelmed by too much jargon (that’s me 🙈). I’d love a simple, friendly explanation — maybe even a tiny bit magical if you can!"
)

# Generate response
response = model.generate_content(prompt)

# Print the response
print("Sona's AI answer:\n", response.text)
