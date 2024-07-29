from fastapi import APIRouter, Request, HTTPException
from llama_cpp import Llama

router = APIRouter()

model = None

@router.post("/llama")
async def generate_response(request: Request):

    global model

    try:
        data = await request.json()

        # Check if the required fields are present in the JSON data
        if 'system_message' in data and 'user_message' in data and 'max_tokens' in data:
            system_message = data['system_message']
            user_message = data['user_message']
            max_tokens = int(data['max_tokens'])

            # Prompt creation
            prompt = f"""<s>[INST] <<SYS>>
            {system_message}
            <</SYS>>
            {user_message} [/INST]"""

            # Create the model if it was not previously created
            if model is None:
                model_path = "/models/llama-2-7b-chat.Q2_K.gguf"
                model = Llama(model_path=model_path)

            # Run the model
            output = model(prompt, max_tokens=max_tokens, echo=True)

            return output

        else:
            raise HTTPException(status_code=400, detail="Missing required parameters")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
