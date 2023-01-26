# discordchatbot
# Anywhere in this script that items are inside {{}}, you must delete the {{}} for the script to work.

import ssl
import discord
import random
import os
from neuralintents import GenericAssistant
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2


chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

print('Bot Running...')

client = discord.Client()

TOKEN = ('{{YOUR_DISCORD_BOT_TOKEN_HERE}}')


class compvis():
    '''
    This is the portion of the script that implements the Clarifai API for the computer vision functionality. 
    To learn more or create your own account to make this work please visit https://portal.clarifai.com/login
    '''
    def vision(image_name):
        USER_ID = '{{YOUR_CLARIFAI_USER_ID_HERE}}'
        # Your PAT (Personal Access Token) can be found in the portal under Authentification
        API = '{{YOUR_CLARIFAI_API_HERE}}'
        APP_ID = '{{YOUR_CLARIFAI_APP_NAME_HERE}}'
        # Change these to whatever model and image URL you want to use
        MODEL_ID = 'general-image-recognition'
        # This is optional. You can specify a model version or the empty string for the default
        MODEL_VERSION_ID = ''

        channel = ClarifaiChannel.get_grpc_channel()
        stub = service_pb2_grpc.V2Stub(channel)

        metadata = (('authorization', 'Key ' + API),)

        request = service_pb2.PostModelOutputsRequest(
            model_id='aaa03c23b3724a16a56b629203edc62c',
            inputs=[
                resources_pb2.Input(data=resources_pb2.Data(
                    image=resources_pb2.Image(url=f'{image_name}')))
            ])
        response = stub.PostModelOutputs(request, metadata=metadata)

        if response.status.code != status_code_pb2.SUCCESS:
            raise Exception("Request failed, status code: " +
                            str(response.status.code))

        response_list = []
        for concept in response.outputs[0].data.concepts:
            response_list.append('%12s: %.2f' % (concept.name, concept.value))

        return response_list


@client.event
async def on_message(message):
    #
    coin = ['heads', 'tails']

    if message.author == client.user:
        return
    if message.content.startswith('/{{YOUR_BOT_NAME_HERE}}'):
        response = chatbot.request(message.content[7:])
        await message.channel.send(response)

    if message.content.startswith('/help'):
        await message.channel.send("I am just chatting for now but more coming soon! Real me is building out my features!")

    if message.content.startswith('/commands'):
        await message.channel.send("/{{YOUR_BOT_NAME_HERE}} - chat with me \n /help - see my feature set \n /commands - get a list of active commands to use \n /vision - paste a picture to have analyzed \n /flip - Flip a coin \n /math - Follow prompts for math")

    if message.content.startswith('/flip'):
        await message.channel.send(random.choice(coin))

    if message.content.startswith('/vision'):
        attachment = message.attachments[0]
        url = attachment.url
        print(attachment.url)
        await message.channel.send(compvis.vision(url))

    if message.content.startswith('/math'):
        def check(m):
            return len(m.content) >= 1

        await message.channel.send("Number 1: ")
        number_1 = await client.wait_for("message", check=check)
        await message.channel.send("Operator: ")
        operator = await client.wait_for("message", check=check)
        await message.channel.send("number 2: ")
        number_2 = await client.wait_for("message", check=check)
        try:
            number_1 = float(number_1.content)
            operator = operator.content
            number_2 = float(number_2.content)
        except:
            await message.channel.send("invalid input")
            return
        output = None
        if operator == "+":
            output = number_1 + number_2
        elif operator == "-":
            output = number_1 - number_2
        elif operator == "/":
            output = number_1 / number_2
        elif operator == "*":
            output = number_1 * number_2
        else:
            await message.channel.send("invalid input")
            return
        await message.channel.send("Answer: " + str(output))


client.run(TOKEN)
