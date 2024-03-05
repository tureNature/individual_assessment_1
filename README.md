
# individual_assessment_1

This project leverages Grobid, a powerful document processing tool, to analyze 10 open-access articles following class best practices. The program automatically extracts keywords from article abstracts, forming a visually informative keyword cloud that highlights key topics. Additionally, it identifies and quantifies figures in each article, presenting a graphical representation of figure distribution. Furthermore, the program compiles a comprehensive list of embedded links in each article, offering a convenient resource reference.

## Installation

To install the project, the following steps should be followed. First, clone the repository:

```bash
  git clone https://github.com/tureNature/individual_assessment_1.git
  cd individual_assessment_1
```

## Deployment

Using this tool is straightforward. You just need to activate Grobid with the following command:

```bash
  ./init_grobid.sh
```
Afterwards, place the PDF files you want to analyze in the data/input_pdf folder. Then, proceed to build and run the Docker container with the following commands:

```bash
  make build
  make run
```

This will send the documents to Grobid, analyze them, retrieve the XML files (which will be stored in the data/output_grobid directory), and produce the requested results for the practice in the data/output_individual_assessment_1 folder.

## Running Tests

To run tests, run the following command

```bash
  make build-test
  make run-test
```

## Integration with Grobid client

It is noted that the grobid_client_python has been utilized for communication with Grobid, available at [link](https://github.com/kermitt2/grobid_client_python) to the repository.

## Zenodo

[![DOI](https://zenodo.org/badge/764234292.svg)](https://zenodo.org/doi/10.5281/zenodo.10783111)

## Author

- [@tureNature](https://www.github.com/tureNature)


## License

[GPL](https://fsf.org/)

