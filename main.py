from grobid_client.grobid_client import GrobidClient
from utilities import generate_wordcloud, visualize_figures, extract_links

def main(folder_path):
    generate_wordcloud(folder_path)
    visualize_figures(folder_path)
    extract_links(folder_path)
    
if __name__ == "__main__":
    config_path = "./config.json"
    input_dir = "./resources/pdf_files"
    output_dir = "./resources/grobid_output/"
    concurrency = 10

    client = GrobidClient(config_path=config_path)
    client.process("processFulltextDocument", input_dir, output=output_dir, consolidate_citations=True, tei_coordinates=True, force=True)

    main(output_dir)