# Testing Guide

This guide covers how to test Academate in different scenarios.

## Prerequisites for Testing

All tests require a valid Google API key. Get one from [Google AI Studio](https://makersuite.google.com/app/apikey).

### Setup Environment

1. **Create `.env` file**:
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` and add your API key**:
   ```ini
   GOOGLE_API_KEY=your_actual_api_key_here
   AGENT_MODEL=gemini-2.5-flash-lite
   AGENT_TEMPERATURE=0.7
   ```

## Test Types

### 1. Unit Tests (No API Key Required)

These tests verify the code structure without making API calls:

```bash
# Test web server structure
python tests/test_web_server.py
```

**What it tests**:
- ✅ Module imports
- ✅ FastAPI app creation
- ✅ Request/Response models
- ✅ API endpoint structure

### 2. Integration Tests (API Key Required)

These tests verify the actual functionality with the LLM:

```bash
# Test agent functionality
python tests/test_agent.py
```

**What it tests**:
- ✅ Environment setup
- ✅ CSV dataset loading
- ✅ Tool imports and creation
- ✅ Individual tool functions
- ✅ Agent initialization
- ✅ Case-insensitive queries

### 3. Evaluation Tests (API Key Required)

Test the agent's accuracy on predefined questions:

```bash
python -c "from chatbot.evaluation import run_evaluations; print(run_evaluations())"
```

**What it tests**:
- ✅ Predefined query responses
- ✅ Answer quality
- ✅ Expected output matching

## Local Development Testing

### Testing the CLI Interface

```bash
# Run the command-line interface
python -m chatbot.main
```

**Test scenarios**:
- Ask about exam schedules
- Request timetables
- Query faculty information
- Check academic calendar
- Exit gracefully with 'quit' or 'exit'

### Testing the ADK Web Interface

```bash
# Run with Google ADK web UI
adk web Academate
```

Visit: http://127.0.0.1:8000

**Test scenarios**:
- Use the ADK built-in chat interface
- Check agent metadata display
- Test conversation history
- Verify tool invocations appear correctly

### Testing the Custom Web Interface

```bash
# Run the custom FastAPI server
python api/server.py
```

Visit: http://localhost:8000

**Test scenarios**:
1. **UI Loads Correctly**:
   - Welcome message displays
   - Input field is active
   - Send button is visible

2. **Basic Interaction**:
   - Type "Hello" and press Enter
   - Verify response appears
   - Check message alignment (user right, AI left)

3. **Error Handling**:
   - Stop the server mid-conversation
   - Verify error message appears
   - Restart and verify recovery

4. **Multiple Questions**:
   - Ask several questions in sequence
   - Verify scroll behavior
   - Check session persistence

5. **Health Check**:
   - Visit http://localhost:8000/health
   - Verify JSON response with status

## Testing Deployment Configurations

### Test Vercel Configuration

```bash
# Install Vercel CLI (if not installed)
npm i -g vercel

# Test local deployment
vercel dev
```

This runs the Vercel serverless environment locally.

### Test Netlify Configuration

```bash
# Install Netlify CLI (if not installed)
npm i -g netlify-cli

# Test local deployment
netlify dev
```

This runs the Netlify functions environment locally.

## Common Test Scenarios

### Scenario 1: Exam Schedule Query

**Input**: "Show me the exam schedule for Computer Science semester 3"

**Expected Output**:
- List of exams with dates
- Subject names and codes
- Exam times and rooms
- Total marks

**Verify**:
- ✅ Data is formatted clearly
- ✅ Dates are readable
- ✅ All exam details are present

### Scenario 2: Faculty Search

**Input**: "Who teaches Data Structures?"

**Expected Output**:
- Faculty name
- Department
- Contact information
- Office hours (if available)

**Verify**:
- ✅ Faculty information is accurate
- ✅ Case-insensitive search works
- ✅ Multiple results handled correctly

### Scenario 3: Timetable Request

**Input**: "Get the timetable for CS2024001"

**Expected Output**:
- Weekly schedule
- Day-by-day breakdown
- Class times and rooms
- Faculty names

**Verify**:
- ✅ Student ID lookup works
- ✅ Schedule is well-formatted
- ✅ All weekdays included

### Scenario 4: Previous Papers

**Input**: "Show previous papers for CS301"

**Expected Output**:
- List of papers by year
- Paper types (midterm, final, etc.)
- Download links (if available)

**Verify**:
- ✅ Papers sorted by year (newest first)
- ✅ Subject code is case-insensitive
- ✅ Year filter works correctly

### Scenario 5: Academic Calendar

**Input**: "What events are coming up?"

**Expected Output**:
- List of upcoming events
- Event dates and types
- Days until each event
- Event descriptions

**Verify**:
- ✅ Only future events shown
- ✅ Sorted by date
- ✅ Time-based descriptions ("in 3 days", "TOMORROW")

## Performance Testing

### Response Time

Expected response times (with warm server):
- **Simple queries**: < 2 seconds
- **Complex queries**: 3-5 seconds
- **First request (cold start)**: 5-10 seconds

### Load Testing

For production deployments, test with tools like:
```bash
# Install Apache Bench
apt-get install apache2-utils

# Test with 100 requests, 10 concurrent
ab -n 100 -c 10 -p post_data.json -T application/json http://localhost:8000/api/chat
```

## Debugging Failed Tests

### API Key Issues

**Symptom**: "API Key not found" or authentication errors

**Solutions**:
1. Check `.env` file exists and contains `GOOGLE_API_KEY`
2. Verify API key is valid (test in Google AI Studio)
3. Ensure Gemini API is enabled in Google Cloud Console
4. Check for extra spaces or quotes in the key

### Data Loading Issues

**Symptom**: "No data found" or CSV errors

**Solutions**:
1. Verify CSV files exist in `data/` directory
2. Check CSV file formatting (headers, encoding)
3. Ensure data directory path is correct
4. Look for trailing commas or special characters

### Agent Initialization Issues

**Symptom**: Agent fails to initialize or crashes

**Solutions**:
1. Check all dependencies installed: `pip install -r requirements.txt`
2. Verify Python version: `python --version` (should be 3.10+)
3. Check for import errors in logs
4. Ensure Google ADK version matches requirements

### Web Server Issues

**Symptom**: Server won't start or crashes

**Solutions**:
1. Check port 8000 is available: `lsof -i :8000`
2. Verify uvicorn is installed
3. Check for syntax errors in `api/server.py`
4. Review server logs for detailed errors

## Continuous Integration Testing

For automated testing in CI/CD:

```yaml
# Example GitHub Actions workflow
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      - run: pip install -r requirements.txt
      - run: python tests/test_web_server.py
      # Note: Skip tests requiring API key in CI
```

## Test Checklist

Before deploying to production:

- [ ] All unit tests pass
- [ ] All integration tests pass (with real API key)
- [ ] Web interface loads correctly
- [ ] All sample queries work
- [ ] Error handling works properly
- [ ] Mobile responsiveness verified
- [ ] Browser compatibility checked
- [ ] API endpoints respond correctly
- [ ] Health check works
- [ ] Session management works
- [ ] Logs are being generated
- [ ] No sensitive data in logs
- [ ] Environment variables properly set
- [ ] Deployment configurations validated

## Getting Help

If tests fail and you can't resolve them:

1. Check the error message carefully
2. Review relevant documentation:
   - [README.md](README.md) - General usage
   - [DEPLOYMENT.md](DEPLOYMENT.md) - Deployment guide
   - [WEB_INTERFACE.md](WEB_INTERFACE.md) - Web UI details

3. Common resources:
   - Google ADK docs: https://github.com/googleapis/python-adk
   - FastAPI docs: https://fastapi.tiangolo.com
   - Gemini API docs: https://ai.google.dev

---

**Remember**: Always test locally before deploying to production!
