# Bank Queue System Simulation (Discrete Event Simulation)

![Project Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![University](https://img.shields.io/badge/UNESP-Rio_Claro-green)
![Subject](https://img.shields.io/badge/Subject-Modeling_&_Simulation-orange)

## 📌 Overview

This project implements a **Discrete Event Simulation (DES)** to model and analyze the performance of a banking queue system. Developed as a Graduation Project in Computer Science, the study aims to reproduce real-world behaviors regarding client waiting times, service efficiency, and employee idleness using pseudo-random number generation.

## 🎯 Objectives

* **Simulation:** Model a system with a fixed number of clients and employees.
* **Stochastic Analysis:** Use probability distributions to determine **Time Between Arrivals (TEC)** and **Service Time (TS)**.
* **Performance Metrics:** Calculate and analyze:
    * Average waiting time in queue.
    * Total time in the system.
    * Employee idle time.
* **Optimization:** Evaluate different scenarios to propose process improvements.

## 🛠️ Methodology

The simulation was built in **Python**. To ensure statistical validity, the model runs **1000 iterations** with different random seeds, generating confidence intervals (95%) for all major metrics.

### Mathematical Model
The system is driven by the following equations for time generation:

1.  **Time Between Arrivals (TEC):**
    $$TEC(i) = \frac{-ln(random(i))}{0.6}$$

2.  **Service Time (TS):**
    $$TS(i) = \frac{-ln(random(i))}{0.4} + 0.3$$

*Where $random(i)$ is a pseudo-random number between 0 and 1.*

## 📊 Scenarios & Results

The study evaluated the system under three distinct configurations (based on an 8-hour workday with 2 employees):

| Scenario | Configuration | Results | Analysis |
| :--- | :--- | :--- | :--- |
| **1. Baseline** | Standard TEC/TS parameters. | **66% Served**<br>Wait: ~5 min<br>Idle: ~30s | System is under-capacity. 34% of clients cannot be served within working hours. |
| **2. High Demand** | TEC reduced by 50% (Double arrivals). | **100% Served**<br>Wait: **+3420%**<br>Idle: 0s | System collapses. While all clients enter, the queue becomes unmanageable. |
| **3. Optimized** | TEC and TS reduced by 50%. | **100% Served**<br>Wait: Reduced<br>Idle: 0s | **Best Balance.** High throughput requires faster service (lower TS) to match arrival rates. |

## 📝 Conclusion

The simulation demonstrates that simply allowing more clients into the system (Scenario 2) without improving service speed leads to exponential growth in waiting times. The most efficient approach (Scenario 3) requires a reduction in service time (TS), allowing for 100% service completion, though it results in zero idle time for employees, suggesting a high-stress environment.

## 👥 Author

* **Felipe Silva Alves de Oliveira**
* **Institution:** UNESP - Instituto de Geociências e Ciências Exatas (Rio Claro)
* **Year:** 2025

---
*Built with Python & Matplotlib*
