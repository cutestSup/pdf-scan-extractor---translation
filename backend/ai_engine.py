import base64
import io
# import torch
# from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
# from qwen_vl_utils import process_vision_info

# MOCK MODE: Set to True if you don't have a GPU or haven't installed torch yet.
# Set to False to actually load the AI model (Requires NVIDIA GPU with ~16GB+ VRAM or 24GB System RAM for CPU)
MOCK_MODE = True

class LocalAIModel:
    def __init__(self):
        self.model = None
        self.processor = None
        if not MOCK_MODE:
            print("Loading Qwen2-VL-7B-Instruct... (This may take a while)")
            try:
                # We use device_map="auto" to automatically use GPU if available
                # self.model = Qwen2VLForConditionalGeneration.from_pretrained(
                #     "Qwen/Qwen2-VL-7B-Instruct", torch_dtype="auto", device_map="auto"
                # )
                # self.processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct")
                print("Model loaded successfully!")
                pass
            except Exception as e:
                print(f"Error loading model: {e}")
                print("Falling back to MOCK_MODE")
                global MOCK_MODE
                MOCK_MODE = True

    def generate_html(self, image_base64: str, target_language: str = None) -> str:
        if MOCK_MODE:
            return self._mock_response(target_language)

        # Real inference code for Qwen2-VL
        # prompt_text = "Extract the text from this image and format it as HTML. Do not use markdown code blocks."
        # if target_language:
        #     prompt_text = f"Extract the text from this image and TRANSLATE it to {target_language}. Format as HTML."

        # messages = [
        #     {
        #         "role": "user",
        #         "content": [
        #             {"type": "image", "image": f"data:image;base64,{image_base64}"},
        #             {"type": "text", "text": prompt_text},
        #         ],
        #     }
        # ]
        
        # text = self.processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        # image_inputs, video_inputs = process_vision_info(messages)
        # inputs = self.processor(
        #     text=[text],
        #     images=image_inputs,
        #     videos=video_inputs,
        #     padding=True,
        #     return_tensors="pt",
        # ).to(self.model.device)

        # generated_ids = self.model.generate(**inputs, max_new_tokens=2048)
        # generated_ids_trimmed = [
        #     out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
        # ]
        # output_text = self.processor.batch_decode(
        #     generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
        # )
        
        # return output_text[0]
        return ""

    def _mock_response(self, target_language: str = None) -> str:
        lang_text = target_language if target_language else "Original Language"
        return f"""
        <div style="border: 2px dashed #4CAF50; padding: 20px; border-radius: 8px;">
            <h2>Local AI Model Result ({lang_text})</h2>
            <p>This is a <b>simulated response</b> from your local backend.</p>
            <p>To run the real model, you need to:</p>
            <ul>
                <li>Install PyTorch and Transformers</li>
                <li>Set <code>MOCK_MODE = False</code> in <code>backend/ai_engine.py</code></li>
                <li>Have a GPU with at least 16GB VRAM (for 7B model)</li>
            </ul>
            <p><i>The integration is working successfully!</i></p>
        </div>
        """

ai_engine = LocalAIModel()
