import requests
import validators
from termcolor import colored
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from html import escape
from lxml import html
from urllib.parse import urlparse
import sys

init()

def check_url_exists(url):
    if not validators.url(url):
        return False, "Invalid URL format"

    try:
        response = requests.head(url)
        if response.status_code == 200 or response.status_code == 301 or response.status_code == 307 or response.status_code == 302:
            return True, "URL Exists, Process Has Been Started"
        else:
            return False, f"URL returned a status code of {response.status_code}"
    except requests.RequestException as e:
        return False, f"URL is not reachable: {e}"

def fetch_and_save_urls(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()

        raw_urls = response.text

        with open(output_file, "w") as file:
            file.write(raw_urls)

        print(f"{Fore.MAGENTA}All URLs have been successfully saved to{Style.RESET_ALL} {Fore.BLUE}{output_file}{Style.RESET_ALL}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

prompt_text = colored("URL Format eg pythagorex.com, Do Not Add HTTPS or HTTP.", 'green')
enter_text = colored("Enter URL:", 'blue')

print(prompt_text)
link = input(enter_text)

full_url = f"http://{link}"
is_valid, message = check_url_exists(full_url)

if is_valid:
    print(colored(message, 'green'))
    url = f"https://web.archive.org/cdx/search/cdx?url=*.{link}/*&output=text&fl=original&collapse=urlkey"
    output_file = "urls.txt"
    fetch_and_save_urls(url, output_file)
    with open("urls.txt", "r") as file:
        urls = file.readlines()
    print(f"{Fore.CYAN}Total Fetched URL {Style.RESET_ALL}{Fore.RED}{len(urls)}{Style.RESET_ALL}")

else:
    print(colored(message, 'red'))
    sys.exit()

with open('urls.txt', 'r') as file:
    urls = file.readlines()

js_urls = [url.strip() for url in urls if url.strip().endswith('.js')]

with open('js_urls.txt', 'w') as file:
    for url in js_urls:
        file.write(f"{url}\n")

with open("js_urls.txt", "r") as file:
    urls = file.readlines()
js_count = len(urls)
print(f"{Fore.YELLOW}Filtered {Style.RESET_ALL}{Fore.RED}{js_count}{Style.RESET_ALL} {Fore.YELLOW}JS URLs saved to js_urls.txt")

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return url
    except requests.RequestException:
        return None

def check_urls(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        urls = file.readlines()

    urls = [url.strip() for url in urls]

    working_urls = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in urls}
        for future in tqdm(as_completed(future_to_url), total=len(urls), desc="Checking URLs", ncols=80):
            result = future.result()
            if result:
                working_urls.append(result)

    open(output_file_path, 'w').close()

    with open(output_file_path, 'w') as file:
        for url in working_urls:
            file.write(url + '\n')

input_file_path = 'js_urls.txt'
output_file_path = 'working_urls.txt'

check_urls(input_file_path, output_file_path)
with open("working_urls.txt", "r") as file:
    working_jss = file.readlines()
working = len(working_jss)
print(f"{Style.RESET_ALL}{Fore.RED}{working}{Style.RESET_ALL} {Fore.MAGENTA}URLs are valid")

