

from anthropic import AnthropicVertex
 
 
PROJECT_ID = "prj-mlops-poc-81cl"  
LOCATION = "europe-west1"
 
class CreateAnthropic:
   
   def __init__(self) -> None:
     self.client = AnthropicVertex(region=LOCATION, project_id=PROJECT_ID)
 
   def create_model(self) -> None:
        message = self.client.messages.create(
                  max_tokens=1024,
                  messages=[
                      {
                      "role": "user",
                      "content": "Send me a recipe for banana bread.",
                      }
                  ],
                  model="claude-3-5-sonnet@20240620"
        )
        print(message.model_dump_json(indent=2))


if __name__ == "__main__":
    print("Creating anthropic.")
    vertex = CreateAnthropic()
    vertex.create_model()
