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


print(get_response("Fait moi un qcm sur les HashMap en java en suivant le modèle suivant :  Question | Réponse 1 | Réponse 2 | Réponse 3 ?"))