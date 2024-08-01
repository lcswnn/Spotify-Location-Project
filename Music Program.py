'''____________________________________________________________________________________
   Concept: Music changes based on where you are driving and location in the world  
                                                                                    
   Lucas Waunn: SWE Side Project                                                    
____________________________________________________________________________________'''

''' 
For GPS Tracking: https://www.geeksforgeeks.org/gps-tracker-using-python/
     Assuming we can just use a loop with a wait-timer and refresh the location
     while program is running

For Spotify Playing: https://pypi.org/project/pyspotify-connect/
      Only works with Spotify Premium so should be good

'''

#Libraries
import spotipy
import json
import webbrowser

#set up
username = "p9a0qcw35f9oqgu3xyzh9d9wy"
clientID = "a640eae6cdbe4f428870af688c9001cf"
clientSecret = "498a4f5822544a3683b41300b7ddae28"
redirect_uri = 'http://google.com/'

# Create OAuth Object
oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirect_uri)
# Create token
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
# Create Spotify Object
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
# To print the response in readable format.
print(json.dumps(user,sort_keys=True, indent=4))



