import openai
import tweepy
import time

# Clé API OpenAI 
openai.api_key = ''

# Fonction pour générer le texte du tweet en utilisant ChatGPT. Prompt à adapter ! 
def generate_tweet():
    prompt = "Par exemple : génère moi un tweet de 80 tokens max, qui parle de l'actualité. Parle sur un ton autain. Génère uniquement le tweet en question, pas de texte avant ni après. Utilise des hashtags liés au tweet et identifie @ des comptes connus. Si besoin utilise des smileys."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=80,
        temperature=0.7,
        stop=None
    )
    return response['choices'][0]['text'].strip()

# Vos clés api twitter
def main():
    client = tweepy.Client(consumer_key="",
                        consumer_secret="",
                        access_token="",
                        access_token_secret="")

    while True:
        tweet_text = generate_tweet()

        client.create_tweet(text=tweet_text)

        print("Tweet publié avec succès:", tweet_text)

        time.sleep(600)

if __name__ == "__main__":
    main()