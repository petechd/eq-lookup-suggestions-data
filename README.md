# eQ Lookup Suggestions Data

This repository contains TextField suggestion data source files used for versioned json files generation for eq-questionnaire-runner.

## Source csv files

Source data files are provided by the business as single column csv files.

| Dataset | Description |
| ------- |-------|
| countries-of-birth.csv | List of countries for country of birth questions |
| ethnic-groups.csv | List of ethnic groups |
| languages.csv | List of languages |
| national-identities.csv | List of national identities |
| passport-countries.csv | List of countries for passport questions |
| religions.csv | List of religions |

These can be manually added/updated in this repository at `./source-data`

Separate source data files are provided for the Northern Ireland region at `./source-data/ni/en` and the non Northern Ireland (GB) region at `./source-data/gb`

For the GB region, separate source data files are provided for the Welsh and English language versions of the suggestions lists at `./source-data/gb/cy` and `./source-data/gb/en` respectively.

- source files to be provided by the business named for the above datasets

- files to be UTF-8 csv

- any values including commas should be double quoted

- data rows to contain lookup terms (as to be presented in the lookup lists)

## Front-end json files

json files generation from source csv files is automated on a new version release using GitHub actions and artifact of an archived folder in .zip format is published. To manually generate the files use `./scripts/convert_csv_to_json.py`.

- csv source file root directory `./source-data`

- json output file root directory `./data`

- two further levels of sub directories are expected corresponding to the `{region}` and `{language_code}` of the suggestions files respectively
