@echo off
python -c "import sys; sys.path.insert(0, 'src'); from todo_app.cli.interface import TodoCLI; cli = TodoCLI(); cli.run()"