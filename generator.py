from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "facebook/opt-1.3b"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",  # Auto-detect GPU/CPU
    torch_dtype=torch.float32,  # Avoid float16 issues
    offload_folder="./offload"  # Offload model to disk if needed
)

def generate_response(query):
    """Generates a response using OPT-1.3B."""
    print(f"\n🧠 Generating Response for: {query}")

    try:
        inputs = tokenizer(query, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
        output = model.generate(**inputs, max_new_tokens=150)

        response = tokenizer.decode(output[0], skip_special_tokens=True)
        print(f"✅ Generated Response: {response}")
        return response

    except Exception as e:
        print(f"❌ Error in Text Generation: {str(e)}")
        return "Error in generating response"
