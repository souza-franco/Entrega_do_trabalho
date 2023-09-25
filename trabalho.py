SsDW2023_api_url = 'https://sdw-2023-prd.up.railway.app'

import pandas as pd
df = pd.read_csv('SsDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

import requests
import json

def get_user(id):
  response = requests.get(f'{SsDW2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

user = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(user, indent=2))

openai_api_key = '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'


import openai

openai.api_key = openai_api_key

def generate_ai_news(user):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", 
       "content": "Voçe é um especialista em marketing bancario."
      },
      {"role": "user", 
       "content": f"Crie uma mensagem para {user['name']} sobre a importancia dos investimentos (máximo de 100 caracteres)"
      }
    ]
  )
  return completion.choices[0].message.content.stripe('\"')

for user in user:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
         "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
         "description": news
    })