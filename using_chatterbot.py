from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Configuration des profils de peau
SKIN_TYPES = {
    "grasse": {
        "routine soir": "1. Nettoyant gel\n2. Tonique\n3. Sérum niacinamide\n4. Crème légère",
        "routine matin": "1. Nettoyant doux\n2. Sérum matifiant\n3. Crème hydratante légère\n4. Écran solaire",
        "sérum": "Un bon sérum doit contenir des ingrédients régulateurs de sébum comme la niacinamide,",
        "nettoyant": "un nettoyant gel moussant",
        "conseil": "Évitez les produits trop riches qui pourraient obstruer vos pores"
    },
    "sèche": {
        "routine soir": "1. Nettoyant crème\n2. Sérum hydratant\n3. Crème riche\n4. Huile visage",
        "routine matin": "1. Nettoyant doux\n2. Sérum hydratant\n3. Crème riche\n4. Écran solaire",
        "sérum": "Choisis un sérum hydratant et nourrissant qui renforce la barrière cutanée. contenant acide hyaluronique, céramides",
        "nettoyant": "un nettoyant sans rinçage",
        "conseil": "Privilégiez les textures riches en céramides"
    },
    "mixte": {
        "routine soir": "1. Nettoyant doux\n2. Sérum adapté\n3. Crème équilibrante",
        "routine matin": "1. Nettoyant doux\n2. Sérum zone T\n3. Crème légère\n4. Écran solaire",
        "sérum": "Opte pour un sérum équilibrant qui hydrate sans graisser et cible les zones à problèmes. contenant  niacinamide, acide hyaluronique, aloe vera.",
        "nettoyant": "un nettoyant qui hydrate la peau et garde un ph équilibré",
        "conseil": "Adaptez les soins aux différentes zones du visage"
    }
}

def reponse_personnalisee(demande, skin_type):
    """Retourne une réponse adaptée au type de peau"""
    demande = demande.lower()
    if "routine" in demande and "soir" in demande:
        return f"Routine soir pour peau {skin_type}:\n{SKIN_TYPES[skin_type]['routine soir']}"
    elif "routine" in demande and "matin" in demande:
        return f"Voici une bonne routine du matin pour une peau {skin_type} :\n{SKIN_TYPES[skin_type]['routine matin']}"
    elif "nettoyant" in demande:
        return f"Pour votre peau {skin_type}, choisissez {SKIN_TYPES[skin_type]['nettoyant']}"
    elif "sérum" in demande:
        return f"Pour votre peau {skin_type}, choisissez {SKIN_TYPES[skin_type]['sérum']}"
    elif "conseil" in demande:
        return f"Conseil pour peau {skin_type}: {SKIN_TYPES[skin_type]['conseil']}"
    return "Je ne comprends pas votre demande."

# Initialisation du chatbot
bot = ChatBot("SkincareBot")
trainer = ListTrainer(bot)

# Entraînement de base
trainer.train([
    "Bonjour", "Bonjour ! Comment puis-je vous aider avec votre routine skincare ?",
    "routine", "Quelle routine vous intéresse ? Dites 'routine soir' ou 'routine matin'",
    "sérum" , "Quel est votre type de peau ? Je vous conseillerai le meilleur sérum",
    "soir", "Pour une routine du soir, quel est votre type de peau ? (grasse, sèche, mixte)",
    "matin", "Pour une routine du matin, quel est votre type de peau ? (grasse, sèche, mixte)",
    "nettoyant", "Quel est votre type de peau ? Je vous conseillerai le meilleur nettoyant",
    "ordre des produits","ordre classique : Nettoyant > Tonique > Sérum > Crème > Protection solaire (matin).",
    "conseil", "Dites-moi votre type de peau pour un conseil personnalisé",
    "merci", "Avec plaisir ! Revenez quand vous voulez pour d'autres conseils.",
    "au revoir", "À bientôt ! Prenez soin de votre peau !"
])

print("SkincareBot: Bonjour ! Je peux vous conseiller sur votre routine skincare.")

# Gestion de la conversation
current_skin_type = None
pending_request = None

while True:
    try:
        user_input = input("Vous: ").lower()
        
        if user_input in ["au revoir", "bye"]:
            print("SkincareBot: À bientôt !")
            break
        
        # Détection du type de peau
        skin_type_detected = None
        for skin_type in SKIN_TYPES: #on parcours le dictionnaire 
            if skin_type in user_input:
                skin_type_detected = skin_type
                current_skin_type = skin_type
                print(f"SkincareBot: Merci, peau {skin_type} notée.")
                if pending_request: #si elle n'est pas vide
                    print(reponse_personnalisee(pending_request, current_skin_type)) #pending request ici contient la demande de user 
                    pending_request = None #on vide le pending request pour stocker les autres message 
                break
        
        if skin_type_detected: #Si un type de peau a été détecté, on passe au prochain tour de boucle (on ne vérifie pas le reste du code dans cette itération).
            continue
            
        if current_skin_type and any(word in user_input for word in ["routine", "nettoyant", "conseil","sérum"]): #Si l’utilisateur a déjà donné son type de peau, et qu’il pose une question skincare (parmi les mots-clés),
                                                                                                                   #on lui répond directement de façon personnalisée. (mele5er bech yjewb ki yabda l user 3ta type de peau mte3ou
            print(reponse_personnalisee(user_input, current_skin_type))
        elif any(word in user_input for word in ["routine", "nettoyant", "conseil","sérum"]): #s'il pose la question sans donner son type de peau 
            pending_request = user_input     #on enregistre la question
            print("SkincareBot: Quel est votre type de peau ? (grasse, sèche, mixte)")#on pose la question pour savoir son type de peau 
        else:
            print("SkincareBot:", bot.get_response(user_input))  
            
    except (KeyboardInterrupt, EOFError): # Si l’utilisateur fait Ctrl+C ou ferme le terminal, on affiche un message d’au revoir et on sort de la boucle principale.
        print("\nSkincareBot: À bientôt !")
        break
