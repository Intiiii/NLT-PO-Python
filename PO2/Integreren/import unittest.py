import unittest
from io import StringIO
import sys

# Importeer de twitter functie uit het bestand twitter.py
from twitter import twitter

class TestTwitterFunction(unittest.TestCase):
    def test_twitter_output(self):
        # Vang de uitvoer van de twitter functie op
        captured_output = StringIO()
        sys.stdout = captured_output
        twitter()
        sys.stdout = sys.__stdout__
        
        # Haal de uitvoer op en converteer naar een float
        output = captured_output.getvalue().strip()
        estimated_area = float(output)
        
        # Controleer of de geschatte oppervlakte binnen het bereik ligt
        self.assertTrue(0.82 <= estimated_area <= 0.83, f"Geschatte oppervlakte {estimated_area} ligt niet binnen het bereik 0.82 - 0.83")

if __name__ == '__main__':
    unittest.main()