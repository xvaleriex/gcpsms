# gcpsms
Google Cloud Function written in Python that sends SMS notification via Twilio on http trigger.

### Prerequisites

- Google Cloud Project
- [Python dev enviroment set up](https://cloud.google.com/python/setup)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/)
- Twillio account with phone number generated

### Function

A function that will accept POST request with a timestamp and will send SMS notification with this timestamp.
