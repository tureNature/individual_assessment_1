import os
from xml.etree import ElementTree as ET
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def parse_xml(file_path, extraction_mode):
    tree = ET.parse(file_path)
    root = tree.getroot()
    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
    if extraction_mode == "abstract":
        abstract_elements = root.findall(".//tei:profileDesc/tei:abstract/tei:div/tei:p", namespaces=ns)
        return  ' '.join([element.text.strip() for element in abstract_elements if element.text])
    elif extraction_mode == "figures":
        return root.findall(".//tei:figure", namespaces=ns)
    elif extraction_mode == "links":
        bibl_structs = root.findall(".//tei:biblStruct", namespaces=ns)
        return [ptr.get("target") for bibl_struct in bibl_structs if (ptr := bibl_struct.find(".//tei:ptr", namespaces=ns)) is not None]

def get_xml_files(folder_path):
    return [file for file in os.listdir(folder_path) if file.endswith(".xml")]

def generate_wordcloud(folder_path):
    xml_files = get_xml_files(folder_path)
    abstracts = {}
    for xml_file in xml_files:
        xml_path = os.path.join(folder_path, xml_file)
        abstract = parse_xml(xml_path, "abstract")
        abstracts[xml_file] = abstract
    all_text = " ".join(abstracts.values())
    wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110).generate(all_text)
    print(os.getenv("pwd"))
    wordcloud.to_file("./output/wordcloud_results/wordcloud.png")

def visualize_figures(folder_path):
    xml_files = get_xml_files(folder_path)
    article_names = []
    figures_counts = []
    for xml_file in xml_files:
        xml_path = os.path.join(folder_path, xml_file)
        article_name = os.path.splitext(xml_file)[0]
        num_figures  = len(parse_xml(xml_path, "figures"))
        article_names.append(article_name)
        figures_counts.append(num_figures)
    plt.bar(range(1, len(figures_counts) + 1), figures_counts)
    plt.xticks(range(1, len(figures_counts) + 1, 1), map(int, range(1, len(figures_counts) + 1)))
    plt.xlabel("Article")
    plt.ylabel("Number of Figures")
    plt.title("Number of Figures per Article")
    plt.savefig("./output/figures_visualization_results/figure_visualization.png")

def extract_links(folder_path):
    xml_files = get_xml_files(folder_path)
    for xml_file in xml_files:
        xml_path = os.path.join(folder_path, xml_file)
        links_in_article = parse_xml(xml_path, "links")
        with open(f"./output/links_extraction_results/{xml_file[:-15]}_links.txt", 'w') as file:
            for link in links_in_article:
                file.write(link + "\n")