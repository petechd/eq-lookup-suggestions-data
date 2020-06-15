#!/usr/bin/env python3

import os
import pandas as pd
import json


def generate_json_files():

    source_directory = './source-data/'
    output_directory = './data/'

    for source_file_name in os.listdir(source_directory):

        source_file_location = os.path.join(source_directory, source_file_name)

        if os.path.isfile(source_file_location):

            source_file = open(source_file_location, 'r')

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
                print("Output could not be written to {0}\nDoes the output folder {1} exist?"
                      .format(output_file_name, output_directory))
                return

            print(source_file.name + " >> " + output_file_location)

            source_file.close()
        else:
            print("{0} is not a regular file").format(source_file_location)


if __name__ == "__main__":
        generate_json_files()
