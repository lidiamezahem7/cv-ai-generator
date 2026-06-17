import os
import openai

# 1) Récupérer la clé API OpenAI depuis la variable d'environnement
openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_cv(text: str) -> str:
    prompt = f"""
    Tu es un assistant IA qui génère un CV professionnel complet à partir du texte brut suivant :
    {text}

    Génère un CV structuré avec sections : Résumé, Expérience, Compétences, Formation.
    """

    # 2) Appeler l'API OpenAI en mode asynchrone
    client = openai.OpenAI()
    response = await client.chat.completions.acreate(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800,
        temperature=0.7,
    )

    # 3) Retourner le texte généré
    return response.choices[0].message.content.strip()