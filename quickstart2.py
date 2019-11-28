
from __future__ import print_function 
from googleapiclient.discovery import build 
from httplib2 import Http 
from oauth2client import file, client,tools
from apiclient.discovery import build
from apiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.json
SCOPES = 'https://www.googleapis.com/auth/drive' 
def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    # The file token.json stores the user's access and refresh tokens, and is created automatically when the authorization flow completes for the 
    # first time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))
    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    # Try to upload a file
    file_metadata = {
        'name' : 'output.mp4',
	'mimeType' : 'application/vnd.google-apps.spreadsheet'
    }
    media = MediaFileUpload('output.mp4',mimetype='video/mp4',resumable=True)
    a = service.files().create(body=file_metadata,media_body=media,fields='id')
    response = None
    while response is None:
        status,response = a.next_chunk()
 	if status:
            print('Uploaded %d%%' %int(status.progress() *100))
    print('Upload complete')
    #print('File ID: %s' % a.get('id'))
    
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

main()
