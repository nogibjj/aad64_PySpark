import os
import tempfile
import unittest
from mylib.lib import (
    initialize_spark,
    read_csv,
    sql_query,
    perform_data_transformation,
    save_summary_report,
)


class TestMyLib(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = initialize_spark()
        cls.file_path = "songs_normalize.csv"
        cls.df = read_csv(cls.spark, cls.file_path)

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_read_csv(self):
        assert self.df.count() == 2000

    def test_sql_query(self):
        sql_query_string = "artist = 'Maroon 5'"
        result_df = sql_query(self.df, sql_query_string)
        assert result_df.count() > 1

    def test_perform_data_transformation(self):
        column_of_interest = "artist"
        target_value = "Maroon 5"
        transformed_df = perform_data_transformation(
            self.df, column_of_interest, target_value
        )
        assert transformed_df.count() > 1

    def test_save_summary_report(self):
        report_content = "This is a summary report."
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "report.txt")
            save_summary_report(report_content, file_path)
            with open(file_path, "r") as f:
                assert f.read() == report_content
