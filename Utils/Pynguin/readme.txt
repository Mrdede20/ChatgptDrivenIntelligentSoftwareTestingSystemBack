此项目用来对经过规定要求对源代码进行函数封装改写，然后生成pynguin测试代码

PythonProgramTobeTested目录处理了function signature加argument type和standard input和output
pynguin-PythonProgramTobeTested目录为自动生成的测试代码

PythonProgramTobeTested
无class
pynguin --project-path ../../ProgramTobeTested/python_2024_04_20_10_58_41/buggy --output-path ./data/python_2024_04_20_10_58_41 --module-name Array_Collapse -v
有class
pynguin --project-path ./stage1 --output-path ./pynguin-results1 --module-name Matrix_Problem -v --seed 1629381673714481067

from ProgramTobeTested.PythonProgramTobeTested


