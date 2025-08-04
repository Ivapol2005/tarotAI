# tarotAI
Open-Source Tarot Readings Powered by LLM

## Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/Ivapol2005/tarotAI.git
  cd tarotAI
  ```

2. Install dependencies *(aren't any yet)*:
  ```bash
  pip install -r requirements.txt
  ```

3. (Optional) Install the package locally:
  ```bash
  pip install .
  ```

## 🧪 Running Tests
To run all unit tests:
  ```bash
    python3 -m pytest tests/
  ```

## Usage
Import the main functions from the tarotai package:
  ```python
  from tarotai import tell, help

  # Example usage
  result = tell("three card spread")
  print(result)

  help()  # If this function prints usage information
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
