import json, requests
#base_url this is the website we will gather weather data from; appid is my api key
base_url = "https://api.openweathermap.org/data/2.5/weather"
  
appid = "72af344e3cb23d58253bb4f5ade8a2cc"

def weather_data(): 
  while True:
    print()
    
    zipcode = input("enter your zipcode: ")
    
    url = f"{base_url}?q={zipcode}&units=imperial&APPID={appid}"
   #if user does not enter a real zipcode, then the program will return an error message
    try: 
      response = requests.get(url)
      print("\nConnection to web service successful")

      if "200" not in str(response):
        raise ValueError("Invalid info, please try again")
    except:
      print("\nInvalid info, please try again")
      continue
    
    unformated_data = response.json()
  # from line 23 - 31, weather info is displayed for the given location
    temp = unformated_data["main"]["temp"]
    print(f"\nThe current temp is: {temp}")
    temp_max = unformated_data["main"]["temp_max"]
    print(f"The max temp is: {temp_max}")
    temp_min = unformated_data["main"]["temp_min"]
    print(f"The min temp is: {temp_min}")
    cloud_condition = unformated_data["weather"][0]["description"]
    print(f"The cloud condition is: {cloud_condition}")
    # the user is given the choice to continue checking the weather or leave the site.
    again = input("\nWould you like to search another zipcode? (Yes or No) ")
  
    if again.lower() != "yes":
      print("Thanks for using the weather app.")
      break
   # the last lines are calling the main and weather data function 
def main():
  weather_data()
  
    
main()
  

  