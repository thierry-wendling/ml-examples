# ML examples for natural language inference (NLI)
## Datasets
* [The Stanford Natural Language Inference (SNLI) Corpus](https://nlp.stanford.edu/projects/snli/)
    * Access: https://huggingface.co/datasets/snli
* [GLUE Benchmark](https://gluebenchmark.com/)
    * Access: https://huggingface.co/datasets/glue:
    * Relevant subsets:
        * MNLI
        * QNLI
        * RTE

## ToDo
0. Add gradient accumulation, lr schedule warmup, early stopping callback
1. Find Automated Short Answer Grading (ASAG) dataset
2. Finetune a MNLI-finetuned transformer on ASAG dataset
3. Try few-shot learning with TARS and compare
4. Try active learning using BaaL and compare
5. Try SetFit and compare

## References
### General
* [Semantics-aware BERT for Language Understanding](https://arxiv.org/pdf/1909.02209.pdf)
### Automated Short Answer Grading (ASAG)
* [Survey on Automated Short Answer Grading with Deep Learning: from Word Embeddings to Transformers](https://arxiv.org/pdf/2204.03503.pdf)
* [Investigating Transformers for Automatic Short Answer Grading](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7334688/pdf/978-3-030-52240-7_Chapter_8.pdf)
* [SemEval-2013 Task 7: The Joint Student Response Analysis and 8th Recognizing Textual Entailment Challenge](https://aclanthology.org/S13-2045.pdf)