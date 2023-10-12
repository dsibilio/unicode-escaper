# unicode-escaper

Escapes all characters in an Excel file other than the [ASCII Printable Characters](https://www.w3schools.com/charsets/ref_html_ascii.asp) then stores the processed copy in the current folder.

## Usage

Create a Python virtual environment:
```shell
python -m venv .venv
```
---

Activate the virtual environment:

### Windows:


```shell
.venv\Scripts\activate
```

### POSIX:

```shell
source .venv/bin/activate
```

---

Install the required dependencies:
```shell
pip install -r requirements.txt
```

---

Run the unicode-escaper pointing to the Excel file to process:
```shell
python unicode_escape.py -s <path/to/excel/file.xlsx>
```

## Help

Run:

```shell
python unicode_escape.py -h
```

to display the help message with a detailed description of all program arguments.