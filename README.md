# Aerodynamic Design of an SUV

## Abstract
This report aims to investigates the effects of grid size on the drag coefficient of an SUV and analyzes the flow field of the default design. 
It then proposes an optimized design through the use of **computational fluid dynamics** (CFD) aimed at reducing drag and compares the resulting drag coefficient with that of a market SUV, the Toyota RAV4. 
The relationship between vehicle velocity and drag coefficient is also explored, demonstrating a strong inverse correlation.

---

## Objective
The objective of this project is to optimize the **aerodynamic** (*i.e., the properties of a solid object regarding the manner in which air flows around it*) design of a Sports Utility Vehicle (SUV) in order to reduce drag and improve fuel efficiency. 
This objective is achieved through the analysis of the impact of grid size on drag coefficient, evaluating the aerodynamic efficiency of the default vehicle design, and proposing modifications to improve performance. 
A comparison with a market SUV's drag coefficient is also conducted to gauge the effectiveness of the design changes.

---

# Methods
## Procedure
The procedure involved three key steps:
1. **Grid Size Effect Analysis**: Mesh sizes were iteratively reduced from 0.5m to 0.125m to observe the impact on the drag coefficient.
2. **Flow Field Analysis**: The default SUV design was analyzed for aerodynamic efficiency by examining pressure and velocity flows.
3. **Design Optimization**: The SUV's design was modified to emulate low-drag coefficient models, aiming to reduce the front-hitting drag force.
4. **Comparison**: The drag coefficient of the optimized design was compared to other SUVs on the market.

---

## Results & Discussion
The results from the CFD analysis indicated a decrease in the drag coefficient with the reduction of mesh size, with 0.125m being the optimal grid size. 
The flow field analysis of the default design revealed aerodynamic inefficiencies, particularly due to the SUV's boxy and bulky front geometry. 
The optimized design achieved a significant reduction in the drag coefficient, from 1.45 to 0.22, outperforming the Toyota RAV4's coefficient of 0.31. 
The plot of vehicle velocity against drag coefficient showed a strong inverse correlation, with an R^2 value of 0.95753, indicating a robust relationship between the two variables.

---

## Conclusion
The optimized design of the SUV, which used a teardrop shape, showed a significant reduction in drag coefficient compared to the default design. The optimized design also showed superior aerodynamics compared to other SUVs on the market. These results demonstrate the effectiveness of using CFD analysis and optimization techniques to improve the aerodynamics of SUVs.
The experiment successfully demonstrated that optimizing grid size and vehicle geometry can substantially reduce the drag coefficient of an SUV. The optimized design not only surpassed the aerodynamic efficiency of the default model, but also showed superior performance compared to a well-regarded (in terms of drag coefficient) market SUV, the Toyota RAV4.
# Dependencies or Technologies Used
- **Ansys**: Used for mesh rendering and flow analysis.
- **Data Analysis Tools**: For calculating drag coefficients and statistical measures like the coefficient of determination (R^2).
- **Plotting Software**: To visualize the relationship between vehicle velocity and drag coefficient.
