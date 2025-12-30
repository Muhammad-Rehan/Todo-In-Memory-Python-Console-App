"""
Main entry point for the Todo In-Memory Python Console App.
"""
if __name__ == "__main__":
    import sys
    import os

    # Add the project root to Python path to allow imports
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, project_root)

    # Also add src to Python path
    src_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)

    from todo_app.cli.interface import TodoCLI

    def main():
        """Main application entry point."""
        cli = TodoCLI()
        cli.run()

    main()