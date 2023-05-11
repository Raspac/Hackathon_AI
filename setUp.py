import os
import openai



openai.api_key = "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"
openai.Model.list()


def get_response(question):
    prompt = f"Q: {question}\nA:"
    completions = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7
    )
    message = completions.choices[0].text.strip()
    return message

question1 = "Fait moi un qcm en 10 questions sur les HashMap en java en suivant le modèle suivant :  Question | Réponse 1 | Réponse 2 | Réponse 3 ?"

retQuestion1 = get_response(question1)

print(retQuestion1)

repQuestion1 = "Quelle est la réponse à la question suivant :" + retQuestion1

repQuestion1 = get_response(repQuestion1)

print(repQuestion1)