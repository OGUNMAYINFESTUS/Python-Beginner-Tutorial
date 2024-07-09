# Here's the equivalent code in Python:

import feedparser
import tkinter as tk

def fetch_rss(rss_url):
    feed = feedparser.parse(rss_url)
    return feed.entries

def display_feed(entries):
    feed_text = ""
    for entry in entries:
        feed_text += f"<h2>{entry.title}</h2><p>{entry.description}</p>"
    return feed_text

def display_error(error):
    return f"<p>Error: {error}</p>"

def fetch_button_clicked():
    rss_url = rss_url_input.get()
    if not rss_url:
        error_label.config(text="Please enter a valid RSS feed URL")
        return
    try:
        entries = fetch_rss(rss_url)
        feed_text = display_feed(entries)
        feed_label.config(text=feed_text)
    except Exception as e:
        error_label.config(text=display_error(str(e)))

root = tk.Tk() # Corrected line
root.title("RSS Feed Reader")

rss_url_input = tk.Entry(root, width=50)
rss_url_input.pack()

fetch_button = tk.Button(root, text="Fetch Feed", command=fetch_button_clicked)
fetch_button.pack()

feed_label = tk.Label(root, text="", wraplength=400)
feed_label.pack()

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

root.mainloop()

# This code uses the feedparser library to parse the RSS feed and tkinter for the GUI. Note that this code assumes you have the feedparser library installed. If not, you can install it using pip install feedparser.
