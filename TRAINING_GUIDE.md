# How to Build & Train Your Own Document AI

This guide explains how to replace generic API models with your own specialized "Document-to-HTML" model.

## 1. Choose Your Base Model
For document layout analysis and OCR, **Vision-Language Models (VLMs)** are superior to standard LLMs.

*   **Best Overall:** [Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct)
    *   *Why:* Handles any image resolution, understands tables extremely well, and supports multiple languages.
*   **Best for Speed:** [GOT-OCR2.0](https://huggingface.co/stepfun-ai/GOT-OCR2_0)
    *   *Why:* Specialized solely for OCR formatting. Faster usage, but less "intelligent" reasoning.

## 2. The Secret Sauce: "Synthetic Distillation" Data
You can't just scrape PDFs and expect the model to learn. You need **Image -> Perfect HTML** pairs.
Since manual labeling is too slow, we use a smarter model (like Gemini Pro or GPT-4o) to *teach* your smaller local model.

### Workflow:
1.  **Collect Data:** Gather 50-100 of your representative PDFs (invoices, contracts, etc.).
2.  **Generate Ground Truth (The Teacher):**
    *   Write a script that sends these PDF images to **Gemini 1.5 Pro**.
    *   Prompt: *"Transcribe this image to clean semantic HTML. Use `<table>` for tables. Do not summarize."*
    *   Save the response as a `.json` file: `{"image": "path/to/img.png", "ground_truth": "<html>...</html>"}`.
    *   *Verify:* Manually check a few to ensure Gemini didn't hallucinate.
3.  **Create Dataset:** Format this data for training. The standard format is similar to LLaVA or standard Instruction Tuning formats.

## 3. Fine-Tuning (The Training)
We will use **Unsloth** because it makes fine-tuning 2x faster and uses 70% less memory. You can run this on Google Colab (Free Tier) or a local gaming GPU.

### Steps using Unsloth:
1.  **Install Unsloth:**
    ```python
    pip install unsloth
    ```
2.  **Load Model:**
    Load `unsloth/Qwen2-VL-7B-Instruct-bnb-4bit` (4-bit quantization allows it to run on smaller GPUs).
3.  **Train:**
    *   Feed your "Image + HTML" pairs into the trainer.
    *   Use LoRA (Low-Rank Adaptation) to update only 1-5% of the weights.
    *   Train for 1-3 epochs (usually takes < 1 hour for small datasets).
4.  **Export:**
    Save the adapter as GGUF (for llama.cpp) or standard Safetensors.

## 4. Running It (The Backend)
The code in `backend/ai_engine.py` is ready for this.
Once you have your fine-tuned model path, update the loading section:

```python
self.model = Qwen2VLForConditionalGeneration.from_pretrained(
    "path/to/your/fine-tuned-model", ...
)
```

## Summary Checklist
- [ ] Set up Python Backend (Done)
- [ ] Collect 50 representative PDF pages
- [ ] Process them with Gemini/GPT-4 to get "Perfect HTML" labels
- [ ] Fine-tune Qwen2-VL using Unsloth
- [ ] Deploy the new weights to your `backend/` folder
