import sys
from grobid_client.grobid_client import GrobidClient
from utilities import generate_wordcloud, visualize_figures, extract_links

def main(folder_path):
    generate_wordcloud(folder_path)

    visualize_figures(folder_path)

    extract_links(folder_path)
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        client = GrobidClient(config_path="./config.json")
        client.process("processFulltextDocument", "./resources/pdf_files", output="./resources/grobid_output/", consolidate_citations=True, tei_coordinates=True, force=True)
    elif len(sys.argv) > 1:
        print("help")
        exit(1)
    main("resources/grobid_output")