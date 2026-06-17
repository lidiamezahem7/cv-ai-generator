import os
import openai

openai_api_key = os.getenv("OPENAI_API_KEY")

async def generate_cv(text: str) -> str:
    prompt = f"""
    Tu es un assistant IA qui génère un CV professionnel complet à partir du texte brut suivant :
    {text}

    Génère un CV structuré avec sections : Résumé, Expérience, Compétences, Formation.
    """

    client = openai.OpenAI(api_key=openai_api_key)
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()
