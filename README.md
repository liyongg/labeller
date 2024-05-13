# Labeller

An interface for labelling text data.
At the moment it requires `.csv` input and expects the column `text` to exist, of which the values are taken and displayed.

## Deployment

### Streamlit Cloud

This app is available on Streamlit Cloud on the domain of [labeller.streamlit.app](https://labeller.streamlit.app/).

### Local

You can run clone this repository and install the dependencies from the `requirements.txt` file.
Then run

```
streamlit run app.py
```

### Docker

There is a Docker image publicly available on Docker hub, registered as `panliyong/labeller`.
