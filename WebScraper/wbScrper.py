import tkinter as tk
from tkinter import Button, Text
import requests
from bs4 import BeautifulSoup

#create the scraping script using BeautifulSoup
def scrape_quotes_and_save():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    #Extract Quotes and display them in the text box
    quotes = soup.select(".quote span.text")
    for quote in quotes:
        result_text.insert(tk.END, quote.get_text() + "\n")

    with open("scraped_Quotes.txt", "a") as file:
        for quote in quotes:
            file.write(quote.get_text() + "\n")

#create main application window
app = tk.Tk()
app.title("Web Scrapper")

#create UI elements
label = tk.Label(app, text = "Click the button to scrap quotes from a website and save them to a text file")
label.pack(pady=10)
scrape_button = tk.Button(app, text="Scrape Quotes and save", command=scrape_quotes_and_save)
scrape_button.pack()
result_text = Text(app, height = 10, width=50)
result_text.pack()

#start the GUI event loop
app.mainloop()






