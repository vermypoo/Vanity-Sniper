import requests
import time

vanity_code = 'VANITY HERE'
server_id = 'SERVER ID HERE'
token = 'YOUR TOKEN HERE'

base_url = 'https://discord.com/api/v9'
invite_url = f'{base_url}/invites/{vanity_code}'
settings_url = f'{base_url}/guilds/{server_id}/vanity-url'
headers = {
    'Authorization': f'{token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

while True:
    try:
        response = requests.get(invite_url)

        if response.status_code == 404:
            print(f'The vanity URL "{vanity_code}" is available.')

            patch_response = requests.patch(
                settings_url,
                headers=headers,
                json={'code': vanity_code}
            )

            if patch_response.status_code == 200:
                print(f'Vanity URL "{vanity_code}" has been set for the server.')
                break
            else:
                print(f'Failed to set vanity URL: {patch_response.text}')

        elif response.status_code == 200:
            print(f'The vanity URL "{vanity_code}" is not available.')

        else:
            print(f'Unexpected status code: {response.status_code}')

    except requests.RequestException as e:
        print(f'Error occurred: {e}')
        break

    time.sleep(60)
