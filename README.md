# 🎙️ Deepfake Detector

A machine learning-based application for detecting deepfakes in audio and video files. This project uses pre-trained ML models to analyze media content and determine whether it contains authentic or artificially generated content.

## 📋 Features

- **Audio Deepfake Detection**: Analyze audio files to detect synthetic or manipulated voice content
- **Video Deepfake Detection Framework**: Foundation in place for video detection implementation
- **Graphical User Interface**: User-friendly GUI built with Tkinter for easy interaction
- **Real-time Processing**: Get instant predictions with confidence scores
- **Progress Tracking**: Visual progress bar and detailed processing logs
- **Multiple Format Support**: Handle `.wav` and `.mp3` audio files; `.mp4`, `.avi`, and `.mov` video files
- **Confidence Metrics**: View detection confidence for both fake and real classifications

## 🛠️ Technologies Used

- **Python 3**: Core programming language
- **Tkinter**: GUI framework for desktop interface
- **Scikit-learn**: Machine learning model support
- **Librosa**: Audio processing and feature extraction
- **NumPy**: Numerical computing
- **OpenCV** (planned): Video frame extraction and processing

## 📁 Project Structure

```
Deepfake_Detector/
├── main.py                 # Main GUI application
├── audio_detector.py       # Audio deepfake detection logic
├── video_detector.py       # Video deepfake detection logic (in development)
├── voice_model.pkl         # Pre-trained voice detection model
├── voice_scaler.pkl        # Feature scaler for voice features
├── LICENSE                 # MIT License
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/i-hmzakhan/Deepfake_Detector.git
cd Deepfake_Detector
```

2. Install required dependencies:
```bash
pip install tkinter librosa scikit-learn numpy opencv-python
```

Note: Tkinter usually comes pre-installed with Python. If not, install it using your system's package manager:
- **Ubuntu/Debian**: `sudo apt-get install python3-tk`
- **macOS**: `brew install python-tk`
- **Windows**: Already included with Python

### Usage

Run the application:
```bash
python main.py
```

#### Audio Detection

**Steps to detect audio deepfakes:**

1. Launch the application
2. Click **"🎙️ Detect Audio Deepfake"** button
3. Select an audio file (`.wav` or `.mp3` format)
4. Wait for the analysis to complete
5. View the result and confidence scores in the application window

#### Video Detection

Video deepfake detection feature is currently under development. The framework is in place and will be enabled soon.

## 📊 How It Works

### Audio Detection Pipeline

1. **Audio Loading**: Loads the audio file using Librosa
2. **Feature Extraction**: Extracts MFCC (Mel-Frequency Cepstral Coefficients) features
3. **Feature Scaling**: Normalizes features using pre-trained scaler
4. **Model Prediction**: Uses the trained ML model to classify audio
5. **Confidence Scoring**: Provides probability scores for both fake and real classifications

### Video Detection Pipeline (In Development)

1. **Frame Extraction**: Extracts frames from video using OpenCV
2. **Face Detection**: Identifies and isolates faces in frames
3. **Feature Analysis**: Analyzes facial and visual artifacts
4. **Model Prediction**: Classifies video as deepfake or authentic
5. **Report Generation**: Provides overall classification with per-frame analysis

### Model Details

- **Audio Model Type**: Classification model trained on audio deepfake datasets
- **Audio Input Features**: 26 MFCC coefficients
- **Output**: Binary classification (Real/Fake) with confidence scores
- **Video Model**: To be implemented

## 🎯 Current Status

- ✅ Audio deepfake detection - Fully implemented
- 🚧 Video deepfake detection - Framework in place, implementation in progress
- 🚧 GUI integration for video - Ready for activation once video detection is complete

## 🔮 Future Enhancements

- [x] Audio deepfake detection
- [ ] Complete video deepfake detection implementation
- [ ] Enable video detection in GUI
- [ ] Multi-file batch processing
- [ ] Model fine-tuning and accuracy improvements
- [ ] Support for additional audio/video formats
- [ ] Export detection reports (PDF/CSV)
- [ ] Real-time stream processing
- [ ] Performance optimization
- [ ] Model comparison and ensemble methods

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📝 Topics

- AI & Machine Learning
- Voice Recognition
- Deepfake Detection
- Video Analysis
- Audio Processing

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report issues
- Suggest improvements
- Submit pull requests
- Help implement video detection

## 📧 Contact

For questions or inquiries about this project, please open an issue on the GitHub repository.

---

**Disclaimer**: This tool is designed for research and educational purposes. Always ensure you have proper authorization before analyzing audio or video files. Use responsibly and ethically.
