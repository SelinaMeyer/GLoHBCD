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

## Citation

A paper around this dataset and experiments has been accepted at LREC2022. The paper will be linked here and the reference will be updated once the proceedings are published. For now, when using the dataset please cite:


    @InProceedings{meyer-elsweiler:2022:LREC,
  author    = {Meyer, Selina  and  Elsweiler, David},
  title     = {GLoHBCD: A Naturalistic German Dataset for Language of Health Behaviour Change on Online Support Forums},
  booktitle      = {Proceedings of the Language Resources and Evaluation Conference},
  month          = {June},
  year           = {2022},
  address        = {Marseille, France},
  publisher      = {European Language Resources Association},
  pages     = {2226--2235},
  abstract  = {Health behaviour change is a difficult and prolonged process that requires sustained motivation and determination. Conversa- tional agents have shown promise in supporting the change process in the past. One therapy approach that facilitates change and has been used as a framework for conversational agents is motivational interviewing. However, existing implementations of this therapy approach lack the deep understanding of user utterances that is essential to the spirit of motivational interviewing. To address this lack of understanding, we introduce the GLoHBCD, a German dataset of naturalistic language around health behaviour change. Data was sourced from a popular German weight loss forum and annotated using theoretically grounded motivational interviewing categories. We describe the process of dataset construction and present evaluation results. Initial experiments suggest a potential for broad applicability of the data and the resulting classifiers across different behaviour change domains. We make code to replicate the dataset and experiments available on Github.},
  url       = {https://aclanthology.org/2022.lrec-1.239}
}

