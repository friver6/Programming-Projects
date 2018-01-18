#Took this from the Firebase documentation website.

from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

# Define the required scopes
scopes = [
  "https://www.googleapis.com/auth/userinfo.email",
  "https://www.googleapis.com/auth/firebase.database"
]

# Authenticate a credential with the service account
credentials = service_account.Credentials.from_service_account_file(
    "projKey.json", scopes=scopes)

request = google.auth.transport.requests.Request()
credentials.refresh(request)
access_token = credentials.token
