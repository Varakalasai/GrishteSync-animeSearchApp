# Created with GrishteSync
# https://suryasticsai.github.io/GrishteSync
# Suryasticsai | suryasticsai@gmail.com
import gradio as gr
import requests

def search_anime(anime_name):
    url = f'https://api.jikan.moe/v4/anime?q={anime_name}'
    response = requests.get(url)
    data = response.json()
    anime_list = [anime['title'] for anime in data['data']]
    return anime_list

demo = gr.Interface(
    fn=search_anime,
    inputs=[gr.Textbox(label='Anime Name')],
    outputs=[gr.JSON(label='Anime List')],
    title='Anime Search App',
    description='Search for anime and get a list of results',
    article='Made with GrishteSync | Suryasticsai | suryasticsai@gmail.com'
)
demo.launch(server_name='0.0.0.0', server_port=7860)