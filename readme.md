# OpenAI-Twilio-Realtime

This project integrates OpenAI's language model with Twilio's real-time messaging API using FastAPI.

## Features

- Real-time messaging with Twilio
- Integration with OpenAI's language model
- Easy to set up and use

## Requirements

- Python 3.7+
- Twilio account
- OpenAI API key

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/anil-unni/OpenAI-Twilio-Realtime.git
    ```
2. Navigate to the project directory:
    ```bash
    cd OpenAI-Twilio-Realtime
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the root directory and add your Twilio and OpenAI credentials:
    ```env
    VOICE='echo'
    WEBSOCKET_URL=''
    PORT=5000
    TWILIO_ACCOUNT_SID=''
    TWILIO_AUTH_TOKEN=''
    OPENAI_API_KEY=''
    ```

2. Setting up Twilio:
    - Create a Twilio Phone Number:
        - Log into your Twilio account.
        - Navigate to Phone Numbers from the console dashboard.
        - Click on Buy a Number and choose a number with voice capabilities.
        - Once purchased, configure this number to route incoming calls to your application.
    - Modify the Webhook Endpoint:
        - Go to the Phone Numbers section in your Twilio console.
        - Select the number you just purchased.
        - Scroll down to the Voice & Fax section.
        - In the A Call Comes In field, set the Webhook URL to the endpoint that connects to your service. For example: `https://your-domain.com/stream/incoming-call`
        - This URL should point to your FastAPI application, specifically the `/stream/incoming-call` route that will handle the incoming Twilio calls.

3. Set up the WEBSOCKET_URL:
    - In your `.env` file, define the `WEBSOCKET_URL`. This is the URL where Twilio will establish a WebSocket connection to stream the voice call to your service.
    - Example: `WEBSOCKET_URL=your-domain.com`
    - Make sure this URL is publicly accessible.

## Usage

1. Start the application:
    ```bash
    python app.py
    ```

## Working Flow

We initiate a phone call using an API, and once the call starts, Twilio triggers a webhook on our backend. The webhook processes the audio stream from the call and sends it to the OpenAI API in real-time. OpenAI responds with a stream, which we pass back to Twilio.

This setup uses the `gpt-4o-realtime-preview-2024-10-01` model with `"OpenAI-Beta": "realtime=v1"`, enabling real-time streaming for seamless interaction during the call.
