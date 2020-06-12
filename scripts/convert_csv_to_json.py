#!/usr/bin/env python3

import os
import pandas as pd
import sys
import json


def generate_json_files(version):

    source_directory = './source-data/'
    output_directory = './data/' + version + '/'

    for source_file_name in os.listdir(source_directory):
        if os.path.isfile(os.path.join(source_directory, source_file_name)):

            source_file = open(os.path.join(source_directory, source_file_name), 'r')

            output_file_name = source_file_name.replace('.csv', '.json')
            output_file_location = os.path.join(output_directory, output_file_name)

            csv_data = pd.DataFrame(
                pd.read_csv(source_file,
                            sep=",",
                            header=0,
                            index_col=False))

            try:
                # This approach will exclude null values
                with open(output_file_location, 'w') as f:
                    json.dump([row.dropna().to_dict() for index, row in csv_data.iterrows()], f, indent=3)
            except FileNotFoundError:
                print("Output could not be written to " + output_file_name +
                      " Does the output folder " + output_directory + " exist?")
                return

            print(source_file.name + " >> " + output_file_location)

            source_file.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        generate_json_files(sys.argv[1])
    else:
        print("Please provide a version folder as the only argument")
