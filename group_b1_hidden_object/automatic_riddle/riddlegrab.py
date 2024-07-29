import requests
import wget
import openai
import certifi
import os


api_key = "your key"


def generate_riddles_response(api_key, artwork_info, object_id):
    """Generate riddles response for a specific artwork"""
    openai.api_key = api_key

    title, painter, context = artwork_info[object_id][2:5]

    # Example interaction with ChatGPT for riddle creation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative riddle master."},
            {"role": "user", "content": f"Create 5 riddles related to the painting {title} by {painter}. Each riddle should correspond to an object in the painting: {context}."},
            {"role": "assistant", "content": "Sure, let's get creative with the riddles!"}
        ]
    )

    response_message = response['choices'][0]['message']['content']
    return response_message
