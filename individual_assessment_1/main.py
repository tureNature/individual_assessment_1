import os
from grobid_client.grobid_client import GrobidClient
from utilities import generate_wordcloud, visualize_figures, extract_links

def main(folder_path):
    generate_wordcloud(folder_path)
    visualize_figures(folder_path)
    extract_links(folder_path)

def init_data_dir(data_dir):
    input_pdf_dir = os.path.join(data_dir, "input_pdf")
    output_grobid_dir = os.path.join(data_dir, "output_grobid")
    output_app_dir = os.path.join(data_dir, "output_individual_assessment_1")
    if not os.path.exists(input_pdf_dir):
        return False, 0, 0
    if not os.path.exists(output_grobid_dir):
        os.mkdir(output_grobid_dir)
    if not os.path.exists(output_app_dir):
        os.mkdir(output_app_dir)
    return True, input_pdf_dir, output_grobid_dir
    
if __name__ == "__main__":
    data_dir = "/app/data"
    config_path = "/app/individual_assessment_1/grobid_client/config.json"
    concurrency = 10
    correct_init, input_pdf_dir, output_grobid_dir = init_data_dir(data_dir)
    if correct_init:
        client = GrobidClient(config_path=config_path)
        client.process("processFulltextDocument", input_pdf_dir, output=output_grobid_dir, consolidate_citations=True, tei_coordinates=True, force=True)
        main(output_grobid_dir)
    else:
        print("Error: no existe la carpeta con los PDF")
    