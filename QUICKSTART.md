# Quick Start Guide - Deploying Academate

This is a simplified guide to get Academate deployed quickly. For detailed instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

## What You'll Get

After deployment, you'll have a live web application where users can chat with the Academate AI assistant through a beautiful web interface.

## Prerequisites (5 minutes)

1. **Get a Google API Key** (Free)
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Click "Create API Key"
   - Copy your API key and save it somewhere safe

2. **Choose a Platform** (Both are free!)
   - **Vercel** (Recommended) - [Sign up here](https://vercel.com)
   - **Netlify** - [Sign up here](https://netlify.com)

## Deploy to Vercel (3 Steps - 5 minutes)

### 1. Fork or Import Repository
   - Go to [Vercel](https://vercel.com)
   - Click "Add New" → "Project"
   - Import this GitHub repository

### 2. Add Environment Variables
   In the Vercel project setup, add:
   ```
   GOOGLE_API_KEY=your_api_key_from_step_1
   ```

### 3. Deploy
   - Click "Deploy"
   - Wait 1-2 minutes
   - Your chatbot is live! 🎉

That's it! Visit `https://your-project.vercel.app` to use your chatbot.

## Deploy to Netlify (3 Steps - 5 minutes)

### 1. Import Repository
   - Go to [Netlify](https://netlify.com)
   - Click "Add new site" → "Import an existing project"
   - Select this GitHub repository

### 2. Add Environment Variables
   Go to "Site settings" → "Environment variables" and add:
   ```
   GOOGLE_API_KEY=your_api_key_from_step_1
   ```

### 3. Deploy
   - Click "Deploy site"
   - Wait 2-3 minutes
   - Your chatbot is live! 🎉

Visit `https://your-site.netlify.app` to use your chatbot.

## Using Your Chatbot

Once deployed, you can:
- ✅ Share the URL with students and faculty
- ✅ Ask about exam schedules, timetables, faculty info
- ✅ Get previous year papers
- ✅ Check academic calendar events
- ✅ Access from any device (mobile, tablet, desktop)

## Example Questions to Try

- "When is my next exam?"
- "Show me the AI timetable"
- "Who teaches Data Structures?"
- "What events are happening this week?"

## Troubleshooting

**Problem**: Build fails
- **Solution**: Make sure you added the `GOOGLE_API_KEY` environment variable

**Problem**: Site works but chatbot doesn't respond
- **Solution**: Check that your Google API key is valid and has Gemini API access enabled

**Problem**: Responses are slow
- **Solution**: First request is always slower (cold start). Subsequent requests will be faster.

## Next Steps

- **Custom Domain**: Add your own domain (e.g., academate.yourschool.edu)
- **Monitor Usage**: Check Google Cloud Console for API usage
- **Customize**: Edit `api/server.py` to customize the UI or behavior
- **Update**: Push changes to GitHub - Vercel/Netlify will auto-deploy

## Support

- Read the full [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions
- Check the main [README.md](README.md) for feature documentation
- Vercel: https://vercel.com/docs
- Netlify: https://docs.netlify.com

---

**🎓 You're all set! Enjoy using Academate!**
