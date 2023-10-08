import requests

headers = {
    "x-api-key": "__________",
    "Content-Type": "application/json",
}

inquiry = input("What would you like to learn from this document? ")

data = {
    "stream": True,
    "sourceId": "cha_YPGzQgRUUuiIt7D3miXri",
    "messages": [
        {
            "role": "user",
            "content": inquiry,
        },
    ],
}


url = "https://api.chatpdf.com/v1/chats/message"

try:
    response = requests.post(url, json=data, headers=headers, stream=True)
    response.raise_for_status()

    if response.iter_content:
        max_chunk_size = 1024
        for chunk in response.iter_content(max_chunk_size):
            text = chunk.decode()
            print("Chunk:", text.strip())
    else:
        raise Exception("No data received")
except requests.exceptions.RequestException as error:
    print("Error:", error)