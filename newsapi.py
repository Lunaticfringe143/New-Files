import requests
import tkinter as tk



def getNews():
	api_key = ""
	url = ""
    request = requests.get(url).json()

	articles = news["articles"]

	my_articles = []
	my_news = ""

	for article in articles:
		my_articles.append[article["title"]]

	for i in range(10):
		my_news = my_news + str(i) + my_articles[i] + "\n"
	label.config(text = my_news)

canvas = tk.TK()

canvas.geometry("900x600")
canvas.title("News APP")

button = tk.Button(canvas, font = 24, text = "Reload", command = getNews)
button.pack(pady = 20)

label = tk.Label(canvas, font = 18, justify = "left")
Label.pack(pady = 20)


getNews()

canvas.mainloop()
