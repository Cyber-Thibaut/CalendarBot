import discord
from discord import Option
from discord.ext import tasks, commands
import google.auth
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime, timedelta, timezone, time
import os
from random import choice
import asyncio
import pytz
import requests

version = "1.0.1"

# Define the bot and load token from environment variables
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Google Calendar API scopes
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Timezone for France
timezone_fr = pytz.timezone('Europe/Paris')


def get_google_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


calendar_ids = {
    'nom': 'ID du calendrier',
}

# Dictionary to keep track of reminders already sent
sent_reminders = {}
sent_weekly = False


@bot.event
async def on_message(message):
    if message.content.lower() == "quoi":
        await message.channel.send("feur")

# démarrage
funFact = [
    "vos fun facts",
]

# confirmation bot Allumé


@bot.event
async def on_ready():
    print(f"Le bot {bot.user.name} est désormais en Ligne")
    embed = discord.Embed(
        title="Statut du Bot", description="Je suis désormais en Ligne ! ✅", color=0x10ef00)
    embed.add_field(
        name="Ma version actuelle est la version " + version, value="")
    embed.set_footer(text=choice(funFact))
    await bot.get_channel(int("channel ID")).send(embed=embed)
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="la version " + version))


@tasks.loop(minutes=1)
async def check_events():
    now = datetime.now(timezone_fr)
    for nom_calendrier, calendar_id in calendar_ids.items():
        try:
            creds = get_google_credentials()
            service = build('calendar', 'v3', credentials=creds)
            events_result = service.events().list(calendarId=calendar_id, timeMin=now.isoformat(),
                                                  maxResults=10, singleEvents=True,
                                                  orderBy='startTime').execute()
            events = events_result.get('items', [])
            for event in events:
                start = event['start'].get(
                    'dateTime', event['start'].get('date'))
                start_dt = datetime.fromisoformat(
                    start).astimezone(timezone_fr)
                fin = event['end'].get('dateTime', event['end'].get('date'))
                fin_dt = datetime.fromisoformat(fin).astimezone(timezone_fr)
                reminder_time = start_dt - timedelta(minutes=30)

                event_id = event['id']
                if reminder_time <= now < start_dt:
                    if event_id not in sent_reminders:
                        # Replace with your channel ID
                        channel = bot.get_channel("channel ID")
                        if nom_calendrier == 'Conduite':
                            phrase = choice(phrases_droles)
                            await channel.send(phrase)

                            gif_url = get_random_car_gif()
                            if gif_url:
                                await channel.send(gif_url)
                            else:
                                await channel.send("Je n'ai pas trouvé de GIF de voiture, mais c'est l'heure de conduire !")
                        else:
                            await channel.send(f":bell: Rappel : L'événement '{event['summary']}' de l'agenda de **{nom_calendrier}** commence dans 30 minutes à {event.get('location', '*Oups aucun lieu trouvé :sweat_smile:*')}, il prendra fin à {fin_dt.strftime('%H:%M')}.")
                        sent_reminders[event_id] = True
                elif now >= start_dt:
                    if event_id in sent_reminders:
                        del sent_reminders[event_id]

            # Check if it's Sunday at 20:00 for weekly calendar
            if now.weekday() == 6 and now.hour == 20 and now.minute == 0 and sent_weekly == False:
                sent_weekly = True
                await send_weekly_calendar()
            if now.weekday() == 6 and now.hour == 20 and now.minute == 10:
                sent_weekly = False
        except Exception as e:
            print(f"An error occurred: {e}")


@bot.slash_command(name="planning", description="Afficher le calendrier d'aujourd'hui")
async def planing(ctx, nom_calendrier: Option(str, "Nom du calendrier", choices=['les noms de vos calendriers'])):
    await process_calendar(ctx, nom_calendrier)


async def process_calendar(ctx, nom_calendrier: str):
    if nom_calendrier not in calendar_ids:
        await ctx.send(f'Calendrier {nom_calendrier} non trouvé.')
        return

    creds = get_google_credentials()
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.now(timezone_fr)
    end_of_day = datetime.combine(
        now.date(), time.max, tzinfo=timezone_fr).isoformat()
    events_result = service.events().list(calendarId=calendar_ids[nom_calendrier], timeMin=now.isoformat(), timeMax=end_of_day,
                                          singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        await ctx.send(f"Pas d'événements aujourd'hui pour l'agenda de {nom_calendrier}.")
    else:
        embed = discord.Embed(title=f"Calendrier d'aujourd'hui ({
                              nom_calendrier})", color=discord.Color.blue())
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            start_dt = datetime.fromisoformat(start).astimezone(timezone_fr)
            fin = event['end'].get('dateTime', event['end'].get('date'))
            fin_dt = datetime.fromisoformat(fin).astimezone(timezone_fr)
            embed.add_field(name=event['summary'], value=f"Début : {start_dt.strftime('%H:%M:%S')} Fin : {fin_dt.strftime(
                '%H:%M')} Lieu : {event.get('location', '*Oups aucun lieu trouvé :sweat_smile:*')}", inline=False)
        await ctx.send(embed=embed)
        await ctx.respond('Calendrier envoyé ✅', ephemeral=True)


