// import { GoogleGenAI } from "@google/genai";

// API Base URL for your local Python backend
const API_BASE_URL = 'http://localhost:8000';

export const analyzePdfPage = async (base64Image: string, targetLanguage?: string): Promise<string> => {
  try {
    // Remove header prefix if present (e.g., "data:image/png;base64,")
    const cleanBase64 = base64Image.replace(/^data:image\/\w+;base64,/, "");

    const response = await fetch(`${API_BASE_URL}/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        image: cleanBase64,
        targetLanguage: targetLanguage
      })
    });

    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `Server error: ${response.status}`);
    }

    const data = await response.json();
    let text = data.html || "";
    
    // Clean up markdown code blocks if present (just in case the local model adds them)
    text = text.replace(/^```html\s*/i, '').replace(/```$/, '');
    
    if (!text.trim()) {
       return "<p><i>(AI trả về nội dung rỗng)</i></p>";
    }

    return text;
  } catch (error) {
    console.error("Local AI API Error:", error);
    return `<div class="text-red-500 font-bold">Lỗi kết nối Backend: ${error instanceof Error ? error.message : String(error)}</div>`;
  }
};