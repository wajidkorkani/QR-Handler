# QR-Handler

QR Handler is a web application built in Django that allows users to generate and scan QR codes. It provides a user-friendly interface for managing QR code-related tasks.

## Features

- **Generate QR Codes**: Create QR codes for various data inputs using the `generateQRCode.html` template.
- **Scan QR Codes**: Upload an image containing a QR code to decode its content via the `scan.html` template.
- **Live Scan**: Use your device's camera to scan QR codes in real-time. This feature is implemented in the `liveScan.html` template.
- **Media Management**: Store and manage QR code images in the `media/qr/` directory.
- **Static Assets**: Includes pre-designed templates and static files for a seamless user experience.

## Live Scan

The **Live Scan** feature allows users to scan QR codes in real-time using their device's camera. It utilizes OpenCV to capture frames from the camera and decode QR codes. The decoded data is displayed on the `liveScan.html` page.

### How It Works:
1. The camera is accessed using OpenCV.
2. Frames are captured and displayed in a window.
3. The application attempts to decode QR codes from the captured frames.
4. The decoded data is displayed on the web interface.

### Notes:
- Ensure your device has a functional camera.
- The feature automatically stops after 10 seconds or when the user presses the 'q' key.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/wajidkorkani/QR-Handler.git