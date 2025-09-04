"""
[입력]
ObjectOrientedProgramming1 3.0 A+
IntroductiontoComputerEngineering 3.0 A+
ObjectOrientedProgramming2 3.0 A0
CreativeComputerEngineeringDesign 3.0 A+
AssemblyLanguage 3.0 A+
InternetProgramming 3.0 B0
ApplicationProgramminginJava 3.0 A0
SystemProgramming 3.0 B0
OperatingSystem 3.0 B0
WirelessCommunicationsandNetworking 3.0 C+
LogicCircuits 3.0 B0
DataStructure 4.0 A+
MicroprocessorApplication 3.0 B+
EmbeddedSoftware 3.0 C0
ComputerSecurity 3.0 D+
Database 3.0 C+
Algorithm 3.0 B0
CapstoneDesigninCSE 3.0 B+
CompilerDesign 3.0 D0
ProblemSolving 4.0 P

[출력]
3.284483
"""
import sys

def grade_cal(value):
    if value == 'A+':
        return 4.5
    elif value == 'A0':
        return 4.0
    elif value == 'B+':
        return 3.5
    elif value == 'B0':
        return 3.0
    elif value == 'C+':
        return 2.5
    elif value == 'C0':
        return 2.0
    elif value == 'D+':
        return 1.5
    elif value == 'D0':
        return 1.0
    else:
        return 0.0

sum = 0
total_sum = 0

for _ in range(20):
    input_data = sys.stdin.readline().split()

    sub_name = input_data[0]
    score = float(input_data[1])
    grade = input_data[2]

    if grade == 'P':
        continue
    else:
        sum += grade_cal(grade) * score
        total_sum += score

print(sum / total_sum)



