from nltk.chat.util import Chat, reflections
import random

# Liste des questions-réponses
paires = [
    # msg de bienvenue
    (r"(?i).*(bonjour|salut|coucou).*", 
     ["Bonjour ! Comment puis-je vous aider avec votre routine skincare ?", 
      "Salut ! Besoin de conseils pour votre peau ?"]),
    # Routines par type de peau
    (r"(?i).*(routine|conseils).*(peau grasse).*", 
     ["Pour peau grasse : nettoyant doux, tonique, crème légère et écran solaire."]),
     
    (r"(?i).*(routine|conseils).*(peau sèche).*", 
     ["Pour peau sèche : nettoyant hydratant, crème riche et protection solaire."]),
     
    (r"(?i).*(routine|conseils).*(peau mixte).*", 
     ["Pour peau mixte : nettoyant doux, hydratant léger et écran solaire."]),
     
    (r"(?i).*(routine|conseils).*(peau sensible).*", 
     ["Pour peau sensible : produits doux, sans parfum et crème apaisante."]),

    # Nettoyage
    (r"(?i).*(nettoyer|laver).*visage.*", 
     ["Nettoyez votre visage matin et soir avec un nettoyant adapté. Évitez l’eau trop chaude."]),
    
    # Ordre des produits
    (r"(?i).*(ordre des produits|dans quel ordre).*", 
     ["Routine classique : Nettoyant > Tonique > Sérum > Crème > Protection solaire (matin)."]),
    
    # Remerciements
    (r"(?i).*(merci|merci beaucoup).*", 
     ["Avec plaisir ! Revenez quand vous voulez pour d'autres conseils."]),

    # msg de sortie
    (r"(?i).*(au revoir|bye|à bientôt).*", 
     ["Au revoir ! Prenez soin de votre peau !"])
]

# Création du chatbot
chatbot = Chat(paires, reflections)

print("Bienvenue ! Posez-moi vos questions sur les soins de la peau.")
print("(Tapez 'au revoir' pour quitter)")

while True:
    # Demande à l'utilisateur
    message = input("Vous: ")
    
    # Quitter si l'utilisateur dit au revoir
    if message.lower() in ["au revoir", "bye", "à bientôt"]:
        print("Skincare Bot: À bientôt ! N'oubliez pas votre routine quotidienne.")
        break
    # Réponse du chatbot
    reponse = chatbot.respond(message)
    
    # Si le bot ne comprend pas
    if not reponse:
        print("Skincare Bot: Je n'ai pas compris. Pouvez-vous reformuler ?")
    else:
        print("Skincare Bot:", reponse)