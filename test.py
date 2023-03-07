import openai
import os
import requests
from requests.structures import CaseInsensitiveDict
import json

def get_text(prompt):
    response = openai.Completion.create(
        model="text-davinci-001",
        prompt=prompt,
        temperature=0.4,
        max_tokens=128,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if response.choices and response.choices[0].text:
        answer = response.choices[0].text.strip()
    else:
        answer = "No valid response received from OpenAI API"
        
    return answer


def get_dalle_image(prompt):
    # Set up the API endpoint and headers
    url = "https://api.openai.com/v1/images/generations"
    headers = {"Content-Type": "application/json",
               "Authorization": "Bearer {}".format(openai.api_key)}

    # Set up the prompt
    data = {
        "model": "image-alpha-001",
        "prompt": prompt,
        "num_images": 1,
        "size": "512x512",
        "response_format": "url"
    }

    # Send the request to the API
    response = requests.post(url, headers=headers, json=data)

    # Parse the response and extract the URL of the image
    response_data = response.json()['data'][0]
    image_url = response_data['url']

    # Return the image URL
    return image_url

#Make sure to update the get_dalle_image function in your code with this new version and try running the code again.




# Define the prompt separately as a string variable
prompt = ""

api_key = "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"
openai.api_key = api_key

try:
    text_response = get_text("give me 3 examples of names for characters for an adventure with a 10 word description")

    # Ask the user to enter their question
    print("You now have to choose a character, here are some examples: \n", text_response)
    prompt = input("Enter your Type of character: ")

    image_url = get_dalle_image(prompt)
    text_response = get_text("Present an adventure for {}".format(prompt) )


    # Download the image and display it
    img_data = requests.get(image_url).content
    with open('image.png', 'wb') as handler:
        handler.write(img_data)

    # Print the answer
    print(text_response)

except Exception as e:
    # Handle any exceptions that occur during the API request
    print("Error: {}".format(str(e)))

#Funtion that generates a Dall-e request
