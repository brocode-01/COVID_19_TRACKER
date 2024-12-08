import requests
import bs4

import tkinter as tk


def get_html_data(url):
    data = requests.get(url)
    return data


def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div",class_="content-inner").findAll("div",id="maincounter-wrap")
    all_data = ""

    for block in info_div:
        text=block.find("h1", class_=None).get_text()

        count=block.find("span",class_=None).get_text()

        all_data = all_data + text + " " + count + "\n"

    return all_data

def get_country_data():
    name = textfield.get()
    url = "https://www.worldometers.info/coronavirus/country/"+name

    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data = ""

    for i in range(3):
        text = info_div[i].find("h1", class_=None).get_text()

        count = info_div[i].find("span", class_=None).get_text()

        all_data = all_data + text + " " + count + "\n"

    mainlabel['text'] = all_data

def reload():
    new_data = get_covid_data()
    mainlabel['text'] = new_data

# GUI

get_covid_data()

root = tk.Tk()
root.geometry("1080x700")
root.title("Covid Tracker")
f = ("Times New Roman NN",30,"bold" )

banner = tk.PhotoImage(file="covid 19.png")
bannerlabel = tk.Label(root, image=banner)
bannerlabel.pack()


textfield = tk.Entry(root, width=30 , font=80 , bg="white")
textfield.pack()


mainlabel = tk.Label(root, text=get_covid_data(), font=f, fg="#191970")
mainlabel.pack()

gbtn = tk.Button(root, text="Get Data", relief='solid',font=f ,command=get_country_data , bg="#CAFF70", fg="black")
gbtn.pack()

rbtn = tk.Button(root, text="Reload", font=f, relief='solid', command=reload , bg="#FFA07A")
rbtn.pack()

root.mainloop()
