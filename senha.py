API_KEY="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"

# import openai

# openai.api_key = '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'

# response = openai.Completion.create(
#   engine="text-davinci-004",  # Nome do novo modelo
#   model="gpt-3.5-turbo",
#   prompt="Qual é a distancia de Brasil ao Chile",
#   max_tokens=60
# )

# print(response.choices[0].text.strip())


# from openai import OpenAI
# import os

# # client = OpenAI(
# #   api_key='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',  # this is also the default, it can be omitted
# #   #api_key=os.environ['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'],  # this is also the default, it can be omitted  
# # )

# client = OpenAI(
#   api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
# )

# client = OpenAI()

# completion = client.completions.create(model='curie')
# print(completion.choices[0].text)
# print(dict(completion).get('usage'))
# print(completion.model_dump_json(indent=2))
