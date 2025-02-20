import unittest
import os
import csv

def load_csv(f):
  
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)

    data = {}  # Dictionary to store parsed CSV data

    # Open CSV file and read data
    with open(full_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row

        for row in reader:
            if len(row) >= 3:  # Ensure there are at least 3 columns
                year, month, value = row[:3]  # Unpack the first 3 columns
                if year not in data:
                    data[year] = {}
                data[year][month] = value  # Store as string (as required)

    return data


def get_annual_max(d):
   
    results = []

    # Iterate through each year in the data
    for year, months in d.items():
        # Find the month with the maximum visitors for the given year
        max_month = max(months.items(), key=lambda x: int(x[1]))  # Find month with max visitors for the year
        # Store the result as a tuple with the year, month, and max visitors
        results.append((year, max_month[0], int(max_month[1])))  # Store tuple (year, month, max)

    # Sort results by year first, ensuring the test can match the expected order
    results.sort(key=lambda x: (x[0], x[1]))  # Sort by year, then by month (if needed)

    return results


def get_month_avg(d):
  
    averages = {}

    for year, months in d.items():
        values = [int(value) for value in months.values()]  # Convert all values to int
        avg = round(sum(values) / len(values))  # Compute and round average
        averages[year] = avg  # Store in dictionary

    return averages

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
