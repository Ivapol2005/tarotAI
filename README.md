# tarotAI
Open-Source Tarot Readings Powered by LLM

## Installation

To install and run the tarotAI application on your PC, you will need to follow these steps. This guide assumes you have Python and Git installed.
If not:
 - install Python (preferably the latest version): https://www.python.org/downloads/
 - install git: https://git-scm.com/downloads

### 1. Clone the repository:
  ```bash
  git clone https://github.com/Ivapol2005/tarotAI.git
  cd tarotAI
  ```

## Set up

### 1. Set up a Virtual Environment (Recommended)
It's a good practice to use a virtual environment to manage dependencies for your project.
  ```bash
  python -m venv venv
  ```
Activate the virtual environment:
 - On Windows: `venv\Scripts\activate`
 - On macOS and Linux: `source venv/bin/activate`

### 2. Install Dependencies
Now, install the required Python packages from the `requirements.txt` file.
  ```bash
  pip install -r requirements.txt
  pip install -e .
  ```

### 3. Create a .env File
The LLM needs a `GITHUB_TOKEN` to function. You'll need to create a `Personal Access Token` on GitHub. No permissions required. [Page about tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

Now, when you have your own token, create a directory named config and a file named .env inside it.
  ```bash
  mkdir config
  echo "GITHUB_TOKEN=your_github_token" > config/.env
  echo "USE_REVERSED=True" >> config/.env
  ```
Replace your_github_token with the token you just created.

## 🧪 Running Tests
To run all unit tests:
  ```bash
    python3 -m pytest tests/
  ```

## Usage
You can now run the TarotAI application from the command line. The tell() function is likely the entry point.
  ```bash
  python -c "from tarotai import tell; tell()"
  ```
If you want to explore the functions or run the script in a more interactive way, you can enter the Python shell.
  ```bash
  python
  ```
Once in the shell (you will see a >>> prompt), type the following:
  ```python
  >>> from tarotai import tell
  >>> tell(useReversed=True)
  ```

### 🔧 `tell()` – Perform a Tarot Spread
  `tell(spreadID=0, useReversed=False, pyPrint=False)`
Performs a Tarot card spread using one of the predefined layouts.

**Arguments:**
 - `spreadID` (int): Index of the spread from the list (see `help()` for available options).
 - `useReversed` (bool): If `True`, cards can be drawn reversed; if `False`, all cards are upright.
 - `pyPrint` (bool): If `True`, prints the result to console; otherwise, returns it as a string.

**Example:**
  ```python
  from tarotai import tell

  # Perform a 3-card reading with reversed cards allowed
  reading = tell(spreadID=0, useReversed=True)
  print(reading)
  ```

**Returns:**
A list of dictionaries, each representing a card in the spread:

  ```python
  [
    {
      "question": "Past",
      "card": "The Fool",
      "ifReversed": False,
      "meaning": ["New beginnings", "Adventure", "Innocence"]
    },
    ...
  ]
  ```

### 🗂️ `help()` – Get Spread Info
  `help(spread_id=-1, pyPrint=False)`

Displays information about available Tarot spreads.

**Arguments:**

 - `spread_id` (int): ID of a specific spread to inspect. Use `-1` (default) to list all available spreads.
 - `pyPrint` (bool): If `True`, prints the result to console; otherwise, returns it as a string.

**Example:**
  ```python
  from tarotai import help

  # List all available spreads
  print(help())

  # View details of spread with ID 0
  print(help(0))
  ```

## 📜 License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

You are free to use, modify, and distribute this software under the terms of the license. Please see the `LICENSE` file for full details.
