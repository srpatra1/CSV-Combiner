"""Concatenates CSV files inputted from command line arguments and outputs to stdout.
Source file name is added as a field to the output CSV file."""

import sys
import pandas as pd


def csv_to_df(filename):
    """Reads CSV and stores it as a pandas dataframe.
    Splits filepath based on '/' and saves the last value as the base filename.
    Adds the base filename field to the dataframe along with its values."""
    df = pd.read_csv(filename, index_col=False, quoting=3)
    split_filename = filename.split('/')
    basename = '"' + split_filename[-1] + '"'
    filename_list = [basename] * len(df)
    df['"filename"'] = filename_list
    return df


def create_dataframe_list(filelist):
    """Creates a list of csvs stored as dataframes from the list of csv files."""
    df_li = []
    for file in filelist:
        df = csv_to_df(file)
        df_li.append(df)
    return df_li


def check_fields(df_li):
    """Iterates through a list of dataframes and checks if dataframes have the same fields"""
    return all(list(df.columns) == list(df_li[0].columns) for df in df_li)


def combine_csv(filelist):
    """Combines csv from inputted list of csv files."""
    if len(filelist) > 1:
        """Code runs only when arguments exist."""
        flist = filelist[1:len(filelist) + 1]
        for file in flist:
            """Checks to make sure file extension is csv."""
            split_filename = file.split('.')
            fileext = split_filename[-1]
            if fileext != "csv":
                raise TypeError("One or more files do not have the .csv file extension.")
        super_df = create_dataframe_list(flist)
        """Checks to see if csv files have the same fields. Raises a valueError if they do not."""
        if not check_fields(super_df):
            raise ValueError("Fields are not the same.")
        df_super_list = pd.concat(super_df)
        sys.stdout.write(df_super_list.to_csv(index=False, quoting=3))


def main():
    combine_csv(sys.argv)


if __name__ == "__main__":
    main()