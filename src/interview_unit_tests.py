import unittest
import pandas as pd
from interview_test import combine_names, categorize_age, age_group_spending

class interview_unit_tests(unittest.TestCase):

    def test_combine_names(self):
        print("Running test_combine_names...")
        row = {'first_name': 'John', 'last_name': 'Doe'}
        result = combine_names(row)
        self.assertEqual(result, 'John Doe')

    def test_categorize_age(self):
        print("Running test_categorize_age...")
        self.assertEqual(categorize_age(25), 'Young')
        self.assertEqual(categorize_age(35), 'Middle-aged')
        self.assertEqual(categorize_age(50), 'Senior')

    def test_compute_age_group_spending(self):
        print("Running test_compute_age_group_spending...")
        test_data = pd.DataFrame({
            'age_group': ['Young', 'Middle-aged', 'Senior', 'Young'],
            'price': [100, 200, 150, 50]
        })

        expected_output = pd.DataFrame({
            'age_group': ['Middle-aged', 'Senior', 'Young'],
            'price': [200, 150, 150]
        }).sort_values(by='age_group').reset_index(drop=True)

        result = age_group_spending(test_data).sort_values(by='age_group').reset_index(drop=True)
        pd.testing.assert_frame_equal(result, expected_output)

if __name__ == "__main__":
    unittest.main()


