# Importation des modules nécessaires de Flask pour créer l'application web
from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Chargement de la configuration IA
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# Création d'une instance de l'application Flask
app = Flask(__name__)

def get_system_context():
    """Lit les fichiers du dossier context pour définir le comportement de l'IA."""
    context_dir = "context"
    files = ["project.txt", "rules.txt", "style.txt", "ui_context.txt"]
    full_context = "Instructions à suivre :\n\n"
    
    for file_name in files:
        path = os.path.join(context_dir, file_name)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                full_context += f.read() + "\n"
    
    return full_context

# Définition de la route pour la page d'accueil (URL racine "/")
@app.route("/")
def home():
    # Rend le template HTML "index.html" pour afficher la page d'accueil
    return render_template("index.html")

# Définition de la route pour traiter les questions (méthode POST sur "/ask")
@app.route("/ask", methods=["POST"])
def ask():
    # Récupération de la question soumise via le formulaire
    question = request.form["question"]
    
    try:
        # Chargement du contexte métier et des règles
        system_context = get_system_context()
        prompt = f"{system_context}\nUtilisateur : {question}"
        
        # Appel à l'IA Gemini pour générer une réponse
        response = model.generate_content(prompt)
        # Renvoie le template avec la réponse pour l'afficher sur la même page
        return render_template("index.html", response=response.text, question=question)
    except Exception as e:
        return render_template("index.html", error=str(e))

# Bloc exécuté uniquement si le script est lancé directement (pas importé)
if __name__ == "__main__":
    # Lancement de l'application en mode debug pour le développement
    app.run(debug=True)