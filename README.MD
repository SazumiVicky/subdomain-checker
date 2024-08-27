This script is used to check the status of subdomains of a root domain. It uses `sublist3r` to find subdomains and `requests` to check the HTTP status of those subdomains.

## Requirements

Make sure you have Python 3.x installed on your system. You also need to install some required Python libraries.

## Installation

1. **Clone this repository or download the script files.**

2. **Install the required libraries using `pip`:**

    ```sh
    pip install -r requirements.txt
    ```

    Contents of `requirements.txt`:
    ```text
    requests
    sublist3r
    colorama
    ```

3. **If you don't have `pip`, you can install it by following the instructions [here](https://pip.pypa.io/en/stable/installation/).**

## Usage

1. **Run the `main.py` script:**

    ```sh
    python main.py
    ```

2. **Enter the root domain you want to check when prompted:**

    ```sh
    Please enter your root domain: example.com
    ```

3. **The script will display a results table showing the status of subdomains and a summary table showing the number of active and inactive subdomains.**

    Example output:
    ```
    ------------------------------------------------------------
    | ROOT DOMAIN        | STATUS |         SUBDOMAIN          |
    ------------------------------------------------------------
    | example.com        | 200    | www.example.com            |
    | example.com        | 503    | api.example.com            |
    | example.com        | 200    | blog.example.com           |
    ------------------------------------------------------------
    | ACTIVE             |        |         INACTIVE           |
    ------------------------------------------------------------
    | 2                  |        | 1                          |
    ------------------------------------------------------------
    ```

## Notes

- If the `colorama` library is not installed, the script will still run but without colored output.
- If you encounter connection issues, the subdomain status will be displayed as `503`.

## Contribution

If you would like to contribute to this project, please fork this repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.