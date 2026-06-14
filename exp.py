import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Configuration des profils de peau
SKIN_TYPES = {
    "grasse": {
        "routine soir": "1. Nettoyant gel\n2. Tonique\n3. Sérum niacinamide\n4. Crème légère",
        "routine matin": "1. Nettoyant doux\n2. Sérum matifiant\n3. Crème hydratante légère\n4. Écran solaire",
        "sérum": "Un bon sérum pour peau grasse doit contenir des ingrédients régulateurs de sébum comme la niacinamide,",
        "nettoyant": "un nettoyant gel moussant",
        "acné": "Utilisez un nettoyant purifiant, un sérum à l'acide salicylique et une crème légère non comédogène.",
        "tache brune": "Utilisez un sérum à la niacinamide ou à l'acide azélaïque pour atténuer les taches sans alourdir la peau.",
        "conseil": "Évitez les produits trop riches qui pourraient obstruer vos pores"
    },
    "sèche": {
        "routine soir": "1. Nettoyant crème\n2. Sérum hydratant\n3. Crème riche\n4. Huile visage",
        "routine matin": "1. Nettoyant doux\n2. Sérum hydratant\n3. Crème riche\n4. Écran solaire",
        "sérum": "Choisis un sérum hydratant et nourrissant qui renforce la barrière cutanée. contenant acide hyaluronique, céramides",
        "acné": "Optez pour un nettoyant doux non asséchant, un sérum à base de niacinamide ou acide azélaïque, et une crème hydratante nourrissante mais non comédogène.",
        "tache brune": "Privilégiez un sérum à la vitamine C stabilisée ou à la niacinamide, accompagné d’une crème riche pour renforcer la barrière cutanée et éviter les irritations.",
        "nettoyant": "un nettoyant sans rinçage",
        "conseil": "Privilégiez les textures riches en céramides"
    },
    "mixte": {
        "routine soir": "1. Nettoyant doux\n2. Sérum adapté\n3. Crème équilibrante",
        "routine matin": "1. Nettoyant doux\n2. Sérum zone T\n3. Crème légère\n4. Écran solaire",
        "sérum": "Opte pour un sérum équilibrant qui hydrate sans graisser et cible les zones à problèmes. contenant  niacinamide, acide hyaluronique, aloe vera.",
        "acné": "Nettoyez votre visage avec un produit doux, appliquez un sérum ciblé (niacinamide ou acide salicylique) sur la zone T, et utilisez une crème équilibrante sur l’ensemble du visage.",
        "tache brune": "Utilisez un sérum à base de niacinamide ou vitamine C le matin, en l’appliquant uniformément. Combinez-le à une crème équilibrante pour unifier le teint sans graisser.",
        "nettoyant": "un nettoyant pour peaux mixtes",
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
    elif "acné" in demande:
        return f"Conseil pour peau {skin_type}: {SKIN_TYPES[skin_type]['acné']}"
    elif "tache brune" in demande:
        return f"Conseil pour peau {skin_type}: {SKIN_TYPES[skin_type]['tache brune']}"
    return "Je ne comprends pas votre demande."

def main():
    # Charger les paires de formation depuis un fichier JSON
    with open('training_pairs.json', 'r', encoding='utf-8') as file:
        training_pairs = json.load(file)

    # Aplatir les paires pour le ListTrainer
    flat_training_pairs = [item for sublist in training_pairs for item in sublist]

    # Initialisation du chatbot
    bot = ChatBot("SkincareBot")
    trainer = ListTrainer(bot)

    # Entraînement avec les données importées
    trainer.train(flat_training_pairs)

    print("SkincareBot: Bonjour ! Je peux vous conseiller sur votre routine skincare.")

    current_skin_type = None
    pending_request = None

    while True:
        try:
            user_input = input("Vous: ").lower()

            if user_input in ["au revoir", "bye"]:
                print("SkincareBot: À bientôt !")
                break

            # Vérification du type de peau
            skin_type_detected = None
            for skin_type in SKIN_TYPES:
                if skin_type in user_input:
                    skin_type_detected = skin_type
                    current_skin_type = skin_type
                    print(f"SkincareBot: Merci, peau {skin_type} notée.")
                    if pending_request:
                        print(reponse_personnalisee(pending_request, current_skin_type))
                        pending_request = None
                    break

            if skin_type_detected:
                    continue
                
            # Vérifier si le type de peau est déjà connu
            if current_skin_type and any(word in user_input for word in ["routine", "nettoyant", "conseil","sérum","acné","tache brune"]):
                print(reponse_personnalisee(user_input, current_skin_type))
            elif any(word in user_input for word in ["routine", "nettoyant", "conseil","sérum","acné","tache brune"]):
                # Enregistrer la demande et poser la question sur le type de peau
                pending_request = user_input
                print("SkincareBot: Quel est votre type de peau ? (grasse, sèche, mixte)")
            else:
                # Utiliser la réponse du chatbot si rien n'est trouvé
                print("SkincareBot:", bot.get_response(user_input))

        except (KeyboardInterrupt, EOFError):
            print("\nSkincareBot: À bientôt !")
            break

if __name__ == "__main__":
    main()

