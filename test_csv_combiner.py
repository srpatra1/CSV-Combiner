import pandas as pd
from csv_combiner import combine_csv
import os


def test_csv_combiner(test_output):
    """Tests whether the script runs with command line inputs and checks whether the output is correct."""
    os.system("python3 ./csv_combiner.py ./test/test.csv ./test/test1.csv > eq_output.csv")
    df1 = pd.read_csv('eq_output.csv')
    df2 = pd.read_csv(test_output)
    os.system("rm eq_output.csv")
    return pd.DataFrame.equals(df1, df2)


def test_csv_combiner_args():
    """Tests to see if an error is raised when the csv fields are different."""
    try:
        combine_csv(['foo.py', './test/test1.csv', './test/test1_diff_fields.csv'])
    except ValueError:
        print("Value Error Raised Successfully when csv fields do not match.")


def test_csv_combiner_fileext():
    """Tests to see if an error is raised when a non csv file is sent as an argument."""
    try:
        combine_csv(['foo.py', './test/test1.txt', './test/test1.csv'])
    except TypeError:
        print("Type Error Raised Successfully when file extension is not a csv.")


test_output = './test/test_output_correct.csv'
print(test_csv_combiner(test_output))
test_csv_combiner_args()
test_csv_combiner_fileext()