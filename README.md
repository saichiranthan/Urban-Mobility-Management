# Team08 - Urban Mobility Management

## Introduction
Team08's Urban Mobility Management project focuses on implementing various models and techniques to manage urban mobility effectively. This project includes regression models for predicting traffic flow, vehicle detection for real-time traffic analysis, and integration of different models for comprehensive urban mobility management.

## Requirements
To run this project, you need to have the following libraries installed:

- scikit-learn (`sklearn`)
- Matplotlib
- NumPy
- Pandas
- Seaborn
- itertools
- Folium
- Math
- Random
- TensorFlow
- OpenCV-Python (`opencv-python`) (version 4.1.2 or higher)
- Pillow (version 8.0.0 or higher)
- PyYAML (version 5.3.1 or higher)
- SciPy (version 1.4.1 or higher)
- PyTorch (version 1.7.0 or higher)
- torchvision (version 0.8.1 or higher)
- tqdm (version 4.41.0 or higher)
- TensorBoard (version 2.4.1 or higher)

## Usage
1. Clone this repository.
2. Navigate to the directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the main file `Astar.py` for integration of models.
5. If you are retraining the models, make sure to change the path of datasets used accordingly in all the files.

## Datasets
- The `Datasets` folder contains datasets used for regression models.
- The image/video dataset for vehicle detection is located in the `vehicle detection` folder.

## Notes
- Random functions are used to simulate densities in junctions for simplicity, as real-time traffic cams cannot be accessed.
- For in-depth understanding of vehicle detection, refer to [Vehicle Detection GitHub Repository](https://github.com/MaryamBoneh/Vehicle-Detection).

## Contributors
- [Sai Chiranthan H M, Abhishek B, Arushi Biswas, Deshmukh]

## License
[License information]
