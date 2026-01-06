# How to Use Google Google Gemini API

This project uses Google's **Gemini** models to perform Optical Character Recognition (OCR) and translation.

## 1. Get Your API Key
To use the app, you need a free API key from Google AI Studio.

1.  Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  Click **"Create API key"**.
3.  Copy the key string (it starts with `AIza...`).

## 2. Configure the App
You need to tell the application your API key.

1.  Create a file named `.env` in the root of the project (next to `package.json`).
2.  Add the following line to the file:
    ```
    VITE_GEMINI_API_KEY=AIzaSyYourKeyHere...
    ```
    *(Replace `AIzaSyYourKeyHere...` with your actual key)*

## 3. Run the App
Now you can run the application normally:

```bash
npm run dev
```

## Troubleshooting
*   **Quota Exceeded:** The free tier has limits (Requests Per Minute). If you hit errors, try waiting a minute.
*   **"Missing API Key":** Ensure you named the variable `VITE_GEMINI_API_KEY` in the `.env` file and restarted the dev server (`Ctrl+C` then `npm run dev`) after creating the file.
