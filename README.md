# Stock Market AI Assistant 📈🤖

An AI-powered assistant for Indian stock market analysis with real-time news aggregation, conversational AI interface, and multi-device support.

## ✨ Features

- 🤖 **AI-Powered Chat** - Ask questions about stocks, news, and market movements
- 📰 **Real-Time News** - Aggregates from Moneycontrol, Economic Times, NSE, BSE
- 📊 **Stock Data** - Live prices and market data for Indian stocks
- ⭐ **Watchlist** - Track your favorite stocks
- 📱 **Multi-Device** - Works on mobile and desktop
- 🔒 **Private** - Self-hosted, your data stays with you

## 🛠️ Tech Stack

### Backend
- Python 3.11+
- FastAPI (API framework)
- SQLite (Database)
- Google Gemini API (AI)
- Alpha Vantage API (Stock data)

### Frontend
- React 18
- Vite (Build tool)
- Tailwind CSS (Styling)
- Axios (HTTP client)

### Deployment
- Docker & Docker Compose
- Nginx (Reverse proxy)

## 🚀 Quick Start

### Prerequisites

1. **Get API Keys** (Both FREE):
   - Google Gemini: https://aistudio.google.com/app/apikey
   - Alpha Vantage: https://www.alphavantage.co/support/#api-key

2. **Install Dependencies**:
   ```bash
   # On Arch Linux
   sudo pacman -S python nodejs npm docker docker-compose
   ```

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/stock-market-ai.git
   cd stock-market-ai
   ```

2. **Configure environment variables**:
   ```bash
   # Backend
   cp backend/.env.example backend/.env
   nano backend/.env  # Add your API keys
   
   # Frontend
   cp frontend/.env.example frontend/.env
   # (Frontend .env is pre-configured for local development)
   ```

3. **Run with Docker** (Recommended):
   ```bash
   docker-compose up -d
   ```

   **OR run manually**:
   
   ```bash
   # Terminal 1: Backend
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   
   # Terminal 2: Frontend
   cd frontend
   npm install
   npm run dev
   ```

4. **Access the application**:
   - Frontend: http://localhost:5173 (Vite dev server)
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 📖 Documentation

- [Setup Guide](docs/SETUP.md) - Detailed setup instructions
- [API Documentation](docs/API.md) - API endpoints reference
- [Deployment Guide](docs/DEPLOYMENT.md) - Production deployment
- [Architecture](docs/ARCHITECTURE.md) - System design and architecture

## 🗂️ Project Structure

```
stock-market-ai/
├── backend/          # Python FastAPI backend
│   ├── app/
│   │   ├── routers/      # API endpoints
│   │   ├── services/     # Business logic
│   │   ├── models/       # Database models
│   │   └── utils/        # Helper functions
│   └── tests/        # Backend tests
├── frontend/         # React frontend
│   └── src/
│       ├── components/   # React components
│       ├── pages/        # Page components
│       ├── services/     # API clients
│       └── hooks/        # Custom hooks
├── nginx/            # Nginx configuration
├── docs/             # Documentation
└── scripts/          # Utility scripts
```

## 🔧 Development

### Backend Development

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run tests
pytest
```

### Frontend Development

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 🐳 Docker Commands

```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild containers
docker-compose up -d --build

# Stop and remove everything
docker-compose down -v
```

## 📝 Environment Variables

### Backend (.env)

```env
GEMINI_API_KEY=your_gemini_api_key
ALPHA_VANTAGE_KEY=your_alpha_vantage_key
DATABASE_URL=sqlite:///./data/stock_market.db
```

### Frontend (.env)

```env
VITE_API_URL=http://localhost:8000
```

## 🤝 Contributing

This is a personal/educational project, but suggestions and feedback are welcome!

## 📄 License

MIT License - Feel free to use for personal and educational purposes.

## 🙏 Acknowledgments

- Google Gemini for AI capabilities
- Alpha Vantage for stock market data
- Indian financial news sources (Moneycontrol, ET, NSE, BSE)

## 📧 Contact

Created as a passion project for Indian stock market traders.

---

**⚠️ Disclaimer**: This tool is for informational purposes only. It does not provide financial advice. Always do your own research before making investment decisions.
