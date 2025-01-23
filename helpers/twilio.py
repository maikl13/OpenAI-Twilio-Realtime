import os
from fastapi.responses import Response
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

WEBSOCKET_URL = os.getenv("WEBSOCKET_URL")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")


def twilio_stream():
    response = f"""
    <Response> 
        <Connect>
            <Stream url="wss://{WEBSOCKET_URL}/stream/websocket" />
        </Connect>
    </Response>
    """
    return Response(content=response, media_type="application/xml")


def initiate_twilio_call(user_phone):
    """
    Initiates an outbound call using Twilio and connects it to the WebSocket URL.
    """
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    try:
        call = client.calls.create(
            to=user_phone,
            from_=TWILIO_PHONE_NUMBER,
            twiml=f"""
            <Response>
                <Connect>
                    <Stream url="wss://{WEBSOCKET_URL}/stream/websocket" />
                </Connect>
            </Response>
            """,
        )
        print(f"Call initiated successfully. Call SID: {call.sid}")
    except Exception as e:
        print(f"Error initiating call: {e}")
