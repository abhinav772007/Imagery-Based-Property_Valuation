# Imagery-Based Property Valuation.

## Project Structure

```
Imagery-Based-Property_Valuation/
├── data/
│   ├── train.csv                    # Training dataset with property features
│   ├── test2.xlsx                   # Test dataset
│   ├── arcgis_images/              # Satellite images for training (16,209 images)
│   ├── test_arcgis_images/         # Satellite images for testing (5,404 images)
│   ├── image_embeddings/           # Pre-computed image embeddings for training
│   ├── test_image_embeddings/      # Pre-computed image embeddings for testing
│   └── cleaned_tabular1.csv         # Preprocessed tabular data
├── fetch.py                        # Script to download satellite images from ArcGIS
├── preprocessing.ipynb             # Data preprocessing and feature engineering
├── model.ipynb                     # Model training and evaluation
├── EDA.ipynb                       # Exploratory data analysis
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Installation

1. Clone the repository:
```bash
cd Imagery-Based-Property_Valuation
```

2. Install required libraries:
```bash
pip install -r requirements.txt
```

## Usage
### 1. Fetching Satellite Images

Run the `fetch.py` script to download satellite images for all properties:
```bash
python fetch.py
```

### 2. Data Preprocessing

Run the preprocessing notebook to clean and prepare the data:
```bash
jupyter notebook preprocessing.ipynb
```
**Note**: Image fetching may take considerable time depending on the dataset size. The script includes sleep intervals to respect API rate limits.

### 3. Model Training

Run the model notebook to train and evaluate models:
```bash
jupyter notebook model.ipynb
```

## Configuration

Key parameters in `fetch.py`:
- `SIZE`: Image size (default: 256x256)
- `BUFFER`: Coordinate buffer for bounding box (default: 0.0008)
- `SLEEP_TIME`: Delay between API requests (default: 0.25 seconds)
- `MAX_RETRIES`: Maximum retry attempts for failed downloads (default: 5)

## Workflow

1. **Data Collection**: Property data with coordinates
2. **Image Fetching**: Download satellite imagery using `fetch.py`
3. **Preprocessing**: Clean and engineer features in `preprocessing.ipynb`
4.**Embeddings Extraction**: Generate image embeddings using ResNet 
5. **Model Training**: Train models in `model.ipynb`
6. **Evaluation**: Assess model performance and generate predictions

## Notes

- The project uses ArcGIS World Imagery service, which is publicly available but subject to rate limits
- The date column is dropped during preprocessing as all sales occurred in 2014-2015
- Log transformation (`log1p`) is applied to prices for better model performance but,during evaulation it is converted to prices then caluculated RSME and R2 Scores.


