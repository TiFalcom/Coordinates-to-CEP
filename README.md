# Coordinates-to-CEP

Coordinates-to-CEP is a program to convert geolocation into Brazilian CEP number.

## Requirements
<ol>
  <li>[geopy](https://pypi.org/project/geopy/) - Used to convert geolocalization to Address/CEP.</li>
  <li>[pandas](https://pypi.org/project/pandas/) - Used to Import - Manipulate - Export data.</li>
</ol>

## Usage

To use the program:
<ol>
  <li>Donwload the file cood-to-cep.py.</li>
  <li>Create a file "EXPORT_CEPS.CSV" in the same folder the file you want to convert is saved.</li>
  <li>Execute the following command on bash.</li>
  ```bash
    python path's cood-to-cep.py\cood-to-cep.py
  ```
  Exemple: if your program is saved on folder C:\Users\TiFalcom\Downloads, the command will be:
  ```bash
    python C:\Users\diego\Downloads\cood-to-cep.py
  ```
  <li>Complete with the folder path where geolocation is saved.</li>
  Exemple: if your file is saved on folder C:\Users\TiFalcom\Downloads, you will complete with the following:
  ```bash
    Insert the file path, without file name: C:\Users\TiFalcom\Downloads
  ```
  <li>Complete with the entire file name where geolocation is saved.</li>
  Exemple: if your file name is COORDS.CSV, you will complete with the following:
  ```bash
    Insert the file full name: COORDS.CSV
  ```
  <li>After completing those two informations the program will run and save the CEPS on file EXPORT_CEPS.CSV(depending on the number of observations, it might take a while).</li>
</ol>

## Roadmap

The next steps are:
  1 - Create a path and file name validation.
  2 - Create the out file if it does not exists.
