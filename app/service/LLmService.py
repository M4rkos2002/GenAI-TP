from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage
import json
import requests
from app.utils.commons.record.LLmMessage import LLmMessage
from app.utils.commons.record.LLmParams import LLmParams

class LLmService:
    def __init__(self, api_key):
        self.__api_key = api_key

    def send_request(self, model: str, llm_messages: list[LLmMessage], params: LLmParams) -> BaseMessage:
        messages = self.__get_messages(llm_messages)
        model = self.__get_model(model, self.__api_key)
        return self.__invoke_model(model, messages, params)

    def send_vision_completion(self, model: str, base64_file_content: str, prompt: str) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.__api_key}"
        }
        payload = {
            "model": f"{model}",
            "messages": [
                {
                    "role": "user",
                    "content":[
                        {
                            "type": "text",
                            "text": f"{prompt}"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_file_content}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 4096,
            "temperature": 0.2,
            "top_p": 1.0,
        }

        response = requests.post(
                url="https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload,
            )

        data = json.loads(response.text)
        return data.get("choices")[0].get("message").get("content")


    def __get_messages(self, llm_messages: list[LLmMessage]):
        return list(map(lambda msg: self.__create_message(msg.role, msg.message), llm_messages))

    def __create_message(self, role, message):
        match role:
            case "human":
                return HumanMessage(content=message)
            case "system":
                return SystemMessage(content=message)
            case _ :
                return "error"

    def __get_model(self, name, key) -> ChatOpenAI:
        return ChatOpenAI(
            model=name,
            openai_api_key=key,
        )

    def __invoke_model(self, model: ChatOpenAI, messages, params: LLmParams) -> BaseMessage:
        return model.invoke(
            messages,
            temperature=params.temperature,
            max_tokens=params.max_tokens,
            top_p=params.top_p,
            presence_penalty=params.presence_penalty,
            stop=params.stop,
        )

