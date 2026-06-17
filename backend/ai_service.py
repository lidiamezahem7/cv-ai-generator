def rewrite_cv(text: str) -> str:
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    cleaned = "\n".join(lines)

    result = f"""
Résumé professionnel
--------------------
Développeur(se) orienté(e) IA / fullstack, capable de concevoir et déployer des applications modernes.

Expérience
----------
{cleaned}

Compétences clés
----------------
- Développement web (React, .NET, Python)
- APIs REST
- Cloud & CI/CD
- IA appliquée

CV original (nettoyé)
---------------------
{cleaned}
"""
    return result.strip()
