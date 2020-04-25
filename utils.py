import dialogflow_v2 as dialogflow
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your dialogflow key here"
# above line refers to path to your key.
# 'GOOGLE_APPLICATION_CREDENTIALS' is a reserved key statement(case sensitive) and should not be changed!


dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "your dialogflow project id"  # special id from dialogflow config


def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(
        text=text_input)  # ignore pylint errors
    response = dialogflow_session_client.detect_intent(
        session=session, query_input=query_input)
    return response.query_result


def find_response(query, session_id):
    response = detect_intent_from_text(query, session_id)
    return response.fulfillment_text
