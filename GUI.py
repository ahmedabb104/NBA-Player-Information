from tkinter import *
from PIL import ImageTk,Image
import requests
import json

def formatStats(data):
    try:
        firstName = data[0]['first_name']
        lastName = data[0]['last_name']
        fullName = str(firstName) + ' ' + str(lastName)
        heightFeet = data[0]['height_feet']
        heightInches = data[0]['height_inches']
        height = str(heightFeet) + "'" + str(heightInches)
        weight = data[0]['weight_pounds']
        position = data[0]['position']
        team = data[0]['team']['full_name']
        finalOutput = 'Full name: %s \nHeight: %s \nWeight: %s lbs \nPosition: %s \nTeam: %s' % (fullName, height, weight, position, team)
    except: 
        finalOutput = "There was a problem retrieving that information."
    
    return finalOutput

def getStats(name):
    url = "https://www.balldontlie.io/api/v1/players"
    params = {'search' : name}
    response = requests.get(url, params=params)
    rawStats = response.json()
    data = rawStats['data']
    label['text'] = formatStats(data)


root = Tk()
root.title('NBA Player Information')
root.geometry('800x600')

backgroundImage = PhotoImage(file='basketball.png')
backgroundLabel = Label(root, image=backgroundImage)
backgroundLabel.place(relwidth=1, relheight=1)

searchFrame = Frame(root, bg='#5bd7d7', bd=5)
searchFrame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(searchFrame, font=('Consolas',15))
entry.place(relwidth=0.65, relheight=1)

button = Button(searchFrame, text="Search", font=('Consolas', 15), command=lambda: getStats(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

outputFrame = Frame(root, bg='#5bd7d7', bd=5)
outputFrame.place(relx=0.5, rely=.25, relwidth=0.75, relheight=0.6, anchor='n')
# try:
#     api_request = requests.get("https://www.balldontlie.io/api/v1/players")
#     api = json.loads(api_request.content)
# except Exception as e:
#     api = "Error connecting to API."

label = Label(outputFrame, bg="white", font=("Courier", 18))
label.place(relwidth=1, relheight=1)

root.mainloop()