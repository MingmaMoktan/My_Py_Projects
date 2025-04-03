import sys
from pathlib import Path

# Add the src directory to sys.path to make the package available for imports
sys.path.append(str(Path(__file__).parents[1] / "src"))