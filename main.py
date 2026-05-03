# Importation de la bibliothèque Google Generative AI pour utiliser l'API Gemini
import google.generativeai as genai
# Importation du module os pour accéder aux variables d'environnement
import os
# Importation de dotenv pour charger les variables d'environnement depuis un fichier .env
from dotenv import load_dotenv

# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()

# Configuration de l'API Google Generative AI avec la clé API récupérée depuis les variables d'environnement
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Création d'un modèle génératif utilisant "gemini-pro"
model = genai.GenerativeModel("gemini-pro")

# Génération de contenu en réponse à la question "Explique Git simplement"
response = model.generate_content("Explique Git simplement")
# Affichage du texte de la réponse générée
print(response.text)