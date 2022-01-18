This repository makes available code to replicate the **German Language of Health Behaviour Change Dataset (GLoHBCD)** and perform some Machine Learning experiments on the data. 

## How can I replicate the dataset?

You can find the webcrawler and the script to preprocess the data in the Crawler folder. To run the crawler you will need to install scrapy:

pip install scrapy

Then, after navigating to the Crawler-folder, execute:

scrapy crawl AbnehmenOhneOp -O abnehmenOhneOp.json
scrapy crawl PsychoTherapie -O psychoTherapie.json

you will get two json-files, which can be processed and mapped to corresponding annotations in the Preprocessing.ipynb. In addition to the complete dataset, the Preprocessing.ipynb also produces all files later needed for the machine learning experiments.

## What do the labels mean?

A description of the labels used for annotation can be found [here](Info/Annotation_scheme.png)

## Where do I find code for the experiments? 

In the Experiments folder! To execute, you will need the files produced in Preprocessing.ipynb.
There are three scripts, one for each annotation level (Label, Sublabel and Valence). They all do roughly the same but take different data-files.