import twitchio

# Créez un client Twitch
client = twitchio.Client()

# Credentials Twitch
client.set_client_id("")
client.set_oauth_token("")

# Définissez les messages qui seront envoyés au début et à la fin du stream
start_message = "Bienvenue à mon stream !"
end_message = "Merci d'avoir regardé mon stream !"

# Définissez les commandes personnalisées
commands = {
    "!snk": "",
    "!game": "Je joue à {game}",
    "!stream_title": "Mon stream s'appelle {title}",
    "!timeout": "Temporisation de l'utilisateur {user} pour {duration} secondes",
    "!ban": "Bannissement de l'utilisateur {user}",
    "!bingo": "Lancement du jeu bingo",
    "!giveaway": "Lancement d'une commande giveaway",
    "!help": "Affiche une liste de toutes les commandes disponibles"
}

# Connectez-vous à Twitch
client.connect()

# Attendez que le stream commence
@client.event
async def on_stream_start():
    print("Le stream a commencé !")
    await client.send_message(start_message)

# Attendez que le stream se termine
@client.event
async def on_stream_end():
    print("Fin du stream, merci d'être passé !")
    await client.send_message(end_message)

# Gestion des commandes personnalisées
@client.event
async def on_message(message):
    command = message.content.split(" ")[0]
    if command in commands:
        await client.send_message(commands[command])

# Timeout utilisateur
@client.event
async def on_timeout(user, duration):
    print("L'utilisateur {} a été timeout pour une durée de {} secondes.".format(user, duration))
    await client.send_message("L'utilisateur {} a été timeout pour une durée de {} secondes.".format(user, duration))

# Ban utilisateur
@client.event
async def on_ban(user):
    print("L'utilisateur {} a été banni.".format(user))
    await client.send_message("L'utilisateur {} a été banni.".format(user))

# Affiche une liste de toutes les commandes disponibles
@client.event
async def on_help():
    print("Voici une liste de toutes les commandes disponibles :")
    for command in commands:
        print("* {}".format(command))
    await client.send_message("Voici une liste de toutes les commandes disponibles :")
    for command in commands:
        await client.send_message("* {}".format(command))

# Change le nom du jeu en cours
@client.event
async def on_setgame(game):
    print("Le jeu en cours a été modifié sur {}".format(game))
    await client.change_game(game)

# Change le nom du stream en cours
@client.event
async def on_settitle(title):
    print("Le titre du stream a été modifié sur {}".format(title))
    await client.change_title(title)

# Continuer de lire tous les messages
client.run()