@bot.slash_command(name="calendrier_demain", description="Afficher le calendrier de demain")
async def calendrier_demain(ctx, nom_calendrier: Option(str, "Nom du calendrier", choices=['les noms de vos calendriers'])):
    await process_calendrier_demain(ctx, nom_calendrier)
    await ctx.respond('Calendrier envoyé ✅', ephemeral=True)


async def process_calendrier_demain(ctx, nom_calendrier: str):
    if nom_calendrier not in calendar_ids:
        await ctx.send(f'Calendrier {nom_calendrier} non trouvé.')
        return

    creds = get_google_credentials()
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.now(timezone_fr)
    tomorrow_start = datetime.combine(
        now.date() + timedelta(days=1), time.min, tzinfo=timezone_fr).isoformat()
    tomorrow_end = datetime.combine(
        now.date() + timedelta(days=1), time.max, tzinfo=timezone_fr).isoformat()
    events_result = service.events().list(calendarId=calendar_ids[nom_calendrier], timeMin=tomorrow_start, timeMax=tomorrow_end,
                                          singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        await ctx.send(f"Pas d'événements pour demain pour l'agenda de {nom_calendrier}.")
    else:
        embed = discord.Embed(title=f"Calendrier de demain ({
                              nom_calendrier})", color=discord.Color.blue())
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            start_dt = datetime.fromisoformat(start).astimezone(timezone_fr)
            fin = event['end'].get('dateTime', event['end'].get('date'))
            fin_dt = datetime.fromisoformat(fin).astimezone(timezone_fr)
            embed.add_field(name=event['summary'], value=f"Début : {start_dt.strftime('%H:%M:%S')} Fin : {fin_dt.strftime(
                '%H:%M')} Lieu : {event.get('location', '*Oups aucun lieu trouvé :sweat_smile:*')}", inline=False)
        await ctx.send(embed=embed)


async def send_weekly_calendar():
    for nom_calendrier in calendar_ids:
        if nom_calendrier == 'Conduite':
            continue
        # Replace with your channel ID
        channel = bot.get_channel("channel ID")
        await process_planning_semaine(channel, nom_calendrier)


@bot.slash_command(name="planning_semaine", description="Afficher le planning de la semaine")
async def planning_semaine(ctx, nom_calendrier: Option(str, "Nom du calendrier", choices=['les noms de vos calendriers'])):
    await process_planning_semaine(ctx, nom_calendrier)
    await ctx.respond('Calendrier envoyé ✅', ephemeral=True)


async def process_planning_semaine(ctx, nom_calendrier: str):
    # Check if calendar exists
    if nom_calendrier not in calendar_ids:
        await ctx.send(f'Calendrier {nom_calendrier} non trouvé.')
        return

    creds = get_google_credentials()
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.now(timezone_fr)
    fin_semaine = (now + timedelta(days=7)).isoformat()
    resultats_evenements = service.events().list(calendarId=calendar_ids[nom_calendrier], timeMin=now.isoformat(), timeMax=fin_semaine,
                                                 singleEvents=True, orderBy='startTime').execute()
    evenements = resultats_evenements.get('items', [])
    if not evenements:
        await ctx.send(f"Pas d'événements prévus pour cette semaine pour l'agenda de {nom_calendrier}.")
    else:
        embed = discord.Embed(title=f"Planning de la semaine ({
                              nom_calendrier})", color=discord.Color.blue())
        for evenement in evenements:
            debut = evenement['start'].get(
                'dateTime', evenement['start'].get('date'))
            debut_dt = datetime.fromisoformat(debut).astimezone(timezone_fr)
            fin = evenement['end'].get(
                'dateTime', evenement['end'].get('date'))
            fin_dt = datetime.fromisoformat(fin).astimezone(timezone_fr)
            embed.add_field(name=evenement['summary'], value=f"Début : {debut_dt.strftime('%d-%m %H:%M')} Fin : {fin_dt.strftime(
                '%H:%M')} Lieu : {evenement.get('location', '*Oups aucun lieu trouvé :sweat_smile:*')}", inline=False)
        await ctx.send(embed=embed)

phrases_droles = [
  "Ajoutez vos phrases drôles ici",
]

TENOR_API_KEY = 'ta clé API tenor'


def get_random_car_gif():
    url = f"https://g.tenor.com/v2/search?q=car&key={TENOR_API_KEY}&limit=100"
    response = requests.get(url)
    if response.status_code == 200:
        gifs = response.json().get('results')
        if gifs:
            return choice(gifs).get('url')
    return None

check_events.start()
bot.run('ton token discord')
