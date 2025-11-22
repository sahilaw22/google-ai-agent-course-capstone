"""Console entry point for the Academate helper bot."""

import os
import sys

# Add parent directory so imports keep working when run directly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from chatbot.configs import MODEL_NAME, TEMPERATURE
from chatbot.runtime import run_cli


def main():
    """Start Academate after making sure the API key exists."""
    # Make sure the key exists before doing anything else
    if not os.getenv("GOOGLE_API_KEY"):
        print("ERROR: GOOGLE_API_KEY not found in environment variables.")
        print("Please set it in your .env file or environment.")
        sys.exit(1)
    
    print("\n" + "="*60)
    print("ACADEMATE - College Helper")
    print("="*60)
    print(f"\n Model: {MODEL_NAME}")
    print(f"Temperature: {TEMPERATURE}")
    print("Agent ready")
    print("\n Ask me about:")
    print("   • Exam schedules and timetables")
    print("   • Previous year question papers")
    print("   • Faculty information")
    print("   • Academic calendar and events")
    print("   • Student results and performance")
    print("\n Type 'exit', 'quit', or 'bye' to stop")
    print("="*60 + "\n")
    
    # Hand over to the interactive loop
    run_cli()


if __name__ == "__main__":
    main()

