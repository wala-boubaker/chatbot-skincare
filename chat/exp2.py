import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Configuration des profils de peau
SKIN_TYPES = {
    "grasse": {
        "routine matin": "1. Nettoyant gel\n2. Tonique\n3. Crème matifiante\n4. Écran solaire",
        "routine soir": "1. Nettoyant gel\n2. Tonique\n3. Sérum niacinamide\n4. Crème légère",
        "nettoyant": "un nettoyant gel moussant",
        "conseil": "Évitez les produits trop riches qui pourraient obstruer vos pores"
    },
    "sèche": {
        "routine matin": "1. Nettoyant doux\n2. Sérum hydratant\n3. Crème nourrissante\n4. Écran solaire",
        "routine soir": "1. Nettoyant crème\n2. Sérum hydratant\n3. Crème riche\n4. Huile visage",
        "nettoyant": "un nettoyant sans rinçage",
        "conseil": "Privilégiez les textures riches en céramides"
    },
    "mixte": {
        "routine matin": "1. Nettoyant doux\n2. Sérum léger\n3. Crème équilibrante\n4. Écran solaire",
        "routine soir": "1. Nettoyant doux\n2. Sérum adapté\n3. Crème équilibrante",
        "nettoyant": "un nettoyant pour peaux mixtes",
        "conseil": "Adaptez les soins aux différentes zones du visage"
    }
}

def reponse_personnalisee(demande, skin_type):
    """Retourne une réponse adaptée au type de peau et aux questions spécifiques"""
    demande = demande.lower()
    
    # Vérifie si la demande est une routine matin ou soir
    if "routine" in demande:
        if "matin" in demande:
            return f"Routine matin pour peau {skin_type}:\n{SKIN_TYPES[skin_type]['routine matin']}"
        elif "soir" in demande:
            return f"Routine soir pour peau {skin_type}:\n{SKIN_TYPES[skin_type]['routine soir']}"
    
    # Cherche une question spécifique dans le fichier JSON
    for question in SKIN_CARE_QUESTIONS["questions"][skin_type]:
        if question["question"].lower() in demande:
            return f"Pour peau {skin_type}, {question['reponse']}"
    
    # Réponse par défaut
    return "Je ne comprends pas votre demande."



def main():
    # Load training pairs from JSON file
    with open('training_pairs.json', 'r', encoding='utf-8') as file:
        training_pairs = json.load(file)

    # Flatten the training pairs into a format suitable for ListTrainer
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

            # Détection du type de peau
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

            if current_skin_type and any(word in user_input for word in ["routine", "nettoyant", "conseil", "matin", "soir"]):

                print(reponse_personnalisee(user_input, current_skin_type))
            elif any(word in user_input for word in ["routine", "nettoyant", "conseil", "matin", "soir"]):
                pending_request = user_input
                print("SkincareBot: Quel est votre type de peau ? (grasse, sèche, mixte)")
            else:
                print("SkincareBot:", bot.get_response(user_input))

        except (KeyboardInterrupt, EOFError):
            print("\nSkincareBot: À bientôt !")
            break


if __name__ == "__main__":
    main()
