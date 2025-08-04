"""
This script downloads a file from a given URL using Python's requests library.
It streams the file in chunks to avoid high memory usage, displays a progress bar using tqdm,
and handles common exceptions like HTTPError, Timeout, and ConnectionError.
"""
import requests
from tqdm import tqdm
from requests import HTTPError,Timeout, ConnectionError

# URL of the file to download and output filename
url="https://www.win-rar.com/fileadmin/winrar-versions/rarmacos-arm-712.tar.gz"
output_file="win.tar.gz"

try:
    # Stream the download to avoid loading the whole file in memory
    with requests.get(url, stream=True) as resp:
        resp.raise_for_status() # Raise HTTPError for bad responses (4xx, 5xx)
        # Get file size from headers (optional but useful for tqdm progress bar)
        file_size=int(resp.headers["Content-Length"])
        chunk_size=8192 # 8KB chunks
        #Output a file in write binary mode
        with open(output_file, "wb") as f,tqdm(
            total=file_size, unit="B", unit_scale=True
        )as progress_bar:
            #iterate over the chucks and update the progress bar
            for chunk in resp.iter_content(chunk_size=chunk_size):
                if chunk:
                  f.write(chunk)
                  progress_bar.update(len(chunk))
        print("Download completed")
# Handle different types of errors
except HTTPError as e:
    print(f"An HTTPError occurred: {e}")
except Timeout as e:
    print(f"An Timeout occurred: {e}")
except ConnectionError as e:
    print(f"An ConnectionError occurred: {e}")
except Exception as e:
    print(f"An unknown error occurred: {e}")
