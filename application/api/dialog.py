from flask import request, jsonify, g
import os
from ..api import api
from ..models.users import User
from ..utils.auth import generate_token, requires_auth, verify_token
import requests
import json
import pusher
import dialogflow



print("pre data /././././. ")
print(os.getenv('DIALOGFLOW_PROJECT_ID'))


project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
pusher_client = pusher.Pusher(
    app_id=os.getenv('PUSHER_APP_ID'),
    key=os.getenv('PUSHER_KEY'),
    secret=os.getenv('PUSHER_SECRET'),
    cluster=os.getenv('PUSHER_CLUSTER'),
    ssl=True)


@api.route('/dialog', methods=['POST'])
def bot():
    input_text = request.form["message"]
    if input_text:
        flow_response = detect_intent_texts(
            project_id, "unique", input_text, 'en')
        pusher_client.trigger('chat_bot', 'new_message',
                            {'query': input_text, 'diaglog_message': flow_response})        
        return flow_response


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        return response.query_result.fulfillment_text


# @api.route('/send_message', methods=['POST'])
# def send_message():
#     socketId = request.form['socketId']
#     message = request.form['message']
#     project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
#     fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
#     response_text = {"message":  fulfillment_text}

#     pusher_client.trigger('chat_bot', 'new_message',
#                           {'human_message': message, 'bot_message': fulfillment_text})

#     return jsonify(response_text)
