#Import necessary library
import requests
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

#Define variable
api_endpoint = 'https://covid19.mathdro.id/api/countries/indonesia'
line_channel_access_token = '(change with your channel access token)'

#Api call
line_bot_api = LineBotApi(str(line_channel_access_token))
api_endpoint = requests.get(str(api_endpoint))

#Make payload
api_data = api_endpoint.text
api_data_json = json.loads(api_data)
parse_confirmed = api_data_json['confirmed']['value']
parse_recovered = api_data_json['recovered']['value']
parse_deaths = api_data_json['deaths']['value']
update_at = api_data_json['lastUpdate']

#Prettify Api data
confirmed = "{:,}".format(parse_confirmed)
recovered = "{:,}".format(parse_recovered)
deaths = "{:,}".format(parse_deaths)

#Setup Message Api payload
str_main_message = "Update COVID-19 di Indonesia\n\n"
str_author = "Rikky"
str_github_link = "https://github.com/masrikky/COVID19-LINE-Bot-Python"
str_confirmed = "Terkonfirmasi : "
str_confirmed_api = str(confirmed)
str_recovered = "Sembuh : "
str_recovered_api = str(recovered)
str_deaths = "Meninggal : "
str_deaths_api = str(deaths)
payload =  str_main_message + str_confirmed + str_confirmed_api + " orang\n" + str_recovered + str_recovered_api + " orang\n" + str_deaths + str_deaths_api + " orang\n\n" + "Terakhir diperbarui pada : " + update_at + "\n\nBot LINE COVID-19 dibuat oleh " + str_author + "\nGithub : " + str_github_link

#Send (broadcast) payload
line_bot_api.broadcast(TextSendMessage(text=payload))
