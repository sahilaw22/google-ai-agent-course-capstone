"""FastAPI server for Academate chatbot - deployable to Vercel/Netlify."""

import os
import sys
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel

# Add parent directory for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from chatbot.runtime import build_agent_bundle
from chatbot.tools import get_all_tools
from chatbot.memory import SESSION_MEMORY
from chatbot.observability import get_logger

logger = get_logger()

# Global agent and runner
agent = None
runner = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize agent on startup."""
    global agent, runner
    
    # Check for API key
    if not os.getenv("GOOGLE_API_KEY"):
        logger.error("GOOGLE_API_KEY not found in environment")
        raise RuntimeError("GOOGLE_API_KEY environment variable is required")
    
    # Build agent and runner
    tools = get_all_tools()
    agent, runner = build_agent_bundle(tools=tools)
    logger.info(f"Agent initialized with {len(tools)} tools")
    
    yield
    
    # Cleanup (if needed)
    logger.info("Shutting down")


# Create FastAPI app
app = FastAPI(
    title="Academate API",
    description="Intelligent College AI Assistant",
    version="1.0.0",
    lifespan=lifespan
)


class ChatRequest(BaseModel):
    """Request model for chat endpoint."""
    message: str
    session_id: Optional[str] = "default"


class ChatResponse(BaseModel):
    """Response model for chat endpoint."""
    response: str
    session_id: str


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main web UI."""
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Academate - College AI Assistant</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            max-width: 800px;
            width: 100%;
            height: 90vh;
            max-height: 700px;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px 30px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 28px;
            margin-bottom: 5px;
        }
        
        .header p {
            font-size: 14px;
            opacity: 0.9;
        }
        
        .chat-messages {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            background: #f5f5f5;
        }
        
        .message {
            margin-bottom: 15px;
            display: flex;
            animation: fadeIn 0.3s ease-in;
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .message.user {
            justify-content: flex-end;
        }
        
        .message-bubble {
            max-width: 70%;
            padding: 12px 18px;
            border-radius: 18px;
            word-wrap: break-word;
            white-space: pre-wrap;
        }
        
        .message.user .message-bubble {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-bottom-right-radius: 4px;
        }
        
        .message.assistant .message-bubble {
            background: white;
            color: #333;
            border: 1px solid #e0e0e0;
            border-bottom-left-radius: 4px;
        }
        
        .input-area {
            padding: 20px;
            background: white;
            border-top: 1px solid #e0e0e0;
        }
        
        .input-container {
            display: flex;
            gap: 10px;
        }
        
        #message-input {
            flex: 1;
            padding: 12px 18px;
            border: 2px solid #e0e0e0;
            border-radius: 25px;
            font-size: 14px;
            outline: none;
            transition: border-color 0.3s;
        }
        
        #message-input:focus {
            border-color: #667eea;
        }
        
        #send-button {
            padding: 12px 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        #send-button:hover:not(:disabled) {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        #send-button:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }
        
        .loading {
            display: none;
            text-align: center;
            padding: 10px;
            color: #667eea;
        }
        
        .loading.active {
            display: block;
        }
        
        .welcome-message {
            text-align: center;
            color: #666;
            padding: 40px 20px;
        }
        
        .welcome-message h2 {
            color: #667eea;
            margin-bottom: 15px;
        }
        
        .welcome-message ul {
            list-style: none;
            margin-top: 20px;
        }
        
        .welcome-message li {
            padding: 8px 0;
            color: #555;
        }
        
        .welcome-message li:before {
            content: "💡 ";
            margin-right: 5px;
        }
        
        .error-message {
            background: #fee;
            color: #c33;
            padding: 10px;
            border-radius: 8px;
            margin: 10px 20px;
            display: none;
        }
        
        .error-message.active {
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎓 ACADEMATE</h1>
            <p>Your Intelligent College Assistant</p>
        </div>
        
        <div id="error-container" class="error-message"></div>
        
        <div class="chat-messages" id="chat-messages">
            <div class="welcome-message">
                <h2>Welcome to Academate!</h2>
                <p>I can help you with:</p>
                <ul>
                    <li>Exam schedules and timetables</li>
                    <li>Previous year question papers</li>
                    <li>Faculty information</li>
                    <li>Academic calendar and events</li>
                    <li>Student results and performance</li>
                </ul>
                <p style="margin-top: 20px; font-style: italic;">Ask me anything about college!</p>
            </div>
        </div>
        
        <div class="loading" id="loading">
            <span>Academate is thinking...</span>
        </div>
        
        <div class="input-area">
            <div class="input-container">
                <input 
                    type="text" 
                    id="message-input" 
                    placeholder="Ask about exams, timetables, faculty, or events..."
                    autocomplete="off"
                />
                <button id="send-button">Send</button>
            </div>
        </div>
    </div>
    
    <script>
        const chatMessages = document.getElementById('chat-messages');
        const messageInput = document.getElementById('message-input');
        const sendButton = document.getElementById('send-button');
        const loadingIndicator = document.getElementById('loading');
        const errorContainer = document.getElementById('error-container');
        const sessionId = 'web-' + Math.random().toString(36).substring(7);
        
        // Remove welcome message on first interaction
        let firstMessage = true;
        
        function addMessage(content, isUser) {
            if (firstMessage) {
                chatMessages.innerHTML = '';
                firstMessage = false;
            }
            
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user' : 'assistant'}`;
            
            const bubbleDiv = document.createElement('div');
            bubbleDiv.className = 'message-bubble';
            bubbleDiv.textContent = content;
            
            messageDiv.appendChild(bubbleDiv);
            chatMessages.appendChild(messageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        function showError(message) {
            errorContainer.textContent = message;
            errorContainer.classList.add('active');
            setTimeout(() => {
                errorContainer.classList.remove('active');
            }, 5000);
        }
        
        async function sendMessage() {
            const message = messageInput.value.trim();
            if (!message) return;
            
            // Add user message to chat
            addMessage(message, true);
            messageInput.value = '';
            
            // Disable input while processing
            sendButton.disabled = true;
            messageInput.disabled = true;
            loadingIndicator.classList.add('active');
            
            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        message: message,
                        session_id: sessionId
                    })
                });
                
                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.detail || 'Failed to get response');
                }
                
                const data = await response.json();
                addMessage(data.response, false);
                
            } catch (error) {
                console.error('Error:', error);
                showError('Sorry, I encountered an error. Please try again.');
                addMessage('Sorry, I encountered an error. Please try again.', false);
            } finally {
                sendButton.disabled = false;
                messageInput.disabled = false;
                loadingIndicator.classList.remove('active');
                messageInput.focus();
            }
        }
        
        sendButton.addEventListener('click', sendMessage);
        
        messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });
        
        // Focus input on load
        messageInput.focus();
    </script>
