# 📚 Academate Documentation Index

Welcome to Academate! This index will help you find the right documentation for your needs.

## 🎯 Quick Navigation

### Getting Started (Choose One)

| I want to... | Read this |
|--------------|-----------|
| **Deploy in 5 minutes** | [QUICKSTART.md](QUICKSTART.md) ⚡ |
| **Understand the full deployment process** | [DEPLOYMENT.md](DEPLOYMENT.md) 📋 |
| **Run locally for development** | [README.md](README.md) → "How to Get Started" 🖥️ |

### Using Academate

| I want to... | Read this |
|--------------|-----------|
| **Learn about features and architecture** | [README.md](README.md) 🏗️ |
| **Use the web interface** | [WEB_INTERFACE.md](WEB_INTERFACE.md) 🌐 |
| **Test the application** | [TESTING.md](TESTING.md) 🧪 |

### Development

| I want to... | Read this |
|--------------|-----------|
| **Understand the codebase** | [assets/architecture.md](assets/architecture.md) 🏛️ |
| **Run tests** | [TESTING.md](TESTING.md) ✅ |
| **Customize the interface** | [WEB_INTERFACE.md](WEB_INTERFACE.md) → "Customization" 🎨 |

## 📖 Document Descriptions

### Core Documentation

#### [README.md](README.md)
**Main project documentation**
- Project overview and features
- Architecture diagram
- Tech stack
- Local installation instructions
- Running the agent (CLI, Web, ADK)
- Sample queries
- Contribution guidelines

**Best for**: First-time users, understanding what Academate does

---

#### [QUICKSTART.md](QUICKSTART.md)
**5-minute deployment guide**
- Minimal steps to get deployed
- Vercel deployment (3 steps)
- Netlify deployment (3 steps)
- Basic troubleshooting
- First queries to try

**Best for**: Users who want to deploy immediately

---

#### [DEPLOYMENT.md](DEPLOYMENT.md)
**Complete deployment guide**
- Prerequisites and setup
- Detailed Vercel instructions
- Detailed Netlify instructions
- Local development testing
- Environment variable configuration
- Troubleshooting common issues
- Custom domain setup
- Security best practices
- Cost considerations

**Best for**: Users who want to understand deployment in depth

---

#### [WEB_INTERFACE.md](WEB_INTERFACE.md)
**Web UI documentation**
- Interface components breakdown
- User experience features
- Sample conversation flow
- Customization guide
- API endpoints
- Browser compatibility
- Performance metrics
- Security features

**Best for**: Users/developers working with the web interface

---

#### [TESTING.md](TESTING.md)
**Testing guide**
- Test types (unit, integration, evaluation)
- Local development testing
- Testing deployment configurations
- Common test scenarios
- Performance testing
- Debugging failed tests
- CI/CD integration
- Test checklist

**Best for**: Developers and QA testing the application

---

### Configuration Files

#### [.env.example](.env.example)
**Environment variables template**
- GOOGLE_API_KEY configuration
- Model selection (AGENT_MODEL)
- Temperature setting (AGENT_TEMPERATURE)

**Usage**: Copy to `.env` and fill in your values

---

#### [vercel.json](vercel.json)
**Vercel deployment configuration**
- Python runtime setup
- Route configuration
- Environment variable references

**Usage**: Automatic - Vercel reads this on deployment

---

#### [netlify.toml](netlify.toml)
**Netlify deployment configuration**
- Build command
- Functions directory
- Redirect rules
- Python version specification

**Usage**: Automatic - Netlify reads this on deployment

---

#### [runtime.txt](runtime.txt)
**Python version specification**
- Specifies Python 3.10

**Usage**: Used by deployment platforms

---

### Source Code

#### [chatbot/](chatbot/)
**Main application code**
- `agent.py` - ADK web entry point
- `runtime.py` - Agent initialization and CLI
- `tools.py` - Custom campus Q&A tools
- `datasets.py` - CSV data loading
- `memory.py` - Session management
- `observability.py` - Logging
- `evaluation.py` - Testing harness
- `llm.py` - LLM configuration
- `configs.py` - Configuration settings

