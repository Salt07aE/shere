import dialogflow
import uuid

class Dialogflow():
    def __init__(self, text):
        self.project_id = 'navi-qhjqut'
        self.client_access_token = '8c389a0b5f144038a199d91aff32b69e'
        self.language_code = 'ja'
        self.session_client = dialogflow.SessionsClient()
        self.final_intent_name = 'SeeYou'
        self.text = text

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
        #print('Query text: {}'.format(response.query_result.query_text))
        #print('Detected intent: {} (confidence: {})'.format(
        #    response.query_result.intent.display_name,
        #    response.query_result.intent_detection_confidence))
        #print('Fulfillment text: {}'.format(response.query_result.fulfillment_text))
        #print('-' * 20)
        return response

    def main(self):
        flag = 0
        session_id = uuid.uuid4().hex
        session = self.session_client.session_path(self.project_id, session_id)
        response = self.send_text_request(session, self.text)
        res_text = format(response.query_result.fulfillment_text)

        if response.query_result.intent.display_name == self.final_intent_name:
            flag = 1
        
        return (res_text, flag)

