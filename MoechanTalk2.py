#!/usr/bin/env python3
import sys
import uuid
import dialogflow
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat

class MoechanTalk2:
    def __init__(self):
        self.project_id = 'asdfasdfasf-c0915'
        self.client_access_token = '1ccc42dfe9e64763b642d0bf6448b0dd'
        self.language_code = 'ja'
        self.session_client = dialogflow.SessionsClient()
        self.final_intent_name = 'see you'

        self.recognizer = aiy.cloudspeech.get_recognizer()
        aiy.audio.get_recorder().start()

        self.status_ui = aiy.voicehat.get_status_ui()

    def send_welcome_request(self, session):
        event_input = dialogflow.types.EventInput(name = 'WELCOME', language_code = self.language_code)
        query_input = dialogflow.types.QueryInput(event = event_input)
        return self.send_request(session, query_input)

    def send_text_request(self, session, text):
        text_input = dialogflow.types.TextInput(text = text, language_code = self.language_code)
        query_input = dialogflow.types.QueryInput(text = text_input)
        return self.send_request(session, query_input)

    def send_request(self, session, query_input):
        response = self.session_client.detect_intent(session = session, query_input = query_input)
        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}'.format(response.query_result.fulfillment_text))
        print('-' * 20)

        return response

    def main(self):
        session_id = uuid.uuid4().hex
        session = self.session_client.session_path(self.project_id, session_id)
        response = self.send_welcome_request(session)
        aiy.audio.say(response.query_result.fulfillment_text)

        while(True):
            self.status_ui.status('listening')
            text = self.recognizer.recognize()
            if not text:
                aiy.audio.say('Sorry, I did not hear you.')
                continue

            print('You said: %s' % text)
            response = self.send_text_request(session, text)
            aiy.audio.say(response.query_result.fulfillment_text)

            if response.query_result.intent.display_name == self.final_intent_name:
                break

if __name__ == '__main__':
    moechantalk2 = MoechanTalk2()
    moechantalk2.main()
    
