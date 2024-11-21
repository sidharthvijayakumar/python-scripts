import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2 import service_account

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
SERVICE_ACCOUNT_FILE = 'credentials.json'

def create_service():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service

def delete_messages(service, user_id, query=''):
    try:
        messages = service.users().messages().list(userId=user_id, q=query).execute()
        if 'messages' in messages:
            for message in messages['messages']:
                service.users().messages().delete(userId=user_id, id=message['id']).execute()
                print('Message with id: %s deleted successfully.' % message['id'])
        else:
            print('No messages found.')
    except Exception as e:
        print('An error occurred: %s' % e)

def main():
    service = create_service()
    delete_messages(service, 'me', 'from:rocketsidharth@gmail.com') # You can change the query as per your requirement

if __name__ == '__main__':
    main()
