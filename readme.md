# PYTHAJS (URL Extractor and Validator)

This script extracts all URLs, filters JavaScript URLs, and validates them from the Wayback Machine (web.archive.org) for a given domain. The valid URLs are then saved to a text file.

## This is for test final version will be available soon 

## Features

- Validates the input URL format.
- Fetches all URLs from the Wayback Machine for the given domain.
- Filters out JavaScript (.js) URLs.
- Validates the fetched JavaScript URLs.
- Saves the valid JavaScript URLs to a text file.

## Requirements

- Python 3.x
- Required Python libraries:
  - requests
  - validators
  - termcolor
  - colorama
  - concurrent.futures
  - tqdm

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/shivangmauryaa/pythajs.git
    cd pythajs
    ```

2. Install the required libraries:

    ```bash
    pip install requests validators termcolor colorama tqdm
    ```

## Usage

1. Run the script:

    ```bash
    python script.py
    ```

2. Follow the prompt to enter the URL in the specified format (e.g., `example.com`, without `https://` or `http://`).

3. The script will:
   - Validate the URL format and existence.
   - Fetch all URLs for the given domain from the Wayback Machine.
   - Save the fetched URLs to `urls.txt`.
   - Filter JavaScript URLs and save them to `js_urls.txt`.
   - Validate the JavaScript URLs and save the valid ones to `working_urls.txt`.

4. The output files (`urls.txt`, `js_urls.txt`, and `working_urls.txt`) will be saved in the same directory as the script.

## Example

1. When prompted, enter the URL:

    ```
    URL Format eg pythagorex.com, Do Not Add HTTPS or HTTP.
    Enter URL: example.com
    ```

2. The script will output the total fetched URLs, filtered JavaScript URLs, and the number of valid JavaScript URLs.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For any questions or suggestions, feel free to open an issue or contact me at shivangmauryaa@gmail.com.
