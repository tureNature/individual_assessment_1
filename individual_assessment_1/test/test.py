import sys
import unittest
import os
from xml.etree import ElementTree as ET
import shutil
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Add the path to the project's root directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from individual_assessment_1.utilities import parse_xml, get_xml_files, generate_wordcloud, visualize_figures, extract_links

class TestXMLFunctions(unittest.TestCase):

    def setUp(self):
        # Create a temporary folder for testing
        self.test_folder = "/app/data/test_folder"
        os.mkdir(self.test_folder)
        self.test_xml_path = os.path.join(self.test_folder, "test.xml")
        with open(self.test_xml_path, 'w') as test_file:
            test_file.write("<root><tei:profileDesc><tei:abstract><tei:div><tei:p>Test Abstract</tei:p></tei:div></tei:abstract></tei:profileDesc></root>")

    def tearDown(self):
        # Remove the temporary folder after testing
        shutil.rmtree(self.test_folder)

    def test_parse_xml_abstract(self):
        result = parse_xml(self.test_xml_path, "abstract")
        self.assertEqual(result, "Test Abstract")

    def test_parse_xml_figures(self):
        result = parse_xml(self.test_xml_path, "figures")
        self.assertEqual(len(result), 0)  # No figures in the test XML

    def test_parse_xml_links(self):
        result = parse_xml(self.test_xml_path, "links")
        self.assertEqual(result, [])

    def test_get_xml_files(self):
        result = get_xml_files(self.test_folder)
        self.assertEqual(result, ["test.xml"])

    def test_generate_wordcloud(self):
        generate_wordcloud(self.test_folder)
        # Check if the wordcloud file is generated
        wordcloud_path = "/app/data/output_individual_assessment_1/wordcloud.png"
        self.assertTrue(os.path.exists(wordcloud_path))

    def test_visualize_figures(self):
        visualize_figures(self.test_folder)
        # Check if the figure visualization file is generated
        figure_path = "/app/data/output_individual_assessment_1/figure_visualization.png"
        self.assertTrue(os.path.exists(figure_path))

    def test_extract_links(self):
        extract_links(self.test_folder)
        # Check if the links files are generated
        links_path = "/app/data/output_individual_assessment_1/links_results/test_links.txt"
        self.assertTrue(os.path.exists(links_path))

if __name__ == '__main__':
    unittest.main()
