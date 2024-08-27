# **CalendarBot**

**CalendarBot** is a Discord bot that integrates with Google Calendar to provide event reminders and calendar information directly within your Discord server. It is designed to help manage and keep track of calendar events, send reminders, and provide quick access to daily, tomorrow's, and weekly event schedules.

## Features

- **Event Reminders**: Sends reminders for upcoming calendar events 30 minutes in advance.
- **Daily and Tomorrow’s Schedule**: Provides a summary of events for today or tomorrow.
- **Weekly Planning**: Sends a summary of the upcoming week's events every Sunday evening.
- **Interactive Commands**: Use slash commands to query and get calendar information.
- **Fun Facts and GIFs**: Includes fun facts and GIFs for certain events, adding a touch of personality to the reminders.

## Prerequisites

- Python 3.7 or higher
- A Discord bot token
- Google Calendar API credentials

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Cyber-Thibaut/CalendarBot.git
   cd CalendarBot
   ```

2. **Create and Activate a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Google Calendar API:**

   - Create a project in the [Google Developers Console](https://console.developers.google.com/).
   - Enable the Google Calendar API for your project.
   - Download the `credentials.json` file and place it in the root directory of the project.

5. **Create a `token.json` File:**

   - The `token.json` file will be generated automatically after the first run. Ensure it is in the same directory as the script.

6. **Set Up Your Environment:**

   - Replace placeholders in the script with your own Discord token and channel IDs where required.
   - Update the `calendar_ids` dictionary with your Google Calendar IDs.
   - Set your Tenor API key for GIF retrieval.

## Configuration

1. **Edit `bot.run('ton token discord')`:**
   
   Replace `'ton token discord'` with your actual Discord bot token.

2. **Edit `calendar_ids` Dictionary:**
   
   Replace `'ID du calendrier'` with your actual Google Calendar IDs.

3. **Edit `TENOR_API_KEY`:**
   
   Replace `'ta clé API tenor'` with your Tenor API key for GIF retrieval.

## Usage

- **Start the Bot:**

  Run the bot using the following command:

  ```bash
  python bot.py
  ```

- **Commands:**

  - `/planning` - Displays today’s calendar events.
  - `/calendrier_demain` - Displays tomorrow’s calendar events.
  - `/planning_semaine` - Displays the week’s calendar events.

## Troubleshooting

- **Google Credentials Issue:**

  Ensure that `credentials.json` is correctly placed and the Google Calendar API is enabled.

- **Bot Not Responding:**

  Verify that your bot token and channel IDs are correctly set.

- **GIF Retrieval:**

  Ensure that your Tenor API key is valid and the URL in `get_random_car_gif` is correct.

## Contributing

Feel free to submit issues, feature requests, or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Cyber-Thibaut/CalendarBot/LICENSE.md) file for details.

---

For more information and to report issues, visit the [GitHub repository]([https://github.com/yourusername/CalendarBot](https://github.com/Cyber-Thibaut/CalendarBot)). 

Happy calendaring! 🗓️✨

---

# **CalendarBot**

**CalendarBot** est un bot Discord qui s'intègre à Google Calendar pour fournir des rappels d'événements et des informations de calendrier directement dans votre serveur Discord. Il est conçu pour aider à gérer et à suivre les événements du calendrier, à envoyer des rappels et à fournir un accès rapide aux horaires des événements du jour, du lendemain et de la semaine.

## Caractéristiques

- **Rappels d'événements** : Envoie des rappels pour les événements à venir 30 minutes à l'avance.
- Calendrier quotidien et de demain** : Fournit un résumé des événements d'aujourd'hui et de demain.
- Planification hebdomadaire** : Envoie un résumé des événements de la semaine à venir tous les dimanches soirs.
- Commandes interactives** : Utilisez les commandes slash pour interroger et obtenir des informations sur le calendrier.
- Faits amusants et GIFs** : Inclut des faits amusants et des GIF pour certains événements, ajoutant une touche de personnalité aux rappels.

## Conditions préalables

- Python 3.7 ou supérieur
- Un jeton de bot Discord
- Des informations d'identification pour l'API Google Calendar

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/CalendarBot.git
   cd CalendarBot
   ```

2. **Créer et activer un environnement virtuel (optionnel mais recommandé):**

   ```bash
   python -m venv venv
   source venv/bin/activate # Sous Windows, utilisez `venv\Scripts\activate`
   ```

3. **Installer les dépendances:**

   ``Bash
   pip install -r requirements.txt
   ```

4. **Configurer l'API Google Calendar:**

   - Créez un projet dans la [Google Developers Console] (https://console.developers.google.com/).
   - Créez un projet dans la [Google Developers Console] (https://console.developers.google.com/).
   - Activez l'API Google Calendar pour votre projet.
   - Téléchargez le fichier `credentials.json` et placez-le dans le répertoire racine du projet.

5. **Créer un fichier `token.json`:**

   - Le fichier `token.json` sera généré automatiquement après la première exécution. Assurez-vous qu'il se trouve dans le même répertoire que le script.

6. **Configurer votre environnement:**

   - Remplacez les espaces réservés dans le script par votre propre jeton Discord et vos identifiants de canaux si nécessaire.
   - Mettez à jour le dictionnaire `calendar_ids` avec vos identifiants Google Calendar.
   - Définissez votre clé API Tenor pour la récupération des GIF.

## Configuration

1. **Éditez `bot.run('ton token discord')`:**
   
   Remplacez `'ton token discord'` par votre token Discord.

2. **Editer le dictionnaire `calendar_ids`:**
   
   Remplacez `'ID du calendrier'` par vos identifiants Google Calendar actuels.

3. **Editer `TENOR_API_KEY`:**
   
   Remplacez `'ta clé API tenor'` par votre clé API Tenor pour la récupération des GIF.

## Utilisation

- **Démarrer le bot:**

  Lancez le bot en utilisant la commande suivante :

  ``bash
  python bot.py
  ```

- **Commandes:**

  - `/planning` - Affiche les événements du calendrier d'aujourd'hui.
  - `/calendrier_demain` - Affiche les événements du calendrier de demain.
  - `/planning_semaine` - Affiche les événements du calendrier de la semaine.

## Résolution des problèmes

- **Google Credentials Issue:**

  Assurez-vous que `credentials.json` est correctement placé et que l'API Google Calendar est activée.
  
- **Bot Not Responding:**

  Vérifiez que le jeton du robot et les identifiants des canaux sont correctement définis.

- **GIF Retrieval:**

  Vérifiez que votre clé API Tenor est valide et que l'URL dans `get_random_car_gif` est correcte.

## Contribuer

N'hésitez pas à soumettre des problèmes, des demandes de fonctionnalités ou des demandes d'extraction. Les contributions sont les bienvenues !

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](https://github.com/Cyber-Thibaut/CalendarBot/LICENSE.md) pour plus de détails.

---

Pour plus d'informations et pour signaler des problèmes, visitez le [dépôt GitHub]([https://github.com/yourusername/CalendarBot](https://github.com/Cyber-Thibaut/CalendarBot)). 

Bonne journée ! 🗓️✨

---




