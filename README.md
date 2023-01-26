# VisionBot
This is a Discord Bot template that implements the Clarifai Computer Vision API out of the box. 

This bot is built upon the Neuralintents library, the Discord API, and the Clarifai API.

## Setup

To configure this bot, you will need to have a few thing ready beforehand. 
 First, you need to have a bot setup for Discord in the Discord Developer Portal: https://discordpy.readthedocs.io/en/stable/discord.html
 Next, you need to have an application setup on the Clarifai Portal: https://portal.clarifai.com/login & https://www.clarifai.com/
 
 Once these accounts are created and the bot is added to your server, you will need to customize the two files in this repository a bit.
 
 Find all instances of {{}} within the VisionBot.py script and replace these with your information. PLEASE NOTE: The way this is setup right now does not abstract any of your account data and anyone with access to your script will have access to your bot token, your API token, and your username for Clarifai. There are plenty of guides online to help you change this if you would like to do so.
 
 You can also customize the intents.json file as well. Simply copy one of the tag sets and change the information inside to match what you would like your bot to be able to talk about. 
 
 Once this has been customized you are ready to deploy your bot! Simply run this script from your computer and let the chatting and visioning begin!
 
 Feel free to use this template and customize to your liking!

## Documentation
Neuralintents: https://pypi.org/project/neuralintents/
Discord API: https://discordpy.readthedocs.io/en/stable/api.html
Clarifai API: https://portal.clarifai.com/login & https://www.clarifai.com/


#### Versioning Notes
This setup uses specific versions of the Discord API (1.7.3), Tensorflow (2.10.0), and protobuf (3.20.*).


#### Packages Used That May require installation (see above for version notes)
discord  
neuralintents  
clarifai-grpc  
