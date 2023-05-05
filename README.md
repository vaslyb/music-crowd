# MusicCrowd
## A Crowdsourced Multi-Domain Music Dataset of Europeana Collections

The dataset is part of the paper entitled *Employing Crowdsourcing for Enriching a Music Knowledge Base in Higher Education* accepted to be published on the 4th International Conference on Artificial Intelligence in Education Technology.

This audio dataset was derived from Europeana collections and includes 854 music tracks annotated across three basic musical domains: *Genre*, *Emotion*, and *Instrument*. It is a valuable resource for Music Information Retrieval (MIR) tasks, such as music audio tagging.

# Guidance
The annotations for multi-class classification tasks can be found in files named **emotion.csv**, **genres.csv**, and **instruments.csv**.
 
In file **metadata.csv** there are the metadata of music tracks derived from Europeana.

In the folder **mfccs**, you can find the MFCCs (mel-frequency cepstral coefficients) for the 854 music tracks. These coefficients were calculated using the Librosa library by sampling at 22kHz with 40 coefficients, a window, and FFT size of 2048.

To download the audio files for the music tracks, run the **download-data.py** script.
# Acknowledgments

The work is co-funded by the Erasmus+ Program of the European Union, project number 2020-1-BE02-KA203-074727. We thank the students of the course “Knowledge Systems and Technologies” for their contributions to the crowdsourcing campaign and valuable feedback.
