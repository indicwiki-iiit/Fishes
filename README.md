# Fishes
This repository contains all the work that was done as a part of enriching Hindi wikipedia in the biomedical domain. The sub-domain chosen is "Fish".

## Stages of the project

The following ordered list will give an idea as to what stage the project currently is in:

- [x] Scrape Data from Web sources
- [x] Clean and Format the data
- [x] Scrape image URLs from Wiki commons
- [x] Scrape infobox information from Wikipedia
- [x] Create a sample article
- [x] Review of the sample article
- [x] Work on feedback from review of sample article
- [x] Review of the dataset
- [x] Create template for article generation
- [x] Review of the template
- [x] Work on feedback from review of template
- [x] Create the XML dump for all the diseases to be published

## Folders

- `Datasets`: Contains all the dataset (csv) files that have been used for this project.
- `Code`: Contains all the code that has been used in the project.

### Datasets

This folder contains the final dataset as well as some other dataset that have been used in the project:

- [FinalFishesHindi_1.pkl](./Datasets/FinalFishesHindi_1.pkl): 
- [FinalFishesHindi_2.pkl](./Datasets/FinalFishesHindi_2.pkl): 
- [Fish_names.csv](./Datasets/Fish_names.csv): 

### Code

This folder contains various files:


### Generating articles
- [template](./template.j2): it contains the template for the structure of the article
- [genXML](./genXML.py): it contains the backbone structure for conversion to XML
- [render](./render.py): it contains the code for generating XML dump of articles using the template and the dataset
- [fishes50Dump](./fishes50Dump.xml): the testing XML dump file of first 50 fish and its atributes.