---

#### [api/](api/)
**Web deployment code**
- `server.py` - FastAPI web server with HTML interface
- `__init__.py` - Module initialization

**Key features**:
- Chat endpoint (`/api/chat`)
- Health check (`/health`)
- Session history (`/api/session/{id}/history`)
- Embedded HTML/CSS/JS for UI

---

#### [tests/](tests/)
**Test suite**
- `test_agent.py` - Integration tests for agent functionality
- `test_web_server.py` - Unit tests for web server structure

---

#### [data/](data/)
**CSV datasets**
- `academic_calendar.csv` - Events and deadlines
- `exam_schedule.csv` - Exam dates and details
- `faculty.csv` - Faculty information
- `previous_papers.csv` - Past exam papers
- `student_results.csv` - Student performance data
- `students.csv` - Student records
- `timetable.csv` - Class schedules

---

## 🎓 Learning Path

### Path 1: Just Want to Use It
1. Read [QUICKSTART.md](QUICKSTART.md)
2. Deploy to Vercel or Netlify
3. Start asking questions!

### Path 2: Want to Develop/Customize
1. Read [README.md](README.md) - "How to Get Started"
2. Set up local environment
3. Read [WEB_INTERFACE.md](WEB_INTERFACE.md) for customization
4. Read [TESTING.md](TESTING.md) for validation
5. Deploy using [DEPLOYMENT.md](DEPLOYMENT.md)

### Path 3: Want to Understand Everything
1. Read [README.md](README.md) - Full overview
2. Read [assets/architecture.md](assets/architecture.md) - Architecture
3. Explore source code in [chatbot/](chatbot/)
4. Read [WEB_INTERFACE.md](WEB_INTERFACE.md)
5. Read [DEPLOYMENT.md](DEPLOYMENT.md)
6. Read [TESTING.md](TESTING.md)

## 🔧 Troubleshooting Quick Links

| Problem | Solution |
|---------|----------|
| Can't deploy | [DEPLOYMENT.md](DEPLOYMENT.md) → "Troubleshooting" |
| Tests failing | [TESTING.md](TESTING.md) → "Debugging Failed Tests" |
| Web UI not working | [WEB_INTERFACE.md](WEB_INTERFACE.md) → "Troubleshooting" |
| API key issues | [DEPLOYMENT.md](DEPLOYMENT.md) → "Security Best Practices" |
| Build errors | [QUICKSTART.md](QUICKSTART.md) → "Troubleshooting" |

## 📞 Support Resources

### Documentation
- This repository's docs (you're here!)
- Jupyter notebook: [Academate-College-Chatbot.ipynb](Academate-College-Chatbot.ipynb)

### External Resources
- **Google ADK**: https://github.com/googleapis/python-adk
- **Gemini API**: https://ai.google.dev
- **FastAPI**: https://fastapi.tiangolo.com
- **Vercel**: https://vercel.com/docs
- **Netlify**: https://docs.netlify.com

## 🎯 Common Tasks

### Deploy for the First Time
1. [QUICKSTART.md](QUICKSTART.md) - Get your API key
2. [QUICKSTART.md](QUICKSTART.md) - Follow 3-step deployment
3. Test your deployment

### Update Deployment
1. Make code changes
2. Run tests: [TESTING.md](TESTING.md)
3. Push to GitHub
4. Auto-deploys!

### Customize the UI
1. Read [WEB_INTERFACE.md](WEB_INTERFACE.md) → "Customization"
2. Edit `api/server.py`
3. Test locally: `python api/server.py`
4. Deploy changes

### Add New Features
1. Understand architecture: [README.md](README.md)
2. Add code in `chatbot/tools.py`
3. Test: [TESTING.md](TESTING.md)
4. Deploy: [DEPLOYMENT.md](DEPLOYMENT.md)

## 📝 Contributing

See [README.md](README.md) → "🤝 Contribute" section for:
- How to fork the repository
- Branch naming conventions
- Pull request process

## 📜 License

MIT License - See [README.md](README.md) → "📜 License"

---

**🎓 Ready to get started? Choose your path above and begin your Academate journey!**
