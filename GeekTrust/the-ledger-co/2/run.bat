@echo off

pip install -r requirements.txt
python -m geektrust sample_input\input1.txt
python -m unittest test_module