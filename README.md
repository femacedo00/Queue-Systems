# Bank Queue System Simulation

![Project Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Type](https://img.shields.io/badge/Type-Discrete_Event_Simulation-orange)
![Subject](https://img.shields.io/badge/Subject-Operations_Research-lightgrey)

## 📌 Overview

[cite_start]This project involves the modeling and simulation of a bank queue system using **Discrete Event Simulation (DES)** techniques[cite: 31, 44]. [cite_start]The goal is to replicate the behavior of a real system with a fixed number of clients and employees to measure service efficiency, waiting times, and employee idleness[cite: 15, 18].

[cite_start]This work was developed as a Graduation Project for the **Computer Science** course at **UNESP - Rio Claro** (State University of São Paulo)[cite: 1, 8].

## 🎯 Objectives

* [cite_start]**Model:** Create a virtual representation of a banking service system using pseudo-random numbers[cite: 15, 16].
* [cite_start]**Analyze:** Calculate statistical metrics such as Time Between Arrivals (TEC), Service Time (TS), Waiting Time, and System Time[cite: 16, 45].
* [cite_start]**Optimize:** Explore different operating scenarios to identify bottlenecks and propose improvements in the process[cite: 19].

## ⚙️ Methodology

[cite_start]The simulation was implemented in **Python**[cite: 52]. [cite_start]To ensure statistical robustness, the simulation was repeated **1000 times** using different seeds for random number generation, allowing for the calculation of confidence intervals (95%) for key metrics[cite: 61, 62].

### Mathematical Models
[cite_start]The system relies on stochastic variables defined by the following expressions[cite: 48, 50]:

* **Time Between Arrivals (TEC):**
    $$TEC(i) = \frac{-ln(random(i))}{0.6}$$
* **Service Time (TS):**
    $$TS(i) = \frac{-ln(random(i))}{0.4} + 0.3$$

### Logic Flow
1.  [cite_start]**Arrival:** Checks if the client arrives within the 8-hour operation limit (480 minutes)[cite: 54, 66].
2.  **Queue/Service:** If an employee is free, service starts immediately. [cite_start]If not, the system assigns the client to the employee who will finish earliest[cite: 57, 58].
3.  [cite_start]**Metrics:** Calculates wait time, total time in system, and employee idle time[cite: 59].

## 📊 Results & Scenarios

[cite_start]Three distinct scenarios were analyzed to test system capacity (initially set for 432 clients and 2 employees)[cite: 66].

| Scenario | Description | Clients Served | Wait Time | Employee Status |
| :--- | :--- | :---: | :---: | :--- |
| **1. Baseline** | Standard TEC and TS parameters. | ~66% | ~5 min | [cite_start]**Idle time:** ~30s per employee[cite: 251, 252, 253, 254]. |
| **2. High Demand** | TEC reduced by half (more frequent arrivals). | **100%** | **+3420%** | **Continuous work** (0s idle time). [cite_start]Huge queues formed[cite: 417, 418]. |
| **3. Optimized** | Both TEC and TS reduced by half. | **100%** | Reduced | **Continuous work** (0s idle time). [cite_start]Efficient flow but high employee stress[cite: 582, 583]. |

## 📝 Conclusion

* [cite_start]**Scenario 1:** The system is comfortable for employees but inefficient for clients, as roughly 34% of clients cannot be served within the 8-hour window[cite: 251].
* [cite_start]**Scenario 2:** Simply increasing the arrival rate ensures everyone gets in the door, but causes the system to collapse with unmanageable waiting times[cite: 417].
* **Scenario 3:** Increasing service speed (reducing TS) is necessary to handle higher volume. [cite_start]This achieves 100% service rate with manageable queues, though it eliminates employee breaks[cite: 582, 583].

## 👥 Author

* [cite_start]**Felipe Silva Alves de Oliveira** [cite: 9]
* **Advisor:** (Not listed in snippet)
* [cite_start]**Institution:** UNESP - Instituto de Geociências e Ciências Exatas (Rio Claro)[cite: 2, 3].

---
*2025 - Modeling and Performance Evaluation*
