# Web Interface Guide

## Overview

The Academate web interface provides a modern, responsive chat experience for interacting with the AI assistant.

## Interface Components

### 1. Header Section
- **Title**: "🎓 ACADEMATE"
- **Subtitle**: "Your Intelligent College Assistant"
- **Color Scheme**: Purple gradient (professional and modern)

### 2. Chat Area
- **Welcome Message**: Displays on first load with:
  - Introduction to Academate
  - List of available features
  - Example queries

- **Message Bubbles**:
  - **User messages**: Right-aligned, purple gradient background, white text
  - **AI responses**: Left-aligned, white background, dark text
  - **Animation**: Smooth fade-in for new messages

### 3. Input Area
- **Text Input**: Rounded input field with placeholder text
- **Send Button**: Purple gradient button that animates on hover
- **Loading Indicator**: Shows "Academate is thinking..." during processing

### 4. Error Handling
- Red error banner appears at top when issues occur
- Auto-dismisses after 5 seconds
- User-friendly error messages

## Features

### Responsive Design
- **Desktop**: Full-width layout with maximum 800px width
- **Tablet**: Adapts to smaller screens
- **Mobile**: Touch-friendly interface, vertical layout

### User Experience
- **Auto-scroll**: Chat automatically scrolls to show latest messages
- **Keyboard Shortcuts**: Press Enter to send message
- **Focus Management**: Input field automatically focused for typing
- **Session Persistence**: Each browser maintains its own conversation

### Accessibility
- Clean, readable fonts (Segoe UI)
- High contrast text
- Clear visual hierarchy
- Keyboard navigation support

## Using the Interface

### Starting a Conversation

1. **First Visit**:
   - You'll see the welcome message
   - Review the list of available features
   - Type your first question

2. **Asking Questions**:
   ```
   Example: "When is my next exam?"
   Example: "Show me the Computer Science timetable"
   Example: "Who teaches Data Structures?"
   ```

3. **Getting Responses**:
   - Your message appears on the right (purple)
   - Loading indicator shows while processing
   - AI response appears on the left (white)

### Sample Conversation Flow

```
You: Hello!

Academate: Hello! I'm Academate, your college assistant. I can help you with:
• Exam schedules and timetables
• Previous year question papers
• Faculty information
• Academic calendar and events
• Student results and performance

What would you like to know?

You: When are the semester 3 exams for Computer Science?

Academate: **Exam Schedule – Computer Science – Semester 3**
Academic Year: 2024-25

📝 Data Structures (CS301)
   Date: 15 January 2025
   Time: 10:00 AM
   Duration: 180 minutes
   Room: Room 101
   Type: Theory
   Total Marks: 100

[... more exams ...]
```

## Customization

The interface can be customized by editing `/api/server.py`:

### Change Colors
Look for the CSS section in the HTML and modify:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Change Welcome Message
Find the welcome-message section and edit:
```html
<div class="welcome-message">
    <h2>Welcome to Academate!</h2>
    <!-- Customize this section -->
</div>
```

### Add New Features
The interface communicates with the backend via `/api/chat` endpoint.
You can extend functionality by:
1. Adding new endpoints in `server.py`
2. Adding new UI buttons/features in the HTML
3. Connecting them via JavaScript fetch calls

## API Endpoints

The web interface uses these endpoints:

### GET /
Returns the HTML chat interface

### POST /api/chat
Send a message and get a response
```json
Request:
{
  "message": "Your question here",
  "session_id": "optional-session-id"
}

Response:
{
  "response": "AI assistant response",
  "session_id": "session-id"
}
```

### GET /api/session/{session_id}/history
Get chat history for a session
```json
Response:
{
  "session_id": "session-id",
  "history": [...]
}
```

### GET /health
Check server health
```json
Response:
{
  "status": "healthy",
  "agent": "ready"
}
```

## Browser Compatibility

Tested and working on:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- **First Load**: 1-2 seconds (includes agent initialization)
- **Subsequent Requests**: < 1 second (cached agent)
- **Cold Start**: First request after inactivity may take 3-5 seconds
- **Message Sending**: Instant UI feedback, 2-5 seconds for AI response

## Security

- ✅ HTTPS enforced (when deployed)
- ✅ No user data stored client-side
- ✅ Session IDs are randomly generated
- ✅ API key never exposed to frontend
- ✅ CORS properly configured

## Troubleshooting

### Interface doesn't load
- Check browser console for errors
- Verify server is running (`/health` endpoint)
- Clear browser cache

### Messages not sending
- Check internet connection
- Verify API key is set in environment
- Check browser console for errors

### Slow responses
- First request is always slower (cold start)
- Check Google Cloud Console for API quotas
- Verify Gemini API is enabled

---

**The web interface provides a professional, user-friendly way to interact with Academate from any device!**
