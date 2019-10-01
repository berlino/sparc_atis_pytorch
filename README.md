# CD-Seq2Seq for SParC 


### Dependency

The model is tested in python 3.6 and pytorch 1.0. We recommend using `conda` and `pip`:

```
conda create -n cdseq2seq python=3.6
source activate cdseq2seq
pip install -r requirements.txt
```

The evaluation scripts use python 2.7, so make sure ``python2.7" is also runnable in your terminal

### Original Database Download

First, download the original SParC from [here](https://yale-lily.github.io/sparc), and put the database files from the downloaded file to the data directory, like  ``data/database". We will need this for evaluation.

Also, download ``glove.840B.300d.txt" from this [site](https://nlp.stanford.edu/projects/glove/), specify its path in run_sparc_cdseq2seq.sh.

### Test Sparc

The model checkpoint is already in the dir `logs_sparc_cdseq2seq/save_23', 
Run the following command to generate the predictions on the validation set. 

- `run_sparc_cdseq2seq.sh` to run the decoding with the trained system
