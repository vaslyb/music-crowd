# MusicCrowd
## A Crowdsourced Multi-Domain Music Dataset of Europeana Collections

The dataset is part of the paper entitled [*Employing Crowdsourcing for Enriching a Music Knowledge Base in Higher Education*](https://scholar.google.com/citations?view_op=view_citation&hl=el&user=rr--MKoAAAAJ&citation_for_view=rr--MKoAAAAJ:9yKSN-GCB0IC) presented at the 4th International Conference on Artificial Intelligence in Education Technology.

This audio dataset was derived from Europeana collections and includes 854 music tracks annotated across three basic musical domains: *Genre*, *Emotion*, and *Instrument*. It is a valuable resource for Music Information Retrieval (MIR) tasks, such as music audio tagging.

# Guidance
The annotations for multi-class classification tasks can be found in files named **emotion.csv**, **genres.csv**, and **instruments.csv**.
 
In file **metadata.csv** there are the metadata of music tracks derived from Europeana.

In the folder **mfccs**, you can find the MFCCs (mel-frequency cepstral coefficients) for the 854 music tracks. These coefficients were calculated using the Librosa library by sampling at 22kHz with 40 coefficients, a window, and FFT size of 2048.

To download the audio files for the music tracks, run the **download-data.py** script.
# Acknowledgments

The work is co-funded by the Erasmus+ Program of the European Union, project number 2020-1-BE02-KA203-074727. We thank the students of the course “Knowledge Systems and Technologies” for their contributions to the crowdsourcing campaign and valuable feedback.
## Citation

If you use this dataset or find the paper's results useful, please consider citing the original paper.

```bibtex
@inproceedings{lyberatos2023employing,
  title={Employing Crowdsourcing for Enriching a Music Knowledge Base in Higher Education},
  author={Lyberatos, Vassilis and Kantarelis, Spyridon and Kaldeli, Eirini and Bekiaris, Spyros and Tzortzis, Panagiotis and Menis-Mastromichalakis, Orfeas and Stamou, Giorgos},
  booktitle={International Conference on Artificial Intelligence in Education Technology},
  pages={224--240},
  year={2023},
  organization={Springer}
}

}
