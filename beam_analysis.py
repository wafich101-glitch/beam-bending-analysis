"""
Beam Bending Analysis
Calculates and plots shear force and bending moment diagrams
for a simply supported beam under multiple point loads.
"""
import numpy as np
import matplotlib.pyplot as plt

L = 6.0
loads = np.array([10,15,8])      
positions = np.array([1.5,3.0,4.5])     

RB = np.sum(loads*positions)/L
RA = np.sum(loads)-RB

print(f"RA = {RA:.2f} kN")
print(f"RB = {RB:.2f} kN")

x_values = np.linspace(0,L,200) 

def shear_force(x, loads, positions, R_A):
    return R_A - np.sum(loads[positions < x])

shear_F = [shear_force(x,loads,positions,RA)for x in x_values]

def bending_moment(x, loads, positions, R_A):
    return R_A * x - np.sum((x - positions[positions < x]) * loads[positions < x])

B_moment = [bending_moment(x,loads,positions,RA)for x in x_values]

def plot_diagram(x_values,y_values,y_label,title,positions,loads):
    colors = ['red', 'green', 'purple', 'orange', 'brown']
    plt.figure(figsize=(8,4))
    plt.plot(x_values,y_values,label=y_label)
    plt.xlabel("Position along beam (m)")
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    for i in range(len(positions)):
        plt.axvline(x=positions[i], color=colors[i], linestyle='--', label=f'F={loads[i]} kN')
    plt.legend()
    plt.show()

plot_diagram(x_values,shear_F,"Shear force (kN)","Shear Force Diagram",positions,loads)
plot_diagram(x_values,B_moment, "Bending moment (kN·m)", "Bending Moment Diagram", positions,loads)