</body>
</html>
    """
    return HTMLResponse(content=html_content)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return JSONResponse({
        "status": "healthy",
        "agent": "ready" if agent else "not_initialized"
    })


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Chat endpoint for the AI assistant."""
    if not runner:
        raise HTTPException(status_code=503, detail="Agent not initialized")
    
    try:
        # Store user message in memory
        SESSION_MEMORY.append(request.session_id, "user", request.message)
        logger.info("User message received", extra={
            "session": request.session_id,
            "message": request.message
        })
        
        # Get response from agent
        # Collect streaming response
        response_text = ""
        async for chunk in runner.run(request.message):
            if hasattr(chunk, 'text'):
                response_text += chunk.text
            elif isinstance(chunk, str):
                response_text += chunk
        
        # Store assistant response in memory
        SESSION_MEMORY.append(request.session_id, "assistant", response_text)
        logger.info("Assistant response generated", extra={
            "session": request.session_id,
            "response_length": len(response_text)
        })
        
        return ChatResponse(
            response=response_text or "I'm sorry, I couldn't generate a response.",
            session_id=request.session_id
        )
        
    except Exception as e:
        logger.exception("Error processing chat request", extra={
            "session": request.session_id,
            "error": str(e)
        })
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")


@app.get("/api/session/{session_id}/history")
async def get_session_history(session_id: str):
    """Get chat history for a session."""
    history = SESSION_MEMORY.get(session_id)
    return JSONResponse({"session_id": session_id, "history": history})


# For Vercel serverless deployment
# Vercel will look for an 'app' object
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
