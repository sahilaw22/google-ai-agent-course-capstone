# Deployment Guide for Academate

This guide explains how to deploy Academate to Vercel or Netlify using the Google ADK web UI.

## Prerequisites

1. A Google Cloud account with Gemini API access
2. Google API Key from [Google AI Studio](https://makersuite.google.com/app/apikey)
3. A GitHub account (for deployment)
4. A Vercel or Netlify account (free tier works)

## Deployment Options

### Option 1: Deploy to Vercel (Recommended)

Vercel provides excellent support for Python serverless functions and is ideal for this application.

#### Step-by-Step Instructions:

1. **Push your code to GitHub** (if not already done)
   ```bash
   git add .
   git commit -m "Prepare for Vercel deployment"
   git push origin main
   ```

2. **Sign up/Login to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign up or log in with your GitHub account

3. **Import your repository**
   - Click "Add New" → "Project"
   - Import your GitHub repository
   - Vercel will auto-detect the configuration from `vercel.json`

4. **Configure Environment Variables**
   - In the Vercel dashboard, go to your project settings
   - Navigate to "Environment Variables"
   - Add the following variables:
     ```
     GOOGLE_API_KEY=your_actual_api_key_here
     AGENT_MODEL=gemini-2.5-flash-lite
     AGENT_TEMPERATURE=0.7
     ```

5. **Deploy**
   - Click "Deploy"
   - Wait for the build to complete (usually 1-2 minutes)
   - Your app will be available at `https://your-project.vercel.app`

6. **Access your Chatbot**
   - Visit your Vercel URL
   - You should see the Academate web interface
   - Start chatting with the AI assistant!

#### Vercel Configuration Details

The `vercel.json` file configures:
- Python runtime with FastAPI
- Serverless function routing
- Environment variables

### Option 2: Deploy to Netlify

Netlify is another excellent platform for deploying web applications.

#### Step-by-Step Instructions:

1. **Push your code to GitHub** (if not already done)
   ```bash
   git add .
   git commit -m "Prepare for Netlify deployment"
   git push origin main
   ```

2. **Sign up/Login to Netlify**
   - Go to [netlify.com](https://netlify.com)
   - Sign up or log in with your GitHub account

3. **Create a new site**
   - Click "Add new site" → "Import an existing project"
   - Choose GitHub and authorize Netlify
   - Select your repository

4. **Configure Build Settings**
   - Netlify should auto-detect settings from `netlify.toml`
   - Build command: `pip install -r requirements.txt`
   - Functions directory: `api`

5. **Set Environment Variables**
   - Go to "Site settings" → "Environment variables"
   - Add the following:
     ```
     GOOGLE_API_KEY=your_actual_api_key_here
     AGENT_MODEL=gemini-2.5-flash-lite
     AGENT_TEMPERATURE=0.7
     ```

6. **Deploy**
   - Click "Deploy site"
   - Wait for the build (2-3 minutes)
   - Your app will be available at `https://your-site.netlify.app`

#### Netlify Configuration Details

The `netlify.toml` file configures:
- Python 3.10 runtime
- Build commands
- Serverless function redirects

## Local Development

Before deploying, you can test the web interface locally:

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your GOOGLE_API_KEY
   ```

3. **Run the development server**
   ```bash
   python api/server.py
   ```

4. **Access the web UI**
   - Open your browser to `http://localhost:8000`
   - Test the chatbot interface

## Features of the Web UI

The deployed web application includes:

- **Modern Chat Interface**: Clean, responsive design that works on all devices
- **Real-time Interaction**: Chat with the AI assistant in real-time
- **Session Management**: Each browser session maintains its own conversation context
- **Error Handling**: Graceful error messages and recovery
- **Health Check Endpoint**: `/health` for monitoring

## API Endpoints

Your deployment includes these endpoints:

- `GET /` - Web chat interface (HTML)
- `POST /api/chat` - Chat with the AI assistant
- `GET /api/session/{session_id}/history` - Get chat history
- `GET /health` - Health check endpoint

## Troubleshooting

### Build Failures

**Issue**: Build fails with module not found errors
- **Solution**: Ensure `requirements.txt` includes all dependencies
- Check that Python version is 3.10+ (specified in `runtime.txt`)

**Issue**: API key not found
- **Solution**: Verify environment variables are set correctly in your platform's dashboard
- Make sure variable name is exactly `GOOGLE_API_KEY`

### Runtime Errors

**Issue**: 503 Service Unavailable
- **Solution**: Check that the GOOGLE_API_KEY is valid
- Verify Gemini API is enabled in your Google Cloud project

**Issue**: Slow responses
- **Solution**: This is normal for the first request (cold start)
- Subsequent requests will be faster
- Consider upgrading to a paid plan for faster performance

### Deployment Platform Issues

**Vercel**:
- Free tier has execution time limits (10 seconds for Hobby plan)
- For longer conversations, consider Pro plan
- Check function logs in Vercel dashboard

**Netlify**:
- Free tier has build minute limits
- Serverless functions have 10-second timeout on free tier
- Check function logs in Netlify dashboard

## Updating Your Deployment

To update your deployed application:

1. Make changes to your code
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update chatbot"
   git push origin main
   ```
3. Both Vercel and Netlify will automatically rebuild and redeploy

## Security Best Practices

1. **Never commit your `.env` file** - It's already in `.gitignore`
2. **Use environment variables** for all secrets
3. **Rotate API keys regularly**
4. **Monitor usage** in Google Cloud Console
5. **Set up budget alerts** to avoid unexpected costs

## Custom Domain (Optional)

Both Vercel and Netlify support custom domains:

1. Purchase a domain from any registrar
2. In your deployment platform dashboard:
   - Go to "Domains" settings
   - Add your custom domain
   - Follow DNS configuration instructions
3. SSL certificates are automatically provisioned

## Support and Resources

- **Vercel Documentation**: https://vercel.com/docs
- **Netlify Documentation**: https://docs.netlify.com
- **Google ADK Documentation**: https://github.com/googleapis/python-adk
- **Gemini API**: https://ai.google.dev/

## Cost Considerations

- **Vercel Free Tier**: 100GB bandwidth, serverless function invocations
- **Netlify Free Tier**: 100GB bandwidth, 125k function requests
- **Google Gemini API**: Pay-per-use (check current pricing)

Both platforms have generous free tiers suitable for development and low-traffic applications.

---

**Note**: The web interface uses the same Google ADK agent as the CLI version, ensuring consistent behavior across all deployment methods.
