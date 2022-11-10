# Fishes
This repository contains all the work that was done as a part of enriching Hindi wikipedia in the biomedical domain. The sub-domain chosen is "Fishes". The aim is to create a large number of articles for different Fishes (34,777 Species) in Hindi.

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

- `Datasets`: Contains all the dataset (csv and pickle) files that have been used for this project.
- `Code`: Contains all the code (python notebooks) that has been used in the project.

### Datasets

This folder contains the final dataset as well as some other dataset that have been used in the project:

- [FinalFishesHindi_1](./Datasets/FinalFishesHindi_1.pkl): This pickle file contains all the scraped data for the first half of the total number of fishes.
- [FinalFishesHindi_2](./Datasets/FinalFishesHindi_2.pkl): This pickle file contains all the scraped data for the second half of the total number of fishes. These pickle files will be further used to generate the articles.
- [Fish_names](./Datasets/Fish_names.csv): This csv file contains the species name of every fish along with its FishBase ID.

### Code

This folder contains various files:
- [Web Scrapping 1](./Code/Web%20Scrapping%201.ipynb): This python notebook contains the code to find and scrape the name and ID of all fish species from FishBase.
- [Web Scraping 2](./Code/Web%20Scrapping%202.ipynb): This python notebook contains the code to scrape the data for all the Fish species collected in Web Scrapping 1.  
- [Image Extraction](./Code/Image%20Extraction.ipynb): This contains the code used to extract Images of all fish species from Wikipedia.
- [References Extraction](./Code/References%20Extraction.ipynb): This contains the code used to extract references for Images and other references.
- [WikiData_and_Categories_Extraction](./Code/WikiData_and_Categories_Extraction.ipynb): Contains the code used to extract the Wikidata ID of every species and Categories the fishes belong to.
- [Translation and Transliteration](./Code/Translation%20and%20Transliteration.ipynb): Translates and transliterates the master dataset.
- [Data Cleaning](./Code/Data%20Cleaning.ipynb): Cleans the master dataset. This code formats the original unstructured dataset into a more structured form and Helps to remove sentences from attributes that are too informal, casual, and directional.
- [Img and IUCN Ref Cleaning](./Code/Img%20and%20IUCN%20Ref%20Cleaning.ipynb): Removes the null values(if any). Cleans the Image and IUCN References columns of the master dataset.  


## Generating articles

- [template](./template.j2): it contains the template for the structure of the article.
- [genXML](./genXML.py): it contains the backbone structure for conversion to XML.
- [render](./render.py): it contains the code for generating XML dump of articles using the template and the dataset.
- [fishes50Dump](./fishes50Dump.xml): the testing XML dump file of first 50 fish and their attributes.


## Sample Article

Click [here](https://hi.wikipedia.org/wiki/%E0%A4%B8%E0%A4%A6%E0%A4%B8%E0%A5%8D%E0%A4%AF:Sanyamx/%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A4%AA%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A0) to view the sample article.

## Contributors
Sanyam Sharma sanyamxsharma@gmail.com <br>
Aastha Jaipura aasthajaipuria2000@gmail.com

