# eQ Lookup Suggestions Data

This repository contains versioned TextField suggestion data for eq-questionnaire-runner

| Dataset | Description |
| ------- |-------|
| countries-of-birth.json | List of countries for country of birth questions |
| ethnic-groups.json | List of ethnic groups |
| languages.json | List of languages |
| national-identities.json | List of national identities |
| passport-countries.json | List of countries for passport questions |
| religions.json | List of religions |


Source data files are provided by the business as multiple column csvs. These can be manually added/updated in this repository at ./source-data

- files to be UTF-8 csv

- any values including commas should be double quoted

- header row to contain comma separated language_codes (e.g `en_gb`, `cy`)

- data rows to contain comma separated translated lookup values (as to be presented in the lookup lists)

- null values for a given language item can be provided by a non-spaced commas. This will reslt in that term not being presented as a suggestion for that language

A json file can be generated from the source csv file using the ./scripts/convert_csv_to_json.py

- default expected source file location ./source-data

- default json file output location ./data

- discussions as ongoing as to how versions of the files will be managed.
