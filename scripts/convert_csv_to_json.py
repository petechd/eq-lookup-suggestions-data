#!/usr/bin/env python3

import os
import csv
import json


def generate_json_files():

    source_root = './source-data'
    output_root = './data'

    for source_region_directory_name in os.listdir(source_root):
        source_region_directory = os.path.join(source_root, source_region_directory_name)

        for language_directory_name in os.listdir(source_region_directory):
            source_directory = os.path.join(source_region_directory, language_directory_name)

            for source_file_name in os.listdir(source_directory):

                source_file_location = os.path.join(source_directory, source_file_name)

                if os.path.isfile(source_file_location):

                    source_file = open(source_file_location, 'r')

                    output_file_name = source_file_name.replace('.csv', '.json')
                    output_file_location = os.path.join(output_root,
                                                        source_region_directory_name,
                                                        language_directory_name,
                                                        output_file_name)

                    json_data = []

                    with open(source_file_location, newline='') as csv_file:
                        for row in csv.DictReader(csv_file, fieldnames=['term']):
                            json_data.append(row.get('term'))
                    try:
                        with open(output_file_location, 'w', encoding='utf8') as f:
                            json.dump(json_data, f, indent=4, ensure_ascii=False)
                            f.write("\n")
                    except FileNotFoundError:
                        print(
                            f"Output could not be written to {output_file_location}\nDoes the output folder"
                            f"{output_root}/{source_region_directory_name}/{language_directory_name} exist?"
                        )
                        return

                    print(f"{source_file.name} >> {output_file_location}")

                    source_file.close()
                else:
                    print(f"{source_file_location} is not a regular file")


if __name__ == "__main__":
    generate_json_files()
