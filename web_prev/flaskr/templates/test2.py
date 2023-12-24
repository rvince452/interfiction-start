import requests
import requests

def upload_file_to_sharepoint(file_path, site_url, folder_path, access_token):
    # Construct the URL for the upload request
    upload_url = f"{site_url}/_api/web/GetFolderByServerRelativeUrl('{folder_path}')/Files/Add(url='{file_path}', overwrite=true)"

    # Read the file contents
    with open(file_path, "rb") as f:
        file_contents = f.read()

    # Set the headers for the upload request
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/octet-stream",
        "Content-Length": str(len(file_contents)),
    }

    # Make the upload request
    response = requests.post(upload_url, headers=headers, data=file_contents)

    # Check the response status code
    if response.status_code == 200:
        print("File uploaded successfully.")
    else:
        print(f"Error uploading file: {response.text}")


        def get_sharepoint_token(client_id, client_secret, tenant_id):
            # Construct the URL for the token request
            token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

            # Set the headers and data for the token request
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = {
                "grant_type": "client_credentials",
                "client_id": client_id,
                "client_secret": client_secret,
                "scope": "https://graph.microsoft.com/.default",
            }

            # Make the token request
            response = requests.post(token_url, headers=headers, data=data)

            # Check the response status code
            if response.status_code == 200:
                # Extract the access token from the response
                access_token = response.json()["access_token"]
                return access_token
            else:
                print(f"Error getting token: {response.text}")
                return